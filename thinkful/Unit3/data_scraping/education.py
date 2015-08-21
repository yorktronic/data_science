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

# Pass the data to BeautifulSoup for parsing
soup = BeautifulSoup(r.content, 'lxml')

# Only scrape entries where class is tcont
table = soup.find_all(class_="tcont")

# Put all contries in a list of lists
# This will create blank entries for countries with spaces in their names
entries = []
for cont in table:
	entry = cont.get_text().encode('ascii', 'ignore').split('\n')
	entries.append(entry)

# Create a new list that does not contain any empty items (item = word)
clean_entries = []
for entry in entries:
	words = []
	for word in entry:
		if word != '':
			items.append(word)

	clean_entries.append(words)

