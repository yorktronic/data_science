# Calculates the population of all land under 90 meters elevation by continent as of 2010 data. Also calculates the population density of each continent in 2010.

# The script can also write this data to a file: that code is commented out at the bottom of the script.


import collections
population_dict = collections.defaultdict(int)
land_area = collections.defaultdict(int)
population_density = collections.defaultdict(float)

# Open the population data file with Unversal read
inputFile = open('./population_data/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU')

# Store and skip the header
header = next(inputFile)

# Add entries to populationdict for each continent, and sum the urban and rural populations of each continent
for line in inputFile:
	line = line.rstrip().split(',')
	line[5] = int(line[5])
	if line[1] == 'Total National Population':
 		population_dict[line[0]] += line[5]
 		land_area[line[0]] = int(line[7])


	#Calculates the population density
for k, v in population_dict.iteritems():
	population_density[k] = v / land_area[k]


# From the previous version where I wrote the populations to a file
# with open('national_population.csv', 'w') as outputFile:
    #outputFile.write('continent,2010_population\n')

    #for k, v in population_dict.iteritems():
     #   outputFile.write(k + ',' + str(v) + '\n')



