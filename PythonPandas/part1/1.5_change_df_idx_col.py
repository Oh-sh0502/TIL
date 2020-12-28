import pandas as pd

# 행 인덱스/열 이름 지정하여 데이터프레임 만들기. 안에 리스트들은 행벡터로 나열된다.
df = pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
                  index=['준서','예은'],
                  columns=['나이','성별','학교'])

# 행 인덱스, 열 이름 확인하기
print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)

# 행 인덱스, 열 이름 변경하기
df.index=['학생1','학생2']
df.columns=['연령','남녀','소속']
# 행 인덱스, 열 이름 확인하기
print(df)
print('\n')
print(df.index)
print('\n')
print(df.columns)

