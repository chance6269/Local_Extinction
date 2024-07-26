# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 10:26:10 2024

@author: Shin
"""
import pandas as pd
import re
file_path = "C:/Users/Shin/Documents/Final_Project/시군구별_인구이동.xlsx"
file_path1 = "C:/Users/Shin/Documents/Final_Project/시군구별_이동.xlsx"


pop= pd.read_excel(file_path)

pop1 = pd.read_excel(file_path1)
pop1.iloc[1:26, 0] = pop1.iloc[1:26, 0].apply(lambda x: f"서울특별시){x}")
pop1.iloc[26:42, 0] = pop1.iloc[26:42, 0].apply(lambda x: f"부산광역시){x}")
pop1.iloc[42:51, 0] = pop1.iloc[42:51, 0].apply(lambda x: f"대구광역시){x}")
pop1.iloc[51:62, 0] = pop1.iloc[51:62, 0].apply(lambda x: f"인천광역시){x}")
pop1.iloc[62:67, 0] = pop1.iloc[62:67, 0].apply(lambda x: f"광주광역시){x}")
pop1.iloc[67:72, 0] = pop1.iloc[67:72, 0].apply(lambda x: f"대전광역시){x}")
pop1.iloc[72:77, 0] = pop1.iloc[72:77, 0].apply(lambda x: f"울산광역시){x}")
#pop1.iloc[77, 0] = pop1.iloc[77, 0].apply(lambda x: f"{x}") # 세종
pop1.iloc[78:119, 0] = pop1.iloc[78:119, 0].apply(lambda x: f"경기도){x}")
pop1.iloc[119:137, 0] = pop1.iloc[119:137, 0].apply(lambda x: f"강원특별자치도){x}")
pop1.iloc[137:149, 0] = pop1.iloc[137:149, 0].apply(lambda x: f"충청북도){x}")
pop1.iloc[149:166, 0] = pop1.iloc[149:166, 0].apply(lambda x: f"충청남도){x}")
pop1.iloc[166:181, 0] = pop1.iloc[166:181, 0].apply(lambda x: f"전북특별자치도){x}")
pop1.iloc[181:205, 0] = pop1.iloc[181:205, 0].apply(lambda x: f"전라남도){x}")
pop1.iloc[205:228, 0] = pop1.iloc[205:228, 0].apply(lambda x: f"경상북도){x}")
pop1.iloc[228:251, 0] = pop1.iloc[228:251, 0].apply(lambda x: f"경상남도){x}")
pop1.iloc[251:255, 0] = pop1.iloc[251:255, 0].apply(lambda x: f"제주특별자치도){x}")
pop1 = pop1.loc[~(pop == 0).any(axis=1)]
# 중복/결측값 처리
pop1.drop(index=range(105, 111), inplace=True)
pop1.drop(index=[110, 112], inplace=True)
pop1.drop(index=[140,158, 159, 166,185,190,228,231,233,243,253,254], inplace=True)
pop1.replace('-', 0, inplace=True)

pop1.columns = [re.sub(r'\.\d+', '', str(col)) for col in pop.columns]
pop1.to_excel("C:/Users/Shin/Documents/Final_Project/시군구별_이동(전처리완).xlsx")





# 연도 뒤 .1 제거
#pop.columns = [re.sub(r'\.\d+', '', str(col)) for col in pop.columns]

#%%
# 서울특별시

seoul = pop.iloc[1:27,0]
pop.iloc[2:27, 0].apply(lambda x: f"서울특별시_{x}")

