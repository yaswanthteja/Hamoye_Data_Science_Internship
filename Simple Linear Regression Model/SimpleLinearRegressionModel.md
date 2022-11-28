According to the United Nations Environmental Program (UNEP) Sustainable Buildings and Climate Initiative, construction trade contributes as much as 30% to all global greenhouse gas emissions and consumes up to 40% of all energy used worldwide. Climate change is currently having a powerful impact on how buildings are designed and constructed.

Predicting numeric outcomes with some accuracy measure is an important facet of machine learning and data science. For this part, we will use a case study to understand linear regression and its associated cousins. We will learn about the assumptions behind linear regression, multiple linear regression, partial least squares and penalizations. We’ll also focus on strategies for measuring regression performance and implementations.

In this module, we will develop a multivariate multiple regression model to study the effect of eight input variables on two output variables, which are the heating load and the cooling load, of residential buildings. The data provided is from the energy analysis data of 768 different building shapes. The features provided are the relative compactness, surface area, wall area, roof area, overall height, orientation, glazing area and glazing area distribution.

Data Source for content:  [Energy efficiency dataset](https://docs.google.com/spreadsheets/d/1vT62mqIIdmSmBc_n47PruZybP-96DVSj/edit?usp=share_link&ouid=103106601474617958935&rtpof=true&sd=true)

Data Quiz:  [Appliances energy prediction dataset](https://drive.google.com/file/d/1Eru_UHVc3WLHVveC9Q8K9QUxlzYeHt18/view?usp=share_link)

Simple Linear Regression
The simple linear regression model.

A simple linear regression model estimates the relationship between two quantitative variables where one is referred to as the independent variable and the other the dependent variable. The independent variable (X) is used to predict and also called the predictor while the predicted variable is referred to as the response variable (Y) (e.g. finding the relationship between the amount of CO2 gas emitted and the number of trees cut down). The value of Y can be obtained from X by finding the line of best fit (regression line) with minimum error for the data points on a scatter plot for both variables. A simple linear regression can be represented as:

![image](https://user-images.githubusercontent.com/93423367/204094553-d93144f0-540f-4a2c-affe-a9a15ac03478.png)

The UCI Machine Learning Repository: Energy efficiency Data Set is used in this module for better understanding of the concepts( [download HERE](https://docs.google.com/spreadsheets/d/1vT62mqIIdmSmBc_n47PruZybP-96DVSj/edit?usp=share_link&ouid=103106601474617958935&rtpof=true&sd=true) ). We select a sample of the dataset and use the relative compactness column as the predictor and the heating load column the response variable.
![image](https://user-images.githubusercontent.com/93423367/204094613-aaee70c4-c276-44e6-9385-0a9df3f06d5c.png)

![image](https://user-images.githubusercontent.com/93423367/204094627-5c7e954d-f7cb-41c7-9ba5-405b0d5ee5c3.png)

- Collinearity and Assumptions for Linear Regression

For better understanding, we explain the assumptions made by linear regression by comparing results on our energy efficiency dataset and a dummy linear dataset generated to have similar shape (same number of rows and column) as the energy efficiency dataset. Some assumptions made by linear regression models about the data are:

- Linearity: the relationship between the variables is linear such that a straight line is the line of best fit.
 ![image](https://user-images.githubusercontent.com/93423367/204094683-d39deb43-fd5c-4d64-9b05-fb91facd0f0a.png)
 From the regression plots above, we can see that the residuals of the dummy data are spread across the regression line as they should be to meet the linearity assumption unlike the residuals of the energy efficiency dataset which are a bit farther from the regression line.

Homoscedasticity: the residuals or prediction errors are of equal or constant variance.

![image](https://user-images.githubusercontent.com/93423367/204094704-b4ea5f70-6e4d-4687-b9ab-28cd41a6f0b0.png)

The variance of the residuals for the dummy dataset appear to be uniform as opposed to the energy efficiency dataset which violates this assumption.

Normality: the residuals are of a normal distribution
![image](https://user-images.githubusercontent.com/93423367/204094726-8eb270c1-5dac-4a08-8f9f-9a470ee9dc55.png)

The energy efficiency dataset flouts this assumption as the residuals are clearly not normally distributed while the dummy dataset has normally distributed residuals with the mean and median at 0. 

Independence of the observations
In multiple linear regression where there are more predictors, it is assumed that these variables are independent of each other without any strong correlation between them.

![image](https://user-images.githubusercontent.com/93423367/204094746-e5000e1d-6af8-4dd2-84b5-6a7d8db6f1f5.png)

![image](https://user-images.githubusercontent.com/93423367/204094758-2385d880-9807-49ca-948c-7f673edfd5b4.png)

The energy efficiency dataset shows a strong correlation between relative compactness and surface area, relative compactness and overall height, surface area and roof area while the variables in the dummy dataset are seen to be independent of each other.

Overall, before inferences are drawn from a linear regression model, all the assumptions discussed above must have been met.

Residual sum of squares and minimizing the cost function
A cost function is a measure of the performance of a model i.e. how far or close the predicted values are to the real values. The objective is to minimise the cost function in order for the model to continuously learn to obtain better results. In linear regression, the cost function can be defined as the sum of squared errors in a training set. The squares of the residuals are taken to penalise errors farther from the line of best fit more than those closer to the line and obtain the best parameter values. 

Gradient descent and coordinate descent algorithm
Gradient descent is an optimization algorithm that minimizes a cost function by specifying the direction to move towards to obtain a local or global minima. This is done by initially starting with random values then iteratively updating the values until the minimum cost is obtained.  A learning rate is usually chosen to determine the step size to be taken for each iteration. It is important to carefully select this parameter because, if a small step is chosen, it will take a long time to converge to the minimum cost while if too large, it can result in an overshoot surpassing the location of the minimum cost.

[All Codes](https://gist.github.com/HamoyeHQ/d44bece91e108d0fb6dda16d61559e86)


- ### Simple Linear Regression.py



```

df=pd.read_excel('https://archive.ics.uci.edu/ml/machine-learning-databases/00242/ENB2012_data.xlsx')
#rename columns
column_names = {'X1':'Relative_Compactness', 'X2': 'Surface_Area', 
                'X3':  'Wall_Area', 'X4': 'Roof_Area', 'X5': 'Overall_Height',
                'X6': 'Orientation', 'X7': 'Glazing_Area', 
                'X8': 'Glazing_Area_Distribution', 
                'Y1': 'Heating_Load', 'Y2': 'Cooling_Load'}


df = df.rename(columns=column_names)
#select a sample of the dataset
simple_linear_reg_df = df[[Relative_Compactness, 'Cooling_Load']]
                       .sample(15, random_state=2)
#regression plot
sns.regplot(x="Relative_Compactness", y="Cooling_Load",
            data=simple_linear_reg_df)
```


