# 라이브러리
import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

# 각 열의 자료형 확인
print(df.dtypes)
print('\n')

# housepower 열의 고유값 확인
print(df['horsepower'].unique())
print('\n')

# 누락 데이터('?') 삭제
import numpy as np
df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset=['horsepower'], axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')
print(df['horsepower'].dtypes)

# origin 열의 고유값 확인
print(df['origin'].unique())

# 정수형 데이터를 문자열 데이터로 변환
df['origin'].replace({1:'USA',2:'EU',3:'JPN'}, inplace=True)

# origin 열의 고유값과 자료형 확인
print(df['origin'].unique())
print(df['origin'].dtypes)

# 문자열을 범주형으로 변환
df['origin'] = df['origin'].astype('category')
print(df['origin'].dtypes)

# 범주형을 문자열로 다시 변환
df['origin'] = df['origin'].astype('str')
print(df['origin'].dtypes)

# model year 열의 정수형을 범주형으로 변환
print(df['model year'].sample(3))
df['model year'] = df['model year'].astype('category')
print(df['model year'].sample(3))