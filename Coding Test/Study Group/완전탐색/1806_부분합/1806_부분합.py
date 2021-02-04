
n, s = map(int, input().split())

seq = list(map(int, input().split()))

# cnt = 0
# sum = 0
# cntlist = []
#
# for i in range(n):
#     sum += seq[i]
#     cnt += 1
#     if sum == s:
#         cntlist.append(cnt)
#     for j in range(i+1,n):
#         sum += seq[j]
#         cnt += 1
#         if sum == s:
#             cntlist.append(cnt)
#     sum = 0
#     cnt = 0
#
# print(min(cntlist))
# 시간 초과가 뜬다 ....

sum = 0
end = 0
length=[]
for start in range(n):
    while sum < s and end < n:
        sum += seq[end]
        end += 1
    if sum >= s:
        length.append(end-start)
    sum -= seq[start]

if len(length)==0:
    print(0)
else:
    print(min(length))
