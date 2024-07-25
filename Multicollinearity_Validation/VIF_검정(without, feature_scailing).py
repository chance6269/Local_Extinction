# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 09:17:24 2024

@author: Shin
"""
# 다중공선성 VIF검정 및 회귀분석을 통해 확인 
# 다중공선성(multicollinearity) : 하나의 독립변수가 다른 여러 개의 독립변수들로 잘 예측되는 경우
# 다중공선성이 있으면,
#계수 추정이 잘 되지 않거나 불안정해져서 데이터가 약간만 바뀌어도 추정치가 크게 달라질 수 있다
#계수가 통계적으로 유의미하지 않은 것처럼 나올 수 있다
# VIF 검정은 다중공선성이 추정 기울기 계수의 표준오차를 얼마나 증가시켰는지를 측정하는 지표
#엄밀한 기준은 없으나 보통 10보다 크면 다중공선성이 있다고 판단(5를 기준으로 하기도 함)

# df : 교육_2015_전국 (교육변수통합)
# df_p : 2015_개선소멸지수를'2015~2023개선소멸지수'에서 추출하여 excel로 저장하였음. 
import pandas as pd

file_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육/EXCEL/교육_2015_전국.xlsx"
file_path_1 = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/개선소멸위험지수2015.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')
df_p = pd.read_excel(file_path_1, engine='openpyxl')
    
#%%
#폰트 설정
from matplotlib import font_manager, rc
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
#%%

# 상관관계 분석 2015 년도 교원_1인당_학생수와 2015 지방소멸지수 상관관계  : 

'''
''교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교'
 '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)','고등학교_학급당 학생 수 (명)',
 '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)','유치원생 수', '초등학생 수'
'''
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
#%%
# 2015지방소멸위험지수 포함 
'''
df['2015'] = df_p['2015']

sns.pairplot(df[['교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교', '2015']])
plt.show()
'''
#%%

sns.pairplot(df[['교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교']])
plt.show()
# 많은 통계 소프트웨어와 라이브러리는 절편을 자동으로 포함하지만, 
#statsmodels의 OLS (Ordinary Least Squares) 함수는 기본적으로 독립 변수 행렬 𝑋에 절편을 포함시키지 않습니다. 
#따라서, 직접 절편을 추가해 주어야 합니다.
df['intercept'] = 1 #(절편) 
model = sm.OLS(df_p['2015'], df[['교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교']])


results = model.fit()
print(results.summary())
'''
OLS Regression Results                                
=======================================================================================
Dep. Variable:                   2015   R-squared (uncentered):                   0.494 : 모델이 종속 변수의 변동성을 얼마나 설명하는지를 나타냅니다.
Model:                            OLS   Adj. R-squared (uncentered):              0.485 : 수정된 R-squared로, 모델의 설명력을 변수의 개수에 대해 조정한 값
Method:                 Least Squares   F-statistic:                              54.95 : F-statistic은 모델의 설명력이 통계적으로 유의미한지 검정
Date:                Thu, 25 Jul 2024   Prob (F-statistic):                    2.84e-32 : 매우 낮은 p-value (0.000000000000000000000000000000284)로, 모델이 유의미하다는 것을 강하게 시사
Time:                        10:01:11   Log-Likelihood:                         -389.25
No. Observations:                 229   AIC:                                      786.5
Df Residuals:                     225   BIC:                                      800.2
Df Model:                           4                                                  
Covariance Type:            nonrobust                                                  
===================================================================================
                                 coef    std err          t      P>|t|      [0.025      0.975] 
-----------------------------------------------------------------------------------
교원_1인당_학생수_유치원      0.0969      0.049      1.981      #0.049       0.001       0.193
교원_1인당_학생수_초등학교    -0.0220      0.068     -0.327      0.744      -0.155       0.111
교원_1인당_학생수_중학교      0.0341      0.069      0.495      0.621      -0.102       0.170
교원_1인당_학생수_고등학교     0.0032      0.045      0.070      0.944      -0.086       0.093
==============================================================================
Omnibus:                       67.987   Durbin-Watson:                   1.299 : 이 통계량은 잔차의 자기상관을 측정 값이 2에 가까울수록 자기상관이 없음을 의미합니다 1.299는 약간의 양의 자기상관이 존재할 수 있음을 시사
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              132.636
Skew:                           1.500   Prob(JB):                     1.58e-29
Kurtosis:                       5.214   Cond. No.                         26.1
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.
'''
# 귀무가설은 차이/영향력/연관성이 없다고 설정하고 대립가설은 차이/영향력/연관성이 있다고 설정한다  
# p-value 값이 0.05미만의 의미는 표본의 통계치가 귀무가설과 같이 나올 확률이 5%미만 즉, 귀무가설을 기각하고 대립가설을 채택
'''
Coefficients and p-values:

교원_1인당_학생수_유치원: 0.0969 (p-value: 0.049)
유의미한 결과 (p-value < 0.05). 유치원 교원 1인당 학생 수가 증가할 때, 2015년 종속 변수 값이 증가합니다.
교원_1인당_학생수_초등학교: -0.0220 (p-value: 0.744)
유의미하지 않음 (p-value > 0.05). 초등학교 교원 1인당 학생 수와 2015년 종속 변수 간에는 유의미한 관계가 없습니다.
교원_1인당_학생수_중학교: 0.0341 (p-value: 0.621)
유의미하지 않음. 중학교 교원 1인당 학생 수와 2015년 종속 변수 간에는 유의미한 관계가 없습니다.
교원_1인당_학생수_고등학교: 0.0032 (p-value: 0.944)
유의미하지 않음. 고등학교 교원 1인당 학생 수와 2015년 종속 변수 간에는 유의미한 관계가 없습니다.'''

'''
결론
유치원 교원 1인당 학생 수는 종속 변수에 유의미한 영향을 미치는 것으로 나타났습니다. 이는 유치원 교원 1인당 학생 수가 증가할수록 종속 변수의 값도 증가하는 경향이 있음을 의미합니다.
그러나 초등학교, 중학교, 고등학교의 경우, 교원 1인당 학생 수와 종속 변수 간의 유의미한 관계는 발견되지 않았습니다.
전반적으로 모델은 2015년 데이터의 약 49.4%를 설명할 수 있지만, 일부 독립 변수의 영향은 통계적으로 유의미하지 않습니다.'''
#%%
#VIF 수치를 확인하는 python 코드:
'''
VIF 값이 (10 이상의 값) 경우, 다중공선성을 고려하여 해당 변수를 적절히 제외 하였지만
 본 연구에서는 머신러닝 분류 모델(K-Fold)활용 하여 변수 간 상관관계에 영향을 줄이고,
 최대한 많은 독립변수들을 고려하여 분류 모델의 정확도를 높이고자 하였다
'''
from statsmodels.stats.outliers_influence import variance_inflation_factor


X_train = df[['교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교']]
def feature_engineering_XbyVIF(X_train):
    vif = pd.DataFrame()
    vif['VIF_Factor'] = [variance_inflation_factor(X_train.values, i)
                         for i in range(X_train.shape[1])]
    vif['Feature'] = X_train.columns
    return vif
vif = feature_engineering_XbyVIF(X_train)
print(vif)
'''
   VIF_Factor          Feature
0   42.764089   교원_1인당_학생수_유치원
1   92.992490  교원_1인당_학생수_초등학교
2   87.481160   교원_1인당_학생수_중학교
3   37.835847  교원_1인당_학생수_고등학교'''
#%%
# 상관관계 분석 2015 년도 교원_1인당_학생수와 2015 지방소멸지수 상관관계:
    
sns.pairplot(df[[    '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)','고등학교_학급당 학생 수 (명)']])
plt.show()
# 많은 통계 소프트웨어와 라이브러리는 절편을 자동으로 포함하지만, 
#statsmodels의 OLS (Ordinary Least Squares) 함수는 기본적으로 독립 변수 행렬 𝑋에 절편을 포함시키지 않습니다. 
#따라서, 직접 절편을 추가해 주어야 합니다.
df['intercept'] = 1 #(절편) 
model = sm.OLS(df_p['2015'], df[['유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)','고등학교_학급당 학생 수 (명)']])

results = model.fit()
print(results.summary())
'''
                                 OLS Regression Results                                
=======================================================================================
Dep. Variable:                   2015   R-squared (uncentered):                   0.495
Model:                            OLS   Adj. R-squared (uncentered):              0.486
Method:                 Least Squares   F-statistic:                              55.18
Date:                Thu, 25 Jul 2024   Prob (F-statistic):                    2.26e-32
Time:                        10:43:07   Log-Likelihood:                         -389.02
No. Observations:                 229   AIC:                                      786.0
Df Residuals:                     225   BIC:                                      799.8
Df Model:                           4                                                  
Covariance Type:            nonrobust                                                  
=====================================================================================
                                 coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
유치원_학급당 학생 수 (명)      0.0640      0.037      1.734      0.084      -0.009       0.137
초등학교_학급당 학생 수 (명)    -0.0163      0.041     -0.401      0.689      -0.097       0.064
중학교_학급당 학생 수 (명)     -0.0041      0.036     -0.114      0.909      -0.075       0.067
고등학교_학급당 학생 수 (명)     0.0211      0.022      0.941      0.348      -0.023       0.065
==============================================================================
Omnibus:                       74.067   Durbin-Watson:                   1.285
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              155.278
Skew:                           1.590   Prob(JB):                     1.91e-34
Kurtosis:                       5.481   Cond. No.                         28.1
==============================================================================
# Cond. No. (Condition Number): 28.1

독립 변수 간의 다중공선성을 나타내는 지표입니다. 값이 30 이상일 경우 다중공선성 문제가 있을 수 있지만, 현재 값은 크게 문제가 되는 수준은 아닙니다.
Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.


Coefficients and p-values:
유치원_학급당 학생 수 (명): 0.0640 (p-value: 0.084)
p-value가 0.05보다 크므로 유의미하지 않다고 판단됩니다. 그러나 계수가 양수로, 유치원 학급당 학생 수가 증가할 때 종속 변수의 값이 약간 증가하는 경향이 있습니다.
초등학교_학급당 학생 수 (명): -0.0163 (p-value: 0.689)
유의미하지 않음 (p-value > 0.05). 초등학교 학급당 학생 수와 종속 변수 간의 유의미한 관계가 없음.
중학교_학급당 학생 수 (명): -0.0041 (p-value: 0.909)
유의미하지 않음. 중학교 학급당 학생 수와 종속 변수 간의 유의미한 관계가 없음.
고등학교_학급당 학생 수 (명): 0.0211 (p-value: 0.348)
유의미하지 않음. 고등학교 학급당 학생 수와 종속 변수 간의 유의미한 관계가 없음.

결론
전체 모델은 통계적으로 유의미하지만, 개별 독립 변수들은 대부분 유의미하지 않으며, 이는 독립 변수들이 종속 변수에 미치는 영향이 크지 않음을 시사합니다.
유치원 학급당 학생 수가 종속 변수에 약간의 긍정적 영향을 미칠 가능성이 있지만, 이는 통계적으로 유의미하지 않습니다.
잔차의 정규성이 부족하고, 약간의 자기상관이 있을 수 있습니다.'''
#%%
from statsmodels.stats.outliers_influence import variance_inflation_factor
X_train = df[['유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)','고등학교_학급당 학생 수 (명)']]
def feature_engineering_XbyVIF(X_train):
    vif = pd.DataFrame()
    vif['VIF_Factor'] = [variance_inflation_factor(X_train.values, i)
                         for i in range(X_train.shape[1])]
    vif['Feature'] = X_train.columns
    return vif
vif = feature_engineering_XbyVIF(X_train)
print(vif)   
'''
  VIF_Factor            Feature
0   55.828692   유치원_학급당 학생 수 (명)
1   81.191601  초등학교_학급당 학생 수 (명)
2  109.096652   중학교_학급당 학생 수 (명)
3   50.853184  고등학교_학급당 학생 수 (명)'''
#%%
# 상관관계 분석 2015 년도 사설학원과 2015 지방소멸지수 상관관계:
    
#'학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)','유치원생 수', '초등학생 수'   
 
sns.pairplot(df[['학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)']])
plt.show()
# 많은 통계 소프트웨어와 라이브러리는 절편을 자동으로 포함하지만, 
#statsmodels의 OLS (Ordinary Least Squares) 함수는 기본적으로 독립 변수 행렬 𝑋에 절편을 포함시키지 않습니다. 
#따라서, 직접 절편을 추가해 주어야 합니다.
df['intercept'] = 1 #(절편) 
model = sm.OLS(df_p['2015'], df[['학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)']])

results = model.fit()
print(results.summary())
'''
    OLS Regression Results                                
=======================================================================================
Dep. Variable:                   2015   R-squared (uncentered):                   0.172
Model:                            OLS   Adj. R-squared (uncentered):              0.161
Method:                 Least Squares   F-statistic:                              15.68
Date:                Thu, 25 Jul 2024   Prob (F-statistic):                    2.68e-09
Time:                        10:53:39   Log-Likelihood:                         -445.64
No. Observations:                 229   AIC:                                      897.3
Df Residuals:                     226   BIC:                                      907.6
Df Model:                           3                                                  
Covariance Type:            nonrobust                                                  
=================================================================================
                             coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------
학교교과 교습학원 (개)     0.0001      0.000      0.449      0.654      -0.000       0.001
평생직업 교육학원 (개)     0.0039      0.003      1.330      0.185      -0.002       0.010
사설학원당 학생수 (명)     0.0029      0.001      4.997      0.000       0.002       0.004
==============================================================================
Omnibus:                       39.290   Durbin-Watson:                   0.946
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              115.165
Skew:                           0.708   Prob(JB):                     9.82e-26
Kurtosis:                       6.172   Cond. No.                         24.8
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.'''



#%%
from statsmodels.stats.outliers_influence import variance_inflation_factor
X_train = df[['학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)']]
def feature_engineering_XbyVIF(X_train):
    vif = pd.DataFrame()
    vif['VIF_Factor'] = [variance_inflation_factor(X_train.values, i)
                         for i in range(X_train.shape[1])]
    vif['Feature'] = X_train.columns
    return vif
vif = feature_engineering_XbyVIF(X_train)
print(vif)   
'''
VIF_Factor        Feature
0    5.593359  학교교과 교습학원 (개)
1    5.592409  평생직업 교육학원 (개)
2    1.013003  사설학원당 학생수 (명)'''
#%%
# 상관관계 분석 2015 년도 사설학원과 2015 지방소멸지수 상관관계:

'유치원생 수', '초등학생 수' 

sns.pairplot(df[['유치원생 수', '초등학생 수']])
plt.show()
# 많은 통계 소프트웨어와 라이브러리는 절편을 자동으로 포함하지만, 
#statsmodels의 OLS (Ordinary Least Squares) 함수는 기본적으로 독립 변수 행렬 𝑋에 절편을 포함시키지 않습니다. 
#따라서, 직접 절편을 추가해 주어야 합니다.
df['intercept'] = 1 #(절편) 
model = sm.OLS(df_p['2015'], df[['유치원생 수', '초등학생 수']])

results = model.fit()
print(results.summary())
'''
OLS Regression Results                                
=======================================================================================
Dep. Variable:                   2015   R-squared (uncentered):                   0.241
Model:                            OLS   Adj. R-squared (uncentered):              0.234
Method:                 Least Squares   F-statistic:                              36.00
Date:                Thu, 25 Jul 2024   Prob (F-statistic):                    2.63e-14
Time:                        11:15:44   Log-Likelihood:                         -435.75
No. Observations:                 229   AIC:                                      875.5
Df Residuals:                     227   BIC:                                      882.4
Df Model:                           2                                                  
Covariance Type:            nonrobust                                                  
==============================================================================
                     coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
유치원생 수     -4.664e-05   9.68e-05     -0.482      0.630      -0.000       0.000
초등학생 수      6.436e-05   2.53e-05      2.540      0.012    1.44e-05       0.000
==============================================================================
Omnibus:                       39.784   Durbin-Watson:                   1.134
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               70.075
Skew:                           0.918   Prob(JB):                     6.07e-16
Kurtosis:                       4.994   Cond. No.                         16.6
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.'''
#%%
from statsmodels.stats.outliers_influence import variance_inflation_factor
X_train = df[['유치원생 수', '초등학생 수']]
def feature_engineering_XbyVIF(X_train):
    vif = pd.DataFrame()
    vif['VIF_Factor'] = [variance_inflation_factor(X_train.values, i)
                         for i in range(X_train.shape[1])]
    vif['Feature'] = X_train.columns
    return vif
vif = feature_engineering_XbyVIF(X_train)
print(vif)   
'''
 VIF_Factor Feature
0    16.69906  유치원생 수
1    16.69906  초등학생 수
'''
#%%
# 상관관계 분석 2015 년도교육변수 통합과 2015 지방소멸지수 상관관계:
'''
   '교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교',
    '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)','고등학교_학급당 학생 수 (명)',
    '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)','유치원생 수', '초등학생 수' 
    '''
    
sns.pairplot(df[['교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교',
 '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)','고등학교_학급당 학생 수 (명)',
 '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)','유치원생 수', '초등학생 수']])
plt.show()
# 많은 통계 소프트웨어와 라이브러리는 절편을 자동으로 포함하지만, 
#statsmodels의 OLS (Ordinary Least Squares) 함수는 기본적으로 독립 변수 행렬 𝑋에 절편을 포함시키지 않습니다. 
#따라서, 직접 절편을 추가해 주어야 합니다.
df['intercept'] = 1 #(절편) 
model = sm.OLS(df_p['2015'], df[['교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교',
 '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)','고등학교_학급당 학생 수 (명)',
 '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)','유치원생 수', '초등학생 수']])

results = model.fit()
print(results.summary())  
'''    OLS Regression Results                                
=======================================================================================
Dep. Variable:                   2015   R-squared (uncentered):                   0.534
Model:                            OLS   Adj. R-squared (uncentered):              0.505
Method:                 Least Squares   F-statistic:                              19.00
Date:                Thu, 25 Jul 2024   Prob (F-statistic):                    3.54e-29
Time:                        11:21:26   Log-Likelihood:                         -379.98
No. Observations:                 229   AIC:                                      786.0
Df Residuals:                     216   BIC:                                      830.6
Df Model:                          13                                                  
Covariance Type:            nonrobust                                                  
=====================================================================================
                                coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
교원_1인당_학생수_유치원        0.1516      0.080      1.899      0.059      -0.006       0.309
교원_1인당_학생수_초등학교       0.3367      0.150      2.246      0.026       0.041       0.632
교원_1인당_학생수_중학교        0.1471      0.112      1.317      0.189      -0.073       0.367
교원_1인당_학생수_고등학교      -0.0698      0.092     -0.758      0.449      -0.251       0.112
유치원_학급당 학생 수 (명)      0.0237      0.046      0.515      0.607      -0.067       0.114
초등학교_학급당 학생 수 (명)    -0.2852      0.106     -2.696      0.008      -0.494      -0.077
중학교_학급당 학생 수 (명)     -0.0852      0.062     -1.373      0.171      -0.208       0.037
고등학교_학급당 학생 수 (명)     0.0692      0.044      1.567      0.119      -0.018       0.156
학교교과 교습학원 (개)        -0.0004      0.000     -1.690      0.093      -0.001    7.04e-05
평생직업 교육학원 (개)         0.0026      0.002      1.053      0.294      -0.002       0.008
사설학원당 학생수 (명)        -0.0005      0.001     -0.807      0.420      -0.002       0.001
유치원생 수            -8.181e-05    9.7e-05     -0.844      0.400      -0.000       0.000
초등학생 수             1.161e-05   2.78e-05      0.418      0.677   -4.32e-05    6.64e-05
==============================================================================
Omnibus:                       58.411   Durbin-Watson:                   1.407
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              103.060
Skew:                           1.345   Prob(JB):                     4.18e-23
Kurtosis:                       4.888   Cond. No.                     3.82e+04
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[3] The condition number is large, 3.82e+04. This might indicate that there are
strong multicollinearity or other numerical problems.'''
#%%
from statsmodels.stats.outliers_influence import variance_inflation_factor
X_train = df[['교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교',
 '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)','고등학교_학급당 학생 수 (명)',
 '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)','유치원생 수', '초등학생 수']]
def feature_engineering_XbyVIF(X_train):
    vif = pd.DataFrame()
    vif['VIF_Factor'] = [variance_inflation_factor(X_train.values, i)
                         for i in range(X_train.shape[1])]
    vif['Feature'] = X_train.columns
    return vif
vif = feature_engineering_XbyVIF(X_train)
print(vif)   
'''
 VIF_Factor            Feature
0   118.583744     교원_1인당_학생수_유치원
1   477.173276    교원_1인당_학생수_초등학교
2   239.581180     교원_1인당_학생수_중학교
3   162.007983    교원_1인당_학생수_고등학교
4    90.040200   유치원_학급당 학생 수 (명)
5   569.452121  초등학교_학급당 학생 수 (명)
6   334.279430   중학교_학급당 학생 수 (명)
7   205.924685  고등학교_학급당 학생 수 (명)
8     7.631829      학교교과 교습학원 (개)
9     6.996400      평생직업 교육학원 (개)
10    2.133011      사설학원당 학생수 (명)
11   25.967622             유치원생 수
12   31.129589             초등학생 수    
'''
#%%
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    