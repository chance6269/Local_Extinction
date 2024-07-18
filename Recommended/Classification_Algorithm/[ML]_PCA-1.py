#!/usr/bin/env python
# coding: utf-8

#%%

# PCA(Principal Component Analisys), 주성분 분석
#   - 비지도학습
#   - 종속변수는 존재하지 않음
#   - 예측하지도 분류하지도 않음
#   - PCA의 목적은 차원축소
#   - 기존 변수들의 정보를 모두 반영하는 새로운 변수들을 만드는 방식으로 차원을 축소
#   - 차원축소
#     . 변수의 갯수를 줄이되, 가능한 그 특정을 보존해내는 기법
#     . 변수 두 개면 2차원 그래프, 세 개면 3차원 그래프로 나타낼 수 있다.
#     . 데이터의 차원은 변수의 갯수와 직결된다.
#     . 차원의 축소는 변수의 수를 줄여 데이터의 차원을 축소한다.
#
# 장점:
#   - 다차원을 2차원에 적합하도록 차원 축소하여 시각화에 유용
#   - 변수 간의 높은 상관관계 문제를 해결
# 단점:
#   - 기존 변수가 아닌 새로운 변수를 사용하여 해석하는 데 어려움이 있다.
#   - 차원이 축소됨에 따라 정보 손실이 불가피하다.    
#
# 유용한 곳
#   - 다차원 변수들을 2차원 그래프로 표현하는 데 사용할 수 있다.
#   - 변수가 너무 많아 모델 학습에 시간이 너무 오래 걸릴 때 유용
#   - 오퍼피팅을 방지하는 용도로 사용할 수도 있다.

#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#%%

# 참고 : [ML]_KMeans-2.py
# 고객별 총 지출금액 및 범주별 지출금액이 스케일링 된 상태로
# 마지막 컬럼은 각 고객이 속한 클러스터 라벨이 들어 있다.

#%%

# 라이브러리 및 데이터 불러오기
file_url = '../dataset/[ML]_PCA_customer_pca.csv'
customer = pd.read_csv(file_url)

#%%

customer.head()

#%%

"""
        amt  category_entertainment  ...  category_travel  label
0 -1.402327               -1.135617  ...        -0.619930      0
1  1.079407                0.414075  ...        -0.222587      3
2  1.200151                0.747127  ...         2.766891      1
3 -1.474915               -1.129427  ...        -0.601675      0
4  0.901491                0.257905  ...        -0.484796      3

[5 rows x 13 columns]
"""

#%%

# 독립변수와 종속변수 분리
customer_X = customer.drop('label', axis = 1) # 독립변수 
customer_y = customer['label']                # 종속변수


#%%

# 그래프 표현을 위한 차원축소

#%%

from sklearn.decomposition import PCA

#%%

# 주성분 분할 갯수 지정 : 2개
pca = PCA(n_components=2)

#%%

# 차원축소
pca.fit(customer_X) # 학습
customer_pca = pca.transform(customer_X) # 변환

#%%

customer_pca

#%%

# 데이터프레임으로 변환
customer_pca = pd.DataFrame(customer_pca, columns = ['PC1','PC2'])

#%%

# 변환된 데이터프레임에 기존 데이터의 목표값인 라벨(label) 결합
customer_pca = customer_pca.join(customer_y)

#%%

customer_pca.head()

#%%

"""
        PC1       PC2  label
0 -3.929061  0.102604      0
1  3.107583 -1.748879      3
2  3.023793  3.212212      1
3 -4.282418  0.011378      0
4  2.590658 -1.906121      3
"""

#%%

# 산점도
# 레이블: 4개, 0,1,2,3
# 보라색과 빨간색 클러스터는 가깝게 붙어 있어서 경계가 모호하지만 잘 분할 됨
sns.scatterplot(x='PC1',y='PC2', data = customer_pca, hue = 'label', palette='rainbow')

#%%

# 주성분과 변수의 관계 확인
pca.components_


#%%

# 넘파이 -> 데이터프레임으로 변환
df_comp = pd.DataFrame(pca.components_,columns=customer_X.columns)

#%%

df_comp.head()
#%%

# 상관관계 히트맵
# 양수: 빨간색
# 음수: 파란색
sns.heatmap(df_comp,cmap='coolwarm')

#%%

# THE END
