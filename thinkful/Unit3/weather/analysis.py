##############################
#
# Analysis of weather data from forecast.io, pulled by weather.py
#
##############################

# Import required libraries
import sqlite3 as lite
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Connect to the database
con = lite.connect('./db/weather.db')
maxTemps = pd.read_sql_query("SELECT * FROM daily_max_temperature", con)

# List of cities, to make things easy
cities = ['atlanta', 'austin', 'boston', 'chicago', 'cleveland', 'denver', 'lasVegas', 'miami', 'minneapolis', 'nashville', 'newOrleans', 'newYork', 'philadelphia', 'phoenix', 'saltLakeCity', 'sanFrancisco', 'seattle', 'washington']

# Calculate the range, mean, median, and variance of each city in the list
ranges = {}
swings = {}
means = {}
medians = {}
variances = {}

for city in cities:
	# All values are rounded to two decimal places
	ranges[city] = (float("{0:.2f}".format(maxTemps[city].min())), 
							float("{0:.2f}".format(maxTemps[city].max()))) 
							# Tuple in the form of (min, max)
	swings[city] = float("{0:.2f}".format(maxTemps[city].max() - maxTemps[city].min()))
	means[city] = float("{0:.2f}".format(maxTemps[city].mean()))
	medians[city] = float("{0:.2f}".format(maxTemps[city].median()))
	variances[city] = float("{0:.2f}".format(maxTemps[city].var()))

# Plot the temperature swings as a bar chart
plt.bar(range(len(swings)), swings.values(), align="center")
plt.xticks(range(len(swings)), list(swings.keys()), rotation="vertical")
plt.subplots_adjust(bottom=0.19)
plt.savefig('./plots/swings.png')

# Who has the biggest swing?

# Who has the larges variance?
var_max = max(variances, key=variances.get) # Seattle, 45.88

# What was the highest temperature overall and where was it?

# Try and fit each temperature range to the normal distribution?

# What patterns are there in the data?

# Histogram?