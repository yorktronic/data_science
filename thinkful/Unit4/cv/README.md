# Metrics and Cross Validation #

## Objective ##

Perform a KFold cross validation of the linear regression model I built in Unit2 to project interest rates offered by Lending Club based on loan term length and FICO credit score. Of all the models I built I got the best results from loan term and FICO score.

## Results ##

`Mean Absolute Error: 0.0184240820785`  
`Mean Squared Error: 0.000542170328631`  
`R Squared: 0.68927852421` 

Plot of predicted interest rates versus actual interest rates:

<img src="https://github.com/yorktronic/data_science/blob/master/thinkful/Unit4/cross_val_plot.png">

## Summary ##

The mean absolute error value of 0.01842 indicates that the average error is +/- 1.8% when then model predicts an interest rate. In isolation this is okay, though I would of course like it to be lower. The R2 value is also not where I'd like it to be, at roughly 0.69, though the mean squared error is very low, which is good. 

Overall, the model is "okay" at predicting interest rates. Moving forward I would likely see if I could do better with a quadratic model and / or slice the data up in to FICO score ranges and build separate regressions on those ranges. My thought process there is that below a certain FICO score range you tend to see less variability in the interest rates offered than that of higher FICO ranges. I hypothesize that other factors such as term length, loan amount, home ownership, etc might come in to play more significantly as the FICO score increases. 