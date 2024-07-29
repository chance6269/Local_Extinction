# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 09:38:38 2024

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
# 인구밀도
file_path = f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Raw_data/인구밀도.xlsx"
df = pd.read_excel(file_path,header=1)
#%%
# 세종
df_sejong = df.iloc[8] # 세로버전 transpose()필요없음
df_sejong =df_sejong[1:]
df_sejong = df_sejong .to_frame()
df_sejong.columns = ['인구밀도(세종인구/면적)']
df_sejong = df_sejong.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/sejong_data/sejong_dens.csv",index=False)
df_sejong  = pd.read_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/sejong_data/sejong_dens.csv")
df_sejong = df_sejong.round(2)
#%%
# 충북
df_chungbuk = df.iloc[11] # 세로버전 transpose()필요없음
df_chungbuk =df_chungbuk[1:]
df_chungbuk = df_chungbuk.to_frame()
df_chungbuk.columns = ['인구밀도(충북인구/면적)']

df_chungbuk = df_chungbuk.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungbuk_data/chungbuk_dens.csv",index=False)
df_chungbuk = pd.read_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungbuk_data/chungbuk_dens.csv")
df_chungbuk = df_chungbuk.round(2)


#%%
# 충남
df_chungnam = df.iloc[12] # 세로버전 transpose()필요없음
df_chungnam = df_chungnam[1:]
df_chungnam = df_chungnam.to_frame()
df_chungnam.columns = ['인구밀도(충남인구/면적)']
df_chungnam = df_chungnam.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungnam_data/chungnam_dens.csv", index=False)
df_chungnam = pd.read_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungnam_data/chungnam_dens.csv")
df_chungnam = df_chungnam.round(2)


#%%

file_path = f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/sejong_data/result_sejong.csv"
edu1 = pd.read_csv(file_path, header=None)
edu1 = edu1.iloc[:, 1]
edu1 = edu1.rename('교육인프라(수)')

#%%

file_path = f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungnam_data/result_chungnam.csv"
edu2 = pd.read_csv(file_path, header=None)
edu2 = edu2.iloc[:, 1]
edu2 = edu2.rename('교육인프라(수)')

#%%

file_path = f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/chungbuk_data/result_chungbuk.csv"
edu3 = pd.read_csv(file_path, header=None)
edu3 = edu3.iloc[:, 1]
edu3 = edu3.rename('교육인프라(수)')

#%%
sejong = pd.concat([edu1, df_sejong],axis=1)
chungnam = pd.concat([edu2, df_chungnam],axis=1)
chungbuk = pd.concat([edu3, df_chungbuk],axis=1)

#%%
'''
fig = plt.figure(figsize=(10,5))
sns.regplot(x='교육인프라(수)', y='인구(수)', data=sejong) 
plt.title('세종 : 교육인프라와 인구관계도')

plt.savefig(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/세종/pop_dens.png")
plt.show()
'''
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
import seaborn as sns
#%%
# 폰트설정
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
#%%



