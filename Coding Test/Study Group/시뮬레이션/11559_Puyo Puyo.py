import sys
from collections import deque
# import numpy as np
input = sys.stdin.readline
puyo = list(list(map(str, input())) for _ in range(12))
dx = [-1, 1, 0, 0]
dy = [0 ,0, 1, -1]
def bfs(x,y):
    visited = [[False] * 6 for _ in range(12)]
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    cnt = 1
    basket = []
    basket.append((x,y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= 12 or ny < 0 or ny >= 6 or puyo[nx][ny] == "." or visited[nx][ny] == True:
                continue
            if puyo[nx][ny] == puyo[x][y]:
                visited[nx][ny] = True
                cnt += 1
                basket.append((nx,ny))
                q.append((nx, ny))
    if cnt >= 4:
        return basket
    return False
def down(x, y):
    for i in range(x,0,-1):
        puyo[i][y] = puyo[i-1][y]
    puyo[0][y] = '.'
def gravity(result):
    result.sort(key=lambda x:x[0])
    # print(result)
    for position_x, position_y in result:
        down(position_x, position_y)



def start(cnt):
    boom = []
    pocket = []
    for i in range(11, -1, -1):
        for j in range(6):
            if puyo[i][j] == ".":
                continue
            result=bfs(i,j)
            if result == False:
                continue
            else:
                for x, y in result:
                    puyo[x][y] = "."
                    boom.append(1)
                # print(np.array(puyo))
                pocket.extend(result)
    if len(boom) == 0:
        return cnt
    else:
        cnt += 1
        gravity(pocket)
        return start(cnt)

print(start(0))