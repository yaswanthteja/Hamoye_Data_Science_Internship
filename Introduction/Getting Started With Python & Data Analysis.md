# The Complete Data Science Pipeline

- The data science pipeline can be described as an end-to-end process in which each step contributes to producing the final insights.
   - Every data science project begins with defining a clear problem it aims to solve or business/technical questions to provide answers to. 
    - Data is the core of data science, hence, scoping and collecting the right data for a project is very crucial to achieving the required results.
   - To collect data, the source it will be collected from has to be identified. Downloading or crawling from the internet, questionnaires and surveys are some common methods used to obtain data.  

<img   src="https://github.com/yaswanthteja/Hamoye_Data_Science_Internship/blob/main/images/1.2%20-%20Complete%20Data%20Science%20Pipeline.png" alt="1"   width="600">

- The next step in the pipeline involves wrangling, reviewing and transforming the data from a messy/raw form to a more appropriate state for ease of use. 
  - Although this can be time-consuming, it is very essential to clean the data extensively since machine learning models are only as good as the data provided - garbage in garbage out. 
  - Conducting Exploratory Data Analysis (EDA) on the cleaned data using visualisations and statistical methods gives a quick insight into the various patterns and relationships between features in the dataset. 
  - Modelling involves using statistical and machine learning methods for classifying and clustering the processed data to create predictive models. 
  - Several evaluation methods are employed to compare the performance of these models and continuously improve before a final model is selected. 
  - Finally, all the work done in the pipeline is irrelevant if the results cannot be interpreted and communicated properly to the appropriate audience. It is imperative to present findings from the analysis done through visualisations and clear reporting. For the most part, the data science pipeline is not a linear process; it’s instead an iterative process.

# Python for Data Analysis
## Why Python is important for data analysis

Python is a programming language widely used by developers and data scientists. It is particularly popular because it is easy to use, has a simple syntax that helps readability and also quick to learn and adapt to. Data can be presented in different forms such as CSV, JSON, Excel files, database etc. Python is very efficient in processing and wrangling most data types. Its massive community makes resources readily available including packages, tools and libraries used in data science some of which are: Pandas, Numpy, Matplotlib, Scikit-Learn and TensorFlow.

# Getting Started With Jupyter Notebook and Google Colab
## Setting up an Integrated Development Environment with Jupyter Notebook and Python 3 through Anaconda installations

- Jupyter notebook is an interactive web environment that supports many programming languages including Python and R, allowing for explanatory text, images and visualisation. 
   - It is a preferred environment for data scientists that runs on a web browser without requiring access to the internet and can be easily set up with Anaconda 
   - an open-source software that has a distribution of data science and machine learning packages for scientific computing with an environment manager that removes the complexities of package management and deployment. 
   - Download the latest version of Anaconda for Python 3 [from the official website](https://www.anaconda.com/products/individual) and follow the instructions to install. To use Jupyter notebooks, open the anaconda navigator and launch Jupyter notebook. Google Colaboratory, known as Colab, is a free cloud-based Jupyter notebook with TPU and GPU.  It is easily accessible and existing libraries can be used and new libraries installed. To get started with Colab, create a new notebook [here](https://colab.research.google.com/).

#  Libraries for Python Data Analysis
## Introduction to essential Python libraries for data analysis: Pandas, NumPy, Matplotlib, Seaborn, and SciPy

Pandas, NumPy, SciPy, Matplotlib, and Seaborn are essential Python libraries used for data analysis. Numerical computations for arrays and multidimensional matrices in data analysis are often done with the Numeric Python library - NumPy. Pandas is a toolkit built on NumPy with data structures called dataframes; used on numerical and time-series data for quick and easy data manipulation, cleaning and analysis.  SciPy can be described as a scientific package that uses NumPy arrays as its basic data structure. Matplotlib and Seaborn are plotting libraries capable of handling large datasets and producing both interactive and statistical graphics.
