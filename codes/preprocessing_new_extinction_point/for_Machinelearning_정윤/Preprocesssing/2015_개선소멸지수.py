# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:30:51 2024

@author: Shin
"""
import pandas as pd
file_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/개선소멸위험지수(2015_2021).xlsx"
df = pd.read_excel(file_path, engine='openpyxl')


data = ['서울특별시', '인천광역시', '부산광역시', '대구광역시', '인천광역시', 
        '광주광역시', '대전광역시', '울산광역시', '경기도', '강원특별자치도',
        '충청북도', '충청남도', '전북특별자치도', '전라남도', '경상북도', 
        '경상남도', '제주특별자치도']
# data에 포함된 행 삭제 
df = df[~df['Unnamed: 0'].isin(data)]

print(df)

#%%
point2015 = df.iloc[:,1]
point2015.to_excel("C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/개선소멸위험지수2015.xlsx", index=False)

