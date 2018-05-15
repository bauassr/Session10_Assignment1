# -*- coding: utf-8 -*-
"""
Created on Sun May 14 00:23:05 2018

@author: singh.shivam"""

import pandas as pd

Dataset = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
#Dataset = pd.read_csv('US_BabyNames.csv')
DF= pd.DataFrame(Dataset)
DF.shape
DF.head()
#Droping Column with name unmaned 
DF.drop(DF.columns[DF.columns.str.contains('unnamed',case = False)],axis = 1,inplace=True)
print('Droping Unnamed columns \n','-'*44,sep="")
print(DF.head())

#Distribution for Gender
Distribution =DF.groupby('Gender').Id.count()
print('Distribution for Gender \n','-'*44,sep="")
print(Distribution)

#Most  Prefered  5 name 
Name= DF.groupby('Name').sum()
print('Most prefered 5 names with Count \n','-'*44,sep="")
print(Name.sort_values('Count',ascending=False).Count.head(5))

#Median Name occurance in dataset 
print('Median Name and its occurance count \n','-'*44,sep="")
print(Name[Name.Count==Name.Count.median()])

#Male and female count by states

#print(DF.groupby('State').Gender.count())
print(DF['State'].value_counts())
