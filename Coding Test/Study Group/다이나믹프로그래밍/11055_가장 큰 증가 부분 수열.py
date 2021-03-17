n = int(input())
seq = list(map(int, input().split()))

d = []
d.append([seq[0]])
if n > 1:
    for i in range(1,n):
        d.append([seq[i]])
        _max = seq[i]
        for j in range(i):
            if d[j][-1] < seq[i] and _max < sum(d[j])+seq[i]:
                d[i] = d[j]+[seq[i]]
                _max = sum(d[j])+seq[i]


result = 0
for i in d:
    if result < sum(i):
        result = sum(i)
print(result)