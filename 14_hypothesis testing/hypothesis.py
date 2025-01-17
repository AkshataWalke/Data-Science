# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:19:48 2025

@author: Akshata Walke
"""

import pandas as pd
import numpy as np
import scipy
from scipy import stats
#provides statical functions
from statsmodels.stats import descriptivestats as sd
#provides descriptive statistics tools,including the sign_test
from statsmodel.stats.weightstats import ztest
#used for conducting Z-tests on dataset

#1 Sample sign test
#whenever there is a single sample data is not normal
marks=pd.read_csv("C:/14_hypothesis testing/Signtest.csv")

#Normal QQ plot
import pylab
stats.probplot(marks.Scores,dist='norm',plot=pylab)
#creates a QQ plot TO visually chcek if the data follows a normal distribution
#Test for normality
shapiro_test=stats.shapiro(marks.Scores)
#perform the Shapiro_Wilk test for normality
#H0(null hypo):the data is normally distributed
#H1(alternative hypo):the data is not normally distributed
print("Shapiro Test:",shapiro_test)
#p-value is 0.024<0.05,data is not normal
#Desriptive statistics
print(marks.Scores.describe())
#mean=84.20 and median=89.00
#1-sample sign test
sign_test_result=sd.sign_test(marks.Scores,mu0=marks.Scores.mean())
print("Sign Test Result:",sign_test_result)
#RESult : p-value=0.82
#Interpretation
#H0:the median of Scores is equal to the mean of Scores
#H!:The median of Scores is not equal to the mean of Scores
#Since the p-value (0.82) is greater than 0.05 we fail to reject the null
#Conclusion:The median and mean of Scores are Statistically not similar



#1-sample z-test
fabric=pd.read_csv("C:/14_hypothesis testing/Fabric_data.csv")

#Normality test
fabric_normality=stats.shapiro(fabric)
print("Fabric Normality Test:",fabric_normality)
#p-value=0.1460>0.05

fabric_mean =np.mean(fabric)
print("Mean Fabric Length:",fabric_mean)

#Z-test
z_test_result,p_val=ztest(fabric['Fabric_length'],value=150)
print("Z-Test Result:",z_test_result,"P-Value:",p_val)
#Result:p-value=7.15x10^-6
#Interpretatation
#H0:mean fabric length is 150
#H1:mean fabric length is not 150
#since the p-value is extremely small ,we reject the 
#coclusion :the mean fabric length significantly differs

#Mean-Whitney Tesy

fuel=pd.read_csv("C:/14_hypothesis testing/mann_whitney_additive.csv")
fuel.columns=["Without_additive","With_additive"]

#Normality tests
print("Without Additive Normality:",stats.shapiro(fuel.Without_additive))
#p=0.50>0.05:accept H0
print("With Additive Normality:",stats.shapiro(fuel.With_additive))
#0.04<0.05:reject H0 data is not normal

#Mann Whitney U test
mannwhitney_result=stats.mannwhitneyu(fuel.Without_additive,fuel.With_additive)
print("Mann-Whitney Test Result:",mannwhitney_result)
#Result:p-value=0.445
#Interpretation
#H0:No diff in performance between without_additive and with_additive
#H1:A significance difference exists.
#since the p-value(0.445)is greater than 0.05,we fail to reject the null hypothesis
#coclusion:Adding fuel additive does not significantlly impact peformance
#applies the Mann-Whitney U test to check if there's a significant difference
#H0:no diff in performance bet two grps
#H1:Significant diff in performance

#Objective:check whether there is diff in transaction time of supplier_A
#ans supplier_B
#Paired T-test

#normality test
print("Supplier A Normality Test:",stats.shapiro(sup.SupplierA))
#
print("Supplier B Normality Test:",stats.shapiro(sup.SupplierB))
#Paired T-Test
t_test_result,p_val=stats.ttest_rel(sup['SupplierA'],sup['SupplierB'])
print("Paired T-Test Result:",t_test_result,"P-Value",p_val)
#Result:p-value=0.00
#H0:No significant difference in transaction times bet supplier A and B
#H1:A significant diff exists
#Since the p-value is less than 0.05 we reject













#############################17/01/25######################
##########################################################
##########################################################
#15-01-2025
#Two-Sample T-Test
import pandas as pd
offers=pd.read_excel("C:/14_Hypothesis_Testing/Promotion.xlsx")
offers.columns=["InterestRateWaiver NOrmality","StandardPromotion"]


print("InterestRateWaiver Normality",stats.shapiro(offers.InterestRateWaiver))
print("StandardPromotion Normality",stats.shapiro(offers.StandardPromotion))
# Normality Test
levene_test = scipy.stats.levene(offers.InterestRateWaiver,offers.StandardPromotion)
print("Leave Test (Varience):" ,levene_test)
# p value 
#
#
#
#
ttest_result=scipy.stats.ttest__ind(offers.InterestRateWaiver,offers.StandardPromotion)
print("Two - sample T-Test",ttest_result)
#result :pvalue=0.0242
#interpretation
#H0 ;BOth offers have same mean
#Ha ; The mean impacts the two offers are different
#since the p value (0.0242) is less than 0.05 ,we reject the null hypothesis
#conclision:: Thereee is a significant diff 

                  
###############################################################################
###############################################################################
#Mood's Median Test
#Objective ::Is the median of Pooh,Piglet and  Tigger are statistically equal
#it has equal meadian or not
animals=pd.read_csv("C:/14_Hypothesis_Testing/animals.csv")


#Normality Tests
print("Pooh Normality :",stats.shapiro(animals.Pooh))
#p value:0.0122
print("Piglet Normality:",stats.shapiro(animals.Piglet))
#pvalue:0.044
print("Tigger Normality :",stats.shapiro(animals.Tigger))
#pvalue:0.021
#H0:data is normal
#Ha:data is not normal
#Since all p value are les  than 0.05 hence  reject null hypothesis
#data is not normal hence Mood's Test
#Median Test
median_test_result=stats.median_test(animals.Pooh,animals.Piglet,animals.Tigger)
print("Moods Median Test :",median_test_result)
#Result :pvalue:0.186
#Interpretation
# H0 :: all group have equal medians.
# Ha :: at least one group has diff meadin


#########################################################
#One way Anova test
#Objective : it is the transaction times for the 3 supplier are not
# significantly different
contract=pd.read_excel("C:/14_Hypothesis_Testing/ContractRenewal_Data(unstacked).xlsx")
contract.columns=["Supp_A","Supp_B","Supp_C"]


#Normality test
print("Supp_A Normality:",stats.shapiro(contract.Supp_A))
print("Supp_B Normality:",stats.shapiro(contract.Supp_B))
print("Supp_C Normality:",stats.shapiro(contract.Supp_C))
# all p value are greater than 0.05
# we fail to rehect H0
# h0 is acepted means data is normal
#varience test
levene_test = scipy.stats.levene(contract.Supp_A,contract.Supp_B,contract.Supp_C)
print("Leave Test (Variance)",levene_test) 
#H0 :data is having equal variance
#
##H1 :data is having equal variance
#p value is =0.7775,H0 is accepted

#Anova Test
anova_result=stats.f_oneway(contract.Supp_A,contract.Supp_B,contract.Supp_C)
print("One way Anova:",anova_result)
#Result :: p value is:0.103
# inter pretation
#H0 :: all supplier have same mean transaction time 
#H1:: At least one supplier have the diff mean
#since  the p value is 0.103 is greater than 0.05  so we fail to reject H0
#conclusion :: The transaction time for the 3 suppliers are not equal


soft_drink=pd.read_excel("C:/14_hypothesis testing/JohnyTalkers.xlsx")
from statsmodels.stats.proportion import proportions_ztest

#data preparation
count=np.array([58,152])
nobs=np.array([480,740])
#the two-proportion Z-test compares the proportions of two groups.

#Counts=[58,152]:the number of asuccesses
#(people consuming soft drinkd)in each group(adults and chirlden).

#nobs=[480,740]:the total no.of observations
#in each gruop(total adults and chirlden surveyed).
#The count and nobs values came from summarizing the data
#Aabout the soft drink consumption for adults and chirlden
#Heres how these values are typically obtained:
    
#count:Represents the no. of individuals in each grp
#who consumes soft drinks 

#nobs=Represents the total number of individuals surveyed in each group

#the total no. of adults surveyed is 480.
#the total no. of chirlden surveyed is 740.
#hence,nobs=[480,740]

#these values are often extracted from a dataset.
#if your data is in a file(like "JohnyTalkers.xls")
#you can calculate these values as follows:



import pandas as pd

#load the datset 
file_path="C:/14_hypothesis testing/JohnyTalkers.xlsx"
soft_drink_data=pd.read.excel(file_path)

#filter the data into adults and chirlden categories
adults=soft_drink_data[soft_drink_data['Person']=='Adults']
chirlden=soft_drink_data[soft_drink_data['Person']=='Chirlden']

#Count of Successes
count_adults=adults[adults['Drinks']=='Purchased'].shape[0]
count_chirlden=chirlden[chirlden['Drinks']=='Purchased'].shape[0]

#Total observations for each group
nobs_adults=adults.shape[0]
nob_children=chirlden.shape[0]

#Final arrays for Z-test
count=[count_adults,count_chirlden]
nobs=[nobs_adults,nobs_children]

print("Counts(Soft drink Consumers):",count)
print("Total observations:",nobs)

#two sided test
z_stat,p_val =proportions_ztest(count, nobs,alternative='two-sided')
print("Two-Sided Propotion Test:",z_stat,"P-value:",p_val)
#Result:p-value=0.000
#Interpretation:
#H0:Proportions of adults and children consuming the soft drink are the same.
#H1:proportions are different.
#Since the p-value(0.000) is less than 0.05,we reject the null hypothesis.
#Conclusion:there is a significant difference in soft drink consumption.

###########################################17/01/2025##########################

#Chi-Square Test
#objective:is defective proportions are independent of the country?
#the datset contains two columns:

    
#Defective:indicates whether an item is defective(likely binary,with 1 for defective and o for not defective)
#Country:specifies the country associated with the item(e.g. India)
#The dataset has 800 entries,there are no missing values in either column.It appears to be designed to analysis.
#To analyze detect rates across different countries, which aligns with the Chi-Sqaure test you performed earlier
#to determine if defectiveness is independent of the country 
Bahaman=pd.read_excel("C:14_hypothesis testing/Bahaman (1).xlsx")
                      
#Crosstabulation
count=pd.crosstab(Bahaman["Defective"], Bahaman["Country"])
count
#Chi-Square Test
chi2_result=scipy.stats.chi2_contingency(count)
print("Chi-Square Test:",chi2_result)
#Resulr:pvalue=0.6315
#Interprestation
#H0=Defective proportions are independent of the country
#H1=Defective proportions depend on the country
#since the p-value (0.6315)is greater than 0.05,we accept the Null hypothesis
#Conclusion:Defective proprtions are proportion are indeependent of the country
