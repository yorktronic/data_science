####################################
#
# This script pulls in data from the NYC CitiBike program to analyze the number of available bikes throughout the city every minute for one hour
# It updates an existing SQL database containing tables created in OTHER SCRIPT
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

# Package with datetime objects
import time

# Package for parsing a string date value into a Python datetime object
from dateutil.parser import parse

# Take the string and parse it in to a Python datetime object, which will be the time at which the data was added to the database
exec_time = parse(r.json()['executionTime'])

# Since I'm only interested in storing the station data every minute for one hour, the exec_time is a seconds value
with con:
    cur.execute("INSERT INTO available_bikes (execution_time) VALUES (?)", (exec_time.strftime("{}:{}:{}".format('%H','%M','%S')),))

# Import the collections library 
import collections 

# Create a defaultdict to store bikes by station
id_bikes = collections.defaultdict(int) 

# Loop through the stations in stationBeanList and store the number of avilable bikes per station, by station id
for station in r.json()['stationBeanList']:
    id_bikes[station['id']] = station['availableBikes']

# iterate through the defaultdict to update the values in the available_bikes table
with con:
    for k, v in id_bikes.iteritems():
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%S') + ";")

