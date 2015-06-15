import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Import the Lending Club dataset
#
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Remove any empty cells in the data set
#
loansData.dropna(inplace=True)

# Create a new set of interest rates, removing the % from the interest rate and and converting it into a 4-digit decimal
#
cleanRate = loansData['Interest.Rate'].map(lambda x: round((float(x.rstrip('%')) / 100), 4))

#...FICO scores by picking the first value out of the range
#
cleanFICO = loansData['FICO.Range'].map(lambda x: int(x.split('-')[0]))

# add these two sets as new columns in the data set (NOTE: this way only works if you know that the index values of the DataFrame are continuous. If you are dealing with non-continuous index values, see http://stackoverflow.com/questions/12555323/adding-new-column-to-existing-dataframe-in-python-pandas for the proper solution)
#

loansData['FICO.Score'] = cleanFICO
loansData['Clean.Interest.Rate'] = cleanRate

# Create the histogram
#
#plt.figure()
loansData.hist(column='FICO.Score')

# Tweak the spacing to prevent clipping of tick-labels
#
plt.subplots_adjust(bottom=0.15)

# Show the histogram
# 
plt.show()
plt.clf()

# Note - if we had wanted to rotate the x-axis labels, we could've used: plt.xticks(rotation='vertical')

scat = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
plt.show()
