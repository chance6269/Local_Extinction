# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:08:13 2024

@author: Shin
"""

import pandas as pd
file_path = "D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/population.xlsx"
df= pd.read_excel("D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/population.xlsx")

sido_df = df[df['행정구역별(읍면동)'].str.contains('서울특별시|도')]
filtered_df = df[df['행정구역별(읍면동)'].str.contains('도$|서울특별시|세종특별자치시|역시', regex=True)].reset_index(drop=True)
print(sido_df)
print(filtered_df)

filtered_df.to_excel(file_path)

#%%

import pandas as pd
import re
file_path1 = "D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/edu_ins.xlsx"
df1= pd.read_excel("D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/edu_ins.xlsx")


total_df = df1[df1['교육기관형태별(1)'].str.contains('관')].reset_index(drop=True)
total_df.columns = [re.sub(r'\.\d+', '', str(col)) for col in total_df.columns]
total_df.rename(columns={'시도별': '교육기관형태별'}, inplace=True)
total_df = total_df.drop(columns=['Unnamed: 0'])
total_df = total_df.drop(columns=['2023'])
total_df.to_excel(file_path1)
