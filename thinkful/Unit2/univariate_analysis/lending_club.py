import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# Read in the Lending Clug loansData.csv
loansData = pd.read_csv('./db/loansData.csv')

# Remove any rows that have null values
loansData.dropna(inplace = True)

# Box plot the Amount Funded By Investors Column

#plt.figure()
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.show()
plt.clf() # Close the plot so that we can run another one

# Plot a histogram of the same data
#plt.figure()
loansData.hist(column='Amount.Funded.By.Investors')
plt.show()
plt.clf()

#plt.figure()
stats.probplot(loansData['Amount.Funded.By.Investors'], dist = "norm", plot = plt)
plt.show()
plt.clf()