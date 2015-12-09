import graphlab as gl
import pandas as pd

# Import ideal v. actual weight dataset
df = pd.read_csv('./db/ideal_weight.csv')

# Remove single quotes from column names
df.columns = ['id', 'sex', 'actual', 'ideal', 'diff']

# Remove single quotes from gender values
clean_genders = []

male = 0
female = 0

for g in df['sex']:
    if g == "'Male'":
        clean_genders.append('male')
        male += 1
    elif g == "'Female'":
        clean_genders.append('female')
        female += 1

df['sex'] = clean_genders

# Plot the distribution of actual and ideal weight
import matplotlib.pyplot as plt
import numpy as np
bins = np.linspace(0, 235, 100)

plt.hist(df['actual'], bins, alpha=0.5, label='Actual')
plt.hist(df['ideal'], bins, alpha=0.5, label='Ideal')
plt.legend(loc='upper right')
plt.savefig('./plots/ideal_v_actual.png')
plt.clf()

# Plot the distributions of difference in weight
bins = np.linspace(-35, 55, 100)
plt.hist(df['diff'], bins, alpha=0.7, label='Difference between actual and ideal')
plt.legend(loc='upper right')
plt.savefig('./plots/diff_actual_v_ideal.png')
plt.clf()

# Not mapping sex to a categorical variable because both scikit-learn and graphlab do it automatically
# 63 men, 119 women

# Convert data to numpy arrays
X 

# Fit to NB Gaussian using sklearn


from sklearn.naive_bayes import GaussianNB
X = np.array()

gnb = GaussianNB()
gnb.fit