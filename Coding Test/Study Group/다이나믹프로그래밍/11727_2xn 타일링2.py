n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3,n+1):
    if i % 2 == 1:
        d[i] = d[i-1]*2 - 1
    elif i % 2 == 0:
        d[i] = d[i-1]*2 + 1

print(d[n]%10007)