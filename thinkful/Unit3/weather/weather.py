####################################
#
# Pull data from cities throughout the United States and determine which state had the largest temperature swing for a given month
#
####################################

# Import required libraries
import datetime
import pandas as pd
import requests
import sqlite3 as lite

# Latitude and longitude of the cities that we'll be querying
cities = {"atlanta": '33.762909,-84.422675', 
			 "austin": '30.303936,-97.754355',
			 "boston": '42.331960,-71.020173', 
			 "chicago": '41.837551,-87.681844',
			 "cleveland": '41.478462,-81.679435',
			 "denver": '39.761850,-104.881105',
			 "lasVegas": '36.229214,-115.26008',
			 "losAngeles": '34.019394,-118.410825',
			 "miami": '25.775163,-80.208615',
			 "minneapolis": '44.963324,-93.268320',
			 "nashville":  '36.171800,-86.785002',
			 "newOrleans": '30.053420,-89.934502',
			 "newYork":  '40.663619,-73.938589',
			 "philadelphia": '40.009376,-75.133346',
			 "phoenix": '33.572154,-112.090132',
			 "saltLakeCity": '40.778996,-111.932630',
			 "sanFrancisco": '37.727239,-123.032229',
			 "seattle": '47.620499,-122.350876',
			 "washington": '38.904103,-77.017229'}

# API key for forecast.io
apiKey = 'b4aac1bc1eeff8f5ba9a3d12d72182c4'

# Formatting string for datetime object, because Windows is stupid
dateFormat = '%Y-%m-%d %H:%M:%S'

# startDate is 30 days ago today, converted to integer epoch time
startDate = int(((datetime.datetime.now() - datetime.timedelta(days=30)) - datetime.datetime(1970,1,1)).total_seconds())

time = startDate

# Get the daily max temperature from the JSON object
#tempMax = r.json()['daily']['data'][0]['temperatureMax']

# sql table creation string
createTable = 'CREATE TABLE daily_max_temperature (date INT PRIMARY KEY, '

# INSERT INTO string
sql = "INSERT INTO daily_max_temperature (date, "

# Loop through the cities dictionary to finish the CREATE TABLE and INSERT INTO statements
for k in cities:
	createTable += (k + ' TEXT, ')
	sql += (k + ', ')

# Remove the training whitespace and comma from both strings, add a close parenthesis, etc
createTable = createTable[:-2]
sql = sql[:-2]
createTable += ')'
sql += ') VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'

# Create the table in the database
con = lite.connect('./db/weather.db')
cur = con.cursor()
with con:
	cur.execute(createTable)

# Function that gets the max temps for the specified time (day) and returns a dict with the city name as the key and the max temp for that city
def getMaxTemps(t):
	
	maxTemps = {}
	
	for k in cities:
		
		# Create the API call string and get the JSON object from forecast.io
		# API call format: 'https://api.forecast.io/forecast/APIKEY/LATITUDE,LONGITUDE,TIME'
		apiCall = 'https://api.forecast.io/forecast/{}/{}/'.format(apiKey, (cities[k] + ',' + str(time)))
		r = requests.get(apiCall)

		# Get the max temp on this particular day from the JSON object and add it to the dictionary of max temps
		maxTemps[k] = r.json()['daily']['data'][0]['temperatureMax']

	return maxTemps

# Next, create a loop that calls getMaxTemps with a day, then takes the dictionary and uses its contents to update the database...