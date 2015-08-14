# Cloudy with a chance of data #
I analyzed 30 days worth of maximum temperatures to answer the following questions: 

1. Plot the temperature swings (difference between the maximum and minimum temperature) and document your results:

Bar chart found here

`In [69]: swing_max
Out[69]: ('saltLakeCity', 26.54)`

2. Who has the largest variance?

`In [70]: var_max
Out[70]: ('seattle', 47.4)`

3. Take the city with the largest variance and plot the distribution of the difference from the mean. What does this tell you?

The plot fits the normal distribution, with an identical R^2 value as the plot of the set of temperatures against the normal distribution. Which makes sense, beause this should always happen if you find a normally distributed set of data.

4. What was the highest temperature overall, when and where was it?

`In [71]: maxTemps['phoenix'].argmax()
Out[71]: 30` (August 13, 2015)

`In [73]: temp_max
Out[73]: ('phoenix', 109.65)`

5. Plot a histogram of every city with temps rounded to nearest degree F
See this folder

6. Create a QQ plot of all cities against the normal distribution
Found here

7. What patterns were found in the data?
Pretty much all of the cities had normally distributed temperature data