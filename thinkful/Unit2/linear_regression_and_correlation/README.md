# Back to School - Linear Regression #

TL:DR - the interest rate you get on a loan is directly related to the loan term and your FICO Score. duh.

## linear_regression.py ##
This script takes in loan data from https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv, cleans it, and plots a histogram and scatterplot of the data

## linear_regression_analysis.py ##
Goes one step further and performs linear regression analysis to the same dataset. The purpose of this analysis is to test whether loan interest rate is directly related to the FICO score of the lendee and the length of the loan. This can be formulated with a simple linear algebra formula: 

interestRate = b + a1*FICOScore + a2*LoanLength

Where b is some constant, and a1 and a2 are coefficients that determine the relationship FICOScore and LoanLength have to interest rate. 

This analysis yeilds p-values of 0, 0, and 4.568e-203 (essentially zero for all intents and purposes), which basically eliminates the possibility of the null hypothesis. The R-squared value is 0.657, indicating that the model we've created explains roughly 66% of the variability in the data, which is pretty decent.

