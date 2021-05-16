## 프로그래머스_Summer/Winter Coding: 소수 만들기

- '`Combinations` 모듈을 써도 될까? '라는 궁금증을 먼저 해결했다.

  -> `nums`의 원소의 개수는 최대 50개로 <sub>50</sub>C<sub>3</sub> = 19600 개로 이중 for문만 아니면 괜찮겠다는 판단을 내렸다.

- `is_prime` 함수로 소수를 판별한다. for문을 제곱근까지만 돌리는 것으로 연산횟수를 줄였다.
  웬만하면 손에 익히자!

```python
import math
from itertools import combinations

def solution(nums):
    answer = 0
    for i in list(combinations(nums,3)):
        if is_prime(sum(i)):
            answer += 1


    return answer

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
```

<br>

<결과>

![소수만들기](https://user-images.githubusercontent.com/71415474/118397886-16904980-b691-11eb-8f75-37215329d5b0.PNG)

<br>

---

