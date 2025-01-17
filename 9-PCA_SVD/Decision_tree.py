# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:24:22 2024

@author: Akshata Walke
"""
##########Decision Tree###########
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("C:/11-Naive Bayes/credit.csv")
#check for null values
data.isnull().sum()
data.dropna()
data.columns
#there are 9 columns having non numeric values,let us treat them
#There is one column called phone which is not useful
data=data.drop(["phone"],axis=1)
#now there are 16 columns
lb=LabelEncoder()
data["Checking_balance"]=lb.fit_transform(data["checking_balance"])
data["credit_history"]=lb.fit_transform(data["credit_history"])
data["purpose"]=lb.fit_transform(data["purpose"])
data["savings_balance"]=lb.fit_transform(data["savings_balance"])
data["employment_duration"]=lb.fit_transform(data["employment_duration"])
data["other_credit"]=lb.fit_transform(data["other_credit"])
data["housing"]=lb.fit_transform(data["housing"])
data["job"]=lb.fit_transform(data["job"])

#check for nun-numeric columns
non_numeric_cols=data.select_dtypes(include=['object']).columns
print(non_numeric_cols)
data["checking_balance"]=lb.fit_transform(data["checking_balance"])
data["default"]=lb.fit_transform(data["default"])



##Now let us check how many unique values are there in target column
data["default"].unique()
data["default"].value_counts()
##Now we want to split tree,we need all feature columns
colnames=list(data.columns)
#Now let us assign these columns to variable predictor
predictors=colnames[:15]
target=colnames[15]

#Spliting data into training and testing data set
from sklearn.model_selection import train_test_split
train,test=train_test_split(data, test_size=0.3)

from sklearn.tree import DecisionTreeClassifier as DT

help(DT)
model=DT(criterion='entropy')
model.fit(train[predictors],train[target])


#prediction on Test Data
preds=model.predict(test[predictors])
pd.crosstab(test[target],preds,rownames=['Actual'],colnames=['Predictions'])


np.mean(preds == test[target])  #test data accuracy

#Predictions on train data
preds=model.predict(train[predictors])
pd.crosstab(train[target], preds, rownames=['Actual'],colnames=['Predictions'])

np.mean(preds==train[target]) #Train Data Accuracy 







###########################################################
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("C:/12_dECISION TREE/salaries.csv")
#check for null values
data.isnull().sum()
data.dropna()
data.columns
#there are 9 columns having non numeric values,let us treat them
#There is one column called phone which is not useful
data=data.drop(["phone"],axis=1)

inputs=df.drop('salary_more_than_100k',axis='columns')
target=df['salary_more_than_100k']
inputs

model.predict([[2,1,0]])


lb=LabelEncoder()
data["company"]=lb.fit_transform(data["company"])
data["job"]=lb.fit_transform(data["job"])
data["degree"]=lb.fit_transform(data["degree"])
data["savings_balance"]=lb.fit_transform(data["savings_balance"])