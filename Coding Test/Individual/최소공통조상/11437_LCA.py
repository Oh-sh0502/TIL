import sys
sys.setrecursionlimit((int(1e5)))       # 런타임 오류를 피하기
n = int(input())

parent = [0] * (n+1)                    # 부모 노드 정보
d = [0] * (n+1)                         # 각 노드까지의 깊이
c = [0] * (n+1)                         # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)]        # 그래프(graph) 정보

# 트리상에 연결된 두 정점을 입력하고 graph에 담는다.
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)                  # a노드에 b가 연결되어있다.
    graph[b].append(a)                  # b노드에 a가 연결되어있다.

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def dfs(x, depth):
    c[x] = True                         # 깊이 계산처리(방문처리)
    d[x] = depth                        # 깊이 대입
    for y in graph[x]:                  # x노드와 연결된 노드 y를 차례로 확인
        if c[y]:                        # 연결된 노드 y의 깊이 계산을 이미 구했다면 넘기기
            continue
        parent[y] = x                   # 그렇지 않으면 y의 부모를 x로 설정하고
        dfs(y, depth + 1)               # 깊이를 +1 하고 재귀

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a,b):
    # 먼저 깊이(depth)가 동일하도록
    while d[a] != d[b]:                 # 깊이가 같아질 때까지
        if d[a] > d[b]:                 # a노드의 깊이가 더 깊으면
            a = parent[a]               # a의 부모를 a에 저장 (while문에 의해 a노드에서 계속 타고 올라간다는 이야기)
        else:                           # 아니라면
            b = parent[b]               # b의 부모를 b에 저장 (while문에 의해 b노드에서 계속 타고 올라간다는 이야기)
    # 노드가 같아지도록
    while a != b:                       # a와 b가 같아질 때까지
        a = parent[a]                   # a의 부모를 a에 저장 (while문에 의해 a노드에서 계속 타고 올라간다는 이야기)
        b = parent[b]                   # b의 부모를 b에 저장 (while문에 의해 b노드에서 계속 타고 올라간다는 이야기)
    return a

dfs(1,0)                                # 루트 노드는 1번 노드

m = int(input())                        # 공통조상을 알고싶은 쌍의 수 입력

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a,b))