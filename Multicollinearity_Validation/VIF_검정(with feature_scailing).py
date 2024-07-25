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

# 동일한 공식을 이용해 산출된 변수들 별로 묶었음.

# 교원당 학생수 : 해당 시도구군의 학생수 /  시도구군의 교원수
#교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교'

# 학급당 학생수 : 해당 시도구군의 학급수 /  시도구군의 학생수
# '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)','고등학교_학급당 학생 수 (명)'

# 사설학원 :
# '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)'
# 사설학원당 학생수 (명) : 해당 시도구군의 초+중+고학생수 / 해당 시도구군의 사설학원 수 

# 학생수 :
#'유치원생 수', '초등학생 수'

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
# aspect = 1보다 크게 하면 좌우 사이즈 증가 # height = 2.5이상 -> 높이 증가
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
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.

F-statistic: 15.68, Prob (F-statistic): 2.68e-09
모델 전체의 유의미성을 평가하는 지표입니다. F-statistic이 상당히 높고 p-value가 매우 낮아(2.68e-09), 모델 전체가 통계적으로 유의미하다는 것을 시사합니다.

Coefficients and p-values:
학교교과 교습학원 (개): 0.0001 (p-value: 0.654)
p-value가 0.05보다 커서, 이 변수는 종속 변수에 대해 통계적으로 유의미한 영향을 미치지 않습니다.
평생직업 교육학원 (개): 0.0039 (p-value: 0.185)
p-value가 0.05보다 커서, 이 변수 역시 통계적으로 유의미하지 않습니다.
사설학원당 학생수 (명): 0.0029 (p-value: 0.000)
p-value가 0.05보다 작아서, 이 변수는 종속 변수에 대해 통계적으로 유의미한 영향을 미치며, 계수는 양수로, 사설학원당 학생 수가 증가할 때 종속 변수의 값이 증가하는 경향이 있음을 나타냅니다.
'''
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
'''Coefficients and p-values:

유치원생 수: -4.664e-05 (p-value: 0.630)
p-value가 0.05보다 크므로 통계적으로 유의미하지 않습니다. 유치원생 수가 종속 변수에 유의미한 영향을 미치지 않는 것으로 보입니다.
초등학생 수: 6.436e-05 (p-value: 0.012)
통계적으로 유의미 (p-value < 0.05). 초등학생 수가 증가할 때 종속 변수의 값이 유의미하게 증가하는 경향이 있습니다.'''
'''
결론
모델의 설명력: 모델은 종속 변수의 변동성을 약 24.1% 설명할 수 있으며, 통계적으로 유의미한 것으로 나타났습니다.
독립 변수의 유의미성: "초등학생 수"는 종속 변수에 유의미한 영향을 미치며, 그 계수는 양수로, 초등학생 수가 증가할 때 종속 변수의 값이 증가하는 경향이 있음을 시사합니다.
잔차의 문제: 잔차의 정규성 부족과 양의 자기상관 가능성이 존재합니다.'''
#잔차 분석을 통해 모델의 적합성을 평가하고, 개선할 수 있는 방법을 모색함으로써 더 나은 예측 모델을 구축할 수 있습니다.
#잔차는 모델의 예측값과 실제 관측값 간의 차이로 정의
'''
# 예측값 : 
df['예측 값'] = results.predict()
df['잔차'] = df['실제 값'] - df['예측 값']
# 잔차 시각화 : 
import matplotlib.pyplot as plt

plt.scatter(df['예측 값'], df['잔차'])
plt.axhline(0, color='red', linestyle='--')
plt.xlabel('예측 값')
plt.ylabel('잔차')
plt.title('잔차 플롯')
plt.show()

#정규 Q-Q 플롯 (Quantile-Quantile Plot):
잔차가 정규분포를 따른다면 Q-Q 플롯에서 데이터 점들이 직선 위에 위치해야 합
import scipy.stats as stats
import numpy as np

stats.probplot(df['잔차'], dist="norm", plot=plt)
plt.title('정규 Q-Q 플롯')
plt.show()

# 잔차의 분포를 확인하여 정규성을 검토
plt.hist(df['잔차'], bins=30, edgecolor='k')
plt.xlabel('잔차')
plt.ylabel('빈도')
plt.title('잔차의 히스토그램')
plt.show()

자기상관 (Autocorrelation):
잔차가 시간 순서나 다른 독립 변수에 따라 자기상관을 갖지 않아야 합니다. Durbin-Watson 통계량을 사용하여 자기상관을 평가할 수 있습니다.
from statsmodels.stats.stattools import durbin_watson
dw = durbin_watson(df['잔차'])
print(f'Durbin-Watson 통계량: {dw}')

'''
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
'''
Coefficients and p-values:

교원_1인당_학생수_유치원: 0.1516 (p-value: 0.059)
p-value가 0.05보다 약간 크지만, 유치원 교원 1인당 학생 수가 증가할 때 종속 변수의 값이 증가하는 경향이 있을 수 있음을 시사합니다.
교원_1인당_학생수_초등학교: 0.3367 (p-value: 0.026)
통계적으로 유의미 (p-value < 0.05). 초등학교 교원 1인당 학생 수가 증가할 때 종속 변수의 값이 유의미하게 증가합니다.
교원_1인당_학생수_중학교: 0.1471 (p-value: 0.189)
유의미하지 않음 (p-value > 0.05). 중학교 교원 1인당 학생 수와 종속 변수 간의 유의미한 관계가 없음.
교원_1인당_학생수_고등학교: -0.0698 (p-value: 0.449)
유의미하지 않음. 고등학교 교원 1인당 학생 수와 종속 변수 간의 유의미한 관계가 없음.
초등학교_학급당 학생 수 (명): -0.2852 (p-value: 0.008)
통계적으로 유의미. 초등학교 학급당 학생 수가 증가할수록 종속 변수의 값이 감소합니다.
그 외 다른 변수들은 대부분 유의미하지 않음 (p-value > 0.05).
'''
'''
결론
모델의 설명력: 모델은 종속 변수의 변동성을 약 53.4% 설명할 수 있으며, 통계적으로 유의미한 것으로 나타났습니다.
독립 변수의 유의미성: 유의미한 변수는 교원_1인당_학생수_초등학교와 초등학교_학급당 학생 수 (명)입니다. 초등학교 교원 1인당 학생 수가 증가할 때 종속 변수의 값이 증가하고, 초등학교 학급당 학생 수가 증가할 때는 종속 변수의 값이 감소하는 경향이 있습니다.
다중공선성 문제: Cond. No.가 매우 높아 다중공선성 문제의 가능성이 있습니다. 이는 변수들 간의 강한 상관관계가 존재하거나, 분석 과정에서의 수치적 문제가 있을 수 있음을 시사합니다.

추가적인 분석 및 고려사항
다중공선성 문제를 해결하기 위해 변수 선택을 재검토하거나, PCA(주성분 분석)와 같은 차원 축소 기법을 사용할 수 있습니다.
잔차의 정규성 및 자기상관 문제를 개선하기 위해 데이터 변환 또는 추가적인 모델링 기법을 고려할 수 있습니다.
추가 변수를 포함하거나, 데이터의 품질을 향상시키는 것도 모델의 성능을 개선하는 방법이 될 수 있습니다.
'''

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
# p-value 값이 0.05근처의 변수들로만 모델설계
'교원_1인당_학생수_유치원', '유치원_학급당 학생 수 (명)', '교원_1인당_학생수_초등학교', '사설학원당 학생수 (명)',  '초등학생 수'

sns.pairplot(df[['교원_1인당_학생수_유치원', '유치원_학급당 학생 수 (명)', '교원_1인당_학생수_초등학교', '사설학원당 학생수 (명)',  '초등학생 수']])
plt.show()

df['intercept'] = 1 #(절편) 
model = sm.OLS(df_p['2015'], df[['교원_1인당_학생수_유치원', '유치원_학급당 학생 수 (명)', '교원_1인당_학생수_초등학교', '사설학원당 학생수 (명)',  '초등학생 수']])

results = model.fit()
print(results.summary())  
'''
     OLS Regression Results                                
=======================================================================================
Dep. Variable:                   2015   R-squared (uncentered):                   0.499
Model:                            OLS   Adj. R-squared (uncentered):              0.488
Method:                 Least Squares   F-statistic:                              44.57
Date:                Thu, 25 Jul 2024   Prob (F-statistic):                    8.35e-32
Time:                        12:08:28   Log-Likelihood:                         -388.22
No. Observations:                 229   AIC:                                      786.4
Df Residuals:                     224   BIC:                                      803.6
Df Model:                           5                                                  
Covariance Type:            nonrobust                                                  
====================================================================================
                       coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------------
교원_1인당_학생수_유치원       0.0447      0.066      0.680      0.497      -0.085       0.174
유치원_학급당 학생 수 (명)     0.0287      0.043      0.669      0.504      -0.056       0.113
교원_1인당_학생수_초등학교      0.0346      0.050      0.686      0.493      -0.065       0.134
사설학원당 학생수 (명)     4.377e-05      0.001      0.080      0.936      -0.001       0.001
초등학생 수           -1.241e-05    9.3e-06     -1.335      0.183   -3.07e-05    5.91e-06
==============================================================================
Omnibus:                       72.024   Durbin-Watson:                   1.287
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              147.104
Skew:                           1.562   Prob(JB):                     1.14e-32
Kurtosis:                       5.380   Cond. No.                     1.48e+04
==============================================================================

Notes:
[1] R² is computed without centering (uncentered) since the model does not contain a constant.
[2] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[3] The condition number is large, 1.48e+04. This might indicate that there are
strong multicollinearity or other numerical problems.'''
    
#%%  
from statsmodels.stats.outliers_influence import variance_inflation_factor
X_train = df[['교원_1인당_학생수_유치원', '유치원_학급당 학생 수 (명)', '교원_1인당_학생수_초등학교', '사설학원당 학생수 (명)',  '초등학생 수']]
def feature_engineering_XbyVIF(X_train):
    vif = pd.DataFrame()
    vif['VIF_Factor'] = [variance_inflation_factor(X_train.values, i)
                         for i in range(X_train.shape[1])]
    vif['Feature'] = X_train.columns
    return vif
vif = feature_engineering_XbyVIF(X_train)
print(vif)      
    
'''
 VIF_Factor           Feature
0   77.527684    교원_1인당_학생수_유치원
1   75.599863  유치원_학급당 학생 수 (명)
2   52.086056   교원_1인당_학생수_초등학교
3    1.458329     사설학원당 학생수 (명)
4    3.359249            초등학생 수'''    
    
'''
결론 및 제언
모델의 설명력: 모델의 설명력(R-squared)이 49.9%로 비교적 높은 편이지만, 여전히 절대적인 설명력은 제한적입니다.
 모델이 상당한 부분의 변동성을 설명하지만, 더 많은 변수나 다른 모델링 기법을 고려할 수 있습니다.

변수의 유의미성: 모든 변수의 p-value가 0.05보다 크기 때문에, 현재 모델에서는 독립 변수들이 종속 변수에 통계적으로 유의미한 영향을 미치지 않는 것으로 나타납니다.
다른 변수들을 고려하거나, 변수 선택 방법을 조정할 필요가 있을 수 있습니다.

잔차의 정규성 부족: 잔차가 정규 분포를 따르지 않으므로, 모델의 가정을 검토하고 필요에 따라 데이터 변환 또는 다른 회귀 기법을 고려해야 합니다.

자기상관: 잔차의 자기상관이 존재할 가능성이 있으므로, 이를 해결하기 위해 다른 회귀 기법이나 시간적 요소를 고려할 수 있습니다.

다중공선성: 매우 높은 condition number는 다중공선성 문제를 시사합니다. 변수 간의 상관관계를 줄이거나, 변수 선택을 조정하여 다중공선성을 완화할 필요가 있습니다.

모델을 개선하기 위해 추가적인 변수 선택, 데이터 변환, 다중공선성 해결 방법 등을 고려하는 것이 중요합니다.'''
    
   
#%%
# 변수별 scailing이 되지않아 vif_factor 값을 보면 분포도가 작은 변수들에 비해 낮은 값으로 도출
# VIF = 1/ 1-R^2
# 이는 R^2 결정계수(설명력) VIF의 분모를 작게하여 결국 VIF값이 커지고 다중공선성이 큰 결과를 보여주게됨.    

#데이터의 값이 고르게 10~1000 단위에 분포하는 경향이 강한 변수일수록 
# VIF_Factor가 낮게 나오는 경향이 있는듯해 변수별 데이터들의 특성을 feature scailing을 통해 조정하면 편향되지않은 결과를 얻을 수 있을까라는 의문점이 생김.

#gpt 대답 :
#특히, 변수가 서로 다른 범위와 단위를 가지는 경우, 변수들의 스케일을 맞추는 것이 중요합니다. 이를 통해 VIF (Variance Inflation Factor)와 같은 지표의 편향을 줄일 수 있습니다.
    
# 표준화(StandardScaler)와[평균을 0으로, 표준편차를 1로 변환합니다.] StandardScaler를 사용하여 
#  정규화(MinMaxScaler)[[데이터를 특정 범위로 변환합니다.보통 0과 1 사이로 변환합니다.] 후 VIF검정을 해보자.


# 변수 표준화 후 모델성능확인 
from sklearn.preprocessing import StandardScaler
import pandas as pd
import statsmodels.api as sm

# 데이터 로드 및 스케일링
file_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육/EXCEL/교육_2015_전국.xlsx"
file_path_1 = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/개선소멸위험지수2015.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')
df_p = pd.read_excel(file_path_1, engine='openpyxl')

# 변수 선택
features = ['교원_1인당_학생수_유치원', '유치원_학급당 학생 수 (명)', '교원_1인당_학생수_초등학교', '사설학원당 학생수 (명)',  '초등학생 수']
X = df[features]
y = df_p['2015']

# 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 데이터프레임으로 변환
X_scaled_df = pd.DataFrame(X_scaled, columns=['scaled_' + feature for feature in features])

# 상수항 추가
X_scaled_df = sm.add_constant(X_scaled_df)

# 모델 생성 및 피팅
model = sm.OLS(y, X_scaled_df)
results = model.fit()

# 결과 출력
print(results.summary())

# 결과에서 원래 변수 이름으로 매핑하기
print("\nOriginal feature names:")
for i, feature in enumerate(features):
    print(f"{feature}: {results.params[i + 1]} (p-value: {results.pvalues[i + 1]})")
    '''
                  OLS Regression Results                            
==============================================================================
Dep. Variable:                   2015   R-squared:                       0.049
Model:                            OLS   Adj. R-squared:                  0.028
Method:                 Least Squares   F-statistic:                     2.316
Date:                Thu, 25 Jul 2024   Prob (F-statistic):             0.0446
Time:                        12:30:45   Log-Likelihood:                -387.86
No. Observations:                 229   AIC:                             787.7
Df Residuals:                     223   BIC:                             808.3
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                       1.2824      0.088     14.550      0.000       1.109       1.456
scaled_교원_1인당_학생수_유치원       0.1776      0.170      1.047      0.296      -0.157       0.512
scaled_유치원_학급당 학생 수 (명)     0.1268      0.165      0.767      0.444      -0.199       0.453
scaled_교원_1인당_학생수_초등학교      0.1110      0.184      0.602      0.548      -0.253       0.474
scaled_사설학원당 학생수 (명)       -0.0010      0.095     -0.011      0.991      -0.188       0.186
scaled_초등학생 수              -0.1940      0.126     -1.542      0.124      -0.442       0.054
==============================================================================
Omnibus:                       69.147   Durbin-Watson:                   1.298
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              136.285
Skew:                           1.520   Prob(JB):                     2.55e-30
Kurtosis:                       5.245   Cond. No.                         4.34
==============================================================================
'''
'''
모델의 성능: 이 회귀 모델은 종속 변수의 변동성을 매우 적게 설명하고 있습니다 (R-squared가 0.049). 이는 모델이 종속 변수와 독립 변수 간의 관계를 잘 설명하지 못한다는 것을 의미합니다.

변수의 중요성: 모든 독립 변수의 p-value가 0.05보다 커서, 통계적으로 유의미한 변수는 없습니다. 이는 독립 변수들이 종속 변수에 미치는 영향이 명확하지 않다는 것을 의미합니다.
'''
#%%
from statsmodels.stats.outliers_influence import variance_inflation_factor
X_scaled_df = df[['교원_1인당_학생수_유치원', '유치원_학급당 학생 수 (명)', '교원_1인당_학생수_초등학교', '사설학원당 학생수 (명)',  '초등학생 수']]
def feature_engineering_XbyVIF(X_scaled_df):
    vif = pd.DataFrame()
    vif['VIF_Factor'] = [variance_inflation_factor(X_scaled_df.values, i)
                         for i in range(X_train.shape[1])]
    vif['Feature'] = X_scaled_df.columns
    return vif
vif = feature_engineering_XbyVIF(X_scaled_df)
print(vif)  
'''   VIF_Factor           Feature
0   77.527684    교원_1인당_학생수_유치원
1   75.599863  유치원_학급당 학생 수 (명)
2   52.086056   교원_1인당_학생수_초등학교
3    1.458329     사설학원당 학생수 (명)
4    3.359249            초등학생 수
'''
#%%
# 변수 정규화 후 모델성능확인 
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import statsmodels.api as sm

# 데이터 로드
file_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육/EXCEL/교육_2015_전국.xlsx"
file_path_1 = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/개선소멸위험지수2015.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')
df_p = pd.read_excel(file_path_1, engine='openpyxl')

# 변수 선택
features = ['교원_1인당_학생수_유치원', '유치원_학급당 학생 수 (명)', '교원_1인당_학생수_초등학교', '사설학원당 학생수 (명)',  '초등학생 수']
X = df[features]
y = df_p['2015']

# MinMaxScaler를 사용하여 데이터 스케일링
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# 데이터프레임으로 변환
X_scaled_df = pd.DataFrame(X_scaled, columns=['scaled_' + feature for feature in features])

# 상수항 추가
X_scaled_df = sm.add_constant(X_scaled_df)

# 모델 생성 및 피팅
model = sm.OLS(y, X_scaled_df)
results = model.fit()

# 결과 출력
print(results.summary())

# 결과에서 원래 변수 이름으로 매핑하기
print("\nOriginal feature names:")
for i, feature in enumerate(features):
    print(f"{feature}: {results.params[i + 1]} (p-value: {results.pvalues[i + 1]})")
'''
                           OLS Regression Results                            
==============================================================================
Dep. Variable:                   2015   R-squared:                       0.049
Model:                            OLS   Adj. R-squared:                  0.028
Method:                 Least Squares   F-statistic:                     2.316
Date:                Thu, 25 Jul 2024   Prob (F-statistic):             0.0446
Time:                        12:33:17   Log-Likelihood:                -387.86
No. Observations:                 229   AIC:                             787.7
Df Residuals:                     223   BIC:                             808.3
Df Model:                           5                                         
Covariance Type:            nonrobust                                         
===========================================================================================
                              coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------------
const                       0.4213      0.273      1.546      0.124      -0.116       0.958
scaled_교원_1인당_학생수_유치원       0.8508      0.812      1.047      0.296      -0.750       2.452
scaled_유치원_학급당 학생 수 (명)     0.5313      0.693      0.767      0.444      -0.833       1.896
scaled_교원_1인당_학생수_초등학교      0.4572      0.760      0.602      0.548      -1.041       1.955
scaled_사설학원당 학생수 (명)       -0.0153      1.430     -0.011      0.991      -2.834       2.804
scaled_초등학생 수              -1.0603      0.688     -1.542      0.124      -2.415       0.295
==============================================================================
Omnibus:                       69.147   Durbin-Watson:                   1.298
Prob(Omnibus):                  0.000   Jarque-Bera (JB):              136.285
Skew:                           1.520   Prob(JB):                     2.55e-30
Kurtosis:                       5.245   Cond. No.                         24.1
=============================================================================='''
#%%
from statsmodels.stats.outliers_influence import variance_inflation_factor
X_scaled_df = df[['교원_1인당_학생수_유치원', '유치원_학급당 학생 수 (명)', '교원_1인당_학생수_초등학교', '사설학원당 학생수 (명)',  '초등학생 수']]
def feature_engineering_XbyVIF(X_scaled_df):
    vif = pd.DataFrame()
    vif['VIF_Factor'] = [variance_inflation_factor(X_scaled_df.values, i)
                         for i in range(X_train.shape[1])]
    vif['Feature'] = X_scaled_df.columns
    return vif
vif = feature_engineering_XbyVIF(X_scaled_df)
print(vif)   
'''   VIF_Factor           Feature
0   77.527684    교원_1인당_학생수_유치원
1   75.599863  유치원_학급당 학생 수 (명)
2   52.086056   교원_1인당_학생수_초등학교
3    1.458329     사설학원당 학생수 (명)
4    3.359249            초등학생 수
'''

#%%
# 표준화 및 정규화를 통해 모델의 성능은 오히려 악화됨. 데이터를 그대로 보존하기로 하고 주성분 분석을 해보자
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# 데이터 로드
file_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육/EXCEL/교육_2015_전국.xlsx"
file_path_1 = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/개선소멸위험지수2015.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')
df_p = pd.read_excel(file_path_1, engine='openpyxl')

# 변수 선택
features = ['교원_1인당_학생수_유치원', '유치원_학급당 학생 수 (명)', '교원_1인당_학생수_초등학교', '사설학원당 학생수 (명)', '초등학생 수']
X = df[features]

# 데이터 스케일링
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA 수행
pca = PCA()
X_pca = pca.fit_transform(X_scaled)

# 주성분의 설명된 분산 비율
explained_variance = pca.explained_variance_ratio_

# 설명된 분산 비율을 그래프로 시각화
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(explained_variance) + 1), explained_variance, marker='o', linestyle='--')
plt.xlabel('주성분 번호')
plt.ylabel('설명된 분산 비율')
plt.title('주성분별 설명된 분산 비율')
plt.grid(True)
plt.show()

# 누적 설명된 분산 비율
cumulative_variance = explained_variance.cumsum()
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linestyle='--')
plt.xlabel('주성분 번호')
plt.ylabel('누적 설명된 분산 비율')
plt.title('누적 설명된 분산 비율')
plt.grid(True)
plt.show()

# 각 주성분의 로딩
loadings = pd.DataFrame(pca.components_.T, index=features, columns=[f'PC{i+1}' for i in range(len(features))])
print("주성분 로딩:")
print(loadings)
'''
주성분 로딩:
                       PC1       PC2       PC3       PC4       PC5
교원_1인당_학생수_유치원    0.508099  0.201388 -0.309887 -0.659653 -0.412440
유치원_학급당 학생 수 (명)  0.509006  0.107202 -0.402380  0.730040 -0.185885
교원_1인당_학생수_초등학교   0.529128 -0.112796 -0.003578 -0.143328  0.828701
사설학원당 학생수 (명)    -0.029756  0.954875  0.242640  0.054881  0.159508
초등학생 수            0.449317 -0.153109  0.826543  0.091352 -0.288362
'''
'''
결과:
PC1: 유치원 및 초등학교 관련 변수들이 주로 영향을 미침.
PC2: 사설학원 관련 변수들이 주요 기여를 함.
PC3: 초등학생 수와 강한 상관관계가 있음.
PC4: 유치원 관련 변수들 간의 변동성을 반영.
PC5: 초등학교와 관련된 변수들이 주요 기여를 함.'''
#%%

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# 데이터 로드
file_path = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/교육/EXCEL/교육_2015_전국.xlsx"
file_path_1 = "C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/개선소멸위험지수2015.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')
df_p = pd.read_excel(file_path_1, engine='openpyxl')

# 변수 선택
features = ['교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교',
 '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)', '고등학교_학급당 학생 수 (명)',
 '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)', '유치원생 수', '초등학생 수']
X = df[features]

# PCA 수행
pca = PCA()
X_pca = pca.fit_transform(X)

# 주성분의 설명된 분산 비율
explained_variance = pca.explained_variance_ratio_

# 설명된 분산 비율을 그래프로 시각화
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(explained_variance) + 1), explained_variance, marker='o', linestyle='--')
plt.xlabel('주성분 번호')
plt.ylabel('설명된 분산 비율')
plt.title('주성분별 설명된 분산 비율')
plt.grid(True)
plt.show()

# 누적 설명된 분산 비율
cumulative_variance = explained_variance.cumsum()
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o', linestyle='--')
plt.xlabel('주성분 번호')
plt.ylabel('누적 설명된 분산 비율')
plt.title('누적 설명된 분산 비율')
plt.grid(True)
plt.show()

# 각 주성분의 로딩
loadings = pd.DataFrame(pca.components_.T, index=features, columns=[f'PC{i+1}' for i in range(len(features))])
print("주성분 로딩:")
print(loadings)


'''
주성분 로딩:
                               PC1       PC2       PC3  ...      PC11      PC12      PC13
교원_1인당_학생수_유치원     0.000089  0.000301 -0.000506  ... -0.005854  0.066161  0.014955
교원_1인당_학생수_초등학교    0.000197 -0.000343 -0.000743  ...  0.071339  0.278737 -0.775216
교원_1인당_학생수_중학교     0.000174 -0.000390 -0.000570  ...  0.008467  0.788213  0.360092
교원_1인당_학생수_고등학교    0.000101  0.000195 -0.000294  ... -0.909118  0.008850 -0.050181
유치원_학급당 학생 수 (명)   0.000161  0.000300 -0.000945  ... -0.013964 -0.042680 -0.032329
초등학교_학급당 학생 수 (명)  0.000267 -0.000582 -0.001046  ...  0.013126 -0.286883  0.491422
중학교_학급당 학생 수 (명)   0.000252 -0.000649 -0.000664  ...  0.032947 -0.460911 -0.154715
고등학교_학급당 학생 수 (명)  0.000186  0.000469 -0.000724  ...  0.408479  0.000564  0.012038
학교교과 교습학원 (개)      0.019538 -0.033734  0.994967  ...  0.000110 -0.000214  0.000288
평생직업 교육학원 (개)      0.001383 -0.007828  0.085971  ...  0.000222  0.002563 -0.003141
사설학원당 학생수 (명)     -0.001233  0.088619 -0.029800  ...  0.000743 -0.001251  0.000212
유치원생 수             0.249538  0.964153  0.030997  ... -0.000014  0.000051  0.000035
초등학생 수             0.968166 -0.247699 -0.028228  ... -0.000007 -0.000013 -0.000006'''
#%%
#설명된 분산 비율을 확인하고 필요한 주성분의 개수를 선택
import numpy as np
from sklearn.linear_model import LinearRegression

# 누적 설명된 분산 비율이 충분히 높은 주성분 개수 선택 (예: 90% 이상)
n_components = np.argmax(cumulative_variance >= 0.90) + 1
X_pca_selected = X_pca[:, :n_components]

# 회귀 모델 생성 및 피팅
model = LinearRegression()
model.fit(X_pca_selected, y)

# 회귀 모델 결과 확인
print(f'회귀 모델의 설명된 분산 (R^2): {model.score(X_pca_selected, y)}')
# 회귀 모델의 설명된 분산 (R^2): 0.0015996638072754976
# 이 값은 0에 매우 가까운 값으로, 회귀 모델이 종속 변수 y (개선소멸위험지수 2015)의 변동성을 거의 설명하지 못한다는 의미
#%%

import sklearn
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RandomizedSearchCV

iris = load_iris()
label = iris.target
data = iris.data
#%%
# 의사결정나무 파라미터 
'''
criterion : 분할 성능 측정 기능

min_samples_split : 노드를 분할하기 위한 최소한의 샘플 데이터수로, 과적합을 제어하는데 주로 사용함.
작게 설정할 수록 분할 노드가 많아져 과적합 가능성이 높아짐

max_depth : 트리의 최대 깊이, 깊이가 깊어지면 과적합될 수 있음.

max_features : 최적의 분할을 위해 고려할 최대 feature 개수
(default = None : 데이터 세트의 모든 피처를 사용)

samples_leaf : 리프노드가 되기 위해 필요한 최소한의 샘플 데이터수 (과적합 제어 용도), 작게 설정 필요

max_leaf_nodes : 리프노드의 최대 개수

param_distributions : 튜닝을 위한 대상 파라미터, 사용될 파라미터를 딕셔너리 형태로 넣어준다.

n_iter : 파라미터 검색 횟수

best score: 최고 평균 정확도 수치
'''
#%%
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=1)

dt_clf = DecisionTreeClassifier(random_state=1)

param_dist = {
    'criterion':['gini','entropy'], 
    'max_depth':[None,2,3,4,5,6], 
    'max_leaf_nodes':[None,2,3,4,5,6,7], 
    'min_samples_split':[2,3,4,5,6], 
    'min_samples_leaf':[1,2,3], 
    'max_features':[None,'sqrt','log2',3,4,5]
    }

rand_search = RandomizedSearchCV(dt_clf, param_distributions = param_dist, n_iter = 50, cv = 5, scoring = 'accuracy', refit=True)
rand_search.fit(X_train, y_train)

print('best parameters : ', rand_search.best_params_)
print('best score : ', round(rand_search.best_score_, 4))

df = pd.DataFrame(rand_search.cv_results_)
df
















    
