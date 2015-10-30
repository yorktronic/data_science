##############################
#
# Scrape data from a United Nations HTML dataset from archive.org
# The data contains the "educational life expectancy" of men and women in school, broken up
# by country and year. The number of years a person is expected to be in school. 
#
##############################

# Import required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import sqlite3 as lite

# Pull the data
url = 'http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm'
r = requests.get(url)

# Pass the data to BeautifulSoup (the scraper)
soup = BeautifulSoup(r.content, 'lxml')

# Create a dataframe to hold the data
# The data consists of the number of years men and women spend in school by country and year
# avg is (men + women) / 2
df = pd.DataFrame(columns=['country', 'year', 'avg', 'male', 'female'])

# Get all the rows from soup (everything with a 'tr' tag within the correct indexes)
rows = soup.findAll('tr')[18:-11]

# Loop through the rows to get the data from each column
k = 0
for row in rows:
	col = row.findAll('td')
	# The columns for country, year, average, male, and female are in 0,1,4,7, and 10
	df.loc[k] = [(col[0].text).encode('ascii', 'ignore'),int(col[1].text),int(col[4].text),int(col[7].text),
					int(col[10].text)]
	k += 1

# Set the dataframe index to country
df = df.set_index('country')

########################################
# Stats analysis of the data #
########################################

stats = pd.DataFrame(columns=['gender', 'minCountry', 'min', 'maxCountry', 'max', 
							'median', 'mean'])
avg = df['avg']
male = df['male']
female = df['female']

minCountryMale = str(df[df['male'] == male.min()].index.tolist()[0])
minCountryFemale = str(df[df['female'] == male.min()].index.tolist()[0])

maxCountryMale = str(df[df['male'] == male.max()].index.tolist()[0])
maxCountryFemale = str(df[df['female'] == male.max()].index.tolist()[0])

minCountryAvg = str(df[df['avg'] == avg.min()].index.tolist()[0])
maxCountryAvg = str(df[df['avg'] == avg.max()].index.tolist()[0])


stats.loc[0] = ['male', minCountryMale, male.min(), maxCountryMale, male.max(), 
						male.median(), male.mean()]
stats.loc[1] = ['female', minCountryFemale, female.min(), maxCountryFemale, female.max(),
						female.median(), female.mean()]
stats.loc[2] = ['avg', minCountryAvg, avg.min(), maxCountryAvg, avg.max(), avg.median(), 
						avg.mean()]

stats = stats.set_index('gender')

########################################
# Pull in GDP data from the World Bank #
########################################
gdpData = pd.read_csv('./db/ny.gdp.mktp.cd_Indicator_en_csv_v2.csv', header=2)
gdpData = gdpData.set_index('Country Name') # set the index to country name to match our education dataframe

# Drop some of the columns we don't need
gdpData = gdpData.drop(gdpData.columns[[0, 1, 2, -1]], axis=1)

# Create a list of the column names to filter out the years we don't need
gdpColumns = list(gdpData.columns.values)

# Remove years we don't need from the gdp data dataframe
for column in gdpColumns:
	if (int(column) < 1999) or (int(column) > 2010):
		gdpData = gdpData.drop(column, 1)

##################################################################
# Add GDP data from appropriate dates to the education dataframe #
##################################################################

# List countries in education dataframe but not in gdp dataframe
educationNotGdp = []
gdpNotEducation = []
gdpCountries = list(gdpData.index)
educationCountries = list(df.index)

for country in educationCountries:
	if country not in gdpCountries:
		educationNotGdp.append(country)

def fuzzThis(countries, choices):
	from fuzzywuzzy import fuzz
	from fuzzywuzzy import process

	matches = {}
	for country in countries:
		print country
		print process.extractOne(country, choices)

fuzzThis(educationNotGdp, gdpCountries)

# Old code from when I though I was going to create a SQL database for this problem, which I 
# probably am not going to do

'''
# Create the database
createTable = 'CREATE TABLE gdp (country_name TEXT PRIMARY KEY, _1999 INT, _2000 INT, _2001 INT, _2002 INT, _2003 INT, _2004 INT, _2005 INT, _2006 INT, _2007 INT, _2008 INT, _2009 INT, _2010 INT)'

con = lite.connect('./db/gdp.db')
cur = con.cursor()

with con:
	cur.execute("DROP TABLE IF EXISTS gdp")
	cur.execute(createTable)

# Parse through the gdp data in the CSV file from the world bank
import csv

with open('./db/ny.gdp.mktp.cd_Indicator_en_csv_v2.csv', 'rU') as inputFile:
	next(inputFile) # skip the first two lines
	next(inputFile)
	header = next(inputFile)
	inputReader = csv.reader(inputFile)

	for line in inputReader:
		with con:
			cur.execute('INSERT INTO gdp (country_name, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES ("' + line[0] + '","' + '","'.join(line[42:-5]) + '");')
			'''