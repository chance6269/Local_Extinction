# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 10:31:25 2024

@author: YS702
"""

import pandas as pd
import os
from scipy.stats import pearsonr

city_name = '서울특별시'

city_names = [
    '서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', 
    '대전광역시', '울산광역시', '세종특별자치시', '경기도평균', '강원도평균', 
    '충청북도평균', '충청남도평균', '전라북도평균', '전라남도평균', '경상북도평균', 
    '경상남도평균', '제주도평균'
]

air_name = '미세먼지(PM2.5)'

# 대기질 지표 리스트
air_names = ['미세먼지(PM2.5)', '미세먼지(PM10)', '이산화질소', '오존', '일산화탄소', '아황산가스']


base_dir = "C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도"

for city_name in city_names:
    for air_name in air_names:

        # 엑셀 파일 경로 (사용자가 업로드한 파일 경로를 지정하세요)
        desired_path = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{city_name}/{city_name}_{air_name}_산점도_Database(utf-8).csv"
        
        df_correlation = pd.read_csv(desired_path)
        
        df_correlation_drop = df_correlation.dropna()
        
        
        correlation_matrix = df_correlation[['인구밀도', f'{air_name}']].corr()
        
        output_file_path_utf_8 = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{city_name}/{city_name}_{air_name}_correlation(utf-8).csv"
        output_file_path_euc_kr = f"C:/Users/YS702/Desktop/LAST_PROJECT/대기질_인구밀도_산점도/{air_name}_도시별_Analytics_Data/{city_name}/{city_name}_{air_name}_correlation(euc-kr).csv"
        
        # to_csv 함수를 사용하여 UTF-8 인코딩으로 CSV 파일 저장
        correlation_matrix.to_csv(output_file_path_utf_8, index=True, encoding='utf-8')
        correlation_matrix.to_csv(output_file_path_euc_kr, index=True, encoding='euc-kr')
    
    
    
    
#%%
#실험실
