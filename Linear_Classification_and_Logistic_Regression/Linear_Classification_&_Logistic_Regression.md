# Linear classifiers and the importance of class probabilities

For simplicity, we define a linear classifier as a binary classifier that separates two classes (positive and negative class) using a linear separator by computing a linear combination of the features and comparing against a set threshold.

# Logistic Regression: Sigmoid, logit and the log-likelihood

Logistic regression is a linear algorithm that can be used for binary or multiclass classification. It is a discriminative classifier that estimates the probability that an instance belongs to a class using an s-shape function curve called the sigmoid function. The predicted values obtained after using a linear equation on the predictors by applying logistic regression can fall in the range of negative infinity to positive infinity. The sigmoid maps these results by shrinking the value to fall between 0 and 1.  We can say that we use the sigmoid function to transform linear regression into logistic regression.


![image](https://user-images.githubusercontent.com/93423367/206644055-51e2fd9a-396f-4a16-8e6d-6d77f3a322fb.png)


![image](https://user-images.githubusercontent.com/93423367/206644075-743405e4-b115-4207-9308-1518d40854a5.png)


![image](https://user-images.githubusercontent.com/93423367/206644217-840a292a-4cf5-472e-86b5-3bcc9cc784ab.png)


For a binary classification task with classes A and B, if a threshold is set for 0.5 and the probability of an instance belonging to a class is p, we can say that if p < 0.5 the instance if of class A while it is of class B is p > 0.5.  

Also known as the log of odds, logit is the logarithm of odds ratio where the odds ratio is the probability that an event occurs divided by the probability that the event does not occur. Logit is the inverse of the sigmoid such that it maps values from negative infinity to positive infinity.
