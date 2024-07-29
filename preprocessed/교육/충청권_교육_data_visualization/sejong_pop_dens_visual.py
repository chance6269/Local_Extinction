# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 11:54:36 2024

@author: Shin
"""

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd
import seaborn as sns

def reg():
    import matplotlib.font_manager as fm
    import os

    user_name = os.getlogin()

    fontpath = [f'C:/Users/{user_name}/AppData/Local/Microsoft/Windows/Fonts']
    font_files = fm.findSystemFonts(fontpaths=fontpath)
    for fpath in font_files:
        
        fm.fontManager.addfont(fpath)
#%%
# 폰트설정

#font_path = "c:/Windows/Fonts/malgun.ttf"
#font_name = font_manager.FontProperties(fname=font_path).get_name()
#rc('font', family=font_name)
plt.rc('font', family='NanumBarunGothic')

#%%
# 세종교육인프라
file_path = f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/sejong_data/result_sejong.csv"
edu1 = pd.read_csv(file_path, header=None)
edu1 = edu1.iloc[:, 1]
edu1 = edu1.rename('Number of Education_Infrstructure')
#%%
# 세종인구밀도
df_sejong  = pd.read_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/sejong_data/sejong_dens.csv")
df_sejong = df_sejong.to_frame()
df_sejong.columns = ['Density(Population/Area)']
df_sejong = df_sejong.round(2)
#%%
sejong = pd.concat([edu1, df_sejong],axis=1)
#%%

sns.set_theme(style="whitegrid", palette="pastel")

sns.regplot(x='Density(Population/Area)', y='Number of Education_Infrstructure', data=sejong,
                     truncate=False,        
                  color="m")
plt.title('Sejong Density+Edu_infra Relation')
plt.savefig(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/세종/pop_dens.png")
plt.show()
