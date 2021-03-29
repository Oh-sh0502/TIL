from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 세로 n, 가로 m
n, m = map(int, input().split())
# (r,c)와 바라보는 방향 d (d=0 : 북쪽, d=1 : 동쪽, d=2 : 남쪽, d=3 : 서쪽)
r, c, d = map(int, input().split())
room = []

for i in range(n):
    room.append(list(map(int, input().split())))


def bfs():

    q = deque()
    while q:

