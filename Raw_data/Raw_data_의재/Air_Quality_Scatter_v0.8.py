# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 10:48:54 2024

@author: YS702
"""

import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd
import matplotlib.font_manager as fm
import os

#%%

# 01 : 지정된 폴더에서 설치된 폰트 꺼내서 matplotlip 그래프에 적용

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc

font_path = "C:/Windows/Fonts/NanumBarunGothic.ttf"
font_name = fm.FontProperties(fname=font_path).get_name()
print(font_name)
rc('font', family=font_name)

#%%

# 02 : windows > fonts 폴더에서 폰트 꺼내서 적용하기

#font_files = fm.findSystemFonts(fontpaths=['C:/Windows/Fonts'])
#for fpath in font_files:
#    fm.fontManager.addfont(fpath)

#%%

# 맑은 고딕
#plt.rcParams['font.family'] = 'malgun'

#%%

# 나눔고딕
#plt.rcParams['font.family'] = 'NanumGothic'

#%%

# 나눔스퀘어
#plt.rcParams['font.family'] = 'NanumSquare'

# In[8]:

# 나눔바른고딕
#plt.rc('font', family='NanumBarunGothic')

#%%

# 글꼴 설치 여부 확인용 그래프

plt.plot([1, 4, 9, 16])
plt.title('간단한 선 그래프')
plt.show()
#%%

# 엑셀 파일 경로 (사용자가 업로드한 파일 경로를 지정하세요)
file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/인구밀도_v0.1(utf-8).csv'
file_path2 = 'C:/Users/YS702/Desktop/LAST_PROJECT/일산화탄소_년평균(시도단위)(utf-8)v0.2.csv'

# 데이터 프레임으로 엑셀 파일을 불러옵니다.
df_population = pd.read_csv(file_path)
df_air = pd.read_csv(file_path2)
# 특정 데이터만 추출
Some_data_population = df_population[df_population['행정구역(시군구)별'] == '부산광역시']
Some_data_air = df_air[df_air['행정구역(시군구)별'] == '부산광역시']

city_name = '부산광역시'



scat = pd.concat([Some_data_population, Some_data_air ]) 
    # 전치
scat = scat.transpose()
    
scat= scat[0:].reset_index(drop=True)
scat = scat.drop(0)
scat.columns = ['인구밀도', '대기질']

#%%

#plt.style.use('default')
scat.plot(kind='scatter', x='인구밀도', y='대기질', c='coral', s=10, figsize=(10, 5), marker ='+')
plt.title('대기질 상관관계')
plt.xlabel('인구밀도')
plt.ylabel('대기질')

#%%

plt.plot([1, 4, 9, 16])
plt.title('간단한 선 그래프')
plt.show()
    
#%%
#plots 저장하기
plt.savefig(f"C:/Users/YS702/Desktop/LAST_PROJECT/{city_name}_산점도.png")


#%%

# 변환된 CSV 파일 저장 경로
output_file_path_utf_8 = f"C:/Users/YS702/Desktop/LAST_PROJECT/{city_name}_산점도_Database(utf-8).csv"
output_file_path_euc_kr = f"C:/Users/YS702/Desktop/LAST_PROJECT/{city_name}_산점도_Database(euc-kr).csv"

# to_csv 함수를 사용하여 UTF-8 인코딩으로 CSV 파일 저장
scat.to_csv(output_file_path_utf_8, index=False, encoding='utf-8')
scat.to_csv(output_file_path_euc_kr, index=False, encoding='euc-kr')
    
    
#%%
# 산점도를 그립니다.
plt.figure(figsize=(10, 6))
plt.scatter(Some_data_air['행정구역(시군구)별'], Some_data_population['행정구역(시군구)별'], color='blue')

# 각 점에 라벨을 추가합니다.
for i in range(len(Some_data_population)):
    plt.text(Some_data_air['행정구역(시군구)별'][i], Some_data_population['행정구역(시군구)별'][i], Some_data_population['행정구역(시군구)별'][i], fontsize=9)

# 제목과 라벨을 추가합니다.
plt.title('Population Density vs. Air Quality (PM2.5)')
plt.xlabel('Population Density (people/km²)')
plt.ylabel('Air Quality (PM2.5)')
plt.grid(True)

# 그래프를 표시합니다.
plt.show()


#%%

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 예시 데이터 생성
data = {
    '지역': ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종'],
    '인구밀도': [16100, 4500, 2900, 2800, 3000, 2800, 1100, 800],  # 단위: 명/km²
    '대기질': [55, 48, 60, 58, 49, 47, 45, 40]  # 임의의 대기질 지수
}

df = pd.DataFrame(data)

# 사용할 폰트 경로 설정 (예: 나눔고딕)
font_path = 'C:/Windows/Fonts/Arial.ttf'

# 폰트 설정
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())


# 산점도 그리기
plt.figure(figsize=(10, 6))
plt.scatter(df['인구밀도'], df['대기질'], color='blue')

# 그래프 제목 및 레이블 설정
plt.title('인구밀도와 대기질의 관계')
plt.xlabel('인구밀도 (명/km²)')
plt.ylabel('대기질 지수')

# 각 데이터 포인트에 레이블 추가
for i in range(len(df)):
    plt.text(df['인구밀도'][i], df['대기질'][i], df['지역'][i], fontsize=9)

# 그래프 보여주기
plt.grid(True)
plt.show()

#%%

import pandas as pd

# 첫 번째 데이터프레임 생성
data1 = {
    '행정구역(시군구)': ['서울특별시', '부산광역시', '대구광역시'],
    '인구': [10000000, 3500000, 2500000]
}
df1 = pd.DataFrame(data1)
df1.set_index('행정구역(시군구)', inplace=True)

# 두 번째 데이터프레임 생성
data2 = {
    '행정구역(시군구)': ['서울특별시', '부산광역시', '대전광역시'],
    '대기질': [50, 60, 55]
}
df2 = pd.DataFrame(data2)
df2.set_index('행정구역(시군구)', inplace=True)

# 현재 데이터프레임 확인
print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# 두 데이터프레임을 인덱스를 기준으로 병합
merged_df = pd.merge(df1, df2, left_index=True, right_index=True, how='outer')

# 결과 확인
print("\nMerged DataFrame:\n", merged_df)


#%%

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 사용할 폰트 경로 설정 (예: 나눔고딕)
font_path = 'C:/Windows/Fonts/malgun.ttf'

# 폰트 설정
font_prop = fm.FontProperties(fname=font_path)
plt.rc('font', family=font_prop.get_name())

# 예제 데이터
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# 그래프 생성
plt.plot(x, y)
plt.title('폰트 테스트')
plt.xlabel('X 축')
plt.ylabel('Y 축')

# 그래프 출력
plt.show()


#%%


import pandas as pd

# 변환할 CSV 파일 경로
input_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/일산화탄소_년평균(시도단위).csv'

# Pandas의 read_csv 함수를 사용하여 데이터 프레임으로 읽음

#utf-8인코딩으로 읽기
#df = pd.read_csv(input_file_path, encoding='utf-8')

#cp949인코딩으로 읽기
#df = pd.read_csv(input_file_path, encoding='cp949')

#euc-kr인코딩으로 읽기
df = pd.read_csv(input_file_path, encoding='euc-kr')

# 변환된 CSV 파일 저장 경로
output_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/일산화탄소_년평균(시도단위)(utf-8).csv'


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
#df = pd.read_csv(input_file_path)

# 변환된 CSV 파일 저장 경로
output_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/인구밀도_v0.1(utf-8).csv'


# to_csv 함수를 사용하여 UTF-8 인코딩으로 CSV 파일 저장
df.to_csv(output_file_path, index=False, encoding='utf-8')


# 데이터 프레임 정보 출력 (옵션)
print(df.info())


#%%

#폰트 확인
from matplotlib import font_manager
font_manager.findSystemFonts()

    
    
    