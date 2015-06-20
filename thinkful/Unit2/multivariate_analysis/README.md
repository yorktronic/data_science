# Multivariate Analysis #

## multivariate.py ##

### Purpose ###
(1) Analyze Lending Club loan data from January 1, 2015 to March 31, 2015 to determine how annual income is related to the interest rate Lending Club provides to lendees and 
(2) Test via multivariate analysis how annual income AND home ownership relate to interest rate

### Process ###
Pull in the data, clean it, then perform (1) and (2) and analyze the model fit summaries.

### Summary ###
Unless I'm missing something, it seems as though annual income and home ownership, both together and independently, have little to no influence on the interest rate that is offered to a lendee, which is actually pretty surprising. I knew that FICO was king in terms of determining one's credit-worthiness, but I thought that home ownership and income would have some bearing.

### Test Result - Interest Rate Influenced by Annual Income ###

                            OLS Regression Results
==============================================================================
Dep. Variable:               int_rate   **R-squared:                       0.011**
Model:                            OLS   Adj. R-squared:                  0.011
Method:                 Least Squares   F-statistic:                     927.8
Date:                Fri, 19 Jun 2015   Prob (F-statistic):          1.12e-202
Time:                        16:41:56   Log-Likelihood:             1.4602e+05
No. Observations:               84277   AIC:                        -2.920e+05
Df Residuals:                   84275   BIC:                        -2.920e+05
Df Model:                           1
Covariance Type:            nonrobust
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
const          0.1343      0.000    576.485      0.000         0.134     0.135
**annual_inc -7.279e-08**   2.39e-09    -30.460      0.000     -7.75e-08 -6.81e-08
==============================================================================
Omnibus:                     5376.847   Durbin-Watson:                   1.984
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             6810.697
Skew:                           0.610   Prob(JB):                         0.00
Kurtosis:                       3.673   Cond. No.                     1.54e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.54e+05. This might indicate that there are
strong multicollinearity or other numerical problems.

### Test Result - Interest Rate Influenced by Annual Income AND Home Ownership ###

Results from the multivariate analysis of whether and how interest rate is 
influenced by annual income AND home ownership

                            OLS Regression Results
==============================================================================
Dep. Variable:               int_rate   **R-squared:                       0.013**
Model:                            OLS   Adj. R-squared:                  0.013
Method:                 Least Squares   F-statistic:                     554.8
Date:                Fri, 19 Jun 2015   Prob (F-statistic):          4.05e-240
Time:                        16:46:09   Log-Likelihood:             1.4611e+05
No. Observations:               84277   AIC:                        -2.922e+05
Df Residuals:                   84274   BIC:                        -2.922e+05
Df Model:                           2
Covariance Type:            nonrobust
======================================================================================
                         coef    std err          t      P>|t|      [95.0% Conf. Int.]
--------------------------------------------------------------------------------------
const                  0.1319      0.000    454.411      0.000         0.131     0.133
**annual_inc         -6.776e-08**   2.42e-09    -28.044      0.000     -7.25e-08  -6.3e-08
**home_ownership_int     0.0021**      0.000     13.413      0.000         0.002     0.002
==============================================================================
Omnibus:                     5076.403   Durbin-Watson:                   1.983
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             6197.406
Skew:                           0.607   Prob(JB):                         0.00
Kurtosis:                       3.540   Cond. No.                     2.04e+05
==============================================================================

Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 2.04e+05. This might indicate that there are
strong multicollinearity or other numerical problems.