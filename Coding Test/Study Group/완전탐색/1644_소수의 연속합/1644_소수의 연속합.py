import sys
n = int(sys.stdin.readline().rstrip())
a = [False,False] + [True]*(n-1)
primes=[]

# 에라토스테네스의 체
for i in range(2,n+1):                  # 2부터 n까지의 수를
  if a[i]:                              # a의 원소가 True이면
    primes.append(i)                    # primes 리스트에 i를 append
    for j in range(2*i, n+1, i):        # i의 배수 값을 가진 모든 인덱스에 대하여
        a[j] = False                    # a 리스트에 False 처리. 연산 수가 기하급수적으로 줄어든다.

cnt = 0                                 # 카운트
sum = 0                                 # 부분합
end = 0                                 # 끝점

# 투 포인터 알고리즘
for start in range(len(primes)):        
    while sum < n and end < len(primes):
        sum += primes[end]
        end += 1
    if sum == n:                        # 부분합이 n일 시
        cnt += 1                        # 카운트 +1
    sum -= primes[start]

print(cnt)