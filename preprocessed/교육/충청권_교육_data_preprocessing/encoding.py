# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:35:14 2024

@author: Shin
"""

import pandas as pd

# 변환할 CSV 파일 경로
input_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/일산화탄소_10년_RawData.csv'  # 실제 경로 입력

# Pandas의 read_csv 함수를 사용하여 데이터 프레임으로 읽음

#utf-8인코딩으로 읽기
#df = pd.read_csv(input_file_path, encoding='utf-8')

#cp949인코딩으로 읽기
#df = pd.read_csv(input_file_path, encoding='cp949')

#euc-kr인코딩으로 읽기
df = pd.read_csv(input_file_path, encoding='euc-kr')

# 변환된 CSV 파일 저장 경로
output_file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/일산화탄소_10년_RawData(euc-kr).csv'


# to_csv 함수를 사용하여 UTF-8 인코딩으로 CSV 파일 저장
df.to_csv(output_file_path, index=False, encoding='euc-kr')


# 데이터 프레임 정보 출력 (옵션)
print(df.info())