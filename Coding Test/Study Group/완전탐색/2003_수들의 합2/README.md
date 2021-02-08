# #2003: 수들의 합2

### 문제

N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

---

### 문제 풀이

- **완전탐색으로 풀이**하였다. 완전탐색 시 발생하는 탐색 수는 **n(n+1)/2**이다. 1 ≤ N ≤ 10,000 이므로 문제에서는 총 50005000번이다. **1초에 1억번의 연산이므로 완전탐색시 무조건 0.5초 이상으로 시간초과가 예상되었다.** 코드 실행 결과, python3에서는 시간초과가 떴으나, pypy3에서는 통과되었다.

<img src="C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210205113325866.png" alt="image-20210205113325866" style="zoom: 50%;" />

``` python
# 입력
n, m = map(int,input().split())
a = list(map(int, input().split()))

cnt = 0							# 부분합이 M인 경우 카운트
sum = 0							# 부분합
for i in range(n):
    sum += a[i]					# 시작점(i)을 먼저 sum에 더해준다.
    if sum == m:				# 단일 원소 자체가 부분합일 수 있다.
        cnt += 1				# 그렇다면 카운트 +1
    for j in range(i+1,n):		# 그렇지 않다면 
        sum += a[j]				# i+1번째 원소부터 부분합이 M이 될때 까지 더한다.
        if sum == m:			# 발견하면
            cnt += 1			# 카운트 +1
    sum = 0						# 시작점이 i인 루프가 완료되면 sum을 초기화
print(cnt)

```



- 이 문제의 시간복잡도는 O(N<sup>2</sup>)이다. 이를 O(N)으로 풀 수 있는 방법은 바로 **투포인터 알고리즘**이다. 2개의 점의 위치를 기록하면서 리스트 안의 원소에 접근하는 방법이다. 위의 문제의 경우, 부분합이 M인 조건을 만족시키는 기준으로 완전탐색을 하면 다음과 같다.

<img src="C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210205120000040.png" alt="image-20210205120000040" style="zoom:50%;" />

```python
# 입력
n, m = map(int,input().split())
a = list(map(int, input().split()))

cnt = 0
sum = 0
end = 0
# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동
    while sum < m and end < n:
        sum += a[end]
        end +=1
    # 부분합이 m일 때 카운트 증가
    if sum == m:
        cnt += 1
    sum -= a[start]
print(cnt)
```



---

### 결과

![image-20210205121253697](C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210205121253697.png)

---

### Reference

- 동빈나 이코테 39강. 투포인터: https://www.youtube.com/watch?v=ttLRltNDiCo&feature=emb_title

