# Cloudy with a chance of data #
I analyzed 30 days worth of maximum temperatures to answer the following questions: 

1. Plot the temperature swings (difference between the maximum and minimum temperature) and document your results:

<img src="https://github.com/yorktronic/data_science/blob/master/thinkful/Unit3/weather/plots/swings.png">

`In [69]: swing_max  
Out[69]: ('saltLakeCity', 26.54)`

2. Who has the largest variance?

`In [70]: var_max  
Out[70]: ('seattle', 47.4)`

3. Take the city with the largest variance and plot the distribution of the difference from the mean. What does this tell you?

<img src="https://github.com/yorktronic/data_science/blob/master/thinkful/Unit3/weather/plots/seattle_difference_plot.png">

The plot fits the normal distribution, with an identical R^2 value as the plot of the set of temperatures against the normal distribution. Which makes sense, beause this should always happen if you find a normally distributed set of data.

Update 12/2/2015 -- it also looks like this data could fit a third order polynomial equation / model, but the linear model is obviously sufficient with an R2 of .98.

4. What was the highest temperature overall, when and where was it?

`In [71]: maxTemps['phoenix'].argmax()
Out[71]: 30` (August 13, 2015)

`In [73]: temp_max
Out[73]: ('phoenix', 109.65)`

5. Plot a histogram of every city with temps rounded to nearest degree F: <a href="https://github.com/yorktronic/data_science/tree/master/thinkful/Unit3/weather/plots/histograms">Histograms</a>

6. Create a QQ plot of all cities against the normal distribution: <a href="https://github.com/yorktronic/data_science/tree/master/thinkful/Unit3/weather/plots/qq_plots">QQ Plots</a>

7. What patterns were found in the data?

Pretty much all of the cities had normally distributed temperature data