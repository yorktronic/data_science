#########################
#
# BROKEN due to missing data
# Study the relationship between doctor visits (mdvis) and both log income and the binary variable health status (hlthp)
# This code came from http://nbviewer.ipython.org/urls/s3.amazonaws.com/datarobotblog/notebooks/multiple_regression_in_python.ipynb#appendix
#
#########################

import pandas as pd

df = pd.read_csv('https://raw2.github.com/statsmodels/statsmodels/master/'
                 'statsmodels/datasets/randhie/src/randhie.csv')

#df["logincome"] = np.log1p(df.income)