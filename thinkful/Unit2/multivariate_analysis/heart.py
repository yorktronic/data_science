#########################
#
# Multivariate analysis investigating chronic heart disease

# This code is courtesy of: http://nbviewer.ipython.org/urls/s3.amazonaws.com/datarobotblog/notebooks/multiple_regression_in_python.ipynb
#
#########################

# Import required libraries
import pandas as pd

# Import dataset
df = pd.read_csv('http://statweb.stanford.edu/~tibs/ElemStatLearn/datasets/SAheart.data', index_col=0)

# copy data and separate predictors and response
X = df.copy()
y = X.pop('chd')

# print the first five rows of the dataset
print df.head()

# compute percentage of chronic heart disease for famhist
print y.groupby(X.famhist).mean()

# famhist is a binary variable (absent / present family history of heart disease), and we can perform a linear regression on them after we convert them to numeric

import statsmodels.formula.api as smf

# encode df.famhist as a numberic via pd.Factor in a new column
df['famhist_ord'] = pd.Categorical(df.famhist).codes

est = smf.ols(formula="chd ~ famhist_ord", data=df).fit()

'''
# another way to encode categorical variables is dummy-encoding, which encodes a k-level categorical varaible into k-1 binary variables. In statsmodels this is done easily using the C() function
def short_summary(est):
	return est.summary().tables[1]

# fit OLS on categorical variables children and occupation
est = smf.ols(formula='chd ~ C(famhist)', data = df).fit()

'''

# looking at est.summary().tables[1], the estimated percentage with chronic heart diesease when famhist = present is 0.2370 + 0.2630 = 0.5000 and the estimated percentage with chronic heart diesease when famhist = absent is 0.2370

