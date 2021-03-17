# 부르트한 풀이
# from itertools import combinations
#
# n = int(input())
# seq = list(map(int, input().split()))
# d= []
# for i in range(1, n+1):
#     partial = list(combinations(seq,i))
#     # print(i,"번째: ", partial)
#     for j in range(len(partial)):
#         cnt = 0
#         for k in range(1, i):
#             if partial[j][k] > partial[j][k-1]:
#                 cnt +=1
#         if cnt == i-1:
#             d.append(i)
# print(d[len(d)-1])

# dp 풀이
# 입력
# n = int(input())                                    # 전체 수열의 길이
# seq = list(map(int, input().split()))           # 수열
#
#
# dp = [0 for i in range(n)]                          # i번째의 최대 수열 길이를 대변하는 dp테이블
# print("dp[0] = 1")
# for i in range(n):
#     for j in range(i):
#         if seq[i] > seq[j] and dp[i] < dp[j]:       # i번째 원소(i번째까지의 맨 뒤 원소)가 j(0 ~ i-1)번째 원소보다 큰데 최대수열 길이는 작았다면
#             print(i,"번째 원소",seq[i],"이 ",j,"번째 원소 ", seq[j],"보다 크고, ", i,"번째까지 나온 최대길이 ",dp[i],"가 ", j,"번째까지에서 부분수열 최대길이 ", dp[j],"보다 작을 때")
#             dp[i] = dp[j]                           # i번째까지의 수열 최대 길이를 j번째까지로 갱신. 즉, 이전 dp값 중에서 가장 최대 길이를 산출
#             print("dp[",i,"]을/를 ",dp[j],"로 갱신합니다",dp)
#         else:
#             print("i = ",i,", j = ",j,"는 넘어갔습니다.")
#     dp[i] += 1                                      # 거기에 +1. 이전단계에서 가장 긴 부분수열에 1을 추가
#     print("dp[",i,"]에 1을 더합니다. dp = ",dp)
# print(max(dp))


# 더 짧은 풀이
n = int(input())
seq = list(map(int, input().split()))

inc = [1] * n

for i in range(n):
    for j in range(i):
        if seq[j] < seq[i] and inc[i] <= inc[j] + 1:
            inc[i] = inc[j] + 1
print(max(inc))

