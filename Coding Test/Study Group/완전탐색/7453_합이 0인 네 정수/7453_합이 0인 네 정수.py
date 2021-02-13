import sys

n = int(sys.stdin.readline())                               # 배열의 크기
A = []; B = []; C = []; D = []                              # 배열 리스트 정의

for i in range(n):
    a,b,c,d = map(int, sys.stdin.readline().split())
    A.append(a); B.append(b); C.append(c); D.append(d)      # A, B, C, D 배열 완성

ab, cd = {},{}                                              # A&B, C&D 딕셔너리 생성
result = 0                                                  # 카운트

for a in A:
    for b in B:
        if a+b not in ab:                                   # a+b가 딕셔너리에 없다면
            ab[a+b] = 1                                     # a+b: 1 생성
        else:                                               # 있으면
            ab[a+b] += 1                                    # key가 a+b인 value에 +1

for c in C:
    for d in D:
        temp = -(c+d)                                       # -(c+d)값을 정의
        if temp in ab:                                      # -(c+d)값이 ab 딕셔너리의 key 중에 있으면
            result += ab[temp]                              # value 값만큼 카운트에 더해준다.

print(result)                                               # 출력