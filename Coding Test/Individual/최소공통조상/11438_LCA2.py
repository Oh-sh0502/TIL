import sys
input = sys.stdin.readline                  # 시간초과가 빡센가 봄.. LCA에서는 그냥 input 썼었음
sys.setrecursionlimit(int(1e5))             # 런타임 오류를 피하기 위한 재귀 깊이 제한 설정
LOG = 21                                    # 2^20 = 1,000,000

n = int(input())
parent = [[0] * LOG for _ in range(n+1)]    # 부모 노드 정보
d = [0] * (n+1)                             # 각 노드까지의 깊이
c = [0] * (n+1)                             # 각 노드의 깊이가 계산되었는지 여부
graph = [[] for _ in range(n+1)]            # 그래프 정보

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)                      # a노드에는 b가 연결되어있다.
    graph[b].append(a)                      # b노드에는 a가 연결되어있다.

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수: 위에서 아래로 진행됩니다~
def dfs(x, depth):
    c[x] = True                             # 깊이 계산 처리(방문처리)
    d[x] = depth                            # 깊이 입력
    for y in graph[x]:                      # x노드와 연결된 노드 y
        if c[y]:                            # y가 이미 깊이 계산이 처리되었다면 (y가 진입노드인 경우)
            continue                        # 넘어가고
        parent[y][0] = x                    # 아니면 y의 2^0번째 부모를 x로 설정 (y가 진출노드일 경우). 위에서 아래로 진행하면서 부모자식관계. 헨젤과 그레텔식 운영
        dfs(y, depth + 1)                   # y노드와 깊이 +1로 재귀

# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1,0)                                # 루트노드 1번에서 출발(깊이는 당연히 0)
    for i in range(1, LOG):                 # 1~20
        for j in range(1, n+1):             # 1~n
            parent[j][i] = parent[parent[j][i-1]][i-1]  # j번 노드에서 2^(i-1)만큼 점프하고 다시 2^(i-1)만큼 점프하므로 2*2^(i-1)=2^i

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # b가 더 깊도록 설정
    if d[a] > d[b]:
        a, b = b, a
    # 먼저 깊이(depth)가 동일하도록
    for i in range(LOG - 1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    # 부모가 같아지도록
    if a == b:
        return a;

    for i in range(LOG - 1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후에 부모가 찾고자 하는 조상
    return parent[a][0]
set_parent()

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))