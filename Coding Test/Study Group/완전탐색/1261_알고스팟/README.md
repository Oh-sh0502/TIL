# # 1261: 알고스팟

### 문제

알고스팟 운영진이 모두 미로에 갇혔다. 미로는 N*M 크기이며, 총 1*1크기의 방으로 이루어져 있다. 미로는 빈 방 또는 벽으로 이루어져 있고, 빈 방은 자유롭게 다닐 수 있지만, 벽은 부수지 않으면 이동할 수 없다.

알고스팟 운영진은 여러명이지만, 항상 모두 같은 방에 있어야 한다. 즉, 여러 명이 다른 방에 있을 수는 없다. 어떤 방에서 이동할 수 있는 방은 상하좌우로 인접한 빈 방이다. 즉, 현재 운영진이 (x, y)에 있을 때, 이동할 수 있는 방은 (x+1, y), (x, y+1), (x-1, y), (x, y-1) 이다. 단, 미로의 밖으로 이동 할 수는 없다.

벽은 평소에는 이동할 수 없지만, 알고스팟의 무기 AOJ를 이용해 벽을 부수어 버릴 수 있다. 벽을 부수면, 빈 방과 동일한 방으로 변한다.

만약 이 문제가 [알고스팟](https://www.algospot.com/)에 있다면, 운영진들은 궁극의 무기 sudo를 이용해 벽을 한 번에 다 없애버릴 수 있지만, 안타깝게도 이 문제는 [Baekjoon Online Judge](https://www.acmicpc.net/)에 수록되어 있기 때문에, sudo를 사용할 수 없다.

현재 (1, 1)에 있는 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하는 프로그램을 작성하시오.

---

### 문제풀이

- DFS & BFS 의 개념과 숙련이 필요하다고 느낀 문제. 다른 2차원 배열을 따로 구성하여 부순 벽의 개수를 따로 표기하는 것이 포인트이다. 

```python
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
```



---

### 결과

![image-20210211233116336](C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210211233116336.png)

---

### Reference

- 다른 사람 풀이: https://codingfull.tistory.com/26