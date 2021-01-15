import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv')
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

# 데이터프레임 df의 각 열이 가지고 있는 원소 개수 확인
print(df.count())
print('\n')

# df.count() 가 반환하는 객체 타입 출력
print(type(df.count()))
print('\n')

# 데이터프레임 df의 특정 열이 가지고 있는 고유값 확인
unique_value = df['origin'].value_counts()
print(unique_value)
print('\n')

# value_counts 메소드가 반환하는 객체 타입 출력
print(type(df['origin'].value_counts()))
