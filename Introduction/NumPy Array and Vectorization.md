# Introduction to NumPy & Creating Arrays.

As mentioned previously, NumPy is a library that has ndarray as its basic data structure used to handle arrays and matrices. A NumPy array has a grid of values all of which are of the same data type, mostly integers and floats. These arrays can also be created from Python lists.

Below are some examples:
<img  src="" alt="np1"  align="right" width="400">

<img  src="" alt="np2"  align="right" width="400">

<img  src="" alt="np3"  align="right" width="400">

<img  src="" alt="np4"  align="right" width="400">

There are also some inbuilt functions that can be used to initialize numpy which include empty(), zeros(), ones(), full(), random.random().

<img  src="" alt="np5"  align="right" width="400">

## Intra-operability of Arrays and Scalars.
Vectorisation in numpy arrays allows for faster processing by eliminating for loops when dealing with arrays of equal shape. This allows for batch arithmetic operations on the arrays by applying the operator elementwise. Similarly, scalars are also propagated element-wise across an array. For arrays with different sizes, it is impossible to perform element-wise operations instead; numpy handles this by broadcasting provided the dimensions of the arrays are the same or, one of the dimensions of the array is 1.

<img  src="" alt="np6"  align="right" width="400">



## Indexing With Arrays & Using Arrays for Data Processing

The elements in the example arrays above can be accessed by indexing like lists in Python such that:

<img  src="" alt="np7"  align="right" width="400">


Elements in arrays  can also be retrieved by slicing rows and columns or a combination of indexing and slicing.

<img  src="" alt="np8"  align="right" width="400">

There are other advanced methods of indexing which are shown below.

<img  src="" alt="np9"  align="right" width="400">

Numpy also has inbuilt mathematical functions like sum(), mean(), std(), corrcoef(), min() and others. It interestingly allows for comparing arrays using == to check if two arrays have the same elements,  elements in the first array are greater than or less than those of the second array using  > and  <.

## File Input and Output With Arrays
Numpy arrays can be loaded from and saved to binary files with .npy as the extension using load() and save() respectively. This can also be done with text files with text files using loadtxt() and savetxt().