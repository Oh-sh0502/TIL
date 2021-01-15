import pandas as pd
import matplotlib.pyplot as plt
# 데이터프레임 변환하여 df에 저장
df = pd.read_excel('./남북한발전전력량.xlsx',engine="openpyxl")
print(df)

# 1991년도부터의 남한, 북한 발전량 합계 데이터만 추출
df_ns = df.iloc[[0,5], 3:]
print(df_ns)
# 행 인덱스를 'South'와 'North'로 변경
df_ns.index = ['South','North']

# 열 이름의 자료형을 정수형을 변경
df_ns.columns = df_ns.columns.map(int)
print(df_ns.head())
print('\n')

# 선 그래프 그리기
df_ns.plot()


# 행, 열 전치하여 다시 그리기
tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')
tdf_ns.plot()
plt.show()