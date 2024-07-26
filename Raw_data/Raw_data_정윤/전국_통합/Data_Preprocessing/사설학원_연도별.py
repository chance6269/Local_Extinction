# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 14:03:58 2024

@author: Shin
"""

import pandas as pd

# 연도별 데이터 저장 dict
annual_data = {str(year): pd.DataFrame() for year in range(2015, 2022)}

# 데이터 파일 경로
file_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/결측치_제거완/사설학원통합.xlsx"
ins = pd.read_excel(file_path)
ins_data = ins.loc[1:, :].reset_index(drop=True)

# 연도별 데이터 통합
for year in range(2015, 2022):
    school_base = str(year)
    life_base = f"{year}.1"
    
    # 두 열이 모두 존재하는지 확인
    if school_base in ins_data.columns and life_base in ins_data.columns:
        # 데이터프레임을 열 기준으로 합치기
        if annual_data[school_base].empty:
            annual_data[school_base] = ins_data[[school_base, life_base]]
        else:
            # 기존 데이터프레임과 새로운 데이터프레임을 열 기준으로 병합
            annual_data[school_base] = pd.concat([annual_data[school_base], ins_data[[school_base, life_base]]], axis=1)
    else:
        print(f"열 {school_base} 또는 {life_base}가 파일에 없습니다.")

# 결과 출력
for year, df in annual_data.items():
    print(f"연도 {year} 데이터:")
    print(df.head())
    
#%%
# 연도별 데이터 저장
output_base_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/사설학원_연도별"

for year in range(2015, 2022):
    year_str = str(year)
    output_file_path = f"{output_base_path}/사설학원_{year}_전국.xlsx"
    if not annual_data[year_str].empty:
        annual_data[year_str].to_excel(output_file_path, index=False)
        print(f"Saved {output_file_path}")
    else:
        print(f"No data for year {year_str}.")


