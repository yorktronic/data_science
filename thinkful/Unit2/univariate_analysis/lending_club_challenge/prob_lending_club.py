import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Read in the Lending Clug loansData.csv
loansData = pd.read_csv('./db/loansData.csv')

# Remove any rows that have null values
loansData.dropna(inplace = True)

data = loansData[['Amount.Requested', 'Amount.Funded.By.Investors']]

# Rather than just plotting the Amount Requested by itself, I created a boxplot and a histogram with both Amount Requested and Amount Funded by Investors on the same plot
plt.figure()
data.boxplot()
plt.savefig('./plots/boxplot_amt_requested_v_funded.png')
plt.clf()


data.hist()
plt.savefig('./plots/histogram_amt_requested_v_funded.png')
plt.clf()

# I don't think the QQ plot can handle two plots on the same figure, so I'm plotting them independently
stats.probplot(loansData['Amount.Funded.By.Investors'], dist = "norm", plot = plt)
plt.savefig('./plots/amt_funded_by_investors_v_normal_distribution.png')
plt.clf()
