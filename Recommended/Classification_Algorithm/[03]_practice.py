#!/usr/bin/env python
# coding: utf-8

# # [03] 데이터 다루기

# ## 1. 파이썬 문법에 대한 이해

# ### 1-3. 함수

# In[1]:


# 사용자 정의 함수 calc
def calc(a, b):
    c = a*2 + b
    print(c)


# In[2]:


calc(1, 2)


# ### 1-4. 조건문

# In[3]:


a = 0.3


# In[4]:


# a가 0.5보다 작으면 0, 0.5보다 크면 1을 출력
if a < 0.5 :
    print(0)
else :
    print(1)


# ### 1-5. 반복문

# In[5]:


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# In[6]:


b = [ ]


# In[7]:


for i in range(10) :
    b.append(i)


# In[8]:


b


# ### 1-6. 자료형

# In[9]:


type(1)


# In[10]:


type(1.2)


# In[11]:


type(1+2j)


# In[12]:


type('setosa')


# In[13]:


type([200, 'setosa', 5.947])


# In[14]:


type((200, 'setosa', 5.947))


# In[15]:


type(True)


# In[16]:


type({200, 'setosa', 5.947})


# In[17]:


type({'name' : 'Jon Snow', 'family' : 'Stark'})


# ---

# ## 2. pandas의 데이터 프레임

# ### 2-1. 데이터 프레임이란? (iris 데이터 셋 불러오기)

# > iris 데이터 셋의 특징
# <div>
# <img src="https://python.astrotech.io/_images/dataset-iris-flowers.png" width="500"/>
# </div>

# >iris 데이터 셋이 데이터 분석 교육용으로 가장 널리 사용되는 이유는 수치형(Numerical) 데이터뿐만 아니라 붓꽃의 종류라는 범주형(Categorical) 데이터까지 존재해 회귀(Regression)와 분류(Classification) 문제 모두를 실습해 볼 수 있기 때문입니다.

# In[18]:


# pandas 패키지 불러오기 및 pd라는 약어로 지칭하기
import pandas as pd  
# sklearn 패키지의 datasets 모듈에서 load_iris 함수 불러오기
from sklearn.datasets import load_iris


# In[19]:


iris = load_iris()  # iris 변수에 iris 데이터셋 입력


# In[20]:


# iris 데이터셋의 독립변수(feature) 이름 및 데이터 출력
print(iris.feature_names)
print(iris.data)


# In[21]:


# iris 데이터셋의 종속변수(target) 이름 및 데이터 출력
print(iris.target_names)
print(iris.target)


# > ※ 함수와 메서드  
# 메서드(method)는 객체(object)에 속하는 함수(function)를 뜻합니다. 
# 예를들어, 아래 사례의 경우 head()를 사용할 때 df 다음에 “.” 점을 찍고 head()를 사용했습니다. 
# df가 객체이기 때문에 이 경우 head()는 메서드라고 부릅니다. 
# 다만, 메서드는 결국 함수의 부분집합이기 때문에 함수라고 불러도 틀린 말은 아닙니다.

# In[22]:


# iris.data 데이터셋 타입 확인
type(iris.data)


# In[23]:


# 다차원배열(ndarray) 타입의 iris.data를 pandas 패키지를 이용해 데이터 프레임으로 변경
df = pd.DataFrame(data = iris.data, columns = iris.feature_names)


# In[24]:


# df 데이터셋에 species 열을 추가하고 iris.target을 추가
df['species'] = iris.target


# In[25]:


# head() 메서드를 이용해 df 데이터셋의 상위 5개 데이터만 출력
df.head(5)


# >※ 데이터프레임 형태의 iris 데이터 셋을 바로 불러오는 방법  
# seaborn 패키지의 load_dataset('iris')를 이용하면 됩니다.  
# (예시)  
# import seaborn as sns  
# iris = sns.load_dataset('iris')  
# iris.head()

# ### 2-2. 데이터 프레임 다루기

# #### ① 열 이름 변경하기

# In[26]:


# df 데이터 셋의 컬럼명 확인
df.columns


# In[27]:


# 컬럼명 변경
df.columns = ['sl','sw','pl','pw','sp']


# In[28]:


df.head(5)


# In[29]:


# 5번째 컬럼명만 sp에서 s로 변경
df.rename(columns = {'sp' : 's'}, inplace = True)


# In[30]:


df.head(5)


# #### ② 특정 데이터만 추출하기

# In[31]:


# df 데이터프레임의 데이터 확인
df.values


# >※ pandas의 속성(attribute)  
# 속성(attribute)은 함수(function)와 변수(variable) 형태로 나뉘며 앞서 설명한 head()의 경우는 함수 형태로 이를 메서드(method)라고 불렀습니다. pandas에서 ()가 붙지 않는 변수 형태의 columns, index, dtypes, values, shape 등은 속성(attribute)이라고 부릅니다.

# In[32]:


# df 데이터프레임의 열 인덱스 확인
df.columns


# In[33]:


# df 데이터프레임의 행 인덱스 확인
df.index


# >※ 인덱싱(indexing), 슬라이싱(slicing)  
# 파이썬에서는 인덱싱과 슬라이싱이라는 용어를 많이 사용합니다. 인덱싱은 개별 요소만 얻고자 할 때, 슬라이싱은 연속적인 요소를 얻고자 할 때 사용합니다. 즉, 슬라이스 기호(:)를 이용해 범위의 개념이 들어가면 슬라이싱인 것입니다. 다만 이 책에서는 인덱싱, 슬라이싱이라는 용어보다는 원하는 데이터만 뽑아서 추출한다는 뜻에서 보다 범용적인 필터링(filtering)이라는 용어를 주로 사용합니다.
# 

# #### ②-1 데이터프레임 행 필터링

# In[34]:


# df 데이터프레임에서 0~3번째 행의 데이터만 불러오기
df[0:4]


# In[35]:


# df 데이터프레임에서 3번째 행의 데이터만 불러오기
df[3:4]


# #### ②-2 데이터프레임 열 필터링

# In[36]:


# df 데이터프레임에서 sl 열의 데이터만 불러오기
df['sl']


# In[37]:


# df 데이터프레임에서 sl, pl, sp 열의 데이터만 불러오기
df[['sl','pl','sp']]


# #### ②-3 데이터프레임 행&열 동시 필터링

# In[38]:


# 3째 행까지 sl, sp 열의 데이터만 불러오기
df[0:4][['sl','sp']]


# #### ②-4 데이터프레임 행&열 동시 필터링(loc)

# In[39]:


# 3째 행까지 sl, s 열의 데이터만 불러오기
df.loc[0:3,('sl','s')]


# #### ②-5 데이터프레임 행&열 동시 필터링(iloc)

# In[40]:


# 3째 행까지 sl, s 열의 데이터만 불러오기
df.iloc[0:4,[0, 4]]


# #### ②-6 데이터프레임 인덱스 활용 4가지 데이터 셋 만들기

# #### Case 1. s가 1인 대상만 추출

# In[41]:


# df 데이터 셋에서 컬럼 s가 1인 대상만 추출해 df_1에 넣음
df_1 = df[df.sp == 1]


# In[42]:


# 데이터프레임의 경우 info() 함수를 이용해 데이터 셋 정보 확인 가능
df_1.info()


# In[43]:


# tail() 함수를 이용하면 끝에서부터 위로 원하는 행만큼 조회 가능
df_1.tail(5)


# #### Case 2. sl이 6보다 크고, s가 1인 대상만 추출

# In[44]:


# df 데이터 셋에서 sl이 6보다 크고, s가 1인 대상만 추출해 df_2에 넣음
df_2 = df[(df.sl > 6) & (df.sp == 1)]


# In[45]:


df_2


# #### Case 3. s가 0인 대상에서 sl, sw, sp 열만 추출

# In[46]:


# df 데이터 셋에서 s가 0인 대상의 sl, sw, sp 열만 추출해 df_3에 넣음
df_3 = df.loc[df.sp == 0, ['sl','sw','sp']]


# In[47]:


df_3.info()


# #### Case 4. s 열만 제외하고 추출

# In[48]:


# df 데이터 셋에서 s 열만 제외하고 추출해 df_4에 넣음
df_4 = df[df.columns.difference(['s'])]


# In[49]:


df_4.head(5)


# ---

# ## 3. numpy의 다차원 배열

# ### 3-1. 다차원 배열이란?

# In[50]:


# numpy 패키지 불러오기 및 np라는 약어로 지칭하기
import numpy as np


# In[51]:


# 스칼라
a0 = np.array(1)
a0


# In[52]:


# 벡터
a1 = np.array([1, 2])
a1


# In[53]:


# 행렬
a2 = np.array([[1, 2],[3, 4]])
a2


# In[54]:


# 텐서
a3 = np.array([[[1, 2, 3],
                [4, 5, 6]],
                [[7, 8, 9],
                [2, 4, 8]]])
a3


# In[55]:


# ndim 속성을 이용해 배열의 차원 확인
print(a0.ndim, a1.ndim, a2.ndim, a3.ndim)


# In[56]:


# shape 속성을 이용해 배열의 크기 확인
print(a0.shape, a1.shape, a2.shape, a3.shape)


# ### 3-2. 다차원 배열 다루기

# In[57]:


# 3차원 배열에서 첫 번째 행렬 필터링
a3[0]


# In[58]:


# 3차원 배열에서 첫 번째 행렬의 두 번째 행 필터링
a3[0, 1]


# In[59]:


# 3차원 배열에서 첫 번째 행렬의 두 번째 행의 3번째 열 필터링
a3[0, 1, 2]


# ---

# ## 4. 데이터 정제

# ### 4-1. 결측치(NaN)

# In[60]:


# pandas 패키지 불러오기 및 pd라는 약어로 지칭하기
import pandas as pd  


# In[61]:


# read_csv() 함수 활용 데이터 셋 불러오기
air = pd.read_csv('./dataset/ch3-1.csv')


# In[62]:


air


# #### ① 결측치 확인하기

# In[63]:


# 결측치 확인하기1
air.info()


# In[64]:


# 결측치 확인하기2
air.isnull()


# In[65]:


# 결측치 확인하기3
air.isnull().sum()


# #### ② 결측치 제거하기

# In[66]:


# 결측치 제거(axis = 0 : 행 제거, axis = 1 : 열 제거)
air_d = air.dropna(axis=0)


# In[67]:


air_d


# #### ③ 결측치 평균값으로 대체하기

# In[68]:


# 결측치 평균대체를 위해 평균 확인
# air.mean()
air.iloc[:, 1:].mean()


# In[69]:


# 평균값으로 결측치 대체
# air_m = air.fillna(air.mean())
air_m = air.fillna(air.iloc[:,1:].mean())


# In[70]:


air_m


# #### ④ 결측치 중앙값으로 대체하기

# In[71]:


# 중앙값 확인
# air.median()
air.iloc[:,1:].median()


# In[72]:


# 중앙값으로 결측치 대체
# air_md = air.fillna(air.median())
air_md = air.fillna(air.iloc[:,1:].median())


# In[73]:


air_md

###############################################################################
# THE END
###############################################################################
