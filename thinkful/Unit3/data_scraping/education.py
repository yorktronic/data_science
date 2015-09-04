##############################
#
# Scrape data from a United Nations HTML dataset from archive.org
# 
##############################

# Import required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd

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
	df.loc[k] = [col[0].text,col[1].text,col[4].text,col[7].text,col[10].text]
	k += 1

# Set the dataframe index to country
df = df.set_index('country')