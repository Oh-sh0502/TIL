number = input()
n = len(number)

digit = [0]+list(map(int,number))
if digit[1] == 0:
    print(0)
else:
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        if digit[i] == 0:
            if 10 * digit[i-1] + digit[i] <= 26:
                dp[i] = dp[i-2]
                if digit[i-1] == 0:
                    dp[n] = 0
                    break
            else:
                dp[n] = 0
                break
        else:
            if 10 * digit[i-1] + digit[i] <= 26:
                dp[i] = dp[i-1] + dp[i-2]
                if digit[i-1] == 0:
                    dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1]
    print(dp[n]%1000000)