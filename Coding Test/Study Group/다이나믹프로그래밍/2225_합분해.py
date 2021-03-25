n, k = map(int, input().split())

dp = []
dp.append(list(range(1,k+1)))
for i in range(n-1):
    dp.append([1] * k)
for i in range(1,n):
    for j in range(1,k):
        dp[i][j] = dp[i][j-1] + dp[i-1][j]

print(dp[n-1][k-1] % 1000000000)