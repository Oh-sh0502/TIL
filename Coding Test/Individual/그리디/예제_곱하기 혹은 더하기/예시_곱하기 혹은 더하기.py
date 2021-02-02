a = list(map(int,input()))
print(a)
result = 0
for i in a:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i

print(result)


