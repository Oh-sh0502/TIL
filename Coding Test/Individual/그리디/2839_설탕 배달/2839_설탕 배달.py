n = int(input())
cnt = 0

while n>=5:
    cnt += (n // 5)
    print(cnt)
    n %= 5
    print(n)

cnt += 1
n -= 3
if n == 0:
    print(cnt)
else:
    print(-1)
