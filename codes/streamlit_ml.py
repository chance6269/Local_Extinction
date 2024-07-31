# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:41:26 2024

@author: jcp
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from scipy.stats import uniform, randint
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import pickle

base_dir = "C:/Users/YS702/Desktop/LAST_PROJECT/"

desired_path = f"{base_dir}/머신러닝_RawData/machine_learning_basedata_v0.2.xlsx"

df_learn = pd.read_excel(desired_path)
      

# pickle 파일로부터 모델 로드
with open('best_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

all_features = list(df_learn.columns[2:])


# 사용자 입력으로 예측
st.write("## 사용자 입력으로 예측")
user_input = [st.slider(f"{feature}", min_value=0.0, max_value=100.0, value=0.0, ) for feature in all_features]

if st.button("예측"):
    user_input = np.array(user_input).reshape(1, -1)
    prediction = loaded_model.predict(user_input)
    st.write(f"예측 결과: {prediction[0]}")