# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 11:28:07 2024

@author: Shin
"""


#'sejong'



import pandas as pd

df = pd.read_csv('D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/population.csv')
df_sejong = df.iloc[[7]]
df_sejong = df_sejong.transpose()
df_sejong =df_sejong[1:]

df_sejong.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/sejong_data/sejong_pop.csv")

#%%
#'chungbuk'

df = pd.read_csv('D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/population.csv')
# df_sejong = df.iloc[[11]] 가로버전
df_sejong = df.iloc[11] # 세로버전 transpose()필요없음
df_sejong =df_sejong[1:]

df_sejong.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungbuk_data/chungbuk_pop.csv")

#%%
#'chungnam'

df = pd.read_csv('D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/population.csv')
df_sejong = df.iloc[11] 
df_sejong =df_sejong[1:]

df_sejong.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungnam_data/chungnam_pop.csv")

#%%
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd

# 폰트설정
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
#%%
#city = ['result_chungbuk', 'chungbuk_pop']

file_path = f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungbuk_data/result_chungbuk.csv"
edu = pd.read_csv(file_path, header=None)
edu = edu.iloc[:, 1]
#edu.columns = ['교육인프라(수)']
edu = edu.rename('교육인프라(수)')
#%%
# 0으로 값 변경
#edu.iloc[:, 0] = 0
#%% 

file_path = f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungbuk_data/chungbuk_pop.csv"
pop = pd.read_csv(file_path)
pop = pop.iloc[:, 1]
#pop.columns = ['인구(수)']
pop = pop.rename('인구(수)')
#%%
chungbuk = pd.concat([edu, pop],axis=1)

chungbuk.plot(kind='scatter', x='인구(수)', y='교육인프라(수)', c='coral', s=10, figsize=(10, 5), marker='+')
plt.title('충북 : 교육인프라와 인구관계도')
plt.xlabel('인구(수)')
plt.ylabel('교육인프라(수)')
plt.savefig(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/충북/pop_edu.png")
plt.show()

#%%

chungbuk = pd.concat([edu, pop],axis=1)

chungbuk.plot(kind='scatter', x='교육인프라(수)', y='인구(수)', c='coral', s=10, figsize=(10, 5), marker='+')
plt.title('충북 : 교육인프라와 인구관계도')
plt.xlabel('교육인프라(수)')
plt.ylabel('인구(수)')
plt.savefig(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/충북/edu_pop.png")
plt.show()





#%%
#,'result_chungnam','result_sejong'
