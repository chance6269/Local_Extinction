# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 11:50:34 2024

@author: jcp
"""

# 탑재할 샘플 모델

import sklearn
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV

df = pd.read_csv("./preprocessed/merged_data.csv", index_col=0)

# LabelEncoder 클래스를 불러옵니다.
from sklearn.preprocessing import LabelEncoder

# LabelEncoder를 객체로 생성합니다.
le = LabelEncoder()

# fit_transform()으로 라벨인코딩을 수행합니다.
df['소멸위험등급'] = le.fit_transform(df['소멸위험등급'])

# 추가 전처리
df = df.replace("Ⅹ",0)
# Object 타입 열들 numeric으로 변환
cols = df.columns[1:]
for col in df.columns[1:]:
    if df[col].dtype == 'object':
        df[col] = pd.to_numeric(df[col].str.replace('[\s,]', '', regex=True), errors='raise')

# %%
'''스케일링'''
# Min-Max 스케일링
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaled = scaler.fit_transform(df.iloc[:, 1:-2])
df.iloc[:, 1:-2] = pd.DataFrame(scaled, columns = df.iloc[:, 1:-2].columns)
# %%
# 2021년 데이터를 테스트 데이터로 분리
test = df[df['행정구역'].str.contains('_2021')]

train = df[~df['행정구역'].str.contains('_2021')]

X = train.iloc[:, 1:-2]
y = train['소멸위험등급']


# %%


X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)


# %%

# LightGBM
import lightgbm as lgb
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score

# LightGBM 모델 초기화
lgb_clf = lgb.LGBMClassifier(random_state=1)
'''
num_leaves: 트리의 잎사귀 수.
learning_rate: 학습률.
n_estimators: 트리의 수.
max_depth: 트리의 최대 깊이.
min_child_samples: 리프 노드의 최소 샘플 수.
subsample: 데이터의 일부를 샘플링할 비율.
colsample_bytree: 각 트리를 학습할 때 사용하는 특성의 비율.'''
# 하이퍼파라미터 공간 정의
param_dist_lgb = {
    'num_leaves': [31, 50, 70],
    'learning_rate': [0.01, 0.1, 0.2],
    'n_estimators': [100, 200, 300],
    'max_depth': [-1, 10, 20],
    'min_child_samples': [5, 10, 20],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0]
}

# RandomizedSearchCV 수행
rand_search_lgb = RandomizedSearchCV(lgb_clf, param_distributions=param_dist_lgb, n_iter=50, cv=5, scoring='accuracy', random_state=1)
rand_search_lgb.fit(X_train, y_train.values.ravel())  # y_train.values.ravel()는 y_train을 1차원 배열로 변환합니다.

print('Best parameters:', rand_search_lgb.best_params_)
print('Best score:', round(rand_search_lgb.best_score_, 4))



# 최적의 모델로 평가
best_lgb_model = rand_search_lgb.best_estimator_
y_pred_lgb = best_lgb_model.predict(X_test)
print(f"LightGBM Accuracy: {accuracy_score(y_test, y_pred_lgb):.4f}")

# 예측 결과의 혼동 행렬과 분류 리포트 출력 (선택 사항)
from sklearn.metrics import confusion_matrix, classification_report

conf_matrix = confusion_matrix(y_test, y_pred_lgb)
print("Confusion Matrix:")
print(conf_matrix)

class_report = classification_report(y_test, y_pred_lgb)
print("Classification Report:")
print(class_report)

# %%
'''2021 등급 예측'''
# 2021 X, y 분리
X_2021 = test.iloc[:,1:-2]
y_2021 = test['소멸위험등급']


y_pred = best_lgb_model.predict(X_2021)

print(f"LightGBM Accuracy: {accuracy_score(y_2021, y_pred):.4f}")

# %%
import joblib

joblib.dump(best_lgb_model, 'lgb.pkl')

# gbm_pickle = joblib.load('lgb.pkl')