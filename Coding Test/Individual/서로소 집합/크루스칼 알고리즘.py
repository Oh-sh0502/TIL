# 대표적인 최소 신장 트리 알고리즘
# 그리디 알고리즘으로 분류
# 간선의 개수가 E개일 때, O(ElogE)의 시간복잡도


# 특정 원소가 속한 집합을 찾기
def find_parnet(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        parent[x] = find_parnet(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parnet(parent, a)
    b = find_parnet(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent =[0] * (v+1)

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for i in range(e):
    a, b, cost= map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parnet(parent, a) != find_parnet(parent, b):            # a의 루트노드와 b의 루트노드가 다른다면(a와 b가 서로 다른 집합이라면)
        union_parent(parent, a, b)                                  # 루트노드를 비교해 하나의 집합으로 만들어주고(그래프상으로는 '두 노드를 이어준다'라는 의미임)
        result += cost                                              # 간선 코스트를 누적한다.
print(result)