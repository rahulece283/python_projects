#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 10:48:06 2018

@author: rahulsharma
"""

import pandas as pd
import numpy as np
import os

path = r"/Users/rahulsharma/Documents/Python/practice"
df1 = pd.read_csv(path + '/DemographicData.csv')

df2 = pd.DataFrame({'Number':[1,2,3,4,5]}, index=['CountryName', 'CountryCode', 'Birthrate', 'Internetusers', 'IncomeGroup'])

class Massage:
    
    def __init__(self):
        pass
    
    def removeSpacesInColumnName(df):
        df.columns = df.columns.str.replace(" ","")
        return df
    
    def filterdata(df, l=[]):
        df_f = df.loc[:,l]
        return df_f
    
    def filterlastcolumn(df):
        df_f = df.iloc[:,len(df.columns.values.tolist())-1]
        return pd.DataFrame(df_f)
    
    def filtercolumncontains(df,s=""):
        df_f = df.loc[df["IncomeGroup"]==s,df.columns.str.contains(s)]
    
    def filterquery(df):
        df_f = df.query('IncomeGroup == "Low income"' )
        return df_f

    def filtercolumnsrowslambda(df,s=""):
        df_f = df.loc[df["IncomeGroup"].apply(lambda x: x if x==s else "NA"),:]
        return df_f
    
    def filterFromDataFrameIndex(df, dff):
        l = dff.index
        df_f = df.loc[:,l[:3]]
        return pd.DataFrame(df_f)
    
    def filterrowcontains(df,f="",s=""):
        df_f = df.loc[df[f].str.contains(s),:]
        return df_f

l=['IncomeGroup']


filtered = Massage.removeSpacesInColumnName(df1)
filtered1 = Massage.filterdata(df1,l)
filtered2 = Massage.filterlastcolumn(df1)
filtered3 = Massage.filtercolumncontains(df1, "come|Birth")
filtered4 = Massage.filterquery(df1)
filtered5 = Massage.filtercolumnsrowslambda(df1, "Low income")
filtered6 = Massage.filterFromDataFrameIndex(df1, df2)
filtered7 = Massage.filterrowcontains(df1,"CountryCode","USA|TZA|IND|ABC")


#create a df with function names
df_func = pd.DataFrame({'seq':[2,1,3,4,5,6,7,8],'func_nm' : ['filterdata','removeSpacesInColumnName','filterlastcolumn','filtercolumncontains','filterquery','filtercolumnsrowslambda','filterFromDataFrameIndex','filterrowcontains']})

#sort  df
df_func = df_func.sort_values(['seq'], ascending=[1])

#reset index
df_func = df_func.set_index('seq')

#dick = df_func.to_dict(orient = 'index')
#create dictionary from a df
dick = dict([(i,a) for i, a in zip(df_func.index, df_func.func_nm)])

print (dick)

eval(dick[1])