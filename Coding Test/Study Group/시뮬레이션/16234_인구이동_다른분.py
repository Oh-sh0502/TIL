import sys
import numpy as np
sys.setrecursionlimit(10000)
N, L, R = map(int, input().split())

mat = []
for i in range(N):
    a = list(map(int, input().split()))
    mat.append(a)


def dfs(r, c, mat):
    check[(r, c)] = True

    if c < N - 1 and L <= abs(mat[r][c] - mat[r][c + 1]) <= R:
        if (r, c + 1) not in stack:
            stack.append((r, c + 1))
            dfs(r, c + 1, mat)
    if r < N - 1 and L <= abs(mat[r][c] - mat[r + 1][c]) <= R:
        if (r + 1, c) not in stack:
            stack.append((r + 1, c))
            dfs(r + 1, c, mat)
    if c > 0 and L <= abs(mat[r][c] - mat[r][c - 1]) <= R:
        if (r, c - 1) not in stack:
            stack.append((r, c - 1))
            dfs(r, c - 1, mat)

    if r > 0 and L <= abs(mat[r][c] - mat[r - 1][c]) <= R:
        if (r - 1, c) not in stack:
            stack.append((r - 1, c))
            dfs(r - 1, c, mat)


sol = 0


def solution(sol):
    global check, stack

    # map copy
    m = mat[:]
    print("복제본 m", np.array(m))
    for i in range(N):
        m[i] = mat[i][:]
    print(m)
    sol += 1
    connect = []
    check = {}

    for i in range(N):
        for j in range(N):
            if (i, j) not in check:
                stack = []
                dfs(i, j, mat)
                connect.append(stack)
    print(connect)
    for i in connect:
        s = 0

        if len(i) != 0:
            for j in i:
                s += mat[j[0]][j[1]]
            ave = s // len(i)

            for j in i:
                mat[j[0]][j[1]] = ave

    print(np.array(mat))

    if m == mat:
        print(sol - 1)
        return
    else:
        return solution(sol)


solution(sol)