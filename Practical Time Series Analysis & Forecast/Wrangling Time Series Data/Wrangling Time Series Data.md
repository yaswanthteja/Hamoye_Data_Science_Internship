


# Wrangling Time Series Data
As expected in any data analysis task, proper cleaning and preprocessing of the data is required.

Handling Missing Time Series Data, Upsampling and Downsampling

Missing data is a common occurrence that happens during data collection due to faulty entries or outright omission. Time series data is no exception to this problem. Imputation, interpolation and deletion of missing data points are methods used to handle missing data in time series.

Imputation: Missing values are filled based on the overall observation of the entire data. They can be imputed using forward fill where the last known data point before the missing value is used and the opposite with backward fill where the next known value is used. The fillna() function in pandas is used to impute time series data for both forward and backward fill strategies. It is worth noting that backward fill is not appropriate as the imputation method when the data will be used in a predictive model.

Another method of imputing missing values is by using a rolling mean or median known as the moving average. Unlike the forward fill, data from multiple recent times in the past are used in moving average to fill missing values. This is a better option particularly when the data is noisy to avoid inputting random noise.

Interpolation: This is another form of imputation where data points used to fill missing values are estimated such that they fit the constraints that arise from neighbouring data points. For example, if the overall behaviour of the time series is quadratic, this trend can be incorporated when filling the missing values such that they have a similar trend. The interpolate() function is provided in pandas to interpolate missing values.

When handling missing data, any method selected can be as a result of the domain and aim of the task.

![image](https://user-images.githubusercontent.com/93423367/213745297-e6f095a5-8050-43fe-a0aa-58f20d20f26d.png)


![image](https://user-images.githubusercontent.com/93423367/213745385-d7600f3b-fa05-43d7-847d-834936dd12c9.png)


![image](https://user-images.githubusercontent.com/93423367/213745430-7f1bbce0-bc5c-41b7-80f4-55531436b7db.png)


Resampling is a method of changing the time period of time series observations such that it can be summarised or aggregated. The frequency can either be increased by upsampling or reduced by downsampling.

### Downsampling:

This reduces the number of samples in the data such that multiple data points are aggregated together. For example, if the temperature in a region is reported every minute and data for the past hour is required, 3600 data points will be obtained. If data for an entire week is needed, 604800 data points will be returned. This becomes quite messy when graphed but can be easily reduced by downsampling. The level of granularity of the original data might not be sensible or informative because it was sampled too frequently.

Additionally, downsampling helps focus on a specific portion of a seasonal cycle by creating subseries for that season. A dataset can match other low-frequency datasets by downsampling.

### Upsampling:

In contrast to downsampling, upsampling tries to create more data points from infrequent samples such as changing the time period from minutes to seconds. Although this creates more samples, it does not necessarily add more information to the data. When a time series is irregular, it can be converted to a regular time series by upsampling.

![image](https://user-images.githubusercontent.com/93423367/213745622-b6b2f6de-7b17-41fb-ad19-28d825392356.png)

![image](https://user-images.githubusercontent.com/93423367/213745663-bebe8480-afd7-44a7-9ecc-77a0efe52ec4.png)

## Smoothing Time Series Data

Smoothing is often applied to time series data to help identify patterns better and generally make the data more understandable. Irregular roughness is often smoothened out to see clearer signals at lower frequencies by removing higher frequency behaviour. Smoothing can also be described as a preprocessing technique to remove noise from a dataset. There are several time series smoothing techniques some of which include moving average, exponential smoothing and Holt’s method.

- Moving average smoothing: this is an effective and naive technique that involves determining the weighted averages of observed values or previous observations surrounding a certain time. A sliding window with a specified window size known as the window width is slid across the series to calculate the average values.  It can either be a centered where observations before and after time t are used or trailing where observations before or at time t  are used.

![image](https://user-images.githubusercontent.com/93423367/213745878-0d63e09d-c231-473a-acba-d46a234f95c1.png)

![image](https://user-images.githubusercontent.com/93423367/213745923-647ae650-e3f8-4fc2-8fd1-66a5defe4252.png)

- Exponential smoothing: this technique handles various time points differently during smoothing because more recent data might be more informative. It assigns an exponentially decreasing weights as the observations get older. It can be described as a weighted moving average. There are three major types of exponential smoothing methods namely single, doubly and triple exponential smoothing. Single exponential smoothing is used for univariate time series data that have no trend or seasonality. <br><br>The smoothing coefficient (alpha) usually between 0 and 1 is the single parameter required to control the decay and influence of previous observations. On the other hand, double exponential smoothing can be used for univariate time series that have a trend. It includes an additional parameter (beta) that controls the decay of the influence of trend. Finally, the triple exponential smoothing is an extension that can handle univariate time series that have both trend and seasonality with the inclusion of gamma - a third parameter that controls the influence of seasonality.

## Time Series Specific Exploratory Methods

Exploratory data analysis helps identify patterns and structure in a dataset. It provides an initial understanding of the data and guide towards the first modelling steps. In time series, it is important to identify if there is any seasonality, trend or stationarity in the series so that the appropriate model can be used to forecast future values.

![image](https://user-images.githubusercontent.com/93423367/213746140-6cc61150-fccb-4e3c-a6eb-813cd42d31b3.png)


![image](https://user-images.githubusercontent.com/93423367/213746176-b8fb2f89-469f-4b6c-b7c6-8c3ff1818faa.png)


![image](https://user-images.githubusercontent.com/93423367/213746224-cf765ca2-8352-44a4-a2f6-29d9b46521ec.png)


![image](https://user-images.githubusercontent.com/93423367/213746261-983c3fac-838d-4a75-8b36-96af384418c1.png)






