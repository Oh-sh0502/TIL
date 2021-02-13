import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())           # m: 가로, n: 세로
a = []

for i in range(n):
    a.append(sys.stdin.readline())

dist = [[-1] * m for _ in range(n)]                     # 원소가 모두 -1인 n x m인 2차원리스트
dist[0][0] = 0                                          # 0행0열을 0으로
q = deque()                                             # deque 정의
dx = [1, -1, 0, 0]                                      # 상하좌우 정의
dy = [0, 0, 1, -1]
q.append([0, 0])                                        # 덱에 (0,0) 추가

# BFS
while q:
    x, y = q.popleft()                                  # (0,0) 빼고
    for i in range(4):                                  # 상하좌우 탐색
        nx, ny = x + dx[i], y + dy[i]                   # 상하좌우 좌표
        if nx >= 0 and nx < n and ny >= 0 and ny < m:   # 맵의 범위 안에서
            if dist[nx][ny] == -1:                      # 방문맵의 값이 -1이면
                if a[nx][ny] == '0':                    # 빈방에 도착했을 경우
                    q.appendleft([nx, ny])              # 좌표를 덱의 왼쪽에 저장
                    dist[nx][ny] = dist[x][y]           # 이전값과 같은 값을 저장
                elif a[nx][ny] == '1':                  # 벽을 만났을 경우
                    q.append([nx, ny])                  # 좌표를 덱의 오른쪽에 저장
                    dist[nx][ny] = dist[x][y] + 1       # 이전 값에 +1을 하여 저장

print(dist[n - 1][m - 1])                               # dist는 시작지점부터 벽의 개수를 카운트하는 맵이었다.