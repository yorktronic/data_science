# Modeling of Samsung Accelerometer Data Using Decision Trees #

## Objective ##
Predict whether smartphone users are laying down, sitting, standing, or walking on a flat, uphill, or downhill surface using accelerometer data. See the <a href="https://github.com/yorktronic/data_science/blob/master/thinkful/Unit4/decision-trees/db/README.txt" target="_blank">README</a> provided by the dataset creators for more information.

## Results ##
Thus far I've built two decision tree models using Dato's GraphLab, with accuracies of 60.18% and 53.14%. I'm not yet satisfied with this accuracy and I hypothesize the cause is due to the fact that I've been using various attributes of computed 3d vector magnitude as my indicators, rather than separating the data into x, y and z dimensional vectors. I think that will differentiate between each of the activities more accurately.

We'll see!