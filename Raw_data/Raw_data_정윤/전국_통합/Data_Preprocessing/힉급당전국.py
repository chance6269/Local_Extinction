# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:28:47 2024

@author: Shin
"""

import pandas as pd

# 파일 리스트
files = ['유치원통합', '초등학교통합', '중학교통합', '고등학교통합']

# 연도별 데이터를 저장할 빈 데이터프레임 딕셔너리 초기화
annual_data = {str(year): pd.DataFrame() for year in range(2015, 2022)}

# 각 파일에서 데이터 읽기 및 연도별로 데이터 분리
for file in files:
    file_path = f"C:/Users/Shin/Documents/Final_Project/Data/교육_전국/학급당학생수/학급당학생수_{file}.xlsx"
    teacher = pd.read_excel(file_path)
    
    for year in range(2015, 2022):
        year_str = str(year)
        
        if year_str in teacher.columns:
            # 데이터프레임을 합치기
            if annual_data[year_str].empty:
                annual_data[year_str] = teacher[[year_str]]
            else:
                annual_data[year_str] = pd.concat([annual_data[year_str], teacher[[year_str]]], axis=1)
        else:
            print(f"열 {year_str}가 파일 {file}에 없습니다.")

# 연도별 데이터 저장
output_base_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/학급당학생수/"

for year in range(2015, 2022):
    year_str = str(year)
    output_file_path = f"{output_base_path}학급당_{year}_전국.xlsx"
    if not annual_data[year_str].empty:
        annual_data[year_str].to_excel(output_file_path, index=False)
        print(f"Saved {output_file_path}")
    else:
        print(f"No data for year {year_str}.")

