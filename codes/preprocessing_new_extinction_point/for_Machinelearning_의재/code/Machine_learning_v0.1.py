# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:27:06 2024

@author: YS702
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import mean_squared_error

base_dir = "C:/Users/YS702/Desktop/LAST_PROJECT/"

desired_path = f"{base_dir}/머신러닝_RawData/machine_learning_basedata_v0.2.xlsx"

df_learn = pd.read_excel(desired_path)

#%%

# 소멸위험등급을 수치형으로 변환
grade_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
df_learn['소멸위험등급'] = df_learn['소멸위험등급'].map(grade_mapping)

df_learn.replace('-', 0, inplace=True)

# 특징 변수(X)와 타겟 변수(y) 분리
X = df_learn[['소멸위험지수', '교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교', '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)', '고등학교_학급당 학생 수 (명)', '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)', '유치원생 수' , '초등학생 수', '종합병원', '병원', '의원', '치과병(의)원', '한방병원', '한의원', '인구 천명당 의료기관병상수(개)', '총병상수 (개)', '하수도보급률', '상수도보급률']]  # 독립변수
y = df_learn['소멸위험등급']                              # 종속변수


#%%

print(df_learn.isnull().sum())  # 결측치 확인


#%%

# 데이터셋 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Gradient Boosting Regressor 모델 초기화
model = GradientBoostingClassifier()

"""
‘n_estimators’: 모델이 구축할 트리의 개수입니다. 이 경우, 50에서 500 사이의 값을 50 단위로 증가시키며 탐색합니다.

‘learning_rate’: 각 트리의 기여를 축소하는 데 사용되는 학습률입니다. 이 경우, 0.01에서 0.2 사이의 값을 동일한 간격으로 20개의 값으로 나누어 탐색합니다.

‘max_depth’: 각 개별 회귀 추정기의 최대 깊이입니다. 이 경우, 3에서 10 사이의 값을 1 단위로 증가시키며 탐색합니다.

‘min_samples_split’: 노드를 분할하기 위한 최소 샘플 수입니다. 이 경우, 2에서 10 사이의 값을 1 단위로 증가시키며 탐색합니다.

‘min_samples_leaf’: 리프 노드에 필요한 최소 샘플 수입니다. 이 경우, 1에서 10 사이의 값을 1 단위로 증가시키며 탐색합니다.

‘subsample’: 각 트리를 학습시키는 데 사용되는 샘플의 비율입니다. 이 경우, 0.5에서 1.0 사이의 값을 동일한 간격으로 6개의 값으로 나누어 탐색합니다.
"""
# 하이퍼파라미터 범위 설정
param_dist = {
    'n_estimators': np.arange(50, 500, 50),
    'learning_rate': np.linspace(0.01, 0.2, 20),
    'max_depth': np.arange(3, 10, 1),
    'min_samples_split': np.arange(2, 10, 1),
    'min_samples_leaf': np.arange(1, 10, 1),
    'subsample': np.linspace(0.5, 1.0, 6)
}


# RandomizedSearchCV 설정
"""
model: 튜닝할 모델입니다. 여기서는 GradientBoostingRegressor 모델을 사용하고 있습니다.

param_distributions: 탐색할 하이퍼파라미터의 분포입니다. 이 경우, param_dist 딕셔너리에 정의된 하이퍼파라미터 범위를 사용합니다.

n_iter: RandomizedSearchCV가 수행할 반복 횟수입니다. 이 경우, 100번의 반복을 수행합니다.

cv: 교차 검증을 위한 폴드 수입니다. 이 경우, 5-폴드 교차 검증을 수행합니다.

scoring: 모델을 평가하기 위한 지표입니다. 이 경우, 'neg_mean_squared_error’를 사용하여 평균 제곱 오차를 최소화하는 모델을 찾습니다.

random_state: 무작위성을 제어하는 데 사용되는 시드 값입니다. 이 경우, 시드 값으로 42를 사용합니다.

n_jobs: 병렬로 실행할 작업 수입니다. -1은 사용 가능한 모든 프로세서를 사용하라는 의미입니다.

error_score: 유효하지 않은 매개변수 조합에 대한 오류 점수입니다. 'raise’는 유효하지 않은 매개변수 조합이 발견되면 오류를 발생시키라는 의미입니다.
"""

random_search = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=100, cv=5, scoring='neg_mean_squared_error', random_state=42, n_jobs=-1, error_score='raise')


# 모델 학습
random_search.fit(X_train, y_train)


# 최적의 하이퍼파라미터 출력
print("Best hyperparameters:", random_search.best_params_)

# 최적의 모델로 예측 및 평가
best_model = random_search.best_estimator_
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

#%%


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import mean_squared_error

base_dir = "C:/Users/YS702/Desktop/LAST_PROJECT/"

desired_path = f"{base_dir}/머신러닝_RawData/machine_learning_basedata_v0.2.xlsx"

df_learn = pd.read_excel(desired_path)

# 소멸위험등급을 수치형으로 변환
grade_mapping = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
df_learn['소멸위험등급'] = df_learn['소멸위험등급'].map(grade_mapping)

df_learn.replace('-', 0, inplace=True)

# 특징 변수(X)와 타겟 변수(y) 분리
X = df_learn[['소멸위험지수', '교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교', '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)', '고등학교_학급당 학생 수 (명)', '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)', '유치원생 수' , '초등학생 수', '종합병원', '병원', '의원', '치과병(의)원', '한방병원', '한의원', '인구 천명당 의료기관병상수(개)', '총병상수 (개)', '하수도보급률', '상수도보급률']]  # 독립변수
y = df_learn['소멸위험등급']   

# 데이터셋 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Gradient Boosting Regressor 모델 초기화
model = GradientBoostingClassifier()

"""
‘n_estimators’: 모델이 구축할 트리의 개수입니다. 이 경우, 50에서 500 사이의 값을 50 단위로 증가시키며 탐색합니다.

‘learning_rate’: 각 트리의 기여를 축소하는 데 사용되는 학습률입니다. 이 경우, 0.01에서 0.2 사이의 값을 동일한 간격으로 20개의 값으로 나누어 탐색합니다.

‘max_depth’: 각 개별 회귀 추정기의 최대 깊이입니다. 이 경우, 3에서 10 사이의 값을 1 단위로 증가시키며 탐색합니다.

‘min_samples_split’: 노드를 분할하기 위한 최소 샘플 수입니다. 이 경우, 2에서 10 사이의 값을 1 단위로 증가시키며 탐색합니다.

‘min_samples_leaf’: 리프 노드에 필요한 최소 샘플 수입니다. 이 경우, 1에서 10 사이의 값을 1 단위로 증가시키며 탐색합니다.

‘subsample’: 각 트리를 학습시키는 데 사용되는 샘플의 비율입니다. 이 경우, 0.5에서 1.0 사이의 값을 동일한 간격으로 6개의 값으로 나누어 탐색합니다.
"""
# 하이퍼파라미터 범위 설정
param_dist = {
    'n_estimators': np.arange(50, 500, 50),
    'learning_rate': np.linspace(0.01, 0.2, 20),
    'max_depth': np.arange(3, 10, 1),
    'min_samples_split': np.arange(2, 10, 1),
    'min_samples_leaf': np.arange(1, 10, 1),
    'subsample': np.linspace(0.5, 1.0, 6)
}


# RandomizedSearchCV 설정
"""
model: 튜닝할 모델입니다. 여기서는 GradientBoostingRegressor 모델을 사용하고 있습니다.

param_distributions: 탐색할 하이퍼파라미터의 분포입니다. 이 경우, param_dist 딕셔너리에 정의된 하이퍼파라미터 범위를 사용합니다.

n_iter: RandomizedSearchCV가 수행할 반복 횟수입니다. 이 경우, 100번의 반복을 수행합니다.

cv: 교차 검증을 위한 폴드 수입니다. 이 경우, 5-폴드 교차 검증을 수행합니다.

scoring: 모델을 평가하기 위한 지표입니다. 이 경우, 'neg_mean_squared_error’를 사용하여 평균 제곱 오차를 최소화하는 모델을 찾습니다.

random_state: 무작위성을 제어하는 데 사용되는 시드 값입니다. 이 경우, 시드 값으로 42를 사용합니다.

n_jobs: 병렬로 실행할 작업 수입니다. -1은 사용 가능한 모든 프로세서를 사용하라는 의미입니다.

error_score: 유효하지 않은 매개변수 조합에 대한 오류 점수입니다. 'raise’는 유효하지 않은 매개변수 조합이 발견되면 오류를 발생시키라는 의미입니다.
"""

random_search = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=100, cv=5, scoring='neg_mean_squared_error', random_state=42, n_jobs=-1, error_score='raise')


# 모델 학습
random_search.fit(X_train, y_train)


# 최적의 하이퍼파라미터 출력
print("Best hyperparameters:", random_search.best_params_)

# 최적의 모델로 예측 및 평가
best_model = random_search.best_estimator_
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)