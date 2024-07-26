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

# 글꼴 설치 여부 확인용 그래프

plt.plot([1, 4, 9, 16])
plt.title('간단한 선 그래프')
plt.show()

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

#%%

city_names = [
    '서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', 
    '대전광역시', '울산광역시', '세종특별자치시', '경기도평균', '강원도평균', 
    '충청북도평균', '충청남도평균', '전라북도평균', '전라남도평균', '경상북도평균', 
    '경상남도평균', '제주도평균'
]

air_names = ['미세먼지(PM2.5)', '미세먼지(PM10)', '이산화질소', '오존', '일산화탄소', '아황산가스']

city_name = '서울특별시'
air_name = '미세먼지(PM2.5)'

# 엑셀 파일 경로 (사용자가 업로드한 파일 경로를 지정하세요)
file_path = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{air_name}_correlation_collection_last(utf-8).csv"
file_path2 = f'C:/Users/YS702/Desktop/LAST_PROJECT/{air_name}_년평균(9년)(시도단위)(utf-8)v0.2.csv'

# 데이터 프레임으로 엑셀 파일을 불러옵니다.
df_population = pd.read_csv(file_path)
df_air = pd.read_csv(file_path2)
# 특정 데이터만 추출
Some_data_population = df_population[df_population['행정구역(시군구)별'] == f'{city_name}']
Some_data_air = df_air[df_air['행정구역(시군구)별'] == f'{city_name}']





scat = pd.concat([Some_data_population, Some_data_air]) 
    # 전치
scat = scat.transpose()
    
scat= scat[0:].reset_index(drop=True)
scat = scat.drop(0)
scat.columns = ['인구밀도', f'{air_name}']

# x, y 좌표 리스트 생성
label_x = scat['인구밀도'].tolist()
label_y = scat[f'{air_name}'].tolist()



# 원하는 경로와 폴더 이름 설정
desired_path = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data"
folder_name = f"{city_name}"  # 원하는 폴더 이름

# 폴더 생성
os.makedirs(os.path.join(desired_path, folder_name), exist_ok=True)



#


#plt.style.use('default')
scat.plot(kind='scatter', x='인구밀도', y=f'{air_name}', c='coral', s=150, figsize=(10, 7), marker ='o')
plt.title(f'{city_name} 인구밀도-{air_name} 농도 산점도',fontsize='22')
labels = [2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]  # 각 점에 지정할 라벨



#plt.ylim(0.0076,0.0168)
#plt.xlim(136,142.5)
plt.xlabel('인구밀도',fontsize='18')
plt.ylabel(f'{air_name} 농도',fontsize='19')
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

for i, txt in enumerate(labels):
    plt.annotate(txt, (label_x[i], label_y[i]), textcoords='offset points', xytext=(-10, 10),fontsize=16)

#폴더생성후 따로 실행 해줘야함
plt.savefig(f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{city_name}/{city_name}_{air_name}_산점도.png")

#

# 변환된 CSV 파일 저장 경로
new_index = pd.Index([2014,2015,2016,2017,2018,2019,2020,2021,2022,2023])
scat = scat.set_index(new_index)

output_file_path_utf_8 = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{city_name}/{city_name}_{air_name}_산점도_Database(utf-8).csv"
output_file_path_euc_kr = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{city_name}/{city_name}_{air_name}_산점도_Database(euc-kr).csv"

# to_csv 함수를 사용하여 UTF-8 인코딩으로 CSV 파일 저장
scat.to_csv(output_file_path_utf_8, index=True, encoding='utf-8')
scat.to_csv(output_file_path_euc_kr, index=True, encoding='euc-kr')
    
    
#%%


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

    
    
    