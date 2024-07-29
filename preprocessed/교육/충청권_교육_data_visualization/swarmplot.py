# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 12:41:43 2024

@author: Shin
"""


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#%%
file_path = f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungbuk_data/result_chungbuk.csv"
edu3 = pd.read_csv(file_path, header=None)
edu3 = edu3.iloc[:, 1]
edu3 = edu3.rename('Number of Education_Infrstructure')

#%%
df_chungbuk = pd.read_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungbuk_data/chungbuk_dens.csv")
df_chungbuk.columns = ['Density(Population/Area)']
df_chungbuk = df_chungbuk.round(2)
#%%
chungbuk = pd.concat([edu3, df_chungbuk],axis=1)
#%%
sns.set_theme(style="whitegrid", palette="pastel")

sns.regplot(x='Density(Population/Area)', y='Number of Education_Infrstructure', data=chungbuk,truncate=False, color="m")
plt.title('Chungbuk : Density+Edu_infra Relation')
plt.savefig(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/충북/pop_dens.png")
plt.show()

#%%
#충남
file_path = f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungnam_data/result_chungnam.csv"
edu2 = pd.read_csv(file_path, header=None)
edu2 = edu2.iloc[:, 1]
edu2 = edu2.rename('Number of Education_Infrstructure')

#%%
df_chungnam = pd.read_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungnam_data/chungnam_dens.csv")
df_chungnam.columns = ['Density(Population/Area)']
df_chungnam = df_chungnam.round(2)
#%%
chungnam = pd.concat([edu2, df_chungnam],axis=1)
#%%
relation = pd.concat([chungnam, chungbuk],axis=0)
relation['Region'] = ''
relation.index = range(len(relation))
relation.loc[0:9, 'Region'] = 'Chungnam'
relation.loc[10:19, 'Region'] = 'Chungbuk'
#%%
'''
sns.set_theme(style="whitegrid", palette="muted")

# Draw a categorical scatterplot to show each observation
ax = sns.swarmplot(data=relation, x='Density(Population/Area)', y='Number of Education_Infrstructure', hue="Region")
ax.set_xticks(range(220, 260, 0.3))
ax.set(ylabel="Number of Education Infrstructure")
'''

#%%

import seaborn as sns
sns.set_theme(style="whitegrid", palette="muted")

# Load the penguins dataset
df = sns.load_dataset("penguins")

# Draw a categorical scatterplot to show each observation
ax = sns.swarmplot(data=df, x="body_mass_g", y="sex", hue="species")
ax.set(ylabel="")

