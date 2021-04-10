import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
map_ = [[0] * 100 for _ in range(100)]
def direction(d, x, y):
    if d == 0:
        map_[x+1][y] = 1
    elif d == 1:
        map_[x][y+1] = 1
    elif d == 2:
        map_[x-1][y] = 1
    elif d == 3:
        map_[x][y-1] = 1
def curve(d, g):
    dp=[]
    dp.append(direction(d,x,y))
for _ in range(n):
    x, y, d, g = map(int,input().split())
    map_[x][y] = 1
    q = deque()
    q.appned((x,y))
    while q:
        x, y = q.popleft()
