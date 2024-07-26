# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 11:51:22 2024

@author: Shin
"""
import pandas as pd
file_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/결측치_제거완/유치원통합.xlsx"
kindergarten = pd.read_excel(file_path)
# kindergarten.replace('-', 0, inplace=True)

#%%
# 2015년도 학급 당 원아수 : 
    
    
kindergarten2015 = pd.read_excel(file_path, usecols=['2015', '2015.1'])
print(kindergarten2015.dtypes)
#kindergarten2015.replace('-', 0, inplace=True)

kindergarten2015['2015'] = pd.to_numeric(kindergarten2015['2015'], errors='coerce')
kindergarten2015['2015.1'] = pd.to_numeric(kindergarten2015['2015.1'], errors='coerce')
kindergarten2015 = kindergarten2015.drop(0)
kindergarten2015['학급 당 원아 수'] = kindergarten2015['2015.1'] / kindergarten2015['2015']
# 기존 열 삭제 
kindergarten2015 = kindergarten2015.drop(columns=['2015', '2015.1'])

# '학급 당 원아 수' 데이터만 남기기
kindergarten2015['학급 당 원아 수'] = kindergarten2015['학급 당 원아 수'].round().astype(int)
kindergarten2015 = kindergarten2015.fillna(0)

#%% 







