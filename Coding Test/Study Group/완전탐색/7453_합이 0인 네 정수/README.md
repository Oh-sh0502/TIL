# # 7453: 합이 0인 네 정수

### 문제

정수로 이루어진 크기가 같은 배열 A, B, C, D가 있다.

A[a], B[b], C[c], D[d]의 합이 0인 (a, b, c, d) 쌍의 개수를 구하는 프로그램을 작성하시오.

---

### 문제풀이

-  아이디어는 생각했으나 코드로 구현하지 못 했다. 다른 분들의 풀이에서 **딕셔너리를 활용**한 것을 보고 내가 아직 자료구조를 잘 사용하지 못한다는 것을 반성하게 됐다.
-   **A&B, C&D 로 그륩을 나누어 각 그륩의 부분합을 구했을 때, T와 -T의 합으로 0이 나오게 하거나, A&B에 T값이 있다면 C&D에는 -T가 있을 때 카운트하여 풀이한다.**
   딕셔너리의 get()함수를 이용하여 `a+b`라는 key 값의 value의 존재여부에 따라 딕셔너리를 만들어나간다. **key값이 존재하지 않으면 key값을 생성하고 value에 1을 준다.** 만약 **존재한다면 기존 값에 1을 더해주면 부분합 종류에 따라 카운트해주는 딕셔너리를 만들 수 있다.** 
- 혹여 `A&B, C&D` 그룹말고 `A&C, B&D` , `A&D, B&C` 그룹들은 왜 안하냐고 생각할 수 있다. 잘 생각해보면 **덧셈의 결합법칙**에 따라 하나의 그룹만 구성해도 된다는 것을 알 수 있다.

```
a+b+c+d
=(a+b)+(c+d)
=(a+c)+(b+d)
=(a+d)+(b+c)
```

- 풀이는 다음과 같다. python3에서는 시간초과가 발생하였으며, pypy3는 통과.

```python
import sys

n = int(sys.stdin.readline())                               # 배열의 크기
A = []; B = []; C = []; D = []                              # 배열 리스트 정의

for i in range(n):
    a,b,c,d = map(int, sys.stdin.readline().split())           
    A.append(a); B.append(b); C.append(c); D.append(d)      # A, B, C, D 배열 완성

ab, cd = {},{}                                              # A&B, C&D 딕셔너리 생성
result = 0                                                  # 카운트

for a in A:
    for b in B:
        if a+b not in ab:                                   # a+b가 딕셔너리에 없다면
            ab[a+b] = 1                                     # a+b: 1 생성
        else:                                               # 있으면
            ab[a+b] += 1                                    # key가 a+b인 value에 +1
            
for c in C:                                                 
    for d in D:                                             
        temp = -(c+d)                                       # -(c+d)값을 정의
        if temp in ab:                                      # -(c+d)값이 ab 딕셔너리의 key 중에 있으면
            result += ab[temp]                              # value 값만큼 카운트에 더해준다.

print(result)                                               # 출력
```

---

### 결과

![image-20210211232226872](C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210211232226872.png)

---

### Reference

- 풀이1: https://suri78.tistory.com/169
- 풀이2: https://richard25.tistory.com/41

- 딕셔너리: https://wikidocs.net/16

  

