INF = int(1e9)

n, m = map(int, input().split())
graph =[[0] * (n+1) for i in range(n+1)]

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 점화식에 따라 플로이드 워셜
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] + graph[k][b] == 2:
                graph[a][b] = 1

cnt = 0
for i in range(1, n+1):
    c = 0
    for j in range(1,n+1):
        c += graph[i][j] + graph[j][i]
    if c == n-1:
        cnt += 1
print(cnt)