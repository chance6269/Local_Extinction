# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 14:19:40 2024

@author: jcp
"""

# import matplotlib.pyplot as plt
# import xgboost as xgb
import time
import numpy as np
import pandas as pd
import streamlit as st

import joblib

gbm_pickle = joblib.load('lgb.pkl')

# 제목
st.title('지방소멸등급 예측 서비스(Sample)')
st.header('Local Extinction Prediction Project')

# Add a placeholder 진행 상황 바
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    # Update the progress bar with each iteration.
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
        
# 변수는 총 5개

st.write("""
## 사용 변수들
1. 고위험음주율
2. 비만율
3. EQ.5D
4. 주관적건강수준인지율
5. 건강보험적용인구
""")

# 지역 변수를 제외한 나머지 변수 설정하는 sidebar
drink = st.slider("고위험음주율", 1, 50)

fat = st.slider("비만율", 1, 60)
eq5d = st.slider("EQ.5D", 0.8, 1.0)
self_health = st.slider("주관적건강수준인지율", 20, 100)
insurance = st.slider("건강보험적용인구", 1, 2000000)


# scaling되기 전의 데이터
realData = [[drink, fat, eq5d, self_health, insurance]]

res = ''
res1 = gbm_pickle.predict(realData)
if res1 == 0:
    res = 'A'
elif res1 == 1:
    res = 'B'
elif res1 == 2:
    res = 'C'
else: res = 'D'

st.header("예측 소멸위험등급 : " + res)
# st.write(res)
