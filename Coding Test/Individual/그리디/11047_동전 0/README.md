# # 11047: 동전 0

### 문제

준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

---

### 문제풀이

- ** 그리디 알고리즘**을 이용하여 해결한다. **동전의 단위가 가치의 합 K보다 작으면서, 그 중 가장 큰 동전 단위부터 나눠주면 최소 동전 개수를 구할 수 있다.**

-  for문을 사용하여 큰 동전 단위부터 나누기 위해 리스트의 **sort함수와 옵션 reverse=True를 사용**하여 **리스트를 내림차순으로 변경**하였다.
- 가치의 합 K보다 큰 동전 단위는 **pass 를 이용하여 점프**해주면서 그리디 알고리즘을 이용하면 풀 수 있다.

```python
n, k = map(int,input().split())

# 코인 리스트 담기
coin = []
for _ in range(n):
    coin.append(int(input()))

# 내림차순으로 변경
coin.sort(reverse=True)
cnt = 0                     # 카운트
for i in range(len(coin)):
    if i > k:               # 남은 가치보다 동전단위가 크면 사용 못하므로 패스
        pass

    cnt += k//coin[i]       # 몫은 곧 카운트
    k = k % coin[i]         # 나머지는 곧 남은 가치

print(cnt)                  # 카운트 출력
```

---

### 결과

![image-20210210001743773](C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210210001743773.png)

---

### Reference

- None