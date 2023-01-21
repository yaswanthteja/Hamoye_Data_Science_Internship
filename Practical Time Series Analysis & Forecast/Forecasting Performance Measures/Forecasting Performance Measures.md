

In this lesson, you will learn about the different ways of evaluating time series models.



# Forecasting Performance Measures
## Various Forecast Performance Measures

As we have emphasised in previous modules, it is essential to correctly evaluate our models with the appropriate metrics. In time series forecasting, there are a number of measures that can be used to evaluate how well a model performs. We discuss some of these below.

## Mean Absolute Error (MAE):

This is a measure of the forecast error obtained by taking the average of the absolute errors of the forecasted values where the error is the difference between the forecasted value and the true value. Simply put, it tells the average of the error that should be expected from a forecast. The MAE is robust to outliers and scale-dependent error so it cannot be used to compare different series. 

![image](https://user-images.githubusercontent.com/93423367/213871998-6cb0d11a-a6b9-4a35-813f-057743127b70.png)

## Mean Absolute Percentage Error (MAPE):

It is a well known measure used to determine the accuracy of a forecasting method. The accuracy is calculated as a percentage such that the average of the difference between the actual value and the forecast value divided by the actual value. The average of the sum of the absolute value of this calculation for every data point forecasted is multiplied by 100 to obtain a percentage error. MAPE can be easily interpreted, scale independent and should not be used with low-volume data. In addition, it should not be used when the values are zero or close to zero because it results in undefined and indefinite values. 

![image](https://user-images.githubusercontent.com/93423367/213872033-e500df7b-1837-4b48-b410-7d3695490dd0.png)


## Root Mean Square Error (RMSE):

The RMSE calculates square root of the average of the squared errors  (i.e. the square of the difference between the actual and forecasted value).  This measure tends to exaggerate large errors by giving a relatively high weight to large errors because it takes the square root of the average squared errors. The Mean Squared Error (MSE) is simply the average of the square of the errors.


![image](https://user-images.githubusercontent.com/93423367/213872074-374c7003-6c7e-4f20-8087-7d112a5e2112.png)




