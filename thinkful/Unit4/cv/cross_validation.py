#############################################################################
#                                                                           #
# Linear regression and cross validation practice exercise using loans data #
# from Lending Club                                                         #
#                                                                           #
#############################################################################

import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
# from sklearn.svm import LinearSVC

# Import Lending Club loan data and drop empty cells
#
LOANS_DATA = pd.read_csv('./db/loansData.csv')
LOANS_DATA.dropna(inplace=True)


############################
# CLEAN DATA, BUILD NEW DF #
############################

def clean():

    # New dataframe for the cleaned data
    cleanData = pd.DataFrame(columns=['Interest.Rate', 'Loan.Length', 'FICO.Score', 
        'Amount.Requested'])

    # Remove % from interest rates and convert to 4-precision float
    cleanData['Interest.Rate'] = pd.Series( (round((float(rate.rstrip('%')) / 100), 4)) for 
                rate in LOANS_DATA['Interest.Rate'] )

    # Remove the word 'months' from the loan term length
    cleanData['Loan.Length'] = pd.Series( float(term.rstrip(' months')) for 
                term in LOANS_DATA['Loan.Length'] )

    # Pick lower limit of lendees FICO score as their FICO score
    cleanData['FICO.Score'] = pd.Series( float(score.rpartition('-')[0]) for 
                score in LOANS_DATA['FICO.Range'] )

    # Amount requested is moved over as-is
    cleanData['Amount.Requested'] = LOANS_DATA['Amount.Requested']

    return cleanData


###########################
# BUILD LINEAR REGRESSION #
###########################

def linReg(cleanData):

    # Create variables
    y = np.matrix(cleanData['Interest.Rate']).transpose()

    # FICO Score and Loan Length are the most reliable predictors, loan amount is excluded
    x1 = np.matrix(cleanData['FICO.Score']).transpose()
    x2 = np.matrix(cleanData['Loan.Length']).transpose()
    
    # Stack X1 and X2 for right side of equation
    x_stack = np.column_stack([x1, x2])

    # Create the linear model
    #
    x = sm.add_constant(x_stack)
    model = sm.OLS(y, x)

    return model

###############################################
# CROSS VALIDATION OF LINEAR REGRESSION MODEL #
###############################################

def kfCrossVal(loansData):
    
    # Import required libraries
    from sklearn.cross_validation import cross_val_predict
    from sklearn import linear_model
    import sklearn.metrics as met
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import PolynomialFeatures

    # Create linear regression model using FICO score as the only predictor
    # Interest Rate is the dependent variable
    lr = linear_model.LinearRegression()
    y = loansData.as_matrix(columns=['Interest.Rate'])
    x = loansData[['Loan.Length', 'FICO.Score']].as_matrix()

    # Run the kfold cross validation and store the results as an array
    predicted = cross_val_predict(lr, x, y, cv=10)

    # Try and run as quadratic?
    # POLY2 = smf.ols(formula = 'Y ~ 1 + X + I(X**2)', data=TRAIN_DF).fit()

    # Calculate MAE, MSE, and R2
    print("Mean Absolute Error: {}".format(met.mean_absolute_error(y, predicted)))
    print("Mean Squared Error: {}".format(met.mean_squared_error(y, predicted)))
    print("R Squared: {}".format(met.r2_score(y, predicted)))

    # Plot the actual versus predicted values
    fix, ax = plt.subplots()
    ax.scatter(y, predicted)
    ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
    ax.set_xlabel('Measured')
    ax.set_ylabel('Predicted')
    plt.show()

#################################
# SHOW REGRESSION MODEL SUMMARY #
#################################

def linRegSummary():
    from datetime import datetime

    startTime = datetime.now()
    print linReg(clean()).fit().summary()
    print ('\nScript took {} seconds to complete').format((datetime.now() - startTime).total_seconds())

