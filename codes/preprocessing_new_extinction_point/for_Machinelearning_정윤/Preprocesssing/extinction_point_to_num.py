# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:49:34 2024

@author: Shin
"""

import pandas as pd

# 개선소멸지수 데이터 로드
new_ep = pd.read_csv('C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/개선_소멸위험지수_2015-2023.csv')

# 인덱스를 다시 열로 전환
new_ep.reset_index(inplace=True)
new_ep.rename(columns={'index' : '행정구역'}, inplace=True)

# 시도 데이터 제거

cities = '서울특별시, 부산광역시, 인천광역시, 대구광역시, 대전광역시, 광주광역시, 울산광역시, 경기도, 충청북도, 충청남도, 전라남도, 경상북도, 경상남도, 강원특별자치도, 전북특별자치도, 제주특별자치도'.split(', ')
for city in cities:
    new_ep = new_ep[new_ep['행정구역(동읍면)별'] != city]
    
# 2015-2021을 제외한 다른 열제거
new_ep = new_ep.loc[:,'행정구역(동읍면)별':'2021']

# %%
# 파일 저장
new_ep.to_csv('C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/개선_소멸위험지수_2015-2023(시도제거).csv', index=False)

# %%
'''소멸 위험 등급 나누기'''
new_ep = pd.read_csv('C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/개선_소멸위험지수_2015-2023(시도제거).csv')

# 연별데이터를 각자 1개의 데이터로 변환
df_long = new_ep.melt(id_vars=['행정구역(동읍면)별'], var_name='항목', value_name='소멸위험지수')

# 행정구역과 항목을 결합하여 새로운 '행정구역' 열 생성
df_long['행정구역(동읍면)별'] = df_long['행정구역(동읍면)별'] + '_' + df_long['항목']

# '항목' 열 제거
df_long = df_long.drop(columns=['항목'])

# 0 이하 음수값 모두 0으로 처리
df_long.loc[df_long['소멸위험지수'] < 0,'소멸위험지수'] = 0

# %%
# 소멸 위험 등급으로 전환
df_long.describe()

# 소멸위험지수 4분위수 계산
quantiles = df_long['소멸위험지수'].quantile([0.25, 0.5, 0.75])

# 소멸위험등급 부여 함수 정의
def assign_grade(value):
    if value <= quantiles[0.25]:
        return 'A'
    elif value <= quantiles[0.5]:
        return 'B'
    elif value <= quantiles[0.75]:
        return 'C'
    else:
        return 'D'
    
    # 소멸위험등급 열 추가
df_long['소멸위험등급'] = df_long['소멸위험지수'].apply(assign_grade)


# %%
# D등급(소멸위험 지역) 추출
d = df_long[df_long['소멸위험등급'] == 'D']
c = df_long[df_long['소멸위험등급'] == 'C']
b = df_long[df_long['소멸위험등급'] == 'B']
a = df_long[df_long['소멸위험등급'] == 'A']


#filtered_df = a[a['행정구역(동읍면)별'].str.contains('2021')]
#filtered_df2 = a[~a['행정구역(동읍면)별'].str.contains('2021')]
#%%
# 2015 등급만 추출
df_long.columns.values[2] = '2015_등급'
df_level = df_long.iloc[:229,[2]]
df_level.drop(columns=['2015'], inplace=True)

#%%

# 범주형 데이터를 수치형으로 변환

df_level['2015_등급'] = df_level['2015_등급'].replace({'A': 1, 'B': 2, 'C': 3, 'D': 4})
df_level.to_csv('C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/2015_소멸등급.csv',index=False)









