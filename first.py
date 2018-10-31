# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 11:24:14 2018

@author: xuduo
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

file = 'world_data_North_Asia.xlsx'
file_2 = 'world_data_hult_regions.xlsx'
WD_NA = pd.read_excel(file)
WD = pd.read_excel(file_2)

WD.count()

WD_NA.isnull().sum()/len(WD_NA)

WD.isnull().sum()/len(WD)

WD_back = pd.DataFrame.copy(WD_NA)
WD_back = WD_back.drop(['incidence_hiv'], axis = 1)

WD_back = WD_back.iloc[:, 4:]
WD_back = WD_back[:-1]

""" Impute missing values using the mean of each column """
for col in WD_back:

    if WD_back[col].isnull().any():
        
        col_mean = WD_back[col].mean()
        
        WD_back[col] = WD_back[col].fillna(col_mean).round(2)

WD_back['income_group_num'] = 0
for each in enumerate(WD_back['income_group']):
    if each[1] == 'Low income':
        WD_back['income_group_num'][each[0]] = 1
    elif each[1] == 'Lower middle income':
        WD_back['income_group_num'][each[0]] = 2
    elif each[1] == 'Upper middle income':
        WD_back['income_group_num'][each[0]] = 3
    elif each[1] == 'High income':
        WD_back['income_group_num'][each[0]] = 4

WD_back = WD_back.iloc[:, 1:]

for each in WD_back:
    WD_back[each].hist(bins = 'fd', hue = 'income_group_num')
    plt.xlabel(f'{each}')
    plt.savefig(f'{each}.png')
    plt.show()

help(pd.DataFrame.hist)
for each in WD_back:
    WD_back[[each]].boxplot()
    plt.title(f'Boxplot for {each}')
    plt.savefig(f'Boxplot for {each}_2.png')
    plt.show()

df_corr = WD_back.corr().round(2)

print(df_corr)

sns.palplot(sns.color_palette('coolwarm', 12))

fig, ax = plt.subplots(figsize=(15,15))

sns.heatmap(df_corr,
            cmap = 'coolwarm',
            square = True,
            annot = True,
            linecolor = 'black',
            linewidths = 0.5)


plt.savefig('World Bank Data corr heat map_2.png')
plt.show()

sns.pairplot(data = WD_back,
             hue = 'income_group_num', palette = 'plasma')


plt.tight_layout()
plt.savefig('WD_back pairplot-first.png')
plt.show()


help(pd.DataFrame)
WD_NA.count()

WD_NA.isnull().any().sum()
#We have 21 columns have missing values

WD_NA.isnull().sum()
#Only Singapore has data at Lit_PCT column

WD_NA.info()
#4 Categorical Data


WD_NA.describe()

WD_NA['access_to_electricity_pop'].hist(bin = 'fd')

count = 1
for col in WD_NA.iloc[:, 5:]:
    col.hist(bin = 'fd')
    plt.savefig(f'Hist{count}')
    count += 1
    plt.show()

#Flaging the income Group
for each in enumerate(WD_NA['income_group']):
    if each[1] == 'Low income':
        WD_NA['income_group_num'][each[0]] = 1
    elif each[1] == 'Lower middle income':
        WD_NA['income_group_num'][each[0]] = 2
    elif each[1] == 'Upper middle income':
        WD_NA['income_group_num'][each[0]] = 3
    elif each[1] == 'High income':
        WD_NA['income_group_num'][each[0]] = 4
        
pd.set_option('display.max_columns', 31)

WD_NA_1 = WD_NA[WD_NA['income_group_num'] == 1]
WD_NA_2 = WD_NA[WD_NA['income_group_num'] == 2]
WD_NA_3 = WD_NA[WD_NA['income_group_num'] == 3]
WD_NA_4 = WD_NA[WD_NA['income_group_num'] == 4]


