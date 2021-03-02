import sys
from collections import defaultdict                     # defaultdict: 기본값을 정의하고 키값이 없을 경우에 에러없이 기본값을 출력해주는 딕셔너리

sys.setrecursionlimit(10**6)                            # 재귀는 100만번

# dfs
def dfs(here, cnt):                                     # here은 현재 노드, cnt는 카운트
    order[here] = cnt                                   # 현재 노드의 방문순서를 저장

    children = 0                                        # 자식의 수 아직 0
    ret = order[here]                                   # 이따가 return할 변수 ret. 현재노드의 방문순서를 저장

    for next in graph[here] :                           # here 노드와 인접한 노드들을 차례대로 검사
        if order[next] :                                # 인접한 노드들의 방문순서가 이미 존재하면
            ret = min(ret, order[next])                 # 현재 노드의 방문순서와 비교하여 가장 작은 것을 저장

        else :                                          # 아니면 (처음에는 1빼고는 방문순서가 None이기 때문에 여기로 올 수 밖에 없다)
            children += 1                               # 자식의 수 1 증가
            subtree = dfs(next, cnt+1)                  # next점을 기준으로 dfs 재귀

            if cnt != 1 and subtree >= order[here] :    # 카운트 수가 1이 아니고 인접노드(서브트리)의 방문순서가 현재 노드의 방문순서보다 클 때
                cutVertex.add(here)                     # 단절점에 추가

            ret = min(subtree, ret)                     # 리턴 값은 현재 노드와 다음 인접노드 중 방문순서가 작은 것으로 한다.

    if cnt == 1 and children >= 2 :                     # 카운트 수가 1(자신이 루트노드라면)이고 자식노드가 2개 이상이면
        cutVertex.add(here)                             # 단절점에 추가한다.

    return ret


# N개
V,E = map(int, sys.stdin.readline().rstrip().split(" "))            # 노드와 간선의 개수
graph = defaultdict(list)                                           # 그래프는 리스트를 기본값으로 하는 defaultdict로 생성
cutVertex = set()                                                   # 단절점
candidates = set()                                                  # 후보

for _ in range(E) :                                                 # 간선 정보를 입력
    a,b = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[a].append(b)                                              # a를 key로 하는 리스트에 b 추가
    graph[b].append(a)                                              # b를 key로 하는 리스트에 a 추가
    candidates.add(a)                                               # candidates 집합에 a 추가
    candidates.add(b)                                               # candidates 집합에 b 추가
print(graph)
print(candidates)
order = [None] * (V+1)                                              # 방문순서
cnt = 1                                                             # 방문순서 카운트 정의

for vertex in candidates:                                           # candidates에서 노드를 차례대로 선택
    if not order[vertex]:                                           # 방문순서에 원소값이 없다면
        dfs(vertex, 1)                                              # 노드와 카운트를 들고 dfs 시작

print(len(cutVertex))

for vertex in sorted(list(cutVertex)) :
    print(vertex, end=" ")