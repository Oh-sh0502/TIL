## 프로그래머스_DP: N으로 표현

#### 문제풀이

5를 1번 사용해서 만들 수 있는 수

```
5
```

5를 2번 사용해서 만들 수 있는 수

```
 55										5를 이어붙여서 만듬
 10(5+5), 0(5-5), 25(5*5), 1(5/5)		1번 사용한 경우를 사칙연산으로 구한 결과들
```

5를 3번 사용해서 만들 수 있는 수

```
555
A1 +-*/ A2
A2 +-*/ A1
```

5를 4번 사용해서 만들 수 있는 수

```
5555
A1 +-*/ A3
A2 +-*/ A2
A3 +-*/ A1
```

5를 n번 사용해서 만들 수 있는 수

```
5555555...5			(5가 n개)
A1 +-*/ An-1
A2 +-*/ An-2
.
.
.
An-1 +-*/ A1
```



<풀이>

- 숫자를 이어붙이는 방법 -> string으로 바꿔서 이어붙인다.
- 4중 for문
  - for i in range(1, 9) -> 9부터 가능하다. 즉, 이 문제는 무조건 9개 이하로 모든 수를 표현할 수 있다.
    - for j in range(0, i-1) -> dp[n] 을 구하려면 dp[1]~dp[n-1] 을 사용해야하므로 0부터 i-2까지 주었다.
      - for x in DP[j], for y in DP[-j-1] -> 인덱스를 더 했을 때 마지막 인덱스(-1)가 나오게 하면 된다. y의 for문을 거꾸로 돌릴 수도 있으나 증가하는 방향으로 한 게 매력적이다
- 찾으려는 값 number가 numbers 리스트에 있다면 추가해버리고 끝.



```python
def solution(N, number):
    answer = -1
    DP = []

    for i in range(1, 9):
        numbers = set()
        numbers.add( int(str(N) * i) )
        
        for j in range(0, i-1):
            for x in DP[j]:
                for y in DP[-j-1]:
                    numbers.add(x + y)
                    numbers.add(x - y)
                    numbers.add(x * y)
                    
                    if y != 0:
                        numbers.add(x // y)

        if number in numbers:
            answer = i
            break
        
        DP.append(numbers)

    return answer
```

---

#### 결과

![N으로표현](https://user-images.githubusercontent.com/71415474/117600174-6c8f5980-b186-11eb-8f76-936583b3c774.PNG)

---

#### Reference

- https://gurumee92.tistory.com/164