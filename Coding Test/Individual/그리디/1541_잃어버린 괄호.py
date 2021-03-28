a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)

n = num[0] * 2
for i in num:
    n -= i
print(n)