# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:38:02 2024

@author: Shin
"""

import pandas as pd

# 연도별 데이터를 저장할 빈 데이터프레임 딕셔너리 초기화
annual_data = {str(year): pd.DataFrame() for year in range(2015, 2022)}

# 파일 리스트
files = ['학생수_유치원통합', '학생수_초등학교통합']

# 교원당 학생 수 계산 함수
def students_per_class(kin, year):
    student_col = str(year)
   
    if student_col in kin.columns:
        return kin[[student_col]]
    else:
        print(f"열 {student_col}가 데이터에 없습니다.")
        return None

# 파일별로 연도별 데이터 계산 및 저장
for file in files:
    file_path = f"C:/Users/Shin/Documents/Final_Project/Data/교육_전국/유_초등학생수/{file}.xlsx"
    kin = pd.read_excel(file_path)
    
    for year in range(2015, 2022):
        result = students_per_class(kin, year)
        if result is not None:
            # 열 이름 형식을 '{year}_{file}'로 변경
            column_name = f"{year}_{file}"
            if annual_data[str(year)].empty:
                annual_data[str(year)] = result.rename(columns={str(year): column_name})
            else:
                annual_data[str(year)] = pd.concat([annual_data[str(year)], result.rename(columns={str(year): column_name})], axis=1)

# 연도별 데이터 저장
output_base_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/유_초등학생수/"

for year, df in annual_data.items():
    output_file_path = f"{output_base_path}/{year}_학생수_전국.xlsx"
    if not df.empty:
        df.to_excel(output_file_path, index=False)
        print(f"Saved {output_file_path}")
    else:
        print(f"No data for year {year}.")
