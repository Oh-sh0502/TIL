n = int(input())
seq = list(map(int, input().split()))

# d = []
# d.append([seq[0]])
# if n > 1:
#     for i in range(1,n):
#         d.append([seq[i]])
#         length = 1
#         for j in range(i):
#             if d[j][-1] > seq[i] and length < len(d[j] + [seq[i]]):
#                 d[i] = d[j] + [seq[i]]
#                 length = len(d[j]) + 1
# result = 0
# for i in d:
#     if result < len(i):
#         result = len(i)
# print(result)

# 고찰해야할 사항
# d의 리스트원소 중 리스트의 길이가 같은게 있을 수 있다.
# 이게 왜 문제냐면 길이가 같은 두 리스트에 다음 원소를 추가하면 길이가 최대인 리스트가 2개 이상이 되기 때문
# 지금 다른 풀이들을 보면 애초에 길이로 접근해서 푸는 문제들이 있음. 즉 원소 구성원이랑 길이랑 독립적이라는 것
# 길이로도 풀어봐야겠따....

decrease = [1] * n

for i in range(n-1, -1, -1):
    for j in range(i,n):
        if seq[i] > seq[j] and decrease[i] <= decrease[j] + 1:
            decrease[i] = decrease[j] + 1
print(max(decrease))
