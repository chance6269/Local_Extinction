# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:51:08 2024

@author: bigdata
"""
#%%
# 보건기관수크롤링 코드
import requests
import pandas as pd

# URL 설정
url = ("https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=MGI2MWUxZGUxOTc1MzQ5NWNjNzgyYTI1NzIyNjZkMDE=&"
       "itmId=1635413103140064SC0+&objL1=1535413102140064HC3.00+1535413102140064HC3.11+1535413102140064HC3.21+"
       "1535413102140064HC3.22+1535413102140064HC3.23+1535413102140064HC3.24+1535413102140064HC3.25+"
       "1535413102140064HC3.26+1535413102140064HC3.41+1535413102140064HC3.31+1535413102140064HC3.32+"
       "1535413102140064HC3.33+1535413102140064HC3.34+1535413102140064HC3.35+1535413102140064HC3.36+"
       "1535413102140064HC3.37+1535413102140064HC3.38+1535413102140064HC3.39+&objL2=&objL3=&objL4=&objL5=&"
       "objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Q&startPrdDe=201501&endPrdDe=202104&orgId=101&tblId=DT_1YL8001E")

# 데이터 가져오기
response = requests.get(url)
data = response.json()

# 데이터 확인
print(data)

# DataFrame 생성
# 'StatisticItem' 부분의 데이터가 리스트 형태라 가정
if isinstance(data, list):
    df = pd.DataFrame(data)
else:
    df = pd.DataFrame([data])

# 데이터 출력하여 확인
print(df.head())

# 엑셀 파일로 저장
excel_file_path = '보건기관수.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"데이터가 {excel_file_path} 파일로 저장되었습니다.")
