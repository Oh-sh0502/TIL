import operator

n = int(input())
seq = list(map(int, input().split()))
increase = [1] * n
decrease = [1] * n

result = [0] * n
for i in range(n):
    for j in range(i):
        if seq[i] > seq[j] and increase[i] <= increase[j] +1:
            increase[i] = increase[j] + 1
for i in range(n-1, -1, -1):
    for j in range(i, n):
        if seq[i] > seq[j] and decrease[i] <= decrease[j] +1:
            decrease[i] = decrease[j] + 1
    result[i] = increase[i] + decrease[i] -1
print(max(result))




# 더 짧은 풀이
# for i in range(n):
#     for j in range(i):
#         if seq[i] > seq[j] and increase[i] <= increase[j] + 1:
#             increase[i] = increase[j] + 1
# for i in range(n-1, -1, -1):
#     for j in range(i, n):
#         if seq[i] > seq[j] and decrease[i] <= decrease[j] + 1:
#             decrease[i] = decrease[j] + 1
#
# print(max(map(operator.add, increase, decrease))-1)