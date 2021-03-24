n = int(input())

stair =[0]
for _ in range(n):
    stair.append(int(input()))
d = [0] * (n+1)
for i in range(1, n+1):
    if i == 1:
        d[1] = stair[1]
    elif i == 2:
        d[2] = stair[1] + stair[2]
    elif i == 3:
        d[3] = max(stair[2]+stair[3], d[1] + stair[3])
    else:
        d[i] = max(stair[i] + stair[i-1] + d[i-3], stair[i] + d[i-2])

print(d[n])


