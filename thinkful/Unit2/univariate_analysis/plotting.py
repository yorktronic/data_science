import matplotlib.pyplot as plt
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
#plt.boxplot(x) #generate a box plot of the data
#plt.show()
# You can save the plot by using savefig() instead of show()
# ex. plt.savefig("boxplot.png")

plt.hist(x, histtype='bar')
plt.show()