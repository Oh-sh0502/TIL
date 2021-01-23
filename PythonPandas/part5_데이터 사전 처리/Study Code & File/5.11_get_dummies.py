# 라이브러리
import pandas as pd
import numpy as np

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header = None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

# horsepower 열의 누락 데이터('?')를 삭제하고 실수형으로 변환
df['horsepower'].replace('?',np.nan,inplace=True)
df.dropna(subset=['horsepower'], axis=0 ,inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

# np.histogram 함수로 3개의 bin으로 구분할 경계값의 리스트 구하기
count, bin_dividers = np.histogram(df['horsepower'], bins=3)

# 3개의 bin에 이름 지정
bin_names = ['저출력','보통출력','고출력']

# pd.cut 함수로 각 데이터를 3개의 bin에 할당
df['hp_bin'] = pd.cut(x=df['horsepower'],
                      labels=bin_names,
                      bins=bin_dividers,
                      include_lowest=True)

# hp_bin 열의 범주형 데이터를 더미 변수로 변환
horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(15))
