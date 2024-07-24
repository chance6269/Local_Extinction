# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 15:57:48 2024

@author: bigdata
"""
#%%
# 인구 천명당 의료기관병상수 크롤링 코드
import requests
import pandas as pd

# URL 설정
url = ("https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=MGI2MWUxZGUxOTc1MzQ5NWNjNzgyYTI1NzIyNjZkMDE=&"
       "itmId=T10+T001+T002+&objL1=00+11+21+22+23+24+25+26+29+31+32+33+34+35+36+37+38+39+&objL2=&objL3=&objL4=&"
       "objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Y&startPrdDe=2015&endPrdDe=2021&orgId=101&tblId=DT_1YL20971")

# 데이터 가져오기
response = requests.get(url)
data = response.json()

# 데이터 확인
print(data)

# JSON 데이터가 리스트 형태인지 확인하고 DataFrame 생성
if isinstance(data, list):
    df = pd.DataFrame(data)
else:
    df = pd.DataFrame([data])

# 데이터 출력하여 확인
print(df.head())

# 엑셀 파일로 저장
excel_file_path = '인구천명당의료기관병상수.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"데이터가 {excel_file_path} 파일로 저장되었습니다.")
