# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 08:18:16 2024

@author: Akshata Walke
"""

'''
1. You are given a dataset of movies with various attributes like genres,
keywords, and descriptions. Your task is to build a content-based
recommendation engine that recommends movies similar to a given movie
based on these attributes.
Steps:
 Preprocess the Data: Extract relevant features (e.g., genres, overview).
 Vectorize the Text Data: Use TF-IDF on the overview field.
 Compute Similarity: Use cosine similarity to find similar movies.
 Recommend: Given a movie, recommend the top 10 most similar movies based on
content.
Note: Use IMDB dataset

'''
import bs4
from bs4 import BeautifulSoup as bs
import requests
link="C:/9-PCA_SVD/IMDb_Movie_Reviews.csv";
page=requests.get(link)
page
page.content
soup=bs(page.content,'html.parser')
print(soup.prettify())
soup
names=soup.find_all('span',class_="a-spacing-small")
names
cust_names=[]

for i in range(0,len(names)):
    cust_names.append(names[i].get_text())
cust_names
len(cust_names)
#cust_names.pop(-1)
#len(cust_names











'''
4. Using the mlxtend library, write a Python program to generate association 
rules from a dataset of transactions. The program should allow setting a 
minimum support threshold and minimum confidence threshold for rule 
generation.

transactions = [['Tea', 'Bun'], ['Tea', 'Bread'], ['Bread', 'Bun'], ['Tea', 'Bun', 
'Bread']]
'''

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
#Sample dataset
transactions = [['Tea', 'Bun'], ['Tea', 'Bread'], ['Bread', 'Bun'], ['Tea', 'Bun', 'Bread']]

#step 1: 
te = TransactionEncoder()
te_ary= te.fit(transactions).transform(transactions)
df= pd.DataFrame(te_ary, columns=te.columns_)

#step 2: 
frequent_itemsets= apriori(df, min_support=0.5, use_colnames=True)

#step 3: 
if frequent_itemsets.empty:
    print("No frequent itemsets found.")
else:
    rules= association_rules(frequent_itemsets, metric="lift", min_threshold=11)

#step 4: 
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules[['antecedents','consequents','support','confidence','lift']])



'''
Q.2. What will be the output of following code?
'''
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

transactions = [['Apple', 'Banana'], ['Apple', 'Orange'], ['Banana', 'Orange'], ['Apple', 'Banana', 'Orange']]

te=TransactionEncoder()
transformed_data=te.fit(transactions).transform(transactions)
df=pd.DataFrame(transformed_data,columns=te.columns_)
frequent_itemsets=fpgrowth(df,min_support=0.5,use_colnames=True)

print(frequent_itemsets)
##OUTPUT
##itemsets
#0     0.75          (Banana)
#1     0.75           (Apple)
#2     0.75          (Orange)
#3     0.50  (Orange, Banana)
#4     0.50   (Banana, Apple)
#5     0.50   (Orange, Apple)
'''
3. Build an item-based collaborative filtering recommendation engine. 
Instead of recommending items based on similar users, recommend items 
that are similar to those that a user has already interacted with.
Steps:
 Preprocess the Data: Create a user-item matrix where rows are users and columns are 
items (movies).
 Compute Item Similarity: Calculate similarity between items based on user 
interactions.
 Recommend Items: For a given user, recommend items that are similar to those the 
user has already rated highly.

'''

'''
5. Build a popularity-based recommendation system. The system should 
recommend movies based on their overall popularity (e.g., number of ratings 
or average rating).
Steps:
 Preprocess the Data: Calculate the total number of ratings and average rating for each 
movie.
 Rank the Movies: Rank movies based on the chosen popularity metric.
 Recommend Movies: Recommend the top N most popular movies to any user
'''
import pandas as pd
