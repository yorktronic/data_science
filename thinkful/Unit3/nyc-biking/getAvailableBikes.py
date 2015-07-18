####################################
#
# Updates the available_bikes table in ./db/citi_bike.db with a new entry
#
####################################

# Import the requests library
import requests 

# Pull the data json object from citibike's website
r = requests.get('http://www.citibikenyc.com/stations/json')

# Package with datetime objects
import time

# Package for parsing a string date value into a Python datetime object
from dateutil.parser import parse

# Take the string and parse it in to a Python datetime object, which will be the time at which the data was added to the database
exec_time = parse(r.json()['executionTime'])

# Import the sqlite3 library and connect to the database
import sqlite3 as lite
con = lite.connect('./db/citi_bike.db')
cur = con.cursor()

# Since I'm only interested in storing the station data every minute for one hour, the exec_time is a seconds value
with con:
    cur.execute("INSERT INTO available_bikes (execution_time) VALUES (?)", (exec_time.strftime('%M'),))

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
        cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + exec_time.strftime('%M') + ";")
