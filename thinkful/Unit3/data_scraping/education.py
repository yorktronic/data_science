##############################
#
# Learning to scrape data from HTML - gonna scrape some UN data, yo
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

# This gets you some of the way there, but you end up with a bunch of empty list entries. Will need to loop through and remove anything that is empty

entries = []

for cont in table:
	entry = cont.get_text().encode('ascii', 'ignore').split('\n')
	entries.append(entry)

# Manually go in to the list and remove + correct the countries that are messed up?
clean_entries = []

for entry in entries:
	items = []
	for item in entry:
		if item != '':
			items.append(item)

	clean_entries.append(items)
