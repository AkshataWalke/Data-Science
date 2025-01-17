# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 08:22:06 2024

@author: Akshata Walke
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
##Loading dataset
email_data=pd.read_csv("C:/11-Naive Bayes/sms_raw_NB.csv",encoding"ISO-8859-1")
#These sms are in text form,open the dataframe and three are ham
#cleaning the data
#the function tokenizes the test and remove words
#with fewer than 4 characters
import re
def cleaning_text(i):
    i=re.sub("[^A-Z a-z""]+"," ",i).lower()
    w=[]
    #every thing else A and Z and a to z is going to convert to space and we will take each row and tokenize
    for word in i.split(" "):
        if len(word)>3:
            w.append(word)
        return(" ".join(w))
#Testing above function with sample text
cleaning_text("Hope you are having good week.just checking")
cleaning_text("Hope i can i understand your feeling12321.123.hi how are you")
cleaning_text("Hi how are you")
#Note the dataframe size is 5559,2,how removing empty spaces 
#removing empty rows
email_data=email_data.loc[email_data.text!=" ",:]
email.data.shape
#you want use count vectoriser which directly converts a collection of documents    
#first we will sploit the data
from sklearn.model_selection import train_test_split
email_train,email_test=train_test_split(email_data,test_size=0.2)

#splits each email into list of words
#creating matrix of token count for entire dataframe
def split_into_words(i):
    return[word for word in i.split(" ")]

#defining the preparation of email text into words count matrix format
emails_bow=CountVectorizer(analyzer=split_into_words).fit(email_data.text)
#defining bowcfor all dataframe
all_emails_matrix=email_bow.transform(email_data.text)
train_email_matrix=emails_bow.transform(email_test.text)
#for testing  messages
test_email_matrix=emails_bow.transform(email_test.text)
##learning term weighting and nomalizing entire emails
tfidf_transform=TfidfTransformer().fit(all_emails_matrix)
##preparing TFIDF for train mails
train_tfidf=tfidf_transform.transform(train_email_matrix)
train_tfidf.shape

test_tfidf=tfidf_transform.transform(test_email_matrix)
test_tfidf.shape

##Now apply to naive bayes
from sklearn.naive_bayes import MultinomialNB as MB
classifier_mb=MB()
classifier_mb.fit(train_tfidf,email_train.type)
#email_train.type:This is the column in the training dataset
#email_train that contains the target labels,
#which specify the whether each message is spam or ham
#The .type attribute refers to that specify column in the email_train dataframe
##training data prepared in terms of tfidf and labels of corresponding training data
#labesls of corrsponding training data

##evaluation on test data
test_pred_m=classifier_mb.predict(test_tfidf)

##calculating accuracy
accuracy_test_m=np.mean(test_pred_m==email_test.type)
accuracy_test_m
#evalution on Test Data accuracy matrix
from sklearn.metrics import accuracy_score
accuracy_score(test_pred_m,email_test.type)
pd.crosstab(test_pred_m,email_test.type)

#Evaluation on training data
#Training data Accuracy
train_pred_m=classifier_mb.predict(train_tfidf)
accuracy_test_m=np.mean(test_pred_m==email_test.type)
accuracy_test_m
#Test Data To the naive bayes model
classifier_mb_lap=MB(alpha=3)
classifier_mb_lap.fit(train_tfidf,email_train.type)
##accuracy after turning 
test_pred_lap=classifier_mb_lap.predict(test_tfidf)
accuracy_test_lap=np.mean(test_pred_lap==email_test.type)
accuracy_test_lap
accuracy_score(test_pred_lap,email_test.type)

from sklearn.metrics import accuracy_score
accuracy_score(test_pred_lap,email_test.type)
pd.crosstab(test_pred_lap, email_test.type)

#Training Data Accuracy
train_pred_lap=classifier_mb_lap.predict(train_tfidf)
accuarcy_train_lap=np.mean(train_pred_lap==email_train.type)
accuracy_train_lap

