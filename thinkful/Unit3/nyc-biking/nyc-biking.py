####################################
#
# This script creates a SQL database which holds two tables of NYC CitiBike data
# citibike_reference contains information on all CitiBike stations in NYC such as ID, address, number of bike docks, etc
# available_bikes is a table where the columns are the station ids and the rows are execution times (when the data was pulled from )
#
####################################

import requests

r = requests.get('http://www.citibikenyc.com/stations/json')

# Create a list of all keys in stationBeanList
key_list = []
for station in r.json()['stationBeanList']:
    for k in station.keys():
        if k not in key_list:
            key_list.append(k)

# Import the data into a dataframe
from pandas.io.json import json_normalize
df = json_normalize(r.json()['stationBeanList'])

# Create a reference table in citi_bike.db that will hold all of the data pertaining to a particular CitiBike station
import sqlite3 as lite
con = lite.connect('./db/citi_bike.db')
cur = con.cursor()
with con:
    cur.execute('CREATE TABLE citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT )')

# Create the SQL statement that will be used to insert data into the citibike_reference table in citi_bike.db
sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

# Populate values in the citibike_reference table based on what we pull in from the citibike website
with con:
    for station in r.json()['stationBeanList']:
        #id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location)
        cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))

# Extract the 'id' column from the table and create a list that I'll use to create a table where the columns are the station id's
station_ids = df['id'].tolist()

# We can't have integer values as columns, so we add '_' to the station name and also add the data type for when we create the table with these columns in the SQLite db
station_ids = ('_' + str(x) + ' INT' for x in station_ids)

# Create the table 'available_bikes' with the _station_id's as columns
with con: 
    cur.execute("CREATE TABLE available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")
