# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 09:46:16 2025

@author: Akshata Walke
"""

import pandas as pd
import numpy as np
import seaborn as sns
wcat=pd.read_csv("C:/linear regression/wc-at.csv")
# FDA
wcat.info()
wcat.describe()
#Average waist is 91.90 and min is 63.50 and max is 121
# Average AT is 101.89 and min is 11.44 and max is 253
import matplotlib.pyplot as plt
plt.bar(height=wcat.AT,x=np.arange(1,110,1))
sns.distplot(wcat.AT)
# Data is normal but right skewed
plt.boxplot(wcat.AT)

plt.boxplot(wcat.AT)
# no outliers but right skewsd
plt.bar(height=wcat.Waist,x=np.arange(1,110,1))
sns.distplot(wcat.AT)

# data is normal binomial
plt.boxplot(wcat.AT)
plt.bar(height=wcat.Waist,x=np.arrange(1,110,1))
sns.distplot(wcat.Waist)
# data is bidonomial
############################
# bivariant analysis
plt.scatter(x=wcat.Waist,y=wcat.AT)
# data is linearly scatterd,direction postive,strength:poor
# now let us check dirction of correletion
np.corrcoef(wcat.Waist,wcat.AT)
# the corrlection coefficienyt is 0.8185<0.85 hence
# the correlction is moderate
# let us check the direction of correlction
cov_output=np.cov(wcat.Waist,wcat.AT)[0,1]
cov_output
#635.91,it is postive means correlation will postive
#################################################
# let us apply to various model and check the feasiblity
import statsmodels.formula.api as smf
# first simple linear model
model=smf.ols('AT~Waist',data=wcat).fit()
#  Y is AT and x is waist
model.summary()
# r-squarred-0.67<0.85,there is scope of imporvement
# p=0<0.05 hence acceptable
# bita-0=-215.98
# bitA -1=3.45
pred1=model.predict(pd.DataFrame(wcat.Waist))
pred1
##############################
# Regression line
plt.scatter(wcat.Waist,wcat.AT)
plt.plot(wcat.Waist,pred1,'r')
plt.legend(['Predicted line','Observed data'])
plt.show()
####################
## error calculations
res1=wcat.AT-pred1
np.mean(res1)
res_sqr1=res1*res1
mse1=np.mean(res_sqr1)
rmse1=np.sqrt(mse1)
rmse1
#32.76
#######################
# let us try another model
# x=log(waist)
plt.scatter(x=np.log(wcat.Waist),y=wcat.AT)
# data  is linerlay scatterd,direction postively,streghth:poor
# now let us check the correlation coefficient
np.corrcoef(np.log(wcat.Waist),wcat.AT)
# the correlation coefficent is 0.8185
#
model2=smf.ols('AT~np.log(Waist)',data=wcat).fit()
#
model2.summary()
#
#
#
#
pred2=model.predict(pd.DataFrame(wcat.Waist))
pred2
##########################
plt.scatter(x=(wcat.Waist), y=np.log(wcat.AT))


np.corrcoef(wcat.Waist,np.log(wcat.AT))

model3=smf.ols('np.log(AT)~Waist',data=wcat).fit()
model3.summary()
#R-sqarred=0.707.<0.85

pred3=model3.predict(pd.DataFrame(wcat.Waist))
pred3_at
###################

plt.scatter(wcat.Waist, np.log(wcat.AT))
plt.plot(wcat.Waist,pred3,'r')
plt.legend(['Predicted line','Observed data_model3'])
plt.show()
############################
####error calculations
res3=wcat.AT-pred3_at

res_sqr3=res3*res3
mse3=np.mean(res_sqr3)
rmse3=np.sqrt(mse3)
rmse3
###########################

#Now let us make Y=log(AT) And X-WAist,X*X=Waist.Waist
#polynomial model 
#here r can be calculated
model4=smf.ols('np.Log(AT)~Waist+I(Waist*Waist)',data=wcat).fit()
model4.summary()
#R-sqarred=0.779<0
pred4=model4.predict(pd.DataFrame(wcat.Waist))
pred4
pred4_at=np.exp(pred4)
pred4_at
####################
#Regression line
plt.scatter(wcat.Waist,np.log(wcat.AT))
plt.plot(wcat.Waist,pred4,'r')
plt.legend(['Predicted line','Observed data_model3'])
plt.show()
#################
#error calculations
res4=wcat.AT-pred4_at

res_sqr4=res4*res4
mse4=np.mean(res_sqr4)
rmse4=np.sqrt(mse4)
rmse4
#32.24
###############################
#generalize the best model
from sklearn.model_selection import train_test_split
train,test=train_test_split(wcat,test_size=0.2)
plt.scatter(train.Waist,np.log(train.AT))
plt.scatter(test.Waist,np.log(test.AT))
final_model=smf.ols('np.log(AT)~Waist+I(Waist*Waist)',data=wcat).fit()
#Y is log*(AT) and X=Waist
final.model.summary()
#R-sqarred=0.779<0.85,there is scope of improvement
#p=0.000<0.05 hence acceptable
#bita-0=-7.8241



test_pred=final_model.predict(pd.DataFrame(test))


test_pred_at=np.exp(test_pred)
test_pred_at
###########################
train_pred=final_model.predict(pd.DataFrame(test))


train_pred_at=np.exp(train_pred)
train_pred_at
##############################
#Evaluation on test data
test_res=test.AT-test_pred_at
test_sqr=test_res*test_res
test_mse=np.mean(test_sqr)
test_rmse=np.sqrt(test_mse)
test_rmse
#############################
#Evaluation on train data
train_res=train.AT-train_pred_at
train_sqr=train_res*train_res
train_mse=np.mean(train_sqr)
train_rmse=np.sqrt(train_mse)
train_rmse
################################
#test_rmse>train_rmse





###########6/01/2025###############################

#Multiple correlation analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


Cars=pd.read_csv("C:/DataSet/Cars.csv")
'''
#Exploratory data analysis
1.Measure the central tendancy
2.measure the dispersion
3.third moment business dicision
4.Fourth moment business dicision
5.probability distribution
6.graphical representation(histogram,boxplot)
'''
Cars.describe()

#Graphical representation

plt.bar(height=Cars.HP,x=np.arange(1,82,1))
plt.hist(Cars.HP)
plt.boxplot(Cars.HP)
'''
There are several outliers in HP columns
similar operations are expected for other three columns
Now let us plot joint plot,joint plot is to show scatter plot
'''
#Histogram

sns.jointplot(x=Cars['HP'],y=Cars['MPG'])
#now let us plot count plot
plt.figure(1,figsize=(16,10))
sns.countplot(Cars['HP'])
#Count plot shows how many times the each value occured
#92 HP value occured 7 times
#QQ plot
from scipy import stats
import pylab
stats.probplot(Cars.MPG,dist="norm",plot=pylab)
plt.show()
#MPG data is noramlly distributed
#there are 10 scatter plots need to be plotted , one by one is
#to plot , so we can use pair plots
import seaborn as sns

sns.pairplot(Cars.iloc[:,:])
#you can check the collinearity problem between the inputs variables
#you can check plot between SP and HP , They are strongly correlated to each other
#same way you can check WT and VOL , it is also strogly correlated to each other

#now let us check r value between variables
Cars.corr()
#you can check SP and HP, r value is 0.97 and same way
#you can check WT and VOL , it has got 0.999 which is greater