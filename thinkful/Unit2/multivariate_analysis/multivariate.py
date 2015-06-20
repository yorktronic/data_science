#########################
#
# Multivariate analysis of Loan Data from Lending Club, testing to see how annual income is correlated with interest rate, and how annual income AND home ownership is correlated with interest rate
#
#########################

# Import required libraries
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Import the 2015 - 3/31/2015 data on approved loans. The 0th row of the csv has useless text so specify the header starts at row 1
df = pd.read_csv('./db/LoanStats3d.csv', header=1)

# Make a new dataframe with only the columns we need
# Note: there has to be a way to do this in an automated fashion, but I don't know how yet
#
loansData = pd.DataFrame(index = df.index, columns=['int_rate', 'annual_inc', 'home_ownership'])
loansData['int_rate'] = df['int_rate']
loansData['annual_inc'] = df['annual_inc']
loansData['home_ownership'] = df['home_ownership']

# Drop any rows with empty cells
loansData.dropna(inplace=True)

#Convert the interest rate from a string to an integer
cleanRate = loansData['int_rate'].map(lambda x: round((float(x.rstrip('%')) / 100), 4))
loansData['int_rate'] = cleanRate

# Convert home_ownership to a categorical variable
loansData['home_ownership_int'] = pd.Categorical(loansData.home_ownership).codes

# Create the right side of the model
#X = loansData[['annual_inc', 'home_ownership_int']]
X = np.column_stack([loansData['annual_inc'], loansData['home_ownership_int']])

#fit a OLS model
X = sm.add_constant(X)
model = sm.OLS(loansData['int_rate'], X)

