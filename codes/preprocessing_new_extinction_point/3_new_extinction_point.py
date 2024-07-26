# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:45:49 2024

@author: pjc62
"""
import pandas as pd

# 기존소멸지수 데이터 로드
ext_df = pd.read_csv('./preprocessed/기존_소멸위험지수_2015-2023.csv')

# log(전입/전출) 데이터 로드
log_df = pd.read_csv('./preprocessed/전입전출_log처리_2015-2023.csv')


'''개선 소멸지수 데이터 생성'''
# 계산을 위해 '행정구역명'열을 인덱스로 지정
ext_df = ext_df.set_index('행정구역(동읍면)별')
log_df = log_df.set_index('행정구역(시군구)별')

ext_df.info()
log_df.info()

# ext_df와 log_df 열이름 통일
ext_df.columns = log_df.columns

# 기존소멸위험지수^2 + log(전입/전출)
new_ep = ext_df ** 2 + log_df

# 인덱스를 다시 열로 전환
new_ep.reset_index(inplace=True)
new_ep.rename(columns={'index' : '행정구역'}, inplace=True)

# 시도 데이터 제거

# cities = '서울특별시, 부산광역시, 인천광역시, 대구광역시, 대전광역시, 광주광역시, 울산광역시, 경기도, 충청북도, 충청남도, 전라남도, 경상북도, 경상남도, 강원특별자치도, 전북특별자치도, 제주특별자치도'.split(', ')
# for city in cities:
#     new_ep = new_ep[new_ep['행정구역'] != city]
    
# 2015-2021을 제외한 다른 열제거
new_ep = new_ep.loc[:,'행정구역':'2021']

# %%
# 파일 저장
new_ep.to_csv('./preprocessed/개선_소멸위험지수_2015-2021.csv')
new_ep.to_excel('./preprocessed/개선_소멸위험지수_2015-2021.xlsx')

# %%
'''소멸 위험 등급 나누기'''
# 연별데이터를 각자 1개의 데이터로 변환
df_long = new_ep.melt(id_vars=['행정구역'], var_name='항목', value_name='소멸위험지수')

# 행정구역과 항목을 결합하여 새로운 '행정구역' 열 생성
df_long['행정구역'] = df_long['행정구역'] + '_' + df_long['항목']

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
# 파일로 저장
df_long.to_csv('./preprocessed/소멸위험등급_2015-2021.csv')
df_long.to_excel('./preprocessed/소멸위험등급_2015-2021.xlsx')

# %%
# D등급(소멸위험 지역) 추출
d = df_long[df_long['소멸위험등급'] == 'D']
c = df_long[df_long['소멸위험등급'] == 'C']
b = df_long[df_long['소멸위험등급'] == 'B']
a = df_long[df_long['소멸위험등급'] == 'A']

filtered_df = a[a['행정구역'].str.contains('2021')]
filtered_df2 = a[~a['행정구역'].str.contains('2021')]
