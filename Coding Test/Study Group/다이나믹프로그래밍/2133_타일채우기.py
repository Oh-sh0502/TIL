n = int(input())

d = [0] * (n+2)
d[2] = 3

for i in range(4, n+2, 2):
    d[i] = 3 * d[i-2]
    for j in range(4, i, 2):
        d[i] += 2 * d[i-j]
        print(d)
    d[i] += 2

print(d[n])


