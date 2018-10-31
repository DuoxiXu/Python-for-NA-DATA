# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:02:50 2018

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

WD.isnull().sum()/len(WD)

WD_NA_back = pd.DataFrame.copy(WD_NA)
WD_NA_back = WD_NA_back.drop(['incidence_hiv','homicides_per_100k','adult_literacy_pct'], axis = 1)

WD_NA_back = WD_NA_back.iloc[:, 1:]

WD_NA_back['income_group_num'] = 0
for each in enumerate(WD_NA_back['income_group']):
    if each[1] == 'Low income':
        WD_NA_back['income_group_num'][each[0]] = 1
    elif each[1] == 'Lower middle income':
        WD_NA_back['income_group_num'][each[0]] = 2
    elif each[1] == 'Upper middle income':
        WD_NA_back['income_group_num'][each[0]] = 3
    elif each[1] == 'High income':
        WD_NA_back['income_group_num'][each[0]] = 4
        
""" Impute missing values using the mean of each column """
for col in WD_NA_back:

    if WD_NA_back[col].isnull().any():
        
        col_mean = WD_NA_back[col].mean()
        
        WD_NA_back[col] = WD_NA_back[col].fillna(col_mean).round(2)


for each in WD_back:
    plt.subplot(1,2,1)
    WD_NA_back[each].hist(bins = 'fd')
    plt.xlabel('NA region')
    plt.title(f'{each}')
    plt.subplot(1,2,2)
    WD_back[each].hist(bins = 'fd')
    plt.xlabel('Whole World')
    plt.title(f'{each}')
    plt.savefig(f'{each}.png')
    plt.show()

help(pd.DataFrame.hist)
for each in WD_NA_back:
    WD_NA_back[[each]].boxplot()
    plt.title(f'Boxplot for {each}')
    plt.savefig(f'Boxplot for {each} of North Asia.png')
    plt.show()

df_corr = WD_NA_back.corr().round(2)

print(df_corr)

sns.palplot(sns.color_palette('coolwarm', 12))

fig, ax = plt.subplots(figsize=(15,15))

sns.heatmap(df_corr,
            cmap = 'coolwarm',
            square = True,
            annot = True,
            linecolor = 'black',
            linewidths = 0.5)


plt.savefig('North Asia Data corr heat map_filter.png')
plt.show()

for col in df_corr:
    for each in enumerate(df_corr[col]):
        if abs(each[1]) > 0.7:
            df_corr[col][each[0]] = 1
        else:
            df_corr[col][each[0]] = 0
            
df_corr.sum()

sns.pairplot(data = WD_NA_back,
             x_vars = ['child_mortality_per_1k', 'pct_agriculture_employment', 'pct_male_employment', 'pct_female_employment', 'CO2_emissions_per_capita','access_to_electricity_pop','internet_usage_pct','urban_population_pct','income_group_num'],
             y_vars = ['child_mortality_per_1k', 'pct_agriculture_employment', 'pct_male_employment', 'pct_female_employment', 'CO2_emissions_per_capita','access_to_electricity_pop','internet_usage_pct','urban_population_pct','income_group_num'],
             hue = 'income_group_num', palette = 'plasma')

WD_selected = WD_NA_back.loc[:,['child_mortality_per_1k', 'pct_agriculture_employment', 'pct_male_employment', 'pct_female_employment', 'CO2_emissions_per_capita','access_to_electricity_pop','internet_usage_pct','urban_population_pct','income_group_num','pct_services_employment']]

df_corr = WD_selected.corr().round(2)

print(df_corr)

sns.palplot(sns.color_palette('coolwarm', 12))

fig, ax = plt.subplots(figsize=(15,15))

sns.heatmap(df_corr,
            cmap = 'coolwarm',
            square = True,
            annot = True,
            linecolor = 'black',
            linewidths = 0.5)

plt.tight_layout()
plt.savefig('WD_selected corr.png')
plt.show()