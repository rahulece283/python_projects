# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import os
import sys
import unittest

os.getcwd()

df = pd.read_csv("DemographicData.csv")

df.info()

#column wise count of unique values
df.nunique()

#Frequency of values in a column
df['IncomeGroup'].value_counts()

#List of columns in a dataframe
df.columns.values.tolist()

#Frequency of column names
df.columns.value_counts()

#rename a column name
df=df.rename(columns={'Income Group':'IncomeGroup'}, inplace=False)

class Wrangle:
    
    def __init__(self, dataframe):
        self.dataframe = dataframe
        #filter data using loc
    def incomeGroupIloc(self):
        d1 = self.dataframe.loc[self.dataframe['Income Group'] == 'High income']
        d2 = self.dataframe.loc[self.dataframe['Income Group'] == 'Low income']
        d3 = self.dataframe.loc[self.dataframe['Income Group'] == 'Upper middle income']
        d4 = self.dataframe.loc[self.dataframe['Income Group'] == 'Lower middle income']
        return d1,d2,d3,d4
        #filter data using a query
    def incomeGroupQuery(self):
        d1 = self.dataframe.query('IncomeGroup == "High income"')
        d2 = self.dataframe.query('IncomeGroup == "Low income"')
        d3 = self.dataframe.query('IncomeGroup == "Upper middle income"')
        d4 = self.dataframe.query('IncomeGroup == "Lower middle income"')
        return d1,d2,d3,d4

    def incomeGroupLambda(self):
        d1 = self.dataframe.apply(lambda x: x['Income Group'] =='High income')
        d2 = self.dataframe['Income Group'].apply(lambda x: x in x == 'Low income')
        d3 = self.dataframe['Income Group'].apply(lambda x: x in x == 'Upper middle income')
        d4 = self.dataframe['Income Group'].apply(lambda x: x in x == 'Lower middle income')
        return d1,d2,d3,d4

wrdf = Wrangle(df)


df1, df2, df3, df4 = wrdf.incomeGroupIloc()

df5, df6, df7, df8 = wrdf.incomeGroupQuery()

#compare column names

#read data from SAS/SQL/ODBC

#Dynamic naming of function

#Filtering Data: Various conditions 

#isin
#isnull