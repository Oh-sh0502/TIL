import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

def dfs(here, parent):                              # 노드와 부모를 변수로 dfs
	global cnt                                      # 외부 변수 cnt 소환
	cnt += 1                                        # cnt 1 증가
	order[here] = cnt                               # 현재 노드의 방문순서를 저장(처음에는 cnt가 0->1이 되어 처음노드가 당연히 첫번째 방문임)
	ret = order[here]                               # 리턴할 값에 현재노드의 방문순서를 저장

	for next in graph[here]:                        # 현재노드와 인접한 노드에 대하여
		if next == parent:                          # 인접노드가 곧 부모라면
			continue

		if order[next]:                             # 방문순서 값이 존재하면
			ret = min(ret, order[next])             # 현재노드의 방문순서와 비교하여 작은 값을 저장
			continue

		subtree = dfs(next, here)
		ret = min(subtree, ret)

		# 부모로 바로가는 간선(현재간선)을 제외하고 서브트리의 간선 중 부모보다 선조로 갈 수 없으면
		if subtree > order[here] :
			cutEdge.add(tuple(sorted([here,next])))

	return ret


# N개
V,E = map(int, sys.stdin.readline().rstrip().split(" "))                # 노드개수와 간선개수
graph = defaultdict(set)                                                # 그래프는 set을 기본값으로 하는 defaultdict
cutEdge = set()                                                         # 단절선
candidates = set()                                                      # 단절선 후보

for _ in range(E) :
    a,b = map(int, sys.stdin.readline().rstrip().split(" "))            # 간선 정보 입력
    graph[a].add(b)                                                     # a를 key로 하는 집합에 b 추가
    graph[b].add(a)                                                     # b를 key로 하는 집합에 a 추가
    candidates.add(a)                                                   # 후보군에도 a 추가
    candidates.add(b)                                                   # 후보군에도 b 추가

order = [None] * (V+1)                                                  # 방문 순서
cnt = 0                                                                 # 방문순서 카운트 0
idx =0                                                                  # 인덱스
for vertex in candidates:                                               # 후보군 안에서 하나씩 뽑아내면서
    if not order[vertex]:                                               # 방문순서 값이 None이면
        dfs(vertex,  None)                                              # 노드와 None 값으로 dfs 시작


print(len(cutEdge))
cutEdge = sorted(cutEdge, key=lambda x : (x[0],x[1]))

for a,b in cutEdge :
    print(a,b)