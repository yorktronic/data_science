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
import numpy as np

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
plt.clf()

# Who has the biggest swing?
swing_max_city = max(swings, key=swings.get)
swing_max_value = swings[swing_max_city]
swing_max = (swing_max_city, swing_max_value)

# Who has the larges variance?
var_max_city = max(variances, key=variances.get) 
var_max_value = variances[var_max_city]
var_max = (var_max_city, var_max_value)
# Answer: Seattle

# Plot the distribution of the difference from the mean for Seattle
# Create a list of all the differences
seattle_diff = []
for temp in maxTemps['seattle']:
	seattle_diff.append(means['seattle'] - temp)

seattle_diff_series = pd.Series(seattle_diff) # Convert the list in to a Series so that you can plot it

plt.figure()
qq_norm = stats.probplot(seattle_diff_series, dist='norm', plot=plt)
plt.savefig('./plots/seattle_difference_plot.png')
plt.clf()

# What was the highest temperature overall and where was it?
temp_max_value = 0
temp_max_city = ''
for city in ranges:
	if ranges[city][1] > temp_max_value:
		temp_max_value = ranges[city][1]
		temp_max_city = city
temp_max = (temp_max_city, temp_max_value)

# Plot a histogram of every city with temps rounded to the nearest degree F
# Convert the objects to numeric (otherwise we can't round them)
df = maxTemps.convert_objects(convert_numeric = True)
df = np.round(df, 0)

# Now, create the histogram for each city
for city in cities:
	plt.figure()
	df.hist(column = city)
	plt.subplots_adjust(bottom = 0.15)
	plt.savefig('./plots/histograms/{}_histogram.png'.format(city))
	plt.clf()

# Create a QQ plot of all cities against the normal distribution
for city in cities:
	plt.figure()
	qq_norm = stats.probplot(maxTemps[city], dist='norm', plot = plt)
	plt.savefig('./plots/qq_plots/{}_qq.png'.format(city))
	plt.clf()

plt.close()