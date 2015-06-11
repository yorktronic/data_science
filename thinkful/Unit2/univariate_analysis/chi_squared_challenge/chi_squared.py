# Goodness of fit: the Chi-Square Test
#####

# A chi-squared distribution of k degrees of freedom is a distribution of the sum of the squares of all the k variables, where k is an independent standard normal random variable

from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

# Loads the reduced version of the Lending Club dataset
loansData = pd.read_csv('../db/loansData.csv')
# Drop null rows
loansData.dropna(inplace = True)

# Store the data from the Open.Credit.Lines column in a variable for cleaner code
ocl = loansData['Open.CREDIT.Lines']

# Sum the items in Open.Credit.Lines to get the total number of open credit lines
print 'The total number of open credit lines is {}'.format(ocl.sum())

# Find the max number of open credit lines and print it
print 'The maximum number of open credit lines is {}'.format(ocl.max())

# Find the most frequent number of open credit lines (mode)
print 'The most frequent number of open credit lines is {}'.format(stats.mode(ocl)[0][0])

# ...average number of open credit lines
print 'The average number of open credit lines is {}'.format(ocl.mean())

# median number of open credit lines
print 'The median number of open credit lines is {}'.format(ocl.median())

freq = collections.Counter(loansData['Open.CREDIT.Lines'])

# Calculate the chi-square test on the Open.CREDIT.Lines data. Note, without specifying f_exp in the test, which would be an array_like variable with the specified probabilities of each value in the dataset, the test assumes that each value is of equal probability
chi, p = stats.chisquare(freq.values())

print 'The result of the chi-squared test on the Open.CREDIT.Lines data is {}, with a p-value of {}'.format(chi,p)