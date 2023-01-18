

# Basics of Time Series
### Component of a Time Series

Time series is a collection of well-defined data points obtained sequentially over a set time period, usually, taken at equal time intervals. Time series allows for the analysis of important patterns that occur such as trends and seasonality. Depending on the domain of application, time series analysis can be used in forecasting future values like GDP, unemployment rates, population, mortality rate, global temperatures, pollution levels etc. Trend (T), Seasonality(S), Cyclic variations (C) and Random or Irregular movements (I) are all components of a time series. 

- Trend: this a long term movement observed in time series that changes over time which can either be positive (increasing) or negative (decreasing).
- Seasonality: it is a periodic fluctuation that occurs in time series where predictable and regular patterns are exhibited at intervals - usually during a 12 month period. These fluctuations can be hourly, daily, weekly, monthly or quarterly and they may be caused by seasons, habits, weather, traditions etc.

- Cyclic variations: these are oscillations occurring around a given trend in time series. The duration of a cycle varies based on the domain and business being analysed. The length of a cycle is described as the period
- Irregular movements: This is the residual after trend and seasonality have been removed from a time series. These are irregular variations that are unforeseen, cannot be predicted and unlikely to be repeated.

### Time Series and Stochastic Process

A stochastic process is a statistical occurrence that consists of a collection of random variables ordered in time. Stochastic processes are often used in modelling time series data and considered to generate an infinite collection of all possible time series that may have been observed. One realization of a stochastic process is  considered an observed time series while an ensemble of a stochastic process is a statistical population.

### Concept of Stationary and Seasonality

A stationary time series is one where the statistical properties such as mean and variance do not change over time. This means that a stationary time series does not have any periodic fluctuations or trend. Many methods and tools for time series analysis have an underlying assumption that the time series is stationary. Hence, it is common to transform a non-stationary time series to stationary by differencing to remove trend and seasonality. 


![image](https://user-images.githubusercontent.com/93423367/213223413-1bf0f278-0222-4898-96ca-43de1cbf352c.png)


### Model Parsimony

The principle of parsimony which is attributed to an English philosopher, William of Occam, suggests that given a set of equally good explanations for a phenomenon, the correct answer is the simplest explanation. Similarly in statistical modelling, a parsimonious model is one that has a great explanatory predictive power and explains data with the minimum number of predictor variables or parameters. These models have just the right amount of predictors required to explain the model. As such, linear models are more preferable than non-linear models; experiments that depend on few assumptions should also be preferred to those that depend on many.


