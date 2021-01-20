# 라이브러리
import seaborn as sns

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')
# age 열의 첫 10개의 데이터 출력(5행에 NaN 값)
print(df['age'].head(10))
print('\n')

# age 열의 NaN 값을 다른 나이 데이터의 평균으로 변경하기
mean_age = df['age'].mean(axis=0)
print(mean_age)
df['age'].fillna(mean_age, inplace=True)

# age 열의 첫 10개 데이터 출력(5행에 NaN 값이 평균으로 대체)
print(df['age'].head(10))