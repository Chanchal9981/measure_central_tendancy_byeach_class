# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#https://drive.google.com/file/d/1jqQkxb7r5hKeDZic259zUw6_6UKeVzGQ/view?usp=sharing
#there is original link to the google drive and make some change
x=r"https://drive.google.com/uc?export=download&id=1jqQkxb7r5hKeDZic259zUw6_6UKeVzGQ"
x1=pd.read_csv(x)
x1

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

x1.isnull().sum()

null_values=x1.isnull().sum()/x1.shape[0]*100
null_values

x2=null_values[null_values>20].keys()
x2

x3=x1.drop(columns=x2)
x3

x4=x3.select_dtypes(include=['int64','float64'])
x4

x4.isnull().sum()

null_columns=[var for var in x4.columns if x4[var].isnull().sum()>0]
null_columns

#most repeated value
x1['LotConfig'].unique()

x1[x1.loc[:,'LotConfig']=="Inside"]["LotFrontage"].replace(np.nan,x1[x1.loc[:,'LotConfig']=="Inside"]["LotFrontage"].mean())

x4_copy=x1.copy()
num_vars_miss=['LotFrontage','MasVnrArea','GarageYrBlt']
cats_vars=['LotConfig','MasVnrType','GarageType']
for cat_var,num_var in zip(cats_vars,num_vars_miss):
    for var_class in x1[cat_var].unique():
        x4_copy.update(x1[x1.loc[:,cat_var]==var_class][num_var].replace(np.nan,x1[x1.loc[:,cat_var]==var_class][num_var].mean()))

x4_copy[num_vars_miss].isnull().sum()

#to access the columns which depands on the others 
#categorical columns which helps to clean  the data if its not clean then data are also not clean
x4_copy[x4_copy[['MasVnrType']].isnull().any(axis=1)]

x4_copy=x1.copy()
num_vars_miss=['LotFrontage','MasVnrArea','GarageYrBlt']
cats_vars=['LotConfig','Exterior2nd','KitchenQual']
for cat_var,num_var in zip(cats_vars,num_vars_miss):
    for var_class in x1[cat_var].unique():
        x4_copy.update(x1[x1.loc[:,cat_var]==var_class][num_var].replace(np.nan,x1[x1.loc[:,cat_var]==var_class][num_var].mean()))

x4_copy[num_vars_miss].isnull().sum()

"""# Data Destribution"""

plt.figure(figsize=(10,10))
sns.set()
for i,var in enumerate(num_vars_miss):
    plt.subplot(2,2,i+1)
    sns.distplot(x1[var],bins=20,kde_kws={'linewidth':8,'color':'red'},label="orignol_data")
    sns.distplot(x4_copy[var],bins=20,kde_kws={'linewidth':5,'color':'green'},label="Destribution_Data")
    plt.legend()

