n = int(input())

d=[[0] * 10 for _ in range(1001)]

for i in range(10):
    d[1][i] = 1
for i in range(2, n+1):
    for j in range(10):
        if j == 9:
            d[i][j] = 1
        else:
            for k in range(j,10):
                d[i][j] += d[i-1][k]
print(sum(d[n])%10007)