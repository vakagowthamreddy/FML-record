Model: "sequential"

 Layer (type)              Output Shape        Param #
 ------------------------------------------------------
 dense (Dense)             (None, 16)          80
 dense_1 (Dense)           (None, 8)           136
 dense_2 (Dense)           (None, 3)            27

 Total params: 243
Example:
Test Loss: 0.0865
Test Accuracy: 0.9667
Example classification result:
              precision    recall  f1-score

setosa           1.00       1.00      1.00
versicolor       0.91       1.00      0.95
virginica        1.00       0.90      0.95
