# The Lending Club Challenge! #

## The Problem ##
<a href="https://www.lendingclub.com">Lending Club</a> is a financial service which provides various types of loans to individuals and businesses, which are backed by investors such as other individuals, banks, etc. Lending Club also <a href="https://www.lendingclub.com/info/download-data.action">provides anonymized data on their loans to the public</a>!

In prob_lending_club.py, I compared the amount of money requested by individuals to the amount of money that Lending Tree actually funded, as well as plotted the amount requested data against the normal distribution.

## Findings ##

### Box Plot ###
The Box Plot reveals that the median of the two data sets is the same, at roughly $10,000. The dollar value of the quartiles @ 25%, 75%, and 90% of the amount funded is generally less than the same quartiles of the amount requested, which indicates that Lending Club likely funds equal or less than the amount requested most of the time.

### Histogram ###
First off, I can't figure out how to truncate the values on the x-axis of the histogram. The x-axis is broken up in to $5,000 increments, and each divider is indicated by the vertical dotted lines. I also need to clean the data some more as it shouldn't be showing negative values on the x-axis. The plot is accurate, it's just showing -5000 on the x-axis for some reason.

The histogram does a better job of showing the volume of loans, both requested and funded, within each dollar value range for both requested and. looking at just after the middle of the range for amount requested, you can see that $10,000 to $20,000 is the sort of sweet spot for what Lending Club likes to offer. Looking at the volume of requested loans in the $15,000 - $35,000 range, it stands to reason that many of these loan requests received a dollar value less than the individual wanted. 

### Probability Plot ###
The data doesn't fit the normal distribution, with an R^2 value of only 93%

### Next Steps ###
I'd like to perform more analysis on the credit ratings of loan requestors as well as other pertinent factors that determine what percentage of their request actually gets loaned to them. The analysis thus far does an okay job of showing the data in aggregate, but my conclusions are, frankly, presumptuous at best. More to come.

/Ty 

