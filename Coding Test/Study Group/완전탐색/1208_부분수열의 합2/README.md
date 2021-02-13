# # 1208: 부분수열의 합2

### 문제

N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

(1 ≤ N ≤ 40, |S| ≤ 1,000,000)

---

### 문제풀이

- 

```python
import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

left = numbers[:n//2]                                   # 왼쪽
right = numbers[n//2:]                                  # 오른쪽
ls = []
rs = []
for i in range(len(left)+1):                         # 왼쪽
    a = list(combinations(left,i))                          # 콤비네이션으로 부분수열 뽑기
    for j in a:                                             # 부분수열을 순서대로
        ls.append(sum(j))                                       # 합을 뽑아서 ls에 저장
for i in range(len(right)+1):                         # 오른쪽
    b = list(combinations(right,i))                         # 콤비네이션으로 부분수열 뽑기
    for j in b:                                             # 부분수열을 순서대로
        rs.append(sum(j))                                       # 합을 뽑아서 rs에 저장

ls.sort()                                               # 왼쪽은 오름차순
rs.sort(reverse=True)                                   # 오른쪽은 내림차순

cnt = 0
i = 0                                                   # left의 끝점
j = 0                                                   # right의 끝점
result = 0
# print("ls 길이: ", len(ls))
# print("rs 길이: ", len(rs))
while i < len(ls) and j < len(rs):                      # i와 j가 모두 끝에 도달할 때까지 돌린다.
    if ls[i] + rs[j] == s:                                  # 왼쪽 오른쪽 부분합의 합이 s인 경우
        c1 = 1                                                  # left 쪽 카운트 +1
        c2 = 1                                                  # right 쪽 카운트 +1
        i += 1                                                  # left의 끝점 +1
        j += 1                                                  # right의 끝점 +1
        while i < len(ls) and ls[i] == ls[i-1]:                 # left 끝점이 끝까지 도달하지 않거나 이전값과 다음값이 같지 않으면
            c1 += 1                                                 # left 카운트 +1
            i += 1                                                   # left의 끝점 +1
        while j < len(rs) and rs[j] == rs[j-1]:                 # right 끝점이 끝까지 도달하지 않거나 이전값과 다음값이 같지 않으면
            c2 += 1                                                 # right 카운트 +1
            j += 1                                                  # right 끝점 +1
        result += c1 * c2                                       # 최종 카운트에 left와 right 카운트의 곱을 더한다.

    elif ls[i] + rs[j] < s:                                 # 부분합들의 합이 s에 미치지 못하면
        i += 1                                                  # left의 끝점이 하나 증가
    else:                                                   # 부분합들의 합이 s보다 크다면
        j += 1                                                  # right의 끝점이 하나 증가
if s == 0:
    result -= 1

print(result)
```



---

### 결과



---

### Reference

- 비트연산자 `<<`: https://soyoja.com/263
- 다른 사람 풀이: https://peisea0830.tistory.com/40
- 메모리제한에 관하여: https://blogyong.tistory.com/14

 

