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

###########################################
# Scrape United Nations education dataset #
###########################################

def getEducationData():

	# Pull the data from the UN website on archive.org
	url = 'http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm'
	r = requests.get(url)

	# Pass the data to BeautifulSoup (the scraper)
	soup = BeautifulSoup(r.content, 'lxml')

	# The data consists of the number of years men and women spend in school by country and year
	# avg is (men + women) / 2
	df = pd.DataFrame(columns=['country', 'year', 'avg', 'male', 'female'])

	# Get all the rows from soup (everything with a 'tr' tag within the correct indexes)
	rows = soup.findAll('tr')[18:-11]

	# Populate the dataframe with columnar data by parsing through each valid <td> HTML tag
	k = 0
	for row in rows:
		col = row.findAll('td')
		# The columns for country, year, average, male, and female are in 0,1,4,7, and 10
		df.loc[k] = [(col[0].text).encode('ascii', 'ignore'),int(col[1].text),int(col[4].text),int(col[7].text),
					int(col[10].text)]
		k += 1

	# Set the dataframe index to country
	df = df.set_index('country')

	return df

########################################
# Stats analysis of the data
########################################

def educationAnalysis(df):

	# RefactorMe
	stats = pd.DataFrame(columns=['gender', 'minCountry', 'min', 'maxCountry', 'max', 
							'median', 'mean'])
	avg = df['avg']
	male = df['male']
	female = df['female']

	minCountryMale = str(df[df['male'] == df['male'].min()].index.tolist()[0])
	minCountryFemale = str(df[df['female'] == df['female'].min()].index.tolist()[0])

	maxCountryMale = str(df[df['male'] == male.max()].index.tolist()[0])
	maxCountryFemale = str(df[df['female'] == female.max()].index.tolist()[0])

	minCountryAvg = str(df[df['avg'] == avg.min()].index.tolist()[0])
	maxCountryAvg = str(df[df['avg'] == avg.max()].index.tolist()[0])


	stats.loc[0] = ['male', minCountryMale, male.min(), maxCountryMale, male.max(), 
						male.median(), male.mean()]
	stats.loc[1] = ['female', minCountryFemale, female.min(), maxCountryFemale, female.max(),
						female.median(), female.mean()]
	stats.loc[2] = ['avg', minCountryAvg, avg.min(), maxCountryAvg, avg.max(), avg.median(), 
						avg.mean()]

	stats = stats.set_index('gender')

	return stats

########################################
# Pull in GDP data from the World Bank #
########################################

def getGdp():

	gdpData = pd.read_csv('./db/ny.gdp.mktp.cd_Indicator_en_csv_v2.csv', header=2)
	gdpData = gdpData.set_index('Country Name')

	# Drop some of the columns we don't need
	gdpData = gdpData.drop(gdpData.columns[[0, 1, 2, -1]], axis=1)

	# Remove years we don't need from the gdp data dataframe
	for year in gdpData.columns.values:
		if (int(year) < 1999 or int(year) > 2010):
			gdpData = gdpData.drop(year, 1)

	return gdpData

#############################################################
# Fuzzy string matching helper function for merging datasets
#############################################################

def fuzzThis(countries, choices):

		from fuzzywuzzy import fuzz
		from fuzzywuzzy import process

		for country in countries:
			print country
			print process.extractOne(country, choices)

##################################################################
# Add GDP data from appropriate dates to the education dataframe #
##################################################################

def mergeDatasets():

	# List countries in education dataframe but not in gdp dataframe
	educationNotGdp = []
	gdpNotEducation = []
	gdpCountries = list(gdpData.index)
	educationCountries = list(df.index)

	for country in educationCountries:
		if country not in gdpCountries:
			educationNotGdp.append(country)

	# fuzzThis(educationNotGdp, gdpCountries)

print educationAnalysis(getEducationData())

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