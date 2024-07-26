# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 16:14:16 2024

@author: YS702
"""




#%%

import pandas as pd

file_path = 'C:/Users/YS702/Desktop/LAST_PROJECT/일산화탄소_년평균(시도단위)(utf-8).csv'

df = pd.read_csv(file_path)

#항목 인덱스 삭제
df.drop(columns=['항목'], inplace=True)

# 인덱스 설정 (예: '지역'을 인덱스로 설정)

#df.set_index('구분', inplace=True)
df.columns = [col.split('_')[0] for col in df.columns]


# 변환된 CSV 파일 저장 경로
output_file_path_utf_8 = 'C:/Users/YS702/Desktop/LAST_PROJECT/일산화탄소_년평균(시도단위)(utf-8)v0.2.csv'
output_file_path_euc_kr = 'C:/Users/YS702/Desktop/LAST_PROJECT/일산화탄소_년평균(시도단위)(euc-kr)v0.2.csv'

# to_csv 함수를 사용하여 UTF-8 인코딩으로 CSV 파일 저장
df.to_csv(output_file_path_utf_8, index=False, encoding='utf-8')
df.to_csv(output_file_path_euc_kr, index=False, encoding='euc-kr')



#%%

