from collections import deque

dx = [0,-1,0,1,0,-1,0,1]  # 서북동남
dy = [-1,0,1,0,-1,0,1,0]  # 서북동남

# 세로 n, 가로 m
n, m = map(int, input().split())
# (r,c)와 바라보는 방향 d (d=0 : 북쪽, d=1 : 동쪽, d=2 : 남쪽, d=3 : 서쪽)
r, c, d = map(int, input().split())
room = []
visited = [[False] * m for _ in range(n)]
for i in range(n):
    room.append(list(map(int, input().split())))
start = (r, c, d)

def bfs(start):
    x, y, d = start
    visited[x][y] = True
    q = deque()
    q. append(start)
    ok = 0
    while q:
        x, y, d = q.popleft()
        if not visited[x][y]:
            visited[x][y] = True
        # 현재 방향의 왼쪽 방향에 있는 칸
        nx = x + dx[d]
        ny = y + dy[d]
        # 왼쪽 방향에 있는 칸이 벽이거나 room을 벗어나 이미 청소를 했다면
        if room[nx][ny] == 1 or nx >= n or nx < 0 or ny >= m or ny < 0 or visited[nx][ny] == True:
            if ok == 4:                         # 만약 4방향 다 청소하거나 벽이면
                nx = x + dx[d+3]              # 후진 칸을 돌아본다
                ny = y + dy[d+3]
                if room[nx][ny] == 1:
                    return count_True()
                else:
                    ok = 0
                    q.append((nx, ny, d))
                    continue
            d -= 1                              # 방향 왼쪽으로 틀기
            if d == -1:
                d = 3
            ok += 1                             # ok 1 적립
            q.append((x, y, d))                 # 큐에 원래 자리 추가 -> 다시돌리기
        else:
            d -=1
            if d == -1:
                d = 3
            ok = 0
            q.append((nx,ny,d))
    return count_True()

def count_True():
    cnt = 0
    for i in range(n):
        cnt += visited[i].count(True)
    return cnt
print(bfs(start))
