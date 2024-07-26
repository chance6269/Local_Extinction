# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 10:19:32 2024

@author: YS702
"""



#%%

#엑셀용

import pandas as pd

# 엑셀 파일 경로 (사용자가 업로드한 파일 경로를 지정하세요)
file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/오존_월별_도시별_대기오염도_20240703121731.xlsx'

# 데이터 프레임으로 엑셀 파일을 불러옵니다.
df_excel = pd.read_excel(file_path)

# 숫자 열을 float 형식으로 변환합니다.
cols = df_excel.columns[2:]  # 구분(1)과 구분(2)를 제외한 나머지 열
df_excel[cols] = df_excel[cols].apply(pd.to_numeric, errors='coerce')

# 각 연도별 평균을 계산합니다.
df_excel['2019_평균'] = df_excel.loc[:, '2019.01':'2019.12'].mean(axis=1)
df_excel['2020_평균'] = df_excel.loc[:, '2020.01':'2020.12'].mean(axis=1)
df_excel['2021_평균'] = df_excel.loc[:, '2021.01':'2021.12'].mean(axis=1)

# 결과를 새로운 데이터 프레임에 저장합니다.
average_df = df_excel[['구분(1)', '구분(2)', '2019_평균', '2020_평균', '2021_평균']]

# 결과를 엑셀 파일로 저장합니다.
output_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/오존_년평균.xlsx'
average_df.to_excel(output_file_path, index=False)

print(f"년도별 평균 데이터가 '{output_file_path}'에 저장되었습니다.")


#%%

#CSV용


import pandas as pd

# 엑셀 파일 경로 (사용자가 업로드한 파일 경로를 지정하세요)
file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/일산화탄소_10년_RawData(utf-8).csv'

# 데이터 프레임으로 엑셀 파일을 불러옵니다.
df = pd.read_csv(file_path)

# 숫자 열을 float 형식으로 변환합니다.
cols = df.columns[3:]  # 구분(1)과 구분(2)를 제외한 나머지 열
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

# 각 연도별 평균을 계산합니다.

df['2014_평균'] = df.loc[:, '2014.01 월':'2014.12 월'].mean(axis=1)
df['2015_평균'] = df.loc[:, '2015.01 월':'2015.12 월'].mean(axis=1)
df['2016_평균'] = df.loc[:, '2016.01 월':'2016.12 월'].mean(axis=1)
df['2017_평균'] = df.loc[:, '2017.01 월':'2017.12 월'].mean(axis=1)
df['2018_평균'] = df.loc[:, '2018.01 월':'2018.12 월'].mean(axis=1)
df['2019_평균'] = df.loc[:, '2019.01 월':'2019.12 월'].mean(axis=1)
df['2020_평균'] = df.loc[:, '2020.01 월':'2020.12 월'].mean(axis=1)
df['2021_평균'] = df.loc[:, '2021.01 월':'2021.12 월'].mean(axis=1)
df['2022_평균'] = df.loc[:, '2022.01 월':'2022.12 월'].mean(axis=1)
df['2023_평균'] = df.loc[:, '2023.01 월':'2023.12 월'].mean(axis=1)


# 결과를 새로운 데이터 프레임에 저장합니다.
average_df = df[['구분', '항목','2014_평균','2015_평균','2016_평균','2017_평균','2018_평균', '2019_평균', '2020_평균', '2021_평균','2022_평균','2023_평균']]

# 결과를 엑셀 파일로 저장합니다.
output_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/일산화탄소_년평균.csv'
average_df.to_csv(output_file_path, index=False, encoding='euc-kr')

print(f"년도별 평균 데이터가 '{output_file_path}'에 저장되었습니다.")

#%%

#미세먼지용

import pandas as pd

# 엑셀 파일 경로 (사용자가 업로드한 파일 경로를 지정하세요)
file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/대기질 RawData/미세먼지(PM10)/미세먼지(PM10)_10년_RawData(utf-8).csv'

# 데이터 프레임으로 엑셀 파일을 불러옵니다.
df = pd.read_csv(file_path)

# 숫자 열을 float 형식으로 변환합니다.
cols = df.columns[3:]  # 구분(1)과 구분(2)를 제외한 나머지 열
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

# 각 연도별 평균을 계산합니다.

df['2015_평균'] = df.loc[:, '2015.01 월':'2015.12 월'].mean(axis=1)
df['2016_평균'] = df.loc[:, '2016.01 월':'2016.12 월'].mean(axis=1)
df['2017_평균'] = df.loc[:, '2017.01 월':'2017.12 월'].mean(axis=1)
df['2018_평균'] = df.loc[:, '2018.01 월':'2018.12 월'].mean(axis=1)
df['2019_평균'] = df.loc[:, '2019.01 월':'2019.12 월'].mean(axis=1)
df['2020_평균'] = df.loc[:, '2020.01 월':'2020.12 월'].mean(axis=1)
df['2021_평균'] = df.loc[:, '2021.01 월':'2021.12 월'].mean(axis=1)
df['2022_평균'] = df.loc[:, '2022.01 월':'2022.12 월'].mean(axis=1)
df['2023_평균'] = df.loc[:, '2023.01 월':'2023.12 월'].mean(axis=1)


# 결과를 새로운 데이터 프레임에 저장합니다.
average_df = df[['구분', '항목','2015_평균','2016_평균','2017_평균','2018_평균', '2019_평균', '2020_평균', '2021_평균','2022_평균','2023_평균']]

# 결과를 엑셀 파일로 저장합니다.
output_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/대기질 RawData/미세먼지(PM10)/미세먼지(PM10)_년평균(9년).csv'
average_df.to_csv(output_file_path, index=False, encoding='euc-kr')

print(f"년도별 평균 데이터가 '{output_file_path}'에 저장되었습니다.")

#%%

import pandas as pd

# 엑셀 파일 경로 (사용자가 업로드한 파일 경로를 지정하세요)
file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/대기질 RawData/미세먼지(PM10)/미세먼지(PM10)_10년_RawData(utf-8).csv'

# 데이터 프레임으로 엑셀 파일을 불러옵니다.
df = pd.read_csv(file_path)

# 숫자 열을 float 형식으로 변환합니다.
cols = df.columns[3:]  # 구분(1)과 구분(2)를 제외한 나머지 열
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')

# 각 연도별 평균을 계산합니다.


# 연간 평균 계산 함수
def calc_yearly_mean(df, year):
    return df[[f"{year}.{i:02d} 월" for i in range(1, 13)]].mean(axis=1)

# 연간 평균 열 추가
for year in range(2014, 2024):
    df[f"{year}_평균"] = calc_yearly_mean(df.copy(), year)
    average_df[f'{year}_평균'] = df[['구분', '항목', f'{year}_평균']]



# 결과를 새로운 데이터 프레임에 저장합니다.
#average_df = df[['구분', '항목', '2019_평균', '2020_평균', '2021_평균']]

# 결과를 엑셀 파일로 저장합니다.
output_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/일산화탄소_년평균.csv'
average_df.to_csv(output_file_path, index=False, encoding='euc-kr')

print(f"년도별 평균 데이터가 '{output_file_path}'에 저장되었습니다.")


#%%


import pandas as pd

# 변환할 CSV 파일 경로
input_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/대기질 RawData/대기질 년평균 데이터/대기질_시도단위/미세먼지(PM2.5)_년평균(9년)(시도단위).csv'

# Pandas의 read_csv 함수를 사용하여 데이터 프레임으로 읽음

#utf-8인코딩으로 읽기
#df = pd.read_csv(input_file_path, encoding='utf-8')

#cp949인코딩으로 읽기
#df = pd.read_csv(input_file_path, encoding='cp949')

#euc-kr인코딩으로 읽기
df = pd.read_csv(input_file_path, encoding='euc-kr')

# 변환된 CSV 파일 저장 경로
output_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/대기질 RawData/대기질 년평균 데이터/대기질_시도단위/미세먼지(PM2.5)_년평균(9년)(시도단위)(utf-8).csv'


# to_csv 함수를 사용하여 UTF-8 인코딩으로 CSV 파일 저장
df.to_csv(output_file_path, index=False, encoding='utf-8')


# 데이터 프레임 정보 출력 (옵션)
print(df.info())


#%%

import pandas as pd

# 변환할 Excel 파일 경로
input_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/인구밀도_v0.1.xlsx'

# Pandas의 read_csv 함수를 사용하여 데이터 프레임으로 읽음

#utf-8인코딩으로 읽기
df = pd.read_excel(input_file_path)

#cp949인코딩으로 읽기
#df = pd.read_csv(input_file_path, encoding='cp949')

#euc-kr인코딩으로 읽기
df = pd.read_csv(input_file_path, encoding='euc-kr')

# 변환된 CSV 파일 저장 경로
output_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/인구밀도_v0.2(utf-8).csv'


# to_csv 함수를 사용하여 UTF-8 인코딩으로 CSV 파일 저장
df.to_csv(output_file_path, index=False, encoding='utf-8')


# 데이터 프레임 정보 출력 (옵션)
print(df.info())


#%%



import chardet


input_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/일산화탄소_10년_RawData(utf-8).csv'

# CSV 파일 내용 읽기
with open(input_file_path, 'rb') as f:
    data = f.read()




# 인코딩 추측
result = chardet.detect(data)

print(result)

encoding = result['encoding']

print(encoding)

# 추측된 인코딩으로 CSV 파일 읽기
df = pd.read_csv(file_path, encoding=encoding)



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