# #6603: 로또

### 문제

독일 로또는 {1, 2, ..., 49}에서 수 6개를 고른다.

로또 번호를 선택하는데 사용되는 가장 유명한 전략은 49가지 수 중 k(k>6)개의 수를 골라 집합 S를 만든 다음 그 수만 가지고 번호를 선택하는 것이다.

예를 들어, k=8, S={1,2,3,5,8,13,21,34}인 경우 이 집합 S에서 수를 고를 수 있는 경우의 수는 총 28가지이다. ([1,2,3,5,8,13], [1,2,3,5,8,21], [1,2,3,5,8,34], [1,2,3,5,13,21], ..., [3,5,8,13,21,34])

집합 S와 k가 주어졌을 때, 수를 고르는 모든 방법을 구하는 프로그램을 작성하시오.

---

### 문제풀이

- 파이썬은 itertools 모듈 안에 있는 combinations 함수를 사용하여 문제를 해결할 수 있다. **combinations(n, m)** 함수는 **n개 중 m개를 뽑았을 때의 경우의 수**를 알려준다. 이 문제에서는 6개의 수를 뽑으므로 combinations(n , 6) 으로 경우를 뽑아낼 수 있다.
-  처음 입력한 데이터를 리스트로 저장한다. **첫번째 원소는 원소의 개수**로 따로 변수에 저장한다. **첫 번째 원소를 제외한 나머지 원소들을 따로 리스트에 저장하여 로또 번호 리스트를 구성한다.** 
   이후에 combinations 함수를 사용하면 k개의 수 중 6개를 뽑아 손쉽게 모든 경우의 수를 뽑아준다. 차례대로 출력해주면 끝.

```python
import sys
from itertools import combinations
while True:
    lotto = list(map(int, sys.stdin.readline().split()))
    a = lotto[0]
    b = list(lotto[1:len(lotto)])
    b = list(combinations(b, 6))
    for i in b:
        for j in range(6):
            print(i[j], end=' ')
        print()
    print()
    if lotto[0] == 0:
        break
```

---

### 결과

![image-20210206235835217](C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210206235835217.png)

---

### Reference

- from 모듈 import 변수: https://dojang.io/mod/page/view.php?id=2441
- itertools & combinations:  https://itholic.github.io/python-combination-permutation/

