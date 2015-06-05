import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Read in the Lending Clug loansData.csv
loansData = pd.read_csv('./db/loansData.csv')

# Remove any rows that have null values
loansData.dropna(inplace = True)

data = loansData[['Amount.Requested', 'Amount.Funded.By.Investors']]

data.boxplot()
plt.savefig('./plots/boxplot_amt_requested_v_funded.png')
plt.clf()

data.hist()
plt.savefig('./plots/histogram_amt_requested_v_funded.png')
plt.clf()

