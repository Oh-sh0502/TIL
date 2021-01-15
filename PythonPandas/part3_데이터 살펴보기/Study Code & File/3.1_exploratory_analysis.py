import pandas as pd

# read_csv() 함수로 df 생성
df = pd.read_csv("./auto-mpg.csv", header = None)

# 열 이름 저장
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

# 데이터프레임 df의 내용을 일부확인
print(df.head())
print('\n')
print(df.tail())
print('\n')
# 데이터프레임 df의 크기 확인: (행의 개수, 열의 개수)를 튜플로 반환
print(df.shape)
print('\n')
# 데이터프레임 df의 내용 확인
print(df.info())
print('\n')
# 데이터프레임 df의 자료형 ㅗ학인
print(df.dtypes)
print('\n')
# 시리즈(mpg 열)의 자료형 확인
print(df.mpg.dtype)
print('\n')
# 데이터프레임 df의 기술 통계 정보 확인
print(df.describe())
print('\n')
print(df.describe(include='all'))