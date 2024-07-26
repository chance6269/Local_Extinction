# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 14:49:15 2024

@author: OSP
"""

# 폰트설치
#   - 나눔고딕 : NanumGothic.ttf
# 사용자가 설치한 폰트 위치
# C:\Users\OSP\AppData\Local\Microsoft\Windows\Fonts

#%%

# 폰트를 사용자 계정 전용으로 윈두우에서 설치

#%%

# 01 : 지정된 폴더에서 설치된 폰트 꺼내서 matplotlip 그래프에 적용

import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import rc

font_path = "C:/Windows/Fonts/malgun.ttf"
font_name = fm.FontProperties(fname=font_path).get_name()
print(font_name)
rc('font', family=font_name)

#%%

# 02 : windows > fonts 폴더에서 폰트 꺼내서 적용하기

font_files = fm.findSystemFonts(fontpaths=['C:/Windows/Fonts'])
for fpath in font_files:
    fm.fontManager.addfont(fpath)

#%%

# 맑은 고딕
plt.rcParams['font.family'] = 'malgun'

#%%

# 나눔고딕
plt.rcParams['font.family'] = 'NanumGothic'

#%%

# 나눔스퀘어
plt.rcParams['font.family'] = 'NanumSquare'

# In[8]:

# 나눔바른고딕
plt.rc('font', family='NanumBarunGothic')

#%%

# 글꼴 설치 여부 확인용 그래프

plt.plot([1, 4, 9, 16])
plt.title('간단한 선 그래프')
plt.show()