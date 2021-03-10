t = int(input())

d = [0] * 12
d[1]=1
d[2]=2
d[3]=4

result =[]
for _ in range(t):
    n = int(input())
    for i in range(4, n+1):
        d[i] = d[i-1]+d[i-2]+d[i-3]
    result.append(d[n])

for i in result:
    print(i)