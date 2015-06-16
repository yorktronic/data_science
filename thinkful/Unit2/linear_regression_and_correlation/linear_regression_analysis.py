import pandas as pd
import numpy as np
import statsmodels.api as sm

# Import the Lending Club dataset
#
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# Remove any empty cells in the data set
#
loansData.dropna(inplace=True)

# Create a new set of interest rates, removing the % from the interest rate and and converting it into a 4-digit decimal
#
cleanRate = loansData['Interest.Rate'].map(lambda x: round((float(x.rstrip('%')) / 100), 4))

# Create a new set of loan lengths with the word "months" removed
# 
noMonths = loansData['Loan.Length'].map(lambda x: x.rstrip(' months'))

#...FICO scores by picking the first value out of the range
#
cleanFICO = loansData['FICO.Range'].map(lambda x: int(x.split('-')[0]))

# replace Interest.Rate and Loan.Length with the cleaned versions, and add FICO.Score as a new column (NOTE: this way only works if you know that the index values of the DataFrame are continuous. If you are dealing with non-continuous index values, see http://stackoverflow.com/questions/12555323/adding-new-column-to-existing-dataframe-in-python-pandas for the proper solution)
#
loansData['FICO.Score'] = cleanFICO
loansData['Interest.Rate'] = cleanRate
loansData['Loan.Length'] = noMonths

# Now we're going to define the relationship: InterestRate = b + a1(FICOScore) + a2(LoanAmount), where b is some constant, and a1 and a2 coefficients defining the relationship between FICOScore and LoanAmount to InterestRate
#
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

# Convert intrate, loanamt, and fico from a Series datatype into the numpy matrix datatype
# 
# The dependent variable (i.e. it's value is directly dependent on the values on loanamt and fico score, or so we believe :)
y = np.matrix(intrate).transpose()
# The independent variables
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()

# Stack the fico and loanamt variables to form value pairs
# 
x = np.column_stack([x1, x2])

# Create the linear model
#
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()



