# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 15:00:53 2024

@author: YS702
"""
#%%




#%%

#상관관계,P밸류값 모으기

import pandas as pd
import os
from scipy.stats import pearsonr

city_names = [
    '서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', 
    '대전광역시', '울산광역시', '세종특별자치시', '경기도평균', '강원도평균', 
    '충청북도평균', '충청남도평균', '전라북도평균', '전라남도평균', '경상북도평균', 
    '경상남도평균', '제주도평균'
]

air_names = ['미세먼지(PM2.5)', '미세먼지(PM10)', '이산화질소', '오존', '일산화탄소', '아황산가스']

base_dir = "C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도"

df_correlation_collection = pd.DataFrame({'Metric': [] , 'Value': []})

for city_name in city_names:
    for air_name in air_names:
        # 엑셀 파일 경로 (사용자가 업로드한 파일 경로를 지정하세요)
        desired_path = f"{base_dir}/{air_name}_도시별_Analytics_Data/{city_name}/{city_name}_{air_name}_correlation(utf-8).csv"
        
        if os.path.exists(desired_path):
            df_correlation = pd.read_csv(desired_path)
            
            df_name = f'df_{air_name}'
            df_name_correlation = f'df_{air_name}_correlation'
            df_name_pvalue = f'df_{air_name}_pvalue'
            if df_name not in globals():
                globals()[df_name] = pd.DataFrame({'Metric': [] , 'Value': []})
            
            
            globals()[df_name] = pd.concat([globals()[df_name], df_correlation], axis=0)
            
            
            
            output_file_path_utf_8 = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{air_name}_correlation_collection(utf-8).csv"
            output_file_path_euc_kr = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{air_name}_correlation_collection(euc-kr).csv"
            globals()[df_name].to_csv(output_file_path_utf_8, index=False, encoding='utf-8')
            globals()[df_name].to_csv(output_file_path_euc_kr, index=False, encoding='euc-kr')
            
        
#%%


import pandas as pd
import os
from scipy.stats import pearsonr

city_names = [
    '서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', 
    '대전광역시', '울산광역시', '세종특별자치시', '경기도평균', '강원도평균', 
    '충청북도평균', '충청남도평균', '전라북도평균', '전라남도평균', '경상북도평균', 
    '경상남도평균', '제주도평균'
]

air_names = ['미세먼지(PM2.5)', '미세먼지(PM10)', '이산화질소', '오존', '일산화탄소', '아황산가스']

base_dir = "C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도"

df_correlation_collection = pd.DataFrame({'Metric': [] , 'Value': []})

for city_name in city_names:
    for air_name in air_names:        
        desired_path_2 = f"{base_dir}/{air_name}_도시별_Analytics_Data/{air_name}_correlation_collection(utf-8).csv"

        df_correlation = pd.read_csv(desired_path_2)
        df_correlation_drop = df_correlation.drop('Unnamed: 0', axis=1)
        
        df_correlation_pvalue = df_correlation_drop[df_correlation_drop['Metric'] == 'P-Value'].reset_index(drop=True)

        df_correlation_pvalue_1 = df_correlation_pvalue.drop('Metric', axis=1)

        df_correlation_pvalue_2 = df_correlation_pvalue_1.rename(columns={"Value": "P-Value"})
        
        df_correlation_reset = df_correlation_drop[df_correlation_drop['Metric'] == 'Correlation'].reset_index(drop=True)

        df_correlation_reset_1 = df_correlation_reset.drop('Metric', axis=1)

        df_correlation_reset_2 = df_correlation_reset_1.rename(columns={"Value": "Correlation"})
        
        scat = pd.concat([df_correlation_pvalue_2, df_correlation_reset_2], axis=1)
        
        output_file_path_utf_8 = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{air_name}_correlation_collection_last(utf-8).csv"
        output_file_path_euc_kr = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{air_name}_correlation_collection_last(euc-kr).csv"
        
        # to_csv 함수를 사용하여 UTF-8 인코딩으로 CSV 파일 저장
        scat.to_csv(output_file_path_utf_8, index=False, encoding='utf-8')
        scat.to_csv(output_file_path_euc_kr, index=False, encoding='euc-kr')
        

#%%

city_names = [
    '서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', 
    '대전광역시', '울산광역시', '세종특별자치시', '경기도평균', '강원도평균', 
    '충청북도평균', '충청남도평균', '전라북도평균', '전라남도평균', '경상북도평균', 
    '경상남도평균', '제주도평균'
]

air_names = ['미세먼지(PM2.5)', '미세먼지(PM10)', '이산화질소', '오존', '일산화탄소', '아황산가스']

air_name = '미세먼지(PM2.5)'

city_name = '서울특별시'

base_dir = "C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도"

desired_path_2 = f"{base_dir}/{air_name}_도시별_Analytics_Data/{air_name}_correlation_collection(utf-8).csv"

df_correlation = pd.read_csv(desired_path_2)

df_correlation_drop = df_correlation.drop('Unnamed: 0', axis=1)

#Pvalue값기준으로 나누기
df_correlation_pvalue = df_correlation_drop[df_correlation_drop['Metric'] == 'P-Value'].reset_index(drop=True)

df_correlation_pvalue_1 = df_correlation_pvalue.drop('Metric', axis=1)

df_correlation_pvalue_2 = df_correlation_pvalue_1.rename(columns={"Value": "P-Value"})

#correlation으로 나누기
df_correlation_reset = df_correlation_drop[df_correlation_drop['Metric'] == 'Correlation'].reset_index(drop=True)

df_correlation_reset_1 = df_correlation_reset.drop('Metric', axis=1)

df_correlation_reset_2 = df_correlation_reset_1.rename(columns={"Value": "Correlation"})


scat = pd.concat([df_correlation_pvalue_2, df_correlation_reset_2], axis=1) 


#df_correlation_T = df_correlation_drop.T


#%%


import pandas as pd

# 데이터를 리스트로 생성
data = {
    "Metric": ["Correlation", "P-Value", "Correlation", "P-Value", "Correlation", "P-Value", "Correlation", "P-Value",
               "Correlation", "P-Value", "Correlation", "P-Value", "Correlation", "P-Value", "Correlation", "P-Value",
               "Correlation", "P-Value", "Correlation", "P-Value", "Correlation", "P-Value", "Correlation", "P-Value",
               "Correlation", "P-Value", "Correlation", "P-Value", "Correlation", "P-Value", "Correlation", "P-Value",
               "Correlation", "P-Value"],
    "Value": [-0.829673196, 0.002981718, -0.947576496, 3.10e-05, -0.496058327, 0.144779562, 0.321926064, 0.364342674,
              -0.850773762, 0.001804642, -0.645447583, 0.043846109, -0.927206411, 0.000112435, 0.56679819, 0.142928697,
              0.875097912, 0.000913339, -0.932750367, 8.25e-05, 0.450330072, 0.191543318, 0.546389132, 0.102225135,
              -0.882274888, 0.000727349, -0.850954011, 0.001796349, -0.886129773, 0.000639742, -0.562063302, 0.09082136,
              0.71259302, 0.020738407]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# Correlation과 P-Value 각각의 데이터프레임으로 나누기
df_correlation = df[df['Metric'] == 'Correlation'].reset_index(drop=True)
df_pvalue = df[df['Metric'] == 'P-Value'].reset_index(drop=True)

# 결과 출력
print("Correlation 데이터프레임:")
print(df_correlation)
print("\nP-Value 데이터프레임:")
print(df_pvalue)
        
#%%



import pandas as pd
import os
from scipy.stats import pearsonr

city_names = [
    '서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', 
    '대전광역시', '울산광역시', '세종특별자치시', '경기도평균', '강원도평균', 
    '충청북도평균', '충청남도평균', '전라북도평균', '전라남도평균', '경상북도평균', 
    '경상남도평균', '제주도평균'
]

air_names = ['미세먼지(PM2.5)', '미세먼지(PM10)', '이산화질소', '오존', '일산화탄소', '아황산가스']

base_dir = "C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도"

df_correlation_collection = pd.DataFrame({'Metric': [] , 'Value': []})

for city_name in city_names:
    for air_name in air_names:
        # 엑셀 파일 경로 (사용자가 업로드한 파일 경로를 지정하세요)
        desired_path = f"{base_dir}/{air_name}_도시별_Analytics_Data/{city_name}/{city_name}_{air_name}_correlation(utf-8).csv"
        
        if os.path.exists(desired_path):
            df_correlation = pd.read_csv(desired_path)
            
            df_name = f'df_{air_name}'
            if df_name not in globals():
                globals()[df_name] = pd.DataFrame({'Metric': [] , 'Value': []})
            
            globals()[df_name] = pd.concat([globals()[df_name], df_correlation], axis=0)
            
            output_file_path_utf_8 = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{air_name}_correlation_collection(utf-8).csv"
            output_file_path_euc_kr = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{air_name}_correlation_collection(euc-kr).csv"
            globals()[df_name].to_csv(output_file_path_utf_8, index=True, encoding='utf-8')
            globals()[df_name].to_csv(output_file_path_euc_kr, index=True, encoding='euc-kr')
            
            
        else:
            print(f"파일을 찾을 수 없습니다: {desired_path}")



#%%     

   
output_file_path_utf_8 = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{city_name}_{air_name}_correlation(utf-8).csv"
output_file_path_euc_kr = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{city_name}_{air_name}_correlation(euc-kr).csv"


#%%        
        
        # 원하는 경로와 폴더 이름 설정
        desired_path = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data"
        plus_folder_name = f"{air_name}_양의상관관계"  # 원하는 폴더 이름
        minus_folder_name = f"{air_name}_음의상관관계"  # 원하는 폴더 이름
        plus_corr = '양의상관관계'
        minus_corr = '음의상관관계'
        
        
#%%        
        if correlation_value > 0:
            os.makedirs(os.path.join(desired_path, plus_folder_name), exist_ok=True)
            output_file_path_utf_8 = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{city_name}/{city_name}_{air_name}_correlation(utf-8).csv"
            output_file_path_euc_kr = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{city_name}/{city_name}_{air_name}_correlation(euc-kr).csv"
            output_file_corr_path_utf_8 = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{air_name}_{plus_corr}/{city_name}_{air_name}_correlation(utf-8).csv"
            output_file_corr_path_euc_kr = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{air_name}_{plus_corr}/{city_name}_{air_name}_correlation(euc-kr).csv"
            
            # to_csv 함수를 사용하여 UTF-8 인코딩으로 CSV 파일 저장
            result_df.to_csv(output_file_path_utf_8, index=True, encoding='utf-8')
            result_df.to_csv(output_file_path_euc_kr, index=True, encoding='euc-kr')
            result_df.to_csv(output_file_corr_path_utf_8, index=True, encoding='utf-8')
            result_df.to_csv(output_file_corr_path_euc_kr, index=True, encoding='euc-kr')
    
        if correlation_value < 0:
            os.makedirs(os.path.join(desired_path, minus_folder_name), exist_ok=True)
            output_file_path_utf_8 = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{city_name}/{city_name}_{air_name}_correlation(utf-8).csv"
            output_file_path_euc_kr = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{city_name}/{city_name}_{air_name}_correlation(euc-kr).csv"
            output_file_corr_path_utf_8 = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{air_name}_{minus_corr}/{city_name}_{air_name}_correlation(utf-8).csv"
            output_file_corr_path_euc_kr = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{air_name}_{minus_corr}/{city_name}_{air_name}_correlation(euc-kr).csv"
            
            # to_csv 함수를 사용하여 UTF-8 인코딩으로 CSV 파일 저장
            result_df.to_csv(output_file_path_utf_8, index=True, encoding='utf-8')
            result_df.to_csv(output_file_path_euc_kr, index=True, encoding='euc-kr')
            result_df.to_csv(output_file_corr_path_utf_8, index=True, encoding='utf-8')
            result_df.to_csv(output_file_corr_path_euc_kr, index=True, encoding='euc-kr')
            
            
#%%
#실험실

import pandas as pd

# 예시 데이터프레임 생성
A = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
B = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})

# 위아래로 결합
result = pd.concat([A, B], axis=0)

# 좌우로 결합
result_side_by_side = pd.concat([A, B], axis=1)

print(result)
print(result_side_by_side)

