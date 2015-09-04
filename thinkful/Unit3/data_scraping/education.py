##############################
#
# Scrape data from a United Nations HTML dataset from archive.org
# 
##############################

# Import required libraries
from bs4 import BeautifulSoup
import requests

# Pull the data
url = 'http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm'
r = requests.get(url)

# Pass the data to BeautifulSoup (the scraper)
soup = BeautifulSoup(r.content, 'lxml')

# Cut out most of what you don't need
table = soup.find_all(class_="tcont")

# Create empty list for entries
entries = []

# Add the entry from each cont to entries
for cont in table:
	# Grab the data based on newlines
	# This will add blank data to the list for countries with more than one word in their name
	entry = cont.get_text().encode('ascii', 'ignore').split('\n')
	entries.append(entry)

# Create a new list to resolve the countries with blank entries for their name 
clean_entries = []
# Check for blank entries
for entry in entries:
	items = []
	for item in entry:
		if item not in ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
		'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
			items.append(item)
	# Populate the list
	clean_entries.append(items)

# Drop the last six entries, they are legend data
clean_entries = clean_entries[:-6]

# Create dataframe with country, year, male, and female life expectancy
import pandas as pd
df = pd.DataFrame(clean_entries, columns=['country', 'year', 'avg', 'male', 'female'])
df = df.set_index('country')