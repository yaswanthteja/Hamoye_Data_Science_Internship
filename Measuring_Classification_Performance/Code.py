#import the libraries
import pandas as pd
import numpy as np


#using python to download the dataset (uncomment the codes below and execute them)
#import urllib.request
#url = 'https://query.data.world/s/wh6j7rxy2hvrn4ml75ci62apk5hgae'
#filename = 'dataworld.csv'
#urllib.request.urlretrieve(url, filename)

#using pandas to download the dataset (uncomment the code below and execute them)
#df = pd.read_csv('https://query.data.world/s/wh6j7rxy2hvrn4ml75ci62apk5hgae')
#df.to_csv('dataset.csv')

#load the dataset
df = pd.read_csv('dataset.csv', low_memory=False)
df.head()

#drop the unnamed column

df.drop('Unnamed: 0', axis = 1, inplace = True)

#check distribution of target variable
df['QScore'].value_counts()

#checking for null values in the dataset
df.isna().sum()

#for simplicity, we will drop the rows with missing values.
df.dropna(inplace = True)
df.isna().sum()
#An obvious change in our target variable after removing the missing values is that there are only three classes left 
#and from the distribution of the 3 classes, we can see that there is an obvious imbalance between the classes. 
#There are methods that can be applied to handle this imbalance such as oversampling and undersampling.
#Oversampling involves increasing the number of instances in the class with fewer instances while undersampling 
#involves reducing the data points in the class with more instances.

#reset the dataframe index
df = df.reset_index(drop = True)

#For now, we will convert this to a binary classification problem by combining class '2A' and '1A'.
df['QScore'] = df['QScore'].replace(['1A'], '2A')
df.QScore.value_counts()

#separating the target variable and 
#selecting some samples
df_2A = df[df.QScore=='2A']
df_3A = df[df.QScore=='3A'].sample(350)
data_df = df_2A.append(df_3A)
data_df

#to reshuffle the dataset for randomness
import sklearn.utils
data_df = sklearn.utils.shuffle(data_df)
data_df = data_df.reset_index(drop=True)
data_df.shape
data_df.QScore.value_counts()


#check the datatype of the dataset
data_df.dtypes

# from the above, we will be dropping country code, country and year
#because they are ambiguous to what we want to predict
#and also we will encode the record feature

#One of the feature is categorical, so we need to encode it ahead 
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
data_df.record = encoder.fit_transform(data_df.record)

#let's preview the encoded feature
data_df.record

#more preprocessing
data_df = data_df.drop(columns=['country_code', 'country', 'year'])
X = data_df.drop(columns = 'QScore')
y = data_df['QScore']

#split the data into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
y_train.value_counts()

#installing imblearn module (uncomment the pip command to install imblearn)
#!pip install imblearn

#encode categorical variable
#from sklearn.preprocessing import LabelEncoder
#encoder = LabelEncoder()
#x_train.record = encoder.fit_transform(x_train.record)
#x_test.record = encoder.transform(x_test.record)

#the encoded feature
x_train.record


#There is still an imbalance in the class distribution. For this, we use SMOTE only on the training data to handle this.
import imblearn
from imblearn.over_sampling import SMOTE
smote = SMOTE(random_state=1)
x_train_balanced, y_balanced = smote.fit_sample(x_train, y_train)
y_train.value_counts()


#min max scaler
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
normalised_train_df = scaler.fit_transform(x_train_balanced.drop(columns=['record']))
normalised_train_df = pd.DataFrame(normalised_train_df, columns=x_train_balanced.drop(columns=['record']).columns)
normalised_train_df['record'] = x_train_balanced['record']


x_test = x_test.reset_index(drop=True)
normalised_test_df = scaler.transform(x_test.drop(columns=['record']))
normalised_test_df = pd.DataFrame(normalised_test_df, columns=x_test.drop(columns=['record']).columns)
normalised_test_df['record'] = x_test['record']


#Logistic Regression
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(normalised_train_df, y_balanced)
#returns
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='auto', n_jobs=None, penalty='l2',
                   random_state=None, solver='lbfgs', tol=0.0001, verbose=0,
                   warm_start=False)


# LESSON 2
# MEASURING CLASSIFICATION PERFORMANCE

# In[31]:


#cross validation score
from sklearn.model_selection import cross_val_score
scores = cross_val_score(log_reg, normalised_train_df, y_balanced, cv=5,
                        scoring='f1_macro')
scores


#confusion matrix
from sklearn.metrics import recall_score, accuracy_score, precision_score, f1_score, confusion_matrix
new_predictions = log_reg.predict(normalised_test_df)
cnf_mat = confusion_matrix(y_true=y_test, y_pred=new_predictions, labels=['2A', '3A'])
cnf_mat


# METRICS 

#Accuracy
accuracy = accuracy_score(y_true = y_test, y_pred = new_predictions)
print('Accuracy: {}'.format(round(accuracy*100, 2)))

#precision
precision = precision_score(y_true=y_test, y_pred=new_predictions, pos_label='2A')
print('Presicion: {}'.format(round(precision*100), 2))


# In[35]:


#recall
recall = recall_score(y_true=y_test, y_pred=new_predictions, pos_label='2A')
print('Recall: {}'.format(round(recall*100), 2))


# In[36]:


#F1 scores
f1 = f1_score(y_true=y_test, y_pred=new_predictions, pos_label='2A')
print('F1: {}'.format(round(f1*100), 2))


#K-Fold
from sklearn.model_selection import KFold

kf = KFold(n_splits=5)
kf.split(normalised_train_df)
f1_scores = []

#run for every split
for train_index, test_index in kf.split(normalised_train_df):
    x_train, x_test = normalised_train_df.iloc[train_index], normalised_train_df.iloc[test_index]
    y_train, y_test = y_balanced[train_index], y_balanced[test_index]
    model = LogisticRegression().fit(x_train, y_train)
    #save result to list
    f1_scores.append(f1_score(y_true = y_test, y_pred = model.predict(x_test),
                            pos_label = '2A')*100)
f1_scores


#StratifiedKFold
from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=1)
f1_scores = []
#run for every split
for train_index, test_index in skf.split(normalised_train_df, y_balanced):
    x_train, x_test = np.array(normalised_train_df)[train_index], np.array(normalised_train_df)[test_index]
    y_train, y_test = y_balanced[train_index], y_balanced[test_index]
    model = LogisticRegression().fit(x_train, y_train)
    #save result to list
    f1_scores.append(f1_score(y_true = y_test, y_pred = model.predict(x_test),
                            pos_label = '2A')*100)
f1_scores


#LeaveOneOut
from sklearn.model_selection import LeaveOneOut
loo = LeaveOneOut()
scores = cross_val_score(LogisticRegression(), normalised_train_df, y_balanced, cv=loo, scoring='f1_macro')
average_score = scores.mean() * 100
average_score


# Tree-Based Methods and The Support Vector Machine
from sklearn.tree import DecisionTreeClassifier
dec_tree = DecisionTreeClassifier()
dec_tree.fit(normalised_train_df, y_balanced)
