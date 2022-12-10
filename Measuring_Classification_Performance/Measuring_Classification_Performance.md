


# Cross-validation and accuracy


From the previous module, we now understand why data scientists and machine learning engineers avoid having models that overfit or underfit. 
Cross Validation (CV) is a well known and trusted method applied to avoid overfitting and enable generalization.
Although there are different techniques used in performing cross validation, the fundamental concept involves partitioning the dataset into a number of subsets, holding out a set for evaluation then training the model on the other sets. This gives a more reliable estimate of how the model performs across different training sets because it provides an average score across different training samples used. The only drawback with cross validation is that it takes more time and computational resources however, the gain obtained in having a better model is very well worth this cost. K-Fold cross validation, Stratified K-Fold cross validation and Leave One Out Cross Validation (LOOCV) are some cross validation techniques.

![image](https://user-images.githubusercontent.com/93423367/206859032-d398d322-f960-4348-a367-1bd479c95d3b.png)




# K-Fold Cross Validation

This technique is called K-Fold because the data is split into K equal groups.  If k=5,a 5-fold cross validation can be performed such that the data is split into k1, k2, k3, k4 and k5. The model is trained on k2 - k5 and evaluated on k1 then repeated k times until every group is used to train and test the model. 

![image](https://user-images.githubusercontent.com/93423367/206859063-01564ece-e3b7-4a7a-bb1c-bb6e9ca129b1.png)

![image](https://user-images.githubusercontent.com/93423367/206859071-10b35300-7bde-43f1-9955-581efb2442a6.png)


# Stratified K-Fold Cross Validation

Although similar to the technique described above, Stratified K-Fold cross validation ensures that in every fold, there is an equal proportion of each target class to obtain a good representation of the data and avoid imbalance and biased results. For example, if there are two target classes t1 and t2 with equal distribution in the data, it is best to ensure that the folds also have the same distribution.

![image](https://user-images.githubusercontent.com/93423367/206859102-a0965278-d28b-4754-b091-6b8c960084dc.png)


# Leave One Out Cross Validation (LOOCV)

In this method, one instance is left out and used as the test set while the model is trained on N-1data points where N is the number of data points. This means that the number of instances and folds are equal.

![image](https://user-images.githubusercontent.com/93423367/206859128-3732019a-02b0-4c28-8991-685d361df84a.png)


# Confusion Matrix, Precision-Recall, ROC curve and the F1-score

Accuracy, precision, recall, F1-score and many others are evaluation metrics used in measuring the performance of classification models. In this section, we discuss these metrics. 

# Confusion Matrix

It is an N x N matrix that gives a summary of the correct and incorrect predicted classification results for the Ntarget classes. The values in the diagonal of the matrix represent the number of correctly predicted classes while every other cell in the matrix indicates the misclassified classes. This means that the more predicted values that fall in the diagonal, the better the model. True positive, false positive, true negative and false negative are terms used when interpreting a confusion matrix.

![image](https://user-images.githubusercontent.com/93423367/206859172-f88107a8-ed13-4bbf-984a-aab57681cf2c.png)

- True Positive (TP): This is a correct classification where the predicted value is the same as the actual value. Using the table above, this means that actual value was positive and the predicted value was also positive.
- True Negative (TN): The predicted value also matches the actual value. In this case, it is for the negative class. The actual value is negative and the predicted value is negative.
- False Positive (FP): Also called a Type I error, this is a misclassification such that the model predicted a positive class while the actual class is negative. Telling a man that he is pregnant is definitely a false positive.
- False Negative (FN): Also another misclassification where the predicted value is negative and the actual value is positive. Another example will be telling a pregnant woman that she is not pregnant. FN is known as a Type II error.
![image](https://user-images.githubusercontent.com/93423367/206859238-ae81052f-dbf2-4f2a-8c13-1bf9ecb080e0.png)

# Accuracy

This is the ratio of the number of correctly predicted instances to the total number of instances. It is a commonly used metric suitable when the target classes are not imbalanced. A high accuracy does not necessarily mean that the model has high predicting power. Hence, depending on the task, it is important to not use only the accuracy metric because it does not provide enough information about the model.

![image](https://user-images.githubusercontent.com/93423367/206859260-1d7a50ff-6251-454a-b0e5-6eb28e282fda.png)

![image](https://user-images.githubusercontent.com/93423367/206859269-2e5e39f6-83ea-40d8-a233-06921b01f95f.png)

# Precision

The ratio of correctly predicted instances of a class to the total number of items predicted by the model to be in that class is referred to as precision (known as Positive Predicted Value - PPV). This translates to the total percentage of the results obtained that are relevant. For the positive class, it is the ratio of true positives to the sum of true positives and false positives

![image](https://user-images.githubusercontent.com/93423367/206859283-01e5ffc8-47fe-42ae-b9fc-d187264200e5.png)

![image](https://user-images.githubusercontent.com/93423367/206859294-e53eb935-aab9-42cb-9b0d-d32d665f419b.png)


# Recall

Known as the sensitivity of the model, recall gives a percentage of total relevant results correctly predicted by the model. It is the ratio of the true positives to the actual number of positives (true positives and false negatives).

![image](https://user-images.githubusercontent.com/93423367/206859310-9b22acb2-ac4f-4f3d-bac8-31ad93ec09d0.png)

![image](https://user-images.githubusercontent.com/93423367/206859317-2f4113a1-b236-4ef7-a6f0-ebce1b8b1521.png)

Like in the previous module where we discussed the bias-variance trade-off, there is also a trade-off between precision and recall. It is impossible to maximise both metrics simultaneously because an increase in recall decreases precision. Identify which metric is important based on your task and optimise.

![image](https://user-images.githubusercontent.com/93423367/206859345-ecc26f77-be99-43c6-8875-58b2580e49a0.png)


# F1-Score

This metric is the harmonic mean of precision and recall that aims to have an optimal balance of both. The F1-Score is quite easy to use and can be focused on to maximize as opposed to maximizing precision and recall.

![image](https://user-images.githubusercontent.com/93423367/206859363-a6aca1a8-7c00-427b-bddd-d8c2c04dd190.png)

![image](https://user-images.githubusercontent.com/93423367/206859370-f5ab7f1d-f160-4d1c-8e2b-340a6c021f36.png)

# ROC Curve

The Receiver Operating Characteristics (ROC) curve is a probability curve that measures the performance of a classification model at different set thresholds. Recall also known as the True Positive Rate (TPR) is plotted on the y-axis against the False Positive Rate (FPR) on the x-axis.

The code examples above are not the optimal results that can be obtained with the model. Hyperparameter tuning can be performed to improve the model.
https://colab.research.google.com/notebooks/mlcc/logistic_regression.ipynb?hl=en

