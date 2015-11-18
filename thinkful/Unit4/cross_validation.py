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

    # Remove % from interest rates and convert to 4-precision float
    cleanRates = pd.Series( (round((float(rate.rstrip('%')) / 100), 4)) for 
                rate in LOANS_DATA['Interest.Rate'] )

    # Remove the word 'months' from the loan term length
    cleanTerms = pd.Series( float(term.rstrip(' months')) for 
                term in LOANS_DATA['Loan.Length'] )

    # Pick lower limit of lendees FICO score as their FICO score
    cleanScore = pd.Series( float(score.rpartition('-')[0]) for 
                score in LOANS_DATA['FICO.Range'] )

    cleanData = pd.DataFrame(columns=['Interest.Rate', 'Loan.Length', 'FICO.Range'])

    cleanData['Interest.Rate'] = cleanRates
    cleanData['Loan.Length'] = cleanTerms
    cleanData['FICO.Range'] = cleanScore

    return cleanData

###########################
# BUILD LINEAR REGRESSION #
###########################

def linReg(cleanData):

    # Create variables
    y = np.matrix(cleanData['Interest.Rate']).transpose()

    x1 = np.matrix(cleanData['Loan.Length']).transpose()
    x2 = np.matrix(cleanData['FICO.Range']).transpose()

    # Stack X1 and X2 for right side of equation
    # x_stack = np.column_stack([x1, x2])

    # Create the linear model
    #
    x = sm.add_constant(x2)
    model = sm.OLS(y, x)

    return model

#################################
# SHOW REGRESSION MODEL SUMMARY #
#################################
from datetime import datetime

startTime = datetime.now()
print linReg(clean()).fit().summary()
print ('\nScript took {} seconds to complete').format((datetime.now() - startTime).total_seconds())
