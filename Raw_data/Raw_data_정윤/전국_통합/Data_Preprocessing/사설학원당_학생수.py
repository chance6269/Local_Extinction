# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 11:09:14 2024

@author: Shin
"""
# 총 학생수 
import pandas as pd

files = ['초등학교통합', '중학교통합', '고등학교통합']
base_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/결측치_제거완"

total_stu = pd.DataFrame()

for file in files:
    file_path = f"{base_path}/{file}.xlsx"
    stu = pd.read_excel(file_path)
    
    # 정수형 데이터만 추출
    stu = stu.loc[1:, :].reset_index(drop=True)
    
    # 2015~2021 초/중/고 학생 합 
    for year in range(2015, 2022):
        student_col = f"{year}.1"
        combined_col = str(year)
        
        if student_col in stu.columns:
            if combined_col in total_stu.columns:
                total_stu[combined_col] += stu[student_col].astype(int)
            else:
                total_stu[combined_col] = stu[student_col].astype(int)
        else:
            print(f"열 {student_col}가 파일 {file}에 없습니다.")

print(total_stu)

#%%
# 초중고 학생 수 / 학교교과 사설학원 = 사설학원 당 학생 수 

file_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/결측치_제거완/사설학원통합.xlsx"
ins = pd.read_excel(file_path)
ins.replace('-', 1, inplace=True)
ins_data = ins.loc[1:,:].reset_index(drop=True) 

results_list = []

def students_per_ins(total_stu, ins_data):
    results = pd.DataFrame()
    
    for year in range(2015, 2022):
        stu_col = str(year)
        ins_col = str(year)
    
        if stu_col in total_stu.columns and ins_col in ins_data.columns:
            results[f'{year}'] = (total_stu[stu_col] / ins_data[ins_col]).round().astype(int)
        else:
            print(f"열 {stu_col} 또는 {ins_col}가 데이터프레임에 없습니다.")
            
      
    return results

for file in files:
   
    stu_ins = students_per_ins(total_stu, ins_data)
 
    output_file_path = "C:/Users/Shin/Documents/Final_Project/Data/사설학원당_학생수.xlsx"
    stu_ins.to_excel(output_file_path, index=False)

    print(f"Saved {output_file_path}")



