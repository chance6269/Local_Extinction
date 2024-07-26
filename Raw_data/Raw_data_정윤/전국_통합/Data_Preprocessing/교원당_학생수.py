# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 11:26:10 2024

@author: Shin
"""

import pandas as pd

# 파일 리스트
files = ['유치원통합', '초등학교통합', '중학교통합', '고등학교통합']

# 교원당 학생 수 계산 함수
def students_per_class(kin1, year, file):
    student_col = f"{year}.1"
    teacher_col = f"{year}.2"
    
    if student_col in kin1.columns and teacher_col in kin1.columns:
        return (kin1[student_col] / kin1[teacher_col]).round().astype(int)
    else:
        print(f"열 {student_col} 또는 {teacher_col}가 파일 {file}에 없습니다.")
        return None

# 파일별로 연도별 데이터 계산 및 저장
for file in files:
    file_path = f"C:/Users/Shin/Documents/Final_Project/Data/교육_전국/결측치_제거완/{file}.xlsx"
    kin = pd.read_excel(file_path)
    kin1 = kin.loc[1:, :].reset_index(drop=True)
    
    yearly_data = pd.DataFrame()
    for year in range(2015, 2022):
        result = students_per_class(kin1, year, file)
        if result is not None:
            yearly_data[f'{year}'] = result

    output_file_path = f"C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교원당학생수/연도별_교원당학생수_{file}.xlsx"
    yearly_data.to_excel(output_file_path, index=False)
    print(f"Saved {output_file_path}")

