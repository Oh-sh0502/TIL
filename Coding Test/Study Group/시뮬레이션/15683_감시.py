import sys
input = sys.stdin.readline
def north(x, y):
    cnt = 0
    for i in range(x):
        if office[i][y] == '#':
            cnt += 1
            continue
        else: office[i][y] = '#'
    return cnt

def south(x, y):
    cnt = 0
    for i in range(x+1,n):
        if office[i][y] == '#':
            cnt +=1
            continue
        else: office[i][y] = '#'
    return cnt

def left(x, y):
    cnt = 0
    for i in range(y):
        if office[x][i] == '#':
            cnt += 1
        else: office[x][i] = '#'
    return cnt

def right(x, y):
    cnt = 0
    for i in range(y+1, m):
        if office[x][i] == '#':
            cnt += 1
            continue
        else: office[x][i] = '#'
    return cnt

n , m = map(int, input().split())