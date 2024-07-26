# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:18:54 2024

@author: YS702
"""

import pandas as pd

file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/지역별_평생교육기관_현황.xlsx'

# 예시 데이터를 바탕으로 DataFrame 생성
data = pd.read_excel(file_path)

df = pd.DataFrame(data)

# DataFrame 확인
print("Original DataFrame:\n", df)


df.columns = [col.split('_')[0] + '_' + col.split('_')[1].split('.')[0] if '_' in col else col for col in df.columns]

# 년도별 열 추출
years = ['2014', '2015']  # 예시로 2014와 2015년만 포함
new_data = {}

for year in years:
    new_data[year] = df.filter(like=year).sum(axis=1)

# 새로운 DataFrame 생성
new_df = pd.DataFrame(new_data)
new_df['교육기관형태'] = df['교육기관형태']

# 재정렬
new_df = new_df[['교육기관형태'] + years]

# 새로운 DataFrame 확인
print("\nTransformed DataFrame:\n", new_df)

#%%

file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/지역별_평생교육기관_현황.xlsx'