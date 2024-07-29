# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 12:40:09 2024

@author: Shin
"""

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
import seaborn as sns

# 폰트설정
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
#%%
#city = ['result_sejong', 'chungbuk_sejong']

file_path = f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/sejong_data/result_sejong.csv"
edu = pd.read_csv(file_path, header=None)
edu = edu.iloc[:, 1]
edu = edu.rename('교육인프라(수)')
#%%
# 0으로 값 변경
#edu.iloc[:, 0] = 0
#%% 

file_path = f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/sejong_data/sejong_pop.csv"
pop = pd.read_csv(file_path)
pop = pop.iloc[:, 1]
pop = pop.rename('인구(수)')
#%%
sejong = pd.concat([edu, pop],axis=1)
#%%
sejong.plot(kind='scatter', x='인구(수)', y='교육인프라(수)', c='coral', s=10, figsize=(10, 5), marker='+')
plt.title('세종 : 교육인프라와 인구관계도')
plt.xlabel('인구(수)')
plt.ylabel('교육인프라(수)')
plt.savefig(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/세종/pop_edu.png")
plt.show()
#%%

sejong = pd.concat([edu, pop],axis=1)

sejong.plot(kind='scatter', x='교육인프라(수)', y='인구(수)', c='coral', s=10, figsize=(10, 5), marker='+')
plt.title('세종 : 교육인프라와 인구관계도')
plt.xlabel('교육인프라(수)')
plt.ylabel('인구(수)')
plt.savefig(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/세종/edu_pop.png")
plt.show()

#%%

fig = plt.figure(figsize=(10,5))

sns.regplot(x='인구(수)', y='교육인프라(수)', data=sejong) #ax= ax1
plt.title('세종 : 교육인프라와 인구관계도')

plt.savefig(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/세종/pop_edu_reg.png")
plt.show()
#%%
fig = plt.figure(figsize=(10,5))
sns.regplot(x='교육인프라(수)', y='인구(수)', data=sejong) 
plt.title('세종 : 교육인프라와 인구관계도')

plt.savefig(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/세종/edu_pop_reg.png")
plt.show()











