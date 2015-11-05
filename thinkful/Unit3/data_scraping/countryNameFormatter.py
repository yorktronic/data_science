##############################
#
# Takes in an array (or Series?) of country names and runs them through REST Countries
# (https://restcountries.eu/) to attempt to match them to standardized country names.
# If successful, it pairs the country names with country codes to make matching easier
#
##############################

import pandas as pd
import requests

testData = ['United States of America', 'Afghanistan', 'Fiji', 'Uzbekistan', 'New Freeland', 'Aruba']

def formatter(countries):
	allCountries = requests.get('https://restcountries.eu/rest/v1/all')
	# loop through the passed in list and print out matches and lack of matches
