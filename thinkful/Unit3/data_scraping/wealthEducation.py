# Don't read this

for i, row in enumerate(table.findAll('tr')[4:]):
 col = row.findAll('td')
 #fix unicode, and convert to integers
 df.loc[i] = [col[0].text.encode('utf-8'), int(col[1].text.encode('utf-8')), int(col[4].text.encode('utf-8')), int(col[7].text.encode('utf-8')), int(col[10].text.encode('utf-8'))]





 for i in soup.findAll('tr')[8:-11]:
     col=i.findAll('td')
     df.loc[k]= [col[0].text,col[1].text,col[4].text,col[7].text,col[10].text]
     k+=1


# Cut out most of what you don't need
# "tr"
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