# Write a script called "prob.py" that outputs frequencies, as well as creates and saves a boxplot, a histogram, and a QQ-plot for the data in this lesson. Make sure your plots have names that are reasonably descriptive. Push your code to GitHub and enter the link below.

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# a and b are the two sets of data supplied in the lesson
a = [1,4,5,6,9,9,9]
b = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

# So the user sees what the hell a and b are
print "The dataset 'a' is defined as {}".format(a)
print "The dataset 'b' is defined as {}".format(b)

# Histograms of a and b
plt.hist(a, histtype='bar')
plt.savefig("./plots/histogram_a.png")
plt.clf() # Clears the last plot
plt.hist(b, histtype='bar')
plt.savefig("./plots/histogram_b.png")
plt.clf() 

# Boxplots of a and b
plt.boxplot(a)
plt.savefig("./plots/boxplot_a.png")
plt.clf()
plt.boxplot(b)
plt.savefig("./plots/boxplot_b.png")
plt.clf()

# QQ-plot of a
qq_a = stats.probplot(a, dist="norm", plot=plt)
plt.savefig("./plots/qq_a.png")
plt.clf()

# QQ-plot of b
qq_b = stats.probplot(b, dist="norm", plot=plt)
plt.savefig("./plots/qq_b.png")
plt.clf()

