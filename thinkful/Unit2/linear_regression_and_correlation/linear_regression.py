import pandas as pd

# Import the Lending Club dataset
#
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Remove any empty cells in the data set
#
loansData.dromna(inplace=True)

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
