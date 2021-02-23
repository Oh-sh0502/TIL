# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트노드를 찾을 때까지 재귀 호출
    if parent[x] != x:                              # 부모노드가 자기자신(루트노드)이 아니면
        return find_parent(parent, parent[x])       # 부모노드에서 다시 함수를 실행
    return x                                        # 부모노드가 자기자신(루트노드)이면 그 노드를 출력

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)                      # a노드로부터 루트노드를 찾아 a에 저장
    b = find_parent(parent, b)                      # b노드로부터 루트노드를 찾아 b에 저장
    if a < b:                                       # a보다 b가 크면
        parent[b] = a                               # b의 부모는 a가 된다. b가 a 밑임
    else:                                           # 아니면
        parent[a] = b                               # a의 부모는 b가 된다.


# 노드의 개수가 간선(Union 연산)의 개수 입력 받기
v, e = map(int, input().split())                    # v가 노드 개수, e가 간선 개수
parent = [0] * (v+1)                                # 부모테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v+1):                             # 1부터 v까지
    parent[i] = i                                   # 나의 부모는 나야

# Union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)                      # a와 b를 Union

# 각 원소가 속한 집합 출력하기
print('각 원소가 속한 집합: ', end='')
for i in range(1, v+1):
    print(find_parent(parent, i), end=' ')
print()

# 부모 테이블 내용 출력하기
for i in range(1, v+1):
    print(parent[i], end=' ')


# 합집합(Union) 연산이 편향괴게 이루어지는 경우 찾기(Find)함수가 비효율적으로 동작
# 최악의 경우 찾기(Find) 함수가 모든 노드를 다 확인하게 되어 시간복잡도가 O(V)
