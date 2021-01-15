import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)
print(df.head())

# 열 이름 지정
df. columns = ['mpg',
               'cylinders',
               'displacement',
               'horsepower',
               'weight',
               'acceleration',
               'model_year',
               'origin',
               'name'
               ]

# 평균갑
print(df.mean())
print('\n')
# 'mpg' 열 평균값
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
# 'mpg', 'weight' 열 평균값
print(df[['mpg','weight']].mean())
print('\n')
# 중간값
print(df.median())
print('\n')
# 'mpg' 열 중간값
print(df.mpg.median())
print(df['mpg'].median())
print(df[['mpg']].median())
print('\n')
# 최댓값
print(df.max())
print('\n')
# 'mpg' 열 최댓값
print(df.mpg.max())
print(df['mpg'].max())
print(df[['mpg']].max())
print('\n')
# 최솟값
print(df.min())
print('\n')
# 'mpg' 열 최솟값
print(df.mpg.min())
print(df['mpg'].min())
print(df[['mpg']].min())

# 표준편차
print(df.std())
print('\n')
# 'mpg' 열 표준편차
print(df.mpg.std())
print(df['mpg'].std())
print(df[['mpg']].std())
# 상관계수
print(df.corr())
print('\n')
# 'mpg'와 'weight'의 상관계수
print(df[['mpg','weight']].corr())