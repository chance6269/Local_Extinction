# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:08:13 2024 

@author: Shin
"""

import pandas as pd

df = pd.read_csv('D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/population.csv')
df1= pd.read_excel("D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/edu_ins.xlsx")

#%%     

import re

#df_daegeon = df.iloc[[5]]
#df_sejong = df.iloc[[7]]
#df_chungbuk = df.iloc[[10]]
#df_chungnam = df.iloc[[11]]

df1 = pd.read_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/edu_ins.csv")
df1.columns = [re.sub(r'\.\d+', '', str(col)) for col in df1.columns]
df1.iloc[0, 0] = '행정구역(시군구)별'

#%%
# 산점도 
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
# 폰트설정
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

plt.style.use('default')

# 비형식
daegeon = pd.read_excel("D:/WORKSPACE/github/MYSELF24/Python/Final_project/Raw_data/daegeon.xlsx")
#daegeon = pd.read_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/informal_ins.csv")

daegeon.rename(columns={'교육기관형태별(1)': '행정구역(시군구)별'}, inplace=True)

df_daegeon = df.iloc[[5]]
#df_sejong = df.iloc[[7]]
#df_chungbuk = df.iloc[[10]]
#df_chungnam = df.iloc[[11]]
df_daegeon_edu_in = daegeon.iloc[[1]]

# 준형식
#df_daegeon_edu_se = daegeon.iloc[[2]]


# 비형식
daegon_scat = pd.concat([df_daegeon, df_daegeon_edu_in])
# 준형식
#daegon_scat = pd.concat([df_daegeon, df_daegeon_edu_se])


# 인구
daegon_scat.iloc[[0]]
# 전치(열, 행 위치 바꾸기)
daegeon_st = daegon_scat.transpose()

daegeon_st.columns = daegeon_st.iloc[0]
daegeon_st = daegeon_st[1:].reset_index(drop=True)
daegeon_st.rename(columns={'대전광역시': '인구(수)'}, inplace=True)


# 비형식 산점도
daegeon_st.plot(kind='scatter', x='비형식 평생교육기관', y='인구(수)', c='coral', s=10, figsize=(10, 5), marker ='*')
plt.title('대전광역시 (비형식)평생교육관과 인구관계도')
plt.savefig("D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/daegeon_informal_edu_ins-1.png")
plt.show()

#준형식  산점도
'''

daegeon_st.plot(kind='scatter', x='인구(수)', y='비형식 평생교육기관', c='coral', s=10, figsize=(10, 5), marker ='+')
plt.title('대전광역시 (비형식)평생교육관과 인구관계도')
plt.savefig("D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/daegeon_informal_edu_ins-2.png")
plt.show()
'''

#%%
#초/중/고/대학교

city_mv = ['junior_sc', 'middle_sc', 'high_sc','uni']
csv_file_paths = []

df_daegeon_pop = df.iloc[[5]]
 
for sc_type in city_mv:

    df_daegeon_pop = df.iloc[[5]]
    csv = pd.read_csv(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/{sc_type}.csv") 
    csv = csv.drop(columns=['Unnamed: 0'])
   
    #대전광역시
    df_daegeon = csv.iloc[[5]]  # 대전인구 + 초/중/고/대 수
    
    
    daegeon_scat2 = pd.concat([df_daegeon_pop, df_daegeon]) 
    # 전치
    daegeon_scat2 = daegeon_scat2.transpose()
    
    daegeon_scat2 = daegeon_scat2[1:].reset_index(drop=True)
    daegeon_scat2 = daegeon_scat2.drop(0)
    
    daegeon_scat2.columns = ['인구(수)', '학교(수)']
    #daegeon_scat['인구(수)'] = daegeon_scat['인구(수)'].astype(object)
    #daegeon_scat['학교(수)'] = daegeon_scat['학교(수)'].astype(object)

    # Plotting
    #font_path = "c:/Windows/Fonts/malgun.ttf"
    # font_name = font_manager.FontProperties(fname=font_path).get_name()
    # rc('font', family=font_name)
    
    # plt.style.use('default')
    daegeon_scat2.plot(kind='scatter', x='인구(수)', y='학교(수)', c='coral', s=10, figsize=(10, 5), marker ='+')
    plt.title('대전광역시 학교과 인구관계도')
    plt.xlabel('인구(수)')
    plt.ylabel('학교(수)')
    
    plt.savefig(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/{sc_type}_school.png")
'''
    school_type = ['junior_sc', 'middle_sc', 'high_sc','uni']
    for grade in school_type:
        plt.savefig(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Visual_data/{grade}_school.png")
        '''
   # plt.show()
    
csv_file_paths.append(daegeon_scat2)
 

























