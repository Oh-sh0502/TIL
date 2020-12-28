import pandas as pd

# 리스트(list_data=['2019-01-02', 3.14, 'ABC', 100, True])를 시리즈로 변환하여 변수 sr에 저장
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr = pd.Series(list_data)
# sr 객체 출력
print(sr)

# 인덱스 배열은 변수 idx에 저장. 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values
# idx 출력
print(idx)
print('\n')
# val 출력
print(val)