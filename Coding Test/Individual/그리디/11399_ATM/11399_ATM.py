n = int(input())
time = list(map(int,input().split()))
# 오름차순 정렬
time.sort()
sum = time[0]
total = sum
for i in range(1,n):
    sum += time[i]
    total += sum
print(total)