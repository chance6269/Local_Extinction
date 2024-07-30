# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:11:07 2024

@author: Shin
"""

import pandas as pd

file_path =  'C:/Users/Shin/Documents/Final_Project/Mysql/data/excel/교육종합_v0.2.xlsx'
file_path_1 = 'C:/Users/Shin/Documents/Final_Project/Data/교육_전국/교육_연도별_전국통합/소멸등급(2015~2021).csv'
df = pd.read_excel(file_path)
df_p = pd.read_csv(file_path_1)
    
#%%
#폰트 설정
from matplotlib import font_manager, rc
font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
#%%

'''
''교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교',
 '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)','고등학교_학급당 학생 수 (명)',
 '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)','유치원생 수', '초등학생 수'
'''

#%%
# aspect = 1보다 크게 하면 좌우 사이즈 증가 # height = 2.5이상 -> 높이 증가
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import statsmodels.api as sm
# Create the pair plot
pairplot = sns.pairplot(df[['교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교',
                            '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)', '고등학교_학급당 학생 수 (명)',
                            '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)', '유치원생 수', '초등학생 수']], 
                    aspect=1.5, height=3)

# Save the plot
pairplot.savefig('C:/Users/Shin/Documents/Final_Project/Mysql/data/교육.png')

# Show the plot (optional, especially if running in an interactive environment)
plt.show()
#%%
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
corr = df.iloc[:,1:].corr()

# 히트맵 시각화
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
#%%

import plotly.express as px

# 데이터 로드
corr = df.iloc[:,1:].corr()

# 히트맵 시각화
fig = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r', title='Correlation Heatmap')
fig.show()



#%%
from sklearn.preprocessing import StandardScaler
import pandas as pd
import statsmodels.api as sm
features = ['교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교',
                            '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)', '고등학교_학급당 학생 수 (명)',
                            '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)', '유치원생 수', '초등학생 수']
X = df[features]
y = df_p['소멸위험등급']
#%%
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
'''
 OLS Regression Results 회귀분석결과                              
==============================================================================
Dep. Variable:                 소멸위험등급   R-squared:                 0.176
Model:                            OLS   Adj. R-squared:                  0.169
Method:                 Least Squares   F-statistic:                     26.03
Date:                Tue, 30 Jul 2024   Prob (F-statistic):           5.47e-58
Time:                        15:40:48   Log-Likelihood:                -2299.1
No. Observations:                1603   AIC:                             4626.
Df Residuals:                    1589   BIC:                             4701.
Df Model:                          13                                         
Covariance Type:            nonrobust                                         
============================================================================================
                               coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------------------
const                        2.4997      0.025     98.132      0.000       2.450       2.550
scaled_교원_1인당_학생수_유치원        0.1643      0.055      2.984      0.003       0.056       0.272
scaled_교원_1인당_학생수_초등학교       0.2105      0.166      1.270      0.204      -0.115       0.536
scaled_교원_1인당_학생수_중학교        0.7743      0.124      6.232      0.000       0.531       1.018
scaled_교원_1인당_학생수_고등학교       0.2332      0.082      2.845      0.005       0.072       0.394
scaled_유치원_학급당 학생 수 (명)      0.1847      0.054      3.418      0.001       0.079       0.291
scaled_초등학교_학급당 학생 수 (명)    -0.5406      0.161     -3.356      0.001      -0.856      -0.225
scaled_중학교_학급당 학생 수 (명)     -0.5490      0.108     -5.076      0.000      -0.761      -0.337
scaled_고등학교_학급당 학생 수 (명)    -0.1025      0.079     -1.295      0.196      -0.258       0.053
scaled_학교교과 교습학원 (개)        -0.3966      0.069     -5.736      0.000      -0.532      -0.261
scaled_평생직업 교육학원 (개)         0.2415      0.067      3.618      0.000       0.111       0.372
scaled_사설학원당 학생수 (명)         0.0293      0.032      0.924      0.356      -0.033       0.092
scaled_유치원생 수               -0.3083      0.091     -3.375      0.001      -0.488      -0.129
scaled_초등학생 수                0.2555      0.095      2.682      0.007       0.069       0.442
==============================================================================
Omnibus:                      260.337   Durbin-Watson:                   1.466
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               60.076
Skew:                           0.062   Prob(JB):                     9.01e-14
Kurtosis:                       2.060   Cond. No.[다중공선성 30이하 -> 정상] 24.2
==============================================================================

'''




#%%
#df['intercept'] = 1 #(절편) 
model = sm.OLS(df_p['소멸위험등급'], df[['교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교',
                            '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)', '고등학교_학급당 학생 수 (명)',
                            '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)', '유치원생 수', '초등학생 수']])


results = model.fit()
print(results.summary())

'''
 OLS Regression Results 회귀분석결과                             
=======================================================================================
Dep. Variable:                 소멸위험등급   R-squared (uncentered):             0.855
Model:                            OLS   Adj. R-squared (uncentered):              0.854
Method:                 Least Squares   F-statistic:                              724.0
Date:                Tue, 30 Jul 2024   Prob (F-statistic):                        0.00
Time:                        15:28:59   Log-Likelihood:                         -2339.0
No. Observations:                1603   AIC:                                      4704.
Df Residuals:                    1590   BIC:                                      4774.
Df Model:                          13                                                  
Covariance Type:            nonrobust                                                  
=====================================================================================
                                 coef    std err          t      P>|t|      [0.025      0.975]
-------------------------------------------------------------------------------------
교원_1인당_학생수_유치원        0.0682      0.021      3.243      0.001       0.027       0.109
교원_1인당_학생수_초등학교      -0.0275      0.045     -0.612      0.541      -0.116       0.061
교원_1인당_학생수_중학교        0.0479      0.033      1.465      0.143      -0.016       0.112
교원_1인당_학생수_고등학교      -0.0091      0.030     -0.297      0.766      -0.069       0.051
유치원_학급당 학생 수 (명)      0.0580      0.014      4.277      0.000       0.031       0.085
초등학교_학급당 학생 수 (명)    -0.0177      0.031     -0.570      0.569      -0.079       0.043
중학교_학급당 학생 수 (명)      0.0077      0.017      0.445      0.657      -0.026       0.042
고등학교_학급당 학생 수 (명)     0.0455      0.015      3.053      0.002       0.016       0.075
학교교과 교습학원 (개)        -0.0003   8.01e-05     -3.950      0.000      -0.000      -0.000
평생직업 교육학원 (개)         0.0019      0.001      2.584      0.010       0.000       0.003
사설학원당 학생수 (명)         0.0007      0.000      3.508      0.000       0.000       0.001
유치원생 수               -0.0001   2.73e-05     -4.902      0.000      -0.000   -8.03e-05
초등학생 수             2.069e-05   7.63e-06      2.713      0.007    5.73e-06    3.57e-05
==============================================================================
Omnibus:                      166.033   Durbin-Watson:                   1.413
Prob(Omnibus):                  0.000   Jarque-Bera (JB):               49.420
Skew:                           0.078   Prob(JB):                     1.86e-11
Kurtosis:                       2.154   Cond. No.[다중공선성 30이하 -> 정상]  3.87e+04 -> 38700 
==============================================================================
'''
#%%

from statsmodels.stats.outliers_influence import variance_inflation_factor


X_train = df[['교원_1인당_학생수_유치원', '교원_1인당_학생수_초등학교', '교원_1인당_학생수_중학교', '교원_1인당_학생수_고등학교',
                            '유치원_학급당 학생 수 (명)', '초등학교_학급당 학생 수 (명)', '중학교_학급당 학생 수 (명)', '고등학교_학급당 학생 수 (명)',
                            '학교교과 교습학원 (개)', '평생직업 교육학원 (개)', '사설학원당 학생수 (명)', '유치원생 수', '초등학생 수']]
def feature_engineering_XbyVIF(X_train):
    vif = pd.DataFrame()
    vif['VIF_Factor'] = [variance_inflation_factor(X_train.values, i)
                         for i in range(X_train.shape[1])]
    vif['Feature'] = X_train.columns
    return vif
vif = feature_engineering_XbyVIF(X_train)
print(vif)
#%%
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
#%%
#정규 Q-Q 플롯 (Quantile-Quantile Plot):
#잔차가 정규분포를 따른다면 Q-Q 플롯에서 데이터 점들이 직선 위에 위치해야 합
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

#자기상관 (Autocorrelation):
#잔차가 시간 순서나 다른 독립 변수에 따라 자기상관을 갖지 않아야 합니다. Durbin-Watson 통계량을 사용하여 자기상관을 평가할 수 있습니다.
from statsmodels.stats.stattools import durbin_watson
dw = durbin_watson(df['잔차'])
print(f'Durbin-Watson 통계량: {dw}')
#%%
