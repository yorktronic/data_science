# Logistic Regression #
This is where I think things get particularly interesting. Logistic regression was developed by statistician D.R. Cox in 1958. If you really want to nerd out, you can read all about it on <a href="https://en.wikipedia.org/wiki/Logistic_regression">Wikipedia</a>/. 

Basically, where linear regression tells you how related some variables are to some outcome (this is called correlaton, and remember, <a href="https://xkcd.com/552/">correlation does not imply causation!</a>), logistic regression asks questions that have binary answers? For example: based off of Lending Club's loan data, will I be able to get a $10,000 loan at or less than 12% interest with a FICO score of 700? Another example: will it rain tomorrow if I live in California?

The answers are "probably not (32% chance)", and "no," respectively. Because it doesn't rain in California. 

In all seriousness, the output of a logistic regression model is a probability of a single event occurring. If you set a particular threshold of probability, say 90%, to indicate whether or not an event will happen, this can create a yes/no, on/off, fat/not fat, loan/no loan output.

<a href="https://github.com/yorktronic/data_science/tree/master/thinkful/Unit2/logistic_regression">logistic_regression.py</a> uses Lending Club data and a user-inputted FICO Score, interest rate, and loan amount to determine the probability of whether or not the user will get a loan. Keep in mind that this probability is based **solely** on the FICO score and loan amount requested - in the real world there are many other factors that contribute to one's loan-worthiness. 