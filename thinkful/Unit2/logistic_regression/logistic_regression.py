import pandas as pd
import statsmodels.api as sm
import numpy as np

# Import the cleaned lending club data from the linear regression lessons
# 
loansData = pd.read_csv('../linear_regression_and_correlation/db/loansData_clean.csv')

# Set the maximum interest rate for future testing
# 
maxInterest = 0.12

# Create a column in the dataframe to hold a binary variable - whether or not the interest rate is below 12% (0.12). 0 indicates the value is less than 12%, 1 indicates the value is more than 12%
#
# Simple function that gets the 0 or 1
def less_max(i):
	if i <= maxInterest:
		return 0
	else:
		return 1

# Create the column of data
ir_tf = loansData['Interest.Rate'].map(lambda x: less_max(x))

# Add the data to the dataframe
loansData['IR_TF'] = ir_tf

# Create an intercept column
loansData['Intercept'] = 1

# Create a list of column names of all independent variables
ind_vars = ['Amount.Requested', 'FICO.Score', 'Intercept']

# Define the logistic regression model
#
logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])

# Fit the model
#
result = logit.fit()

# Get the fitted coefficients from the results
# 
coeff = result.params
print coeff

# This function will return p (the probability that you'll get a loan with an interest rate under 12% given your fico score and the loan amount you're requesting). We're going to access the coefficients produced by the logit.fit() above, which outputs a series where 0, 1, and 2 are the indicies for the coefficients of Loan.Amount, FICO.Score, and Intercept respectively
#
# First, let's get the constants
loan_amt_c = coeff[0]
fico_c = coeff[1]
intercept_c = coeff[2]

# Now, the function. There's some math behind this, which I may or may not explain later.
def logistic_function(fico, loan_amt):
	return (1 / (1 + np.exp(intercept_c + (fico_c * fico) + (loan_amt_c * loan_amt))))

