# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 17:42:23 2024

@author: 신정윤
"""
#%%
#kin.replace('-', 0, inplace=True)
#kin15 = kin.loc[1:,['2015', '2015.1']]

#%%
import pandas as pd

files = ['유치원통합', '초등학교통합', '중학교통합', '고등학교통합']

results_list = []

def students_per_class(kin1):
    results = pd.DataFrame()
    
    for year in range(2015, 2022):
        class_col = str(year)
        student_col = f"{year}.1"
        
        results[f'학급당 학생 수 {year}'] = (kin1[student_col] / kin1[class_col]).round().astype(int)
    
    return results


for file in files:
    file_path = f"D:/Python_preporcessing/Raw_data_정윤/전국_통합/{file}.xlsx"
    kin = pd.read_excel(file_path)
    kin1 = kin.loc[1:,:].reset_index(drop=True) 
    
    stu_years = students_per_class(kin1)
    results_list.append(stu_years)

for idx, df in enumerate(results_list):
    output_file_path = f"D:/Python_preporcessing/Raw_data_정윤/전국_통합/연도별_학급당학생수_{files[idx]}.xlsx"
    df.to_excel(output_file_path, index=False)

    print(f"Saved {output_file_path}")





