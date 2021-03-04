import sys
from collections import deque
input = sys.stdin.readline

def searchindex(nx ,ny ,value):
    newlist=[(i,j) for i in range(1,h+1) for j in range(1,w+1) if (i !=nx and j != ny) and graph[i][j]==value]
    return newlist
def bfs(x,y):
    q = deque()
    q.append((x,y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or nx >= h or ny < 1 or ny >= w:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] >= 10:
                exit = searchindex(nx, ny, graph[nx][ny])
                if not exit:
                    return "Never"
                else:
                    bfs(exit[0],exit[1])
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
        if not q:
            return "Impossible"
    return graph[h][w]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
marking = 10
while True:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break
    time = [[0]*(w+1) for _ in range(h+1)]
    graph = [[1] * (w+1) for _ in range(h+1)]
    print(graph)
    g = int(input().rstrip())
    tomb = [[0,0]]
    for i in range(g):
        tomb.append(list(map(int, input().rstrip().split())))
        print(tomb)
        for x, y in tomb:
            graph[x][y] = 0
    print(graph)
    e = int(input().rstrip())
    if e != 0:
        worp = []
        for i in range(e):
            worp.append(list(map(int, input().rstrip().split())))
        for x1, y1, x2, y2, t in worp:
            if x1 == x2 and y1 == y2:
                break;
            graph[x1][y1] = marking
            graph[x2][y2] = marking
            time[x1][y1] = t
            marking += 1

print(bfs(1,1))
