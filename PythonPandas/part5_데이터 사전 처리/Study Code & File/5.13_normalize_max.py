# 라이브러리
import pandas as pd
import numpy as np

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header =None)

# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year','origin','name']

# horsepower 열의 누락 데이터('?')를 삭제하고 실수형으로 변환
df['horsepower'].replace('?', np.nan, inplace=True)
df.dropna(subset='horsepower', axis=0, inplace=True)
df['horsepower'] = df['horsepower'].astype('float')

# horsepower 열의 통계 용약 정보로 최대값(max)확인
print(df.horsepower.describe())
print("\n")

# horsepower 열의 최댓값의 절대값으로 모든 데이터를 나눠서 저장
df.horsepower = df.horsepower/abs(df.horsepower.max())
print(df.horsepower.head())
print('\n')
print(df.horsepower.describe())
