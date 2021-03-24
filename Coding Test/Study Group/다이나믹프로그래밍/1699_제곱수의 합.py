# 내 풀이: 재귀함수를 사용함. 그러나 메모리 초과가 뜸
# import math
# import sys
# sys.setrecursionlimit(1000001)
# n = int(input())
# n_root = math.floor(math.sqrt(n))
# cnt = 0
# def substraction(number,number_root,cnt):
#     if number == 1:
#         return cnt
#     number -= (number_root ** 2)
#     next_root = math.floor(math.sqrt(number))
#     cnt += 1
#     cnt = substraction(number, next_root, cnt)
#     return cnt
#
# print(substraction(n,n_root,cnt)+1)

n = int(input())
dp = [0] * (n+1)
sqare = [i*i for i in range(1,317)]
for i in range(1, n+1):
    s = []
    for j in sqare:
        if j > i:
            break
        s. append(dp[i-j])
    dp[i] = min(s) + 1
print(dp[n])