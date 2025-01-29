# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 08:22:58 2025

@author: Akshata Walke
"""

import pandas as pd
import numpy as np
letters=pd.read_csv("C:/15-logistic_Regression/letterdata.csv")

'''
dataset typically used for handwritten character recognition or related
 machine learning tasks.
 
 '''
 #let us carry out
 a=letters.describe()
 from sklearn.svm import SVC
 from sklearn.model_selection import train_test_split
 train,test=train_test_split(letters,test_size=0.2)
 #let us split the data in terms X and y for both train and test data
 train_X=train.iloc[:,1:]
 train_y=train.iloc[:,0]
 test_X=test.iloc[:,1:]
 test_y=test.iloc[:,0]
 
 #Kernel Linear
 model_linear=SVC(kernel="linear")
 model_linear.fit(train_X,train_y)
 pred_test_linear=model_linear.predict(test_X)
 #now let us check the accuracy=0.85675
 np.mean(pred_test_linear==test_y)
 
 #Kernel rbf
 model_rbf=SVC(kernel="rbf")
 pred_test_rbf=model_rbf.predict(test_X)
 #now let us check the accuracy=0.92275
 np.mean(pred_test_rbf==test_y)