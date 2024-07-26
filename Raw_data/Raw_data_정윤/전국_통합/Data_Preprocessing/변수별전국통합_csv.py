# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:48:44 2024

@author: Shin
"""

# 파일 리스트 및 파라미터
# files = ['유치원통합', '초등학교통합', '중학교통합', '고등학교통합']
# params = '교육'

import pandas as pd
annual_data = {str(year): pd.DataFrame() for year in range(2015, 2022)}

for year in range(2015, 2022):
    year_str = str(year)
    file_path = f"C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육_{year}_전국.xlsx"
    data = pd.read_excel(file_path)

    
    data['행정구역(동읍면)별'] = data.apply(lambda row: row[0] + ' ' + row[1], axis=1)
    cols = ['행정구역(동읍면)별'] + [col for col in data.columns if col not in ['행정구역(동읍면)별', '시도별', '시군별']]
    data = data[cols]
    #data = data.drop(columns=['시도별', '시군별'])
    
    sejong = data.iloc[149:171, 1:]
   # columns_to_average = sejong.columns[:-1]  # 마지막 열 제외
    sejong = sejong.replace('-', 0)
    sejong = sejong.apply(pd.to_numeric, errors='coerce')
    sejong_mean = sejong.mean().round(0)
 
    sejong_mean['행정구역(동읍면)별'] = '세종특별자치시'
    sejong_mean = pd.DataFrame(sejong_mean).T
    data = data.drop(index=data.index[149:171])
    data = pd.concat([sejong_mean, data])
    
    columns = ['행정구역(동읍면)별'] + [col for col in data.columns if col != '행정구역(동읍면)별']
    data = data[columns]
    
    data = data.replace('-', 0)
    #data = data.apply(pd.to_numeric, errors='coerce')
    
    new_row = pd.DataFrame({
    '행정구역(동읍면)별': ['서울특별시', '인천광역시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시',
                   '경기도', '강원특별자치도','충청북도', '충청남도', '전북특별자치도', '전라남도', '경상북도', '경상남도', '제주특별자치도']})
    data = pd.concat([data, new_row])
    
    for col in data.columns:
        if col != '행정구역(동읍면)별':
            data[col] = data[col].fillna(0).astype(int)
            
    annual_data[year_str] = data
    
    output_file_path = f"C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육/CSV/교육_{year}_전국.csv"
    data.to_csv(output_file_path, index=False)

#%%
import pandas as pd


annual_data = {}


start_year = 2015
end_year = 2021


def add_year_suffix(row, year):
    if any(row.endswith(suffix) for suffix in ["시", "군", "구"]):
        return f"{row}_{year}"
    return row


for year in range(start_year, end_year + 1):
    year_str = str(year)
    file_path = f"C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육_{year}_전국.xlsx"
    data = pd.read_excel(file_path, engine='openpyxl')

    # '행정구역(동읍면)별' 열 생성 및 데이터 처리
    data['행정구역(동읍면)별'] = data.apply(lambda row: row[0] + ' ' + row[1], axis=1)
    cols = ['행정구역(동읍면)별'] + [col for col in data.columns if col not in ['행정구역(동읍면)별', '시도별', '시군별']]
    data = data[cols]

    sejong = data.iloc[149:171, 1:]
    sejong = sejong.replace('-', 0)
    sejong = sejong.apply(pd.to_numeric, errors='coerce')
    sejong_mean = sejong.mean().round(0)
 
    sejong_mean['행정구역(동읍면)별'] = '세종특별자치시'
    sejong_mean = pd.DataFrame(sejong_mean).T
    data = data.drop(index=data.index[149:171])
    data = pd.concat([sejong_mean, data], ignore_index=True)

    columns = ['행정구역(동읍면)별'] + [col for col in data.columns if col != '행정구역(동읍면)별']
    data = data[columns]
    
    data = data.replace('-', 0)
    for col in data.columns:
        if col != '행정구역(동읍면)별':
            data[col] = data[col].fillna(0)
    

    data['행정구역(동읍면)별'] = data['행정구역(동읍면)별'].apply(lambda x: add_year_suffix(x, year))
    
    annual_data[year_str] = data

     
    output_file_path = f"C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육/CSV/교육_{year}_전국.csv"
    data.to_csv(output_file_path, index=False)
