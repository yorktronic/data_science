# Goal, write a script that prints out the cities with July being the warmest month

# Connect to the database
# Create the cities and weather tables
# Insert data into the two tables
# Join the data together
# Load into a pandas DataFrame
# Print out the resulting city and state in a full sentence
# Push code to github

import sqlite3 as lite
import pandas as pd

# Make some data
cities = (('New York City', 'NY'), ('Boston', 'MA'), ('Chicago', 'IL'), ('Miami', 'FL'), ('Seattle', 'WA'), ('Portland', 'OR'), ('Los Angeles', 'CA'), ('Washington', 'DC'), ('Houston', 'TX'), ('Las Vegas', 'NV'), ('Atlanta', 'GA'), ('San Francisco', 'CA'), ('Dallas', 'TX'), )

weather = (('Las Vegas', 2013, 'July', 'December', 90), ('Atlanta', 2013, 'July', 'January', 80), ('New York City', 2013, 'July', 'January', 62), ('Boston', 2013, 'July', 'January', 59), ('Chicago', 2013, 'July', 'January', 59), ('Miami', 2013, 'August', 'January', 84), ('Dallas', 2013, 'July', 'January', 77), ('Seattle', 2013, 'July', 'January', 61), ('Portland', 2013, 'July', 'December', 63), ('San Francisco', 2013, 'September', 'December', 64), ('Los Angeles', 2013, 'September', 'December', 75), ('Washington', 2013, 'July', 'January', 65), ('Houston', 2013, 'July', 'January', 79))

# Connect to the database (I created a new database rather than re-using the old one and erasing it)
con = lite.connect('../db/challenge.db')
# Create the cursor object
cur = con.cursor()

with con:
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("DROP TABLE IF EXISTS weather")
	cur.execute("CREATE TABLE cities (name text. state text)")
	cur.execute("CREATE TABLE weather (city text, year int, warm_month text, cold_month text, average_high int")
	cur.executemany("INSERT INTO cities VALUES(?,?)", cities)
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)", weather)
	



	


