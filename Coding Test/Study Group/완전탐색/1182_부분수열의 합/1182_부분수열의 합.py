import sys
from itertools import combinations

a = list(map(int, sys.stdin.readline().split()))
n = a[0]
s = a[1]

seq = list(map(int,sys.stdin.readline().split()))
cnt = 0
for i in range(1,(n+1)):
    p = list(combinations(seq, i))
    for j in p:
        if sum(j) == s:
            cnt +=1

print(cnt)


