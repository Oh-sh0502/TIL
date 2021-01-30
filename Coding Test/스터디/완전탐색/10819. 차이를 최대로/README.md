# 10819. 차이를 최대로

> ### 문제

N개의 정수로 이루어진 배열 A가 주어진다. 이때, 배열에 들어있는 정수의 순서를 적절히 바꿔서 다음 식의 최댓값을 구하는 프로그램을 작성하시오.

|A[0] - A[1]| + |A[1] - A[2]| + ... + |A[N-2] - A[N-1]|

---

> ### 풀이

- 순열을 이용
- 처음엔 20 1 15 4  10 8 처럼 큰짝큰짝 인줄 알았으나, 이렇게 계산하면 52가 나옴
- 모든 경우를 돌려보고 최댓값을 산출

- 코드

``` python
from itertools import permutations

n = int(input())
a = list(map(int,input().split()))
# 경우의 수를 산출
p = list(permutations(a,n)) 
r = 0                               # 결과물 = 가장 큰 수

for i in p:
    s=0                             # 합
    li = list(i)                    # 경우 (ex. 20 1 15 4  10 8 )
    for j in range(1,n):
        s += abs(li[j-1]-li[j])		# 
    r = max(r,s)

print(r)
```

---

