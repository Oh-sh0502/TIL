# 라이브러리 불러오기
import pandas as pd
import matplotlib.pyplot as plt

# matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = "./malgun.ttf"  # 폰트 파일 위치
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


# Excel 데이터를 데이터프레임으로 변환
df = pd.read_excel('시도별 전출입 인구수.xlsx', header = 0)

# 누락값(NaN)을 앞 데이터로 채움(엑셀 양식 병합 부분)
df = df.fillna(method='ffill')
print(df)
# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
print(mask)
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)                          # '전출지별' 열 삭제
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)             # inplace=True로 원본객체 변경
df_seoul.set_index('전입지',inplace=True)
print(df_seoul.head(8))
# 서울에서 경기도로 이동한 인구 데이터 값만 선택
sr_one = df_seoul.loc['경기도']
print(sr_one)

# 스타일 서식 지정
plt.style.use('seaborn-darkgrid')

# 그림 사이즈 지정
plt.figure(figsize=(14,5))

# x축 눈금 라벨 회전
plt.xticks(size=10, rotation='vertical')

# x, y축 데이터를 plot 함수에 입력
plt.plot(sr_one.index, sr_one.values, marker='o', markersize=10)

plt.title('서울 -> 경기 인구 이동', size=30)
plt.xlabel('기간', size=20)
plt.ylabel('이동 인구 수', size=20)

plt.legend(labels=['서울 -> 경기'], loc = 'best', fontsize=15)      # 범례 표시
plt.show()