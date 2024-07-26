# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:19:32 2024

@author: YS702
"""

import pandas as pd

# 엑셀 파일을 불러옵니다
file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/오존_월별_도시별_대기오염도_20240703121731.xlsx'  # 실제 파일 경로로 변경해야 합니다.
df = pd.read_excel(file_path)

# 년평균을 계산합니다.
years = [str(year) for year in range(2019, 2022)]
monthly_columns = [f'{year}.{month:02d}' for year in years for month in range(1, 13)]

# 구분(1)과 구분(2)을 기준으로 년평균을 계산합니다.
average_data = df.groupby(['구분(1)', '구분(2)'])[monthly_columns].mean(axis=1).reset_index()
average_data.columns = ['구분(1)', '구분(2)', '년평균']

# 결과를 엑셀 파일로 저장합니다.
output_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/오존_년평균.xlsx'  # 저장할 파일 경로
average_data.to_excel(output_file_path, index=False)

print(f"년도별 평균 데이터가 '{output_file_path}'에 저장되었습니다.")


#%%

import pandas as pd

# 엑셀 파일 경로 (사용자가 업로드한 파일 경로를 지정하세요)
file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/오존_월별_도시별_대기오염도_20240703121731.xlsx'

# 데이터 프레임으로 엑셀 파일을 불러옵니다.
df = pd.read_excel(file_path)

# 숫자 열을 float 형식으로 변환합니다.
cols = df.columns[2:]  # 구분(1)과 구분(2)를 제외한 나머지 열
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

# 각 연도별 평균을 계산합니다.
df['2019_평균'] = df.loc[:, '2019.01':'2019.12'].mean(axis=1)
df['2020_평균'] = df.loc[:, '2020.01':'2020.12'].mean(axis=1)
df['2021_평균'] = df.loc[:, '2021.01':'2021.12'].mean(axis=1)

# 결과를 새로운 데이터 프레임에 저장합니다.
average_df = df[['구분(1)', '구분(2)', '2019_평균', '2020_평균', '2021_평균']]

# 결과를 엑셀 파일로 저장합니다.
output_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/오존_년평균.xlsx'
average_df.to_excel(output_file_path, index=False)

print(f"년도별 평균 데이터가 '{output_file_path}'에 저장되었습니다.")


#%%

import pandas as pd

# 엑셀 파일 경로 (사용자가 업로드한 파일 경로를 지정하세요)
file_path = '/mnt/data/your_excel_file.xlsx'

# 데이터 프레임으로 엑셀 파일을 불러옵니다.
df = pd.read_excel(file_path)

# 숫자 열을 float 형식으로 변환합니다.
cols = df.columns[2:]  # 구분(1)과 구분(2)를 제외한 나머지 열
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

# 각 연도별 평균을 계산합니다.
df['2019_평균'] = df.loc[:, '2019.01':'2019.12'].mean(axis=1)
df['2020_평균'] = df.loc[:, '2020.01':'2020.12'].mean(axis=1)
df['2021_평균'] = df.loc[:, '2021.01':'2021.12'].mean(axis=1)

# 결과를 새로운 데이터 프레임에 저장합니다.
average_df = df[['구분(1)', '구분(2)', '2019_평균', '2020_평균', '2021_평균']]

# 결과를 엑셀 파일로 저장합니다.
output_file_path = '/mnt/data/yearly_averages.xlsx'
average_df.to_excel(output_file_path, index=False)

print(f"년도별 평균 데이터가 '{output_file_path}'에 저장되었습니다.")
















#%%

import os

# 현재 작업 경로 확인
current_path = os.getcwd()
print("현재 작업 경로:", current_path)


#%%
# 작업 경로 변경
new_path = 'C:/Users/YS702/Desktop/LAST_PROJECT'
os.chdir(new_path)


#%%
# 변경된 작업 경로 확인
new_current_path = os.getcwd()
print("변경된 작업 경로:", new_current_path)