a = int(input())

b = list(map(int, input().split()))
group = 0
b.sort()
print(b)
c = []
for i in b:
    c.append(i)
    print(c)
    if len(c) == i:
        group += 1
        c = []

print(group)
