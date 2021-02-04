import sys
from itertools import combinations
while True:
    lotto = list(map(int, sys.stdin.readline().split()))
    a = lotto[0]
    b = list(lotto[1:len(lotto)])
    b = list(combinations(b, 6))
    for i in b:
        for j in range(6):
            print(i[j], end=' ')
        print()
    print()
    if lotto[0] == 0:
        break