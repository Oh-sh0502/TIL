import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

# 노드의 개수, 간선의 개수
v, e, k = map(int, input().split())

# 가중치테이블
dp = [INF] * (v+1)
heap = []
graph = [[] for _ in range(v+1)]
rank = [[] for _ in range(v+1)]

def dijkstra(start):
    # 가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    dp[start] = 0
    heapq.heappush(heap,(start, 0))

    # 힙에 원소가 없을 때까지 반복
    while heap:
        now, w =heapq.heappop(heap)
        # 현재 테이블과 비교하여 불필요한(더 가중치가 큰) 튜플은 무시
        if dp[now] < w:
            continue
        for next_node, nw in graph[now]:
            # 현재 정점까지의 가중치 w + 현재 정점에서 다음 정점(next_node)까지의 가중치 next_w
            # = 다음 노드까지의 가중치 (next_w)
            next_w = w + nw
            # 다음 노드까지의 가중치(next_w)가 현재 기록된 값보다 작으면 조건 성립.
            if next_w < dp[next_node]:
                # 계산했던 next_w를 가중치 테이블에 저장
                dp[next_node] = next_w
                # 다음 점까지의 가중치와 다음 점에 대한 정보를 튜플로 묶어 최소 힙에 삽입
                heapq.heappush(heap,(next_node,next_w))

# 초기화
for _ in range(e):
    a, b, c = map(int, input().split())
    # (노드, 가중치) 형태로 저장
    graph[a].append((b,c))

dijkstra(1)

for i in range(1, v+1):
    print("INFINITY" if dp[i] == INF else dp [i])