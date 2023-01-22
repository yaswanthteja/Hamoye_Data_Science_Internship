


# Time Series at Scale
## Time series with Facebook Prophet

Prophet is an open-source library for univariate time series forecasting developed by Facebook. It implements decomposable additive models that support trends, seasonality and holidays. The components of the model can be combined such that

![image](https://user-images.githubusercontent.com/93423367/213924350-a60b9cef-47db-4d28-bee0-a638a42a2d1f.png)

While y(t) is the forecast, g(t)is the piecewise linear or logistic growth curve trend that models non-periodic changes in time series; s(t) represents the seasonality in the series for periodic changes; h(t) allows for irregularities by factoring in the effects of specified holidays; 𝝐tis the error term in the model for unusual changes.

Prophet helps automate the calculation of terms within the model and prevents forecast errors. This library forecasts data by using either of two models: the logistic growth model for non-linear data or the piecewise linear model for data with linear properties but selects the latter by default. The library provides easy to tune and intuitive parameters that can be used without necessarily being a forecasting expert.

![image](https://user-images.githubusercontent.com/93423367/213924356-12db1438-0725-476d-a90a-782474b76395.png)

![image](https://user-images.githubusercontent.com/93423367/213924367-b3ca2be6-dc1c-4c54-98fc-c2bbd87ff484.png)

![image](https://user-images.githubusercontent.com/93423367/213924377-6cf4df80-de82-43b2-80e6-908196f4e63a.png)


### Time series using Neural Networks

As opposed to the classical forecasting methods that assume that there is a linear relationship between the inputs and outputs, neural networks can approximate nonlinear functions without having a priori information about the properties of the series. Neural networks can support multiple inputs and outputs and learn complex mappings between them. Multilayer perceptron (MLPs) are robust to noise and missing values; Convolutional Neural Networks (CNNs)  have the ability to automatically extract features from raw data which can be done to time series; Recurrent Neural Networks (RNNs) and Long Short-Term Memory Networks (LSTMs) support for sequences in input data as in time series. 





