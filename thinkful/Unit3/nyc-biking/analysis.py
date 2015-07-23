# Analyzing one hour's worth of Citi Bike data in NYC (data logged every minute)

# Import required libraries
import pandas as pd
import sqlite3 as lite
import collections
import datetime

# Connect to the SQLite database
con = lite.connect('./db/citi_bike.db')
cur = con.cursor()

# Read in the data as a dataframe
df = pd.read_sql_query("SELECT * FROM available_bikes ORDER BY execution_time", con, index_col='execution_time')

# Create a defaultdict of integers for the amount of change in an hour
hour_change = collections.defaultdict(int)

# For each column, turn it in to a list, remove the "_" in the column name 
for col in df.columns:
	station_vals = df[col].tolist()
	station_id = col[1:] # Removing the '_' from the column name
	station_change = 0

	# Recurse through the values in each column, taking each difference along the way and adding it to station_change, in order to determine the total change in bikes for that station over the hour
	for k,v in enumerate(station_vals):
		if k < len(station_vals) - 1:
			station_change += abs(station_vals[k] - station_vals[k+1])
	
	# Store the total change for each station in the dictionary hour_change
	hour_change[int(station_id)] = station_change

# Now, we find the winner!
def keywithmaxval(d):
	v = list(d.values())
	k = list(d.keys())

	# return the key with the max value
	# fwiw this is allegedly the fastest way to perform this operation in python
	return k[v.index(max(v))]

max_station = keywithmaxval(hour_change)
# Now, query the reference table for information about the highest-traffic station
cur.execute("SELECT id, stationname, latitude, longitude FROM citibike_reference where id = ?", (max_station,))

# Store this query as a variable
data = cur.fetchone()

# Print the most active station
print "The most active station is station id %s at %s latitude: %s longitude: %s" % data

# Print the information on that station
print "With " + str(hour_change[max_station]) + " bicycles coming and going in the hour between " + datetime.datetime.fromtimestamp(int(df.index[0])).strftime('%Y-%m-%d %H:%M:%S') + " and " + datetime.datetime.fromtimestamp(int(df.index[-1])).strftime('%Y-%m-%d %H:%M:%S')

# Plot the results
import matplotlib.pyplot as plt
plt.bar(hour_change.keys(), hour_change.values())
plt.savefig('./plots/num-bikes-in-and-out-in-one-hour.png')
