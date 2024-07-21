# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 12:45:49 2024

@author: pjc62
"""
import pandas as pd

# 기존소멸지수 데이터 로드
ext_df = pd.read_csv('기존_소멸위험지수_2015-2023.csv')

# log(전입/전출) 데이터 로드
log_df = pd.read_csv('전입전출_log처리_2015-2023.csv')


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

# %%
# 파일 저장
new_ep.to_csv('개선 소멸지수_2015-2023.csv')
new_ep.to_excel('개선 소멸지수_2015-2023.xlsx')