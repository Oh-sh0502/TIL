# 내 풀이
n, k = map(int,input().split())
print(n, k)
cnt = 0
while True:
    if n % k == 0:
       cnt += 1
       n //= k
    else:
        cnt += 1
        n -= 1
    if n == 1:
        print(cnt)
        break

# 그리디 사용의 정당성 분석
# - 가능하면 최대한 많이 나누는 작업이 최적의 해를 항상 보장할 수 있을까?
#   N이 아무리 큰 수여도, K로 계속 나눈다면 기하급수적으로 빠르게 줄일 수 있다
#   즉, k가 2 이상이기만 하면, K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N을 줄일 수 있고,
#   N은 항상 1에 도달하게 된다.(최적의 해 성립)

# 동빈나 풀이 (이 풀이로 하면 시간복잡도가 logN 이 나온다고 함)
n,k = map(int, input().split())

result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n//k) * k
    result = (n - target)       # 이때 result는 나머지라 볼 수 있다.
    n = target

    # N이 K보다 적을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)