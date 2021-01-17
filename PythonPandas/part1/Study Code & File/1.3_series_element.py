import pandas as pd

# 투플을 시리즈로 변환 (인덱스 옵션 저장)
tup_data = ('영인', '2010-05-01', '여', True)
sr = pd.Series(tup_data, index=['이름','생년월일','성별','학생여부'])
print(sr)

# 원소를 1개 선택
print(sr[0])
print(sr['이름'])

# 여러 개의 원소를 선택(인덱스 리스트 활용)
print(sr[[1,2]])
print('\n')
print(sr[['생년월일','성별']])
# 둘의 차이를 알아보자
print(sr[1])                    # sr[1]은 데이터 값을 출력
print(sr[[1]])                  # sr[[1]]은 1행의 원소들을 출력

# 여러개의 원소를 선택(인덱스 범위 지정)
print(sr[1:2])
print('\n')
print(sr['생년월일':'성별'])