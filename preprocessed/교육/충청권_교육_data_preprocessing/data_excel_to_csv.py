# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 12:39:38 2024

@author: Shin
"""

import pandas as pd
file_path = "D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/population.xlsx"
df= pd.read_excel("D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/population.xlsx")

filtered_df = df[df['행정구역(시군구)별'].str.contains('도$|서울특별시|세종특별자치시|역시', regex=True)].reset_index(drop=True)
print(filtered_df)

filtered_df.to_excel(file_path)
#filtered_df = filtered_df.drop(columns=['Unnamed: 0'])
filtered_df.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/population.csv",index=False)
#%%

import pandas as pd
import re
file_path1 = "D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/edu_ins.xlsx"
df1= pd.read_excel("D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/edu_ins.xlsx")


total_df = df1[df1['교육기관형태별(1)'].str.contains('관')].reset_index(drop=True)
total_df.columns = [re.sub(r'\.\d+', '', str(col)) for col in total_df.columns]
# . : 한개 임의의 문자 , \ : 문자자체를 의미, + : 앞의 무자 최소 한개 이상 존재 
total_df.rename(columns={'시도별': '교육기관형태별'}, inplace=True)
#total_df = total_df.drop(columns=['Unnamed: 0'])

total_df.to_excel(file_path1)
total_df.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/edu_ins.csv",index=False)
#%%
import pandas as pd

city_mv = ['uni', 'junior_sc', 'middle_sc', 'high_sc'] 

csv_file_paths = []

for sc_type in city_mv:
    
    df = pd.read_excel(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/{sc_type}.xlsx") 
    df = df.drop(columns=['설립주체별(1)'])
    df.rename(columns={'시도별(1)': '행정구역(시군구)별'}, inplace=True)
    df = df.drop(index=0)
    csv_file_path = f"D:/WORKSPACE/github/MYSELF24/Python//Final_project/csv_data/{sc_type}.csv"
    df.to_csv(csv_file_path)
    # index=False, header=False 옵션
    csv_file_paths.append(csv_file_path)

print(csv_file_paths)

#%%

# 비형식 기관
df_informal = df1.iloc[:2]
df_informal = df_informal.drop(columns=['Unnamed: 0'])
df_informal.to_excel("D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/informal_ins.xlsx", index=False)
# 준형식 기관
df_semi_formal = df1.iloc[[0, 2]]
df_semi_formal =df_semi_formal.drop(columns=['Unnamed: 0'])
df_semi_formal.to_excel("D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/semiformal_ins.xlsx",index=False)
#%%
# 준형식
semi = pd.read_excel("D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/semiformal_ins.xlsx")
#semi = semi.drop(columns=['Unnamed: 0'])
semi.columns = [re.sub(r'\.\d+', '', str(col)) for col in semi.columns]
semi.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/semiformal_ins.csv",index= False)

# 비형식
informal = pd.read_excel("D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/informal_ins.xlsx")
#informal = informal.drop(columns=['Unnamed: 0'])

informal.columns = [re.sub(r'\.\d+', '', str(col)) for col in informal.columns]
informal.to_csv("D:/WORKSPACE/github/MYSELF24/Python/Final_project/csv_data/informal_ins.csv",index= False)
#%%
#충북충남세종

import pandas as pd

city = ['chungbuk', 'chungnam', 'sejong'] 

csv_file_paths = []

for sc_type in city:
    
    df = pd.read_excel(f"D:/WORKSPACE/github/MYSELF24/Python/Final_project/Excel_data/{sc_type}.xlsx")
    df.rename(columns={'교육기관형태별(1)': '행정구역(시군구)별'}, inplace=True)
    df = df.drop(index=0)
    csv_file_path = f"D:/WORKSPACE/github/MYSELF24/Python//Final_project/csv_data/{sc_type}.csv"
    df.to_csv(csv_file_path)
    # index=False, header=False 옵션
    csv_file_paths.append(csv_file_path)

print(csv_file_paths)