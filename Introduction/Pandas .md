# Pandas - So Much More Than A Cute Animal

## Introducing Pandas data structures: Series, DataFrames and Index objects.

Pandas is a library  built on Numpy which is used for data manipulation, with other ways of indexing other than integers. Series, DataFrame, and index are the basic data structures in this library.  Series in pandas can be referred to as a one dimensional array with homogenous elements of different types somewhat similar to numpy arrays; however, it can be indexed differently with specified descriptive labels or integers.


<img  src="" alt="pd1"  align="right" width="400">


<img  src="" alt="np2"  align="right" width="400">

<img  src="" alt="np3"  align="right" width="400">

Series can be accessed using the specified index as shown below
<img  src="" alt="np4"  align="right" width="400">


A DataFrame can be described as a table (2 dimensions) made up of many series with the same index. It holds data in rows and columns just like a spreadsheet. Series, dictionaries, lists, other dataframes, and numpy arrays can be used to create new ones. 

<img  src="" alt="np5"  align="right" width="400">

at, iat, iloc and loc are accessors used to retrieve data in dataframes. iloc selects values from the rows and columns by using integer index to locate positions, while loc selects rows or columns using labels. at and iat are used to retrieve single values such that at uses the column and row labels and iat uses indices.   

<img  src="" alt="np6"  align="right" width="400">

- Finally, Indexes in pandas are immutable arrays with unique elements. They can also be described as ordered sets for retrieving data in a dataframe and collaborating with multiple dataframes.

  - The important Pandas functionalities: indexing, reindexing, selection, group, drop entities, ranking, sorting, duplicates and indexing by hierarchy.
  - Summary and descriptive statistics: measure of central tendency, measure of dispersion, skewness and kurtosis, correlation and multicollinearity.
- Similar to Numpy, Pandas has some functions that provide descriptive statistics such as the measures of central tendency, dispersion, skewness and kurtosis, correlation and multicollinearity. Some functions are mode(), median(), mean(), sum(), std(), var(), skew(), kurt() and min(). The describe function gives the summary  of the numeric columns in a dataframe displaying count, mean, standard deviation, interquartile range, minimum and maximum values.


<img  src="" alt="np7"  align="right" width="400">

- The missing data enigma: Importance, types and handling missing data.
Often, data used for analysis in real life scenarios is incomplete as a result of omission, faulty devices, and many other factors. Pandas represent missing values as NA or NaN which can be filled, removed, and detected with functions like fillna(), dropna(), isnull(), notnull(), replace().
<img  src="" alt="np8"  align="right" width="400">



