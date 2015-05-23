# Determine the population increase in the low elevation zones of each country from the year 2010 to the year 2100

# Input = population data file
# Output = two dictionaries, one with the population differences in numbers, and the other by percentage. 

# Update this to output a single disct that has a tuple of (percentage, number) for the population change

import collections
population_2010 = collections.defaultdict(int)
population_2100 = collections.defaultdict(int)

# This dictionary will contain a 2-entry list for each country. The first entry will be % change in population, the second entry will be the total difference in population
population_diff = collections.defaultdict(int)
population_percentage_diff = collections.defaultdict(float)

# Open the population data file 
inputFile = open('./population_data/lecz-urban-rural-population-land-area-estimates_country-90m.csv','rU')

# Store and skip the header
header = next(inputFile)

# Add each countries 2010 population to population_2010, and add each contries 2100 population to populatio_2100

for line in inputFile:
	line = line.rstrip().split(',')
	
	line[11] = int(line[11])
	line[12] = int(line[12])

	population_2010[line[2]] += line[11]
	population_2100[line[2]] += line[12]

# Populate percentages
for k, v in population_2010.iteritems():
	population_diff[k] = population_2100[k] - v

	if population_2100[k] > population_2010[k]:
		population_percentage_diff[k] = "%.2f" % ((((float(population_2100[k]) / float(v)) - 1) * 100))
	elif population_2100[k] < population_2010[k]:
		population_percentage_diff[k] = "%.2f" % (-(1 - ((float(population_2100[k]) / float(v))))*100)
	else:
		population_percentage_diff[k] = 0.0









