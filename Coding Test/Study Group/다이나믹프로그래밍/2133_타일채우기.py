n = int(input())

d = [0] * (n+1)
d[2] = 3
if n > 2  and n % 2 == 0:
    for i in range(2, int(n/2)):
        d[2*i] = 2*(d[2(i-1)]+1)

