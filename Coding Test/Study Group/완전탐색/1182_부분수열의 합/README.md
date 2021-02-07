# #1182: 부분수열의 합

### 문제

N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.

---

### 문제풀이

- 파이썬에서 itertools 모듈의 combinations() 함수를 통해 해결할 수 있다. for문과 combinations() 함수를 연계하여 원소의 개수가 1개인 부분수열부터 n개인 부분수열까지 리스트에 담았다. 그리고 sum() 함수를 사용하여 부분수열 원소의 합이 S인 수열을 발견하여 카운트하였다..

``` python
import sys
from itertools import combinations

# 입력
a = list(map(int, sys.stdin.readline().split()))
n = a[0]        # 정수의 개수
s = a[1]        # 원소의 합

seq = list(map(int,sys.stdin.readline().split()))
cnt = 0
for i in range(1,(n+1)):
    p = list(combinations(seq, i))      # 원소의 개수가 i인 부분수열 리스트를 p에 저장
    for j in p:                         # j는 p 안에 부분수열들 중 하나
        if sum(j) == s:                 # 부분수열의 합이 s인지 확인
            cnt +=1                     # 맞다면 카운트한다.

print(cnt)                              # 개수 출력


```



- 풀이는 이중 for문을 사용하여 시간복잡도 O(N<sup>2</sup>)를 가진다. **투 포인터**는 사용할 수 없다. **투 포인터는 연속된 수들의 합을 다룰 때 사용된다.** 만약 투포인터를 쓴다면, 입력한 수열의 순서를 바꿔가며 투 포인터를 사용하는 것이 방법이 될 수 있겠으나, 중복 카운트가 염려된다. 따라서 combinations() 함수에 감사하자.

<img src="C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210207211359071.png" alt="image-20210207211359071" style="zoom:50%;" />

---

### 결과

![image-20210207211524756](C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210207211524756.png)

---

### Reference

- None