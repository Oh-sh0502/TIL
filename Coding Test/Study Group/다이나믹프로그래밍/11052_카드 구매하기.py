n = int(input())

p =[0] + list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = p[1]
for i in range(2, n+1):
    for j in range(1,i):
        if i-j >= j:                                    # 중복은 회피
            dp[i] = max(dp[i-j] + dp[j], dp[i])    # 점화식 ex) dp[5] = max(dp[4]-dp[1], dp[3]-dp[2], [중복]dp[2]-dp[3])
    dp[i] = max(dp[i],p[i])                        # dp[5] = max(dp[5], p[5])
print(dp[n])