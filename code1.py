#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 27 00:11:14 2018

@author: rahulsharma
"""

import pandas as pd
import numpy as np
import os
import zipfile

path_zip = r"/Users/rahulsharma/Documents/Python/HomeCreditDefaultRisk/csvfiles/"
#path = r"/Users/rahulsharma/Documents/Python/HomeCreditDefaultRisk/csvfiles/"

#Reading csv files from a zipped folder

zip = zipfile.ZipFile(path_zip+"Archive.zip")

file_names_all = zip.namelist()

file_names_csv = [name for name in zip.namelist() if name.startswith('__MACOSX/')==False]

for i,v in enumerate(file_names_csv):
    print(i,v)
    df[i]= pd.read_csv(zip.open(v))
    
    
df_application_test = pd.read_csv(zip.open('application_test.csv'))

#Reading csv files from a folder inside a zipped folder:

'''
zip1 = zipfile.ZipFile(r"/Users/rahulsharma/Documents/Python/HomeCreditDefaultRisk/csvfiles.zip")

print (zip1)

zip1.printdir()

df_application_test_1 = pd.read_csv(zip1.open('csvfiles/application_test.csv'))
'''


#Reading .csv.zip files from a folder:
'''
zip2 = zipfile.ZipFile(r"/Users/rahulsharma/Documents/Python/HomeCreditDefaultRisk/zip_csvfiles/application_test.csv.zip")

df_application_test_2 = pd.read_csv(zip2.open('application_test.csv'))
'''

#Data Exploration:

l_df_application_test = list(df_application_test.columns)

