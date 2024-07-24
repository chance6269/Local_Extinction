# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 10:44:29 2024

@author: bigdata
"""
#%%
# 상수도보급률 크롤링 코드
import requests
import pandas as pd

# URL 설정
url = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=MGI2MWUxZGUxOTc1MzQ5NWNjNzgyYTI1NzIyNjZkMDE=&itmId=T10+&objL1=00+11+21+22+23+24+25+26+29+31+32+33+34+35+36+37+38+39+&objL2=&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Y&startPrdDe=2015&endPrdDe=2021&orgId=101&tblId=DT_1YL20741"

# 데이터 가져오기
response = requests.get(url)
data = response.json()

# DataFrame 생성
df = pd.DataFrame(data)

# 엑셀 파일로 저장
excel_file_path = '상수도보급률.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"데이터가 {excel_file_path} 파일로 저장되었습니다.")
#%%
# 하수도보급률 크롤링 코드
import requests
import pandas as pd

# URL 설정
url = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=MGI2MWUxZGUxOTc1MzQ5NWNjNzgyYTI1NzIyNjZkMDE=&itmId=T10+&objL1=00+11+21+22+23+24+25+26+29+31+32+33+34+35+36+37+38+39+&objL2=&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=Y&startPrdDe=2015&endPrdDe=2022&orgId=101&tblId=DT_1YL20751"

# 데이터 가져오기
response = requests.get(url)
data = response.json()

# DataFrame 생성
df = pd.DataFrame(data)

# 엑셀 파일로 저장
excel_file_path = '하수도보급률.xlsx'
df.to_excel(excel_file_path, index=False)

print(f"데이터가 {excel_file_path} 파일로 저장되었습니다.")
