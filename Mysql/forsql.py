# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 10:10:40 2024

@author: Shin
"""

import pandas as pd
# 보건
df = pd.read_excel("C:/Users/Shin/Documents/Final_Project/Mysql/data/health.xlsx")  

csv_file_path = "C:/Users/Shin/Documents/Final_Project/Mysql/data/health.csv"
df.to_csv(csv_file_path, index=False, header=False)
print(csv_file_path)
#%%
# 교육
df = pd.read_excel("C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육/교육종합_v0.2.xlsx")  
csv_file_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육/education.csv"
df.to_csv(csv_file_path, index=False, header=False)
print(csv_file_path)

#%%
# 등급종합
df3 = pd.read_excel("C:/Users/Shin/Documents/Final_Project/Mysql/data/등급.xlsx")  
csvfile = "C:/Users/Shin/Documents/Final_Project/Mysql/data/grade.csv"
df3.to_csv(csvfile, index=False, header=False)
print(csv_file_path)



#%%
df = pd.read_excel("C:/Users/Shin/Documents/Final_Project/Data/Mysql/data/excel/등급.csv")  
df2 = df.iloc[:,1]
df1 = df.iloc[:,25:]

level = pd.concat([df2,df1],axis=1, ignore_index = True)

df1
csv_file_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육/merged.csv"
level.to_csv(csv_file_path, index=False, header=False)

csv_file_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육/merged1.csv"
df1.to_csv(csv_file_path, index=False, header=False)
print(csv_file_path)
#%%
# 주거행정
df4 = pd.read_excel("C:/Users/Shin/Documents/Final_Project/Mysql/data/공공행정.xlsx")  
df5 =  pd.read_excel("C:/Users/Shin/Documents/Final_Project/Mysql/data/상하수도종합.xlsx")  
df5 = df5.iloc[:,1:]

df6 = pd.concat([df4,df5], axis=1, ignore_index=True)

csvfile = "C:/Users/Shin/Documents/Final_Project/Mysql/data/dwewllingadministration.csv"
df6.to_csv(csvfile, index=False, header=False)

#%%
# 주거교통
df7 = pd.read_excel("C:/Users/Shin/Documents/Final_Project/Mysql/data/excel/행정.xlsx")
csvfile = "C:/Users/Shin/Documents/Final_Project/Mysql/data/csv/dwewllingtraffic.csv"
df7.to_csv(csvfile, index=False, header=False)
#%%
# 사회보호
df8 = pd.read_excel("C:/Users/Shin/Documents/Final_Project/Mysql/data/excel/사회보호.xlsx")
csvfile = "C:/Users/Shin/Documents/Final_Project/Mysql/data/csv/socialprotection.csv"
df8.to_csv(csvfile, index=False, header=False)
