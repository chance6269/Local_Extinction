# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 16:35:05 2024

@author: Shin
"""

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

    output_file_path = f"C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육/EXCEL/교육_{year}_전국.xlsx"
    data.to_excel(output_file_path, index=False)
