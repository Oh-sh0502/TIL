import pandas as pd

# read_excel() 함수로 데이터프레임 변환
df1 = pd.read_excel('./남북한발전전력량.xlsx')
df2 = pd.read_excel('./남북한발전전력량.xlsx', header=None)

# 데이터 프레임 출력
print(df1)
print('\n')
print(df2)