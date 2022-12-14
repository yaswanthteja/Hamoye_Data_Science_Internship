# Introduction to NumPy & Creating Arrays.

As mentioned previously, NumPy is a library that has ndarray as its basic data structure used to handle arrays and matrices. A NumPy array has a grid of values all of which are of the same data type, mostly integers and floats. These arrays can also be created from Python lists.

Below are some examples:

<img  src="https://github.com/yaswanthteja/Hamoye_Data_Science_Internship/blob/main/images/np1.png" alt="np1"  width="400">



<img  src="https://github.com/yaswanthteja/Hamoye_Data_Science_Internship/blob/main/images/np2.png" alt="np2"  width="400">


<img  src="https://github.com/yaswanthteja/Hamoye_Data_Science_Internship/blob/main/images/np3.png" alt="np3"   width="400">

<img  src="https://github.com/yaswanthteja/Hamoye_Data_Science_Internship/blob/main/images/np4.png" alt="np4"  width="400">

There are also some inbuilt functions that can be used to initialize numpy which include empty(), zeros(), ones(), full(), random.random().

<img  src="https://github.com/yaswanthteja/Hamoye_Data_Science_Internship/blob/main/images/np5.png" alt="np5"  width="400">

## Intra-operability of Arrays and Scalars.
Vectorisation in numpy arrays allows for faster processing by eliminating for loops when dealing with arrays of equal shape. This allows for batch arithmetic operations on the arrays by applying the operator elementwise. Similarly, scalars are also propagated element-wise across an array. For arrays with different sizes, it is impossible to perform element-wise operations instead; numpy handles this by broadcasting provided the dimensions of the arrays are the same or, one of the dimensions of the array is 1.

<img  src="https://github.com/yaswanthteja/Hamoye_Data_Science_Internship/blob/main/images/np6.png" alt="np6"   width="400">



## Indexing With Arrays & Using Arrays for Data Processing

The elements in the example arrays above can be accessed by indexing like lists in Python such that:

<img  src="https://github.com/yaswanthteja/Hamoye_Data_Science_Internship/blob/main/images/np7.png" alt="np7"   width="400">


Elements in arrays  can also be retrieved by slicing rows and columns or a combination of indexing and slicing.

<img  src="https://github.com/yaswanthteja/Hamoye_Data_Science_Internship/blob/main/images/np8.png" alt="np8"  width="400">

There are other advanced methods of indexing which are shown below.

<img  src="https://github.com/yaswanthteja/Hamoye_Data_Science_Internship/blob/main/images/np9.png" alt="np9"   width="400">

Numpy also has inbuilt mathematical functions like sum(), mean(), std(), corrcoef(), min() and others. It interestingly allows for comparing arrays using == to check if two arrays have the same elements,  elements in the first array are greater than or less than those of the second array using  > and  <.

## File Input and Output With Arrays
Numpy arrays can be loaded from and saved to binary files with .npy as the extension using load() and save() respectively. This can also be done with text files with text files using loadtxt() and savetxt().
