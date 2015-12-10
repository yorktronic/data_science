# Modeling of Samsung Accelerometer Data Using Decision Trees #

## Objective ##
Predict whether smartphone users are laying down, sitting, standing, or walking on a flat, uphill, or downhill surface using accelerometer data. See the <a href="https://github.com/yorktronic/data_science/blob/master/thinkful/Unit4/decision-trees/db/README.txt" target="_blank">README</a> provided by the dataset creators for more information.

## Results ##
Of the three models I built, the most accurate was the "black box" approach, anonymizing each of the columns of data provided and then building a decision tree model with all of the data. That is to say, in this case, building a decision tree model where you only know what column the target or dependent variable is, is more accurate than building a model based on an informed or intuitive assessment of what features are important. Here's some metrics on my model accuracy:

```python
'accuracy': 0.8395437262357415
'f1_score': 0.8273680293095115
 'log_loss': 0.7209217738660755
 'precision': 0.8499104420591913
 'recall': 0.8331896228185193
```
The accuracy of my informed models were 60.18% and 53.14%, so the black box approach is a dramatic improvement. If I were to look more in to this, I might play around with the columns identified by the black box model as the most important indicators of whether someone is lying down, sitting, standing, etc, but for now I'll leave this be. The most important features / indicators are:

| actual_name | index | count |
| ----------- | ----- | ----- |
| tGravityAcc-min()-Z | X55 | 28 |
| tGravityAcc-energy()-Z | X59 | 14 |
| tGravityAcc-sma() | X56 | 14 |
| tGravityAcc-mean()-Z | X43 | 12 |
| tBodyAcc-mean()-Z | X3 | 11 |
| tBodyAcc-std()-Y | X5 | 10 |
| fBodyGyro-bandsEnergy()-1,8 | X461 | 10 |
| tBodyAcc-mad()-Y | X8 | 10 |
| tGravityAcc-arCoeff()-Y,2 | X71 | 10 |
| tBodyAcc-max()-X | X10 | 10 |

That's it for now!

