####################################
#
# Perform ARIMA Analysis with loan data
# ARIMA = Auto-Regressive Integrated Moving Average
# General idea: A Series can be expressed as a function of its most recent observation.
# Auto-regressive: a regression of an observation on itself - running a regression on an observation using previous observations as explanatory variables as well as a trend component of the forecast errors (moving average)
# ARIMA models assume that the time-series is stationary, i.e. the mean, variance, etc don't change over time
#
####################################


import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

# Import the 2013-2015 data on loans
# Note: I tried to use parse_dates on this and it didn't work, I guess because of the way the dates are formatted
df = pd.read_csv('../multivariate_analysis/db/LoanStats3c.csv', header=1, low_memory=False)

# Drop the last two rows from the dataframe - they contain summary data that doesn't fit in the dataframe columns 
df = df.drop(df.tail(2).index)

# Convert strings to datetime objects in pandas (
df['issue_d_format'] = pd.to_datetime(df['issue_d'])

# Setting the index on the datetime-formatted issue date
df2 = df.set_index('issue_d_format')

# Groups the rows by months
# For more information on groupby: http://pandas.pydata.org/pandas-docs/stable/groupby.html
year_month_summary = df2.groupby(lambda x : x.month).count()
loan_count_summary = year_month_summary['issue_d']

# Create a plot of the number of loans per month 
loan_count_summary.plot()
plt.savefig('./plots/loan_count_per_month.png')
plt.clf()

# Create an ACF plot 
fig = sm.graphics.tsa.plot_acf(loan_count_summary.values)
plt.savefig('./plots/ACF_plot.png')
plt.clf()

# Create a PACF plot
fig = sm.graphics.tsa.plot_pacf(loan_count_summary.values)
plt.savefig('./plots/PACF_plot.png')