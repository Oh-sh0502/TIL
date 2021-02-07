n, m = map(int,input().split())

a = list(map(int, input().split()))
# cnt = 0
# sum = 0
# for i in range(n):
#     sum += a[i]
#     if sum == m:
#         cnt += 1
#     for j in range(i+1,n):
#         sum += a[j]
#         if sum == m:
#             cnt += 1
#     sum = 0
# print(cnt)

cnt = 0
sum = 0
end = 0
# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동
    while sum < m and end < n:
        sum += a[end]
        end +=1
    # 부분합이 m일 때 카운트 증가
    if sum == m:
        cnt += 1
    sum -= a[start]
print(cnt)