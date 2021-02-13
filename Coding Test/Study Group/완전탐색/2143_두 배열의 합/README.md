# # 2143: 배열의 합

### 문제

한 배열 A[1], A[2], …, A[n]에 대해서, 부 배열은 A[i], A[i+1], …, A[j-1], A[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다. 이러한 부 배열의 합은 A[i]+…+A[j]를 의미한다. 각 원소가 정수인 두 배열 A[1], …, A[n]과 B[1], …, B[m]이 주어졌을 때, A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.

예를 들어 A = {1, 3, 1, 2}, B = {1, 3, 2}, T=5인 경우, 부 배열 쌍의 개수는 다음의 7가지 경우가 있다.

```
T(=5) = A[1] + B[1] + B[2]
      = A[1] + A[2] + B[1]
      = A[2] + B[3]
      = A[2] + A[3] + B[1]
      = A[3] + B[1] + B[2]
      = A[3] + A[4] + B[3]
      = A[4] + B[2] 
```

---

### 문제풀이

-  **딕셔너리를 이용하여 완전탐색을 구성할 수 있다는 것이 포인트.** 부분합으로 나올 수 있는 결과들을 key로 하고 이를 카운트하여 value값에 넣는다. 즉, {부분합: 개수, 부분합: 개수, ...} 형식의 딕셔너리를 만드는 것이다.
   **딕셔너리를 이용한 완전탐색은 코드구성만 잘 한다면 연속적인 부분합과 부분수열과 같은 불연속적 부분합에서도 사용이 가능하다.** 딕셔너리로 "부분합: 개수" 폼을 구성할 수 있다는 것!

```python
import sys

t = int(sys.stdin.readline().rstrip())

n = int(sys.stdin.readline().rstrip())
alist = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline().rstrip())
blist = list(map(int, sys.stdin.readline().split()))

acm, bcm = {}, {}
for i in range(n):				# 시작점
    asum = 0
    for j in range(i,n):		# 끝점
        asum += alist[j]
        if acm.get(asum):
            acm[asum] += 1
        else:
            acm[asum] = 1

for i in range(m):
    bsum = 0
    for j in range(i,m):
        bsum += blist[j]
        if bcm.get(bsum):
            bcm[bsum] += 1
        else:
            bcm[bsum] = 1

cnt = 0
for key in acm:
    if bcm.get(t-key):
      cnt += acm[key]*bcm[t-key]

print(cnt)
```



---

### 결과

![image-20210212014651254](C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210212014651254.png)

---

### Reference

- 다른 사람 풀이: https://suri78.tistory.com/171

