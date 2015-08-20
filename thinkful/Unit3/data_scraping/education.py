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

# Pass the data to BeautifulSoup
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
		if item != '':
			items.append(item)
	# Populate the list
	clean_entries.append(items)
