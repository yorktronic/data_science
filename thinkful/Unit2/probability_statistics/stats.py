import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

# Split the text block into a list by new lines, resulting in a string for each row
data = data.split('\n')

# Split the list into a list of lists 
data = [i.split(', ') for i in data]

# Convert the list of lists into a pandas dataframe
column_names = data[0] # First row
data_rows = data[1:] # all the following rows of data
df = pd.DataFrame(data_rows, columns = column_names)

# Calculate the mean, median, and mode of the Alcohol and Tobacco columns
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

alc = df['Alcohol']
tob = df['Tobacco']
###### Alcohol ######
#####
alc_mean = alc.mean()
# 5.443634
alc_median = alc.median()
# 5.63
alc_mode = stats.mode(alc)
# 4.02
alc_range = max(alc) - min(alc)
# 2.45000000
alc_std = alc.std()
# 0.797762
alc_var = alc.var() #alc_std ** 2 also works
# 0.636425

##### Tobacco ######
######
tob_mean = tob.mean()
# 3.6181819
tob_median = tob.median()
# 3.53
tob_mode = stats.mode(tob)
#2.71
tob_range = max(tob - min(tob))
# 1.849999999999
tob_std = tob.std()
# 0.59070836
tob_var = tob.var()
# 0.348936

# latter part of the string to print, setting the decimal precision to 3 to make the code and output cleaner
msg = "for the Alcohol and Tobacco dataset is {:.3f} for Alcohol and {:.3f} for Tobacco \n"

# Output
print "The range " + msg.format(alc_range, tob_range)
print "The mean " + msg.format(alc_mean, tob_mean)
print "The median " + msg.format(alc_mean, tob_mean)
print "The mode " + msg.format(alc_mode[0][0], tob_mode[0][0])
print "The standard deviation for the " + msg.format(alc_std, tob_std)
print "The variance for the " + msg.format(alc_var, tob_var)


