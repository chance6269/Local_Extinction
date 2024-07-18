# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 09:16:12 2024

@author: Solero
"""

#%%
# 피어슨 상관계수
# 두 변수 간의 선형 관계를 측정하는 통계적 방법
# 두 변수의 공분산을 각 변수의 표준편차의 곱으로 나눈 값으로 정의된다.

import numpy as np
from scipy.stats import pearsonr

x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])
y = np.array([5,  10, 15, 20, 25, 30, 25, 20, 15, 10, 5])


# 스피어만 상관계수 계산
corr, p_value = pearsonr(x, y)

print(f"피어슨 상관계수: {corr}")
print(f"p-value: {p_value}")

# 결과 해석
if p_value < 0.05:
    print("두 변수 간의 상관 관계가 유의미합니다.")
else:
    print("두 변수 간의 상관 관계가 유의미하지 않습니다.")
    
#%%

# 데이터 시각화

import matplotlib.pyplot as plt

plt.scatter(x, y)
plt.title('Scatter plot of x and y')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#%%
# THE END