import sys
input = sys.stdin.readline
# 북쪽 체크
def north_checking(x, y):
    cnt = 0
    for i in range(x):
        if office[i][y] == '#':
            continue
        else:
            cnt += 1
    return cnt
# 북쪽 # 마킹
def north_marking(x, y):
    cnt = 0
    for i in range(x):
        if office[i][y] == '#':
            continue
        else:
            office[i][y] = '#'
            cnt += 1
    return cnt
# 서쪽 체크
def south_checking(x, y):
    cnt = 0
    for i in range(x+1,n):
        if office[i][y] == '#':
            continue
        else:
            cnt += 1
    return cnt
# 서쪽 # 마킹
def south_marking(x, y):
    cnt = 0
    for i in range(x+1,n):
        if office[i][y] == '#':
            continue
        else:
            office[i][y] = '#'
            cnt += 1
    return cnt
# 왼쪽 체크
def left_checking(x, y):
    cnt = 0
    for i in range(y):
        if office[x][i] == '#':
            continue
        else:
            cnt += 1
    return cnt
# 왼쪽 # 마킹
def left_marking(x, y):
    cnt = 0
    for i in range(y):
        if office[x][i] == '#':
            continue
        else:
            office[x][i] = '#'
            cnt += 1
    return cnt
# 오른쪽 체크
def right_checking(x, y):
    cnt = 0
    for i in range(y+1, m):
        if office[x][i] == '#':
            continue
        else:
            cnt += 1
    return cnt
# 오른쪽 # 마킹
def right_marking(x, y):
    cnt = 0
    for i in range(y+1, m):
        if office[x][i] == '#':
            continue
        else:
            office[x][i] = '#'
            cnt += 1
    return cnt

def four(x, y):
    north_marking(x, y)
    south_marking(x, y)
    left_marking(x, y)
    right_marking(x, y)
def three(x, y):
    cnt_list = []
    cnt_max = north_checking() + south_checking() + left_checking()
    cnt_list.append(north_checking() + south_checking() + left_checking())
    if cnt_max <
    cnt_list.append(north_checking() + south_checking() + right_checking())
    cnt_list.append(north_checking() + left_checking() + right_checking())
    cnt_list.append(south_checking() + left_checking() + right_checking())


n, m = map(int, input().split())
office = []
for i in range(n):
    office.append(list(map(int, input().split())))
