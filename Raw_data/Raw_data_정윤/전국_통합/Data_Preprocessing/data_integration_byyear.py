# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:04:19 2024

@author: Shin
"""

import pandas as pd

# 파일 리스트 및 파라미터
files = ['유치원통합', '초등학교통합', '중학교통합', '고등학교통합']
params = ['교원당', '사설학원', '학급당']


annual_data = {str(year): pd.DataFrame() for year in range(2015, 2022)}


for year in range(2015, 2022):
    year_str = str(year)
    year_1 = f"{year}.1"
    for file in files:
        for param in params:
            file_path = f"C:/Users/Shin/Documents/Final_Project/Data/교육_전국/통합/{param}_{year}_전국.xlsx"
            
            try:
                data = pd.read_excel(file_path)
                
                if not data.empty:
                    if param == '사설학원':
                        cols_to_use = [col for col in [year_str, year_1] if col in data.columns]
                    else:
                        cols_to_use = [year_str] if year_str in data.columns else []

                    if cols_to_use:
                        selected_data = data[cols_to_use]
                        selected_data.columns = [f"{param}_{col}" for col in selected_data.columns]  # 열 이름을 구분할 수 있도록 수정
                        
                        if annual_data[year_str].empty:
                            annual_data[year_str] = selected_data
                        else:
                            annual_data[year_str] = pd.concat([annual_data[year_str], selected_data], axis=1)
                    else:
                        print(f"열 {year_str} 또는 {year_1}가 파일 {file_path}에 없습니다.")
            except FileNotFoundError:
                print(f"파일을 찾을 수 없습니다: {file_path}")
            except Exception as e:
                print(f"파일 {file_path}를 읽는 중 오류가 발생했습니다: {e}")


output_base_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/test"
for year, df in annual_data.items():
    output_file_path = f"{output_base_path}/교육_{year}_전국.xlsx"
    if not df.empty:
        #df = df.iloc[:, :4]  # 첫 4열만남기기 
        df.to_excel(output_file_path, index=False)
        print(f"Saved {output_file_path}")
    else:
        print(f"No data for year {year}.")






