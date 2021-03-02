import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
# 찾기 함수
def find_parent(x):
    if parent[x] == x:
        return x
    else:                                                   # x의 부모가 자기 자신이 아니면
        r = find_parent(parent[x])                          # r은 x의 최고 조상을 의미한다.(x의 루트노드)
        print(parent[x])
        dist[x] += dist[parent[x]]                          # x와 부모노드 사이의 거리에 부모의 부모노드 사이의 거리만큼 더하면 x와 조부모의 거리를 구할 수 있다. 이게 재귀가 되면 x와 루트노드 사이의 거리다.
        parent[x] = r                                       # x의 부모를 루트노드로 설정한다.
        return parent[x]                                    # 그럼 반환되는 건 루트노드이다. 그렇다 find는 원래 루트노드를 찾는 함수였다..



# 합집합 함수
def union_parent(a, b, k):
    aroot = parent[a]                                       # a의 루트노드를 찾는다.
    broot = parent[b]                                       # b의 루트노드를 찾는다.
    if aroot != broot:                                      # a와 b가 다를 경우
        parent[broot] = aroot                               # b의 부모를 a로 한다. 둘은 하나로 연결된다.
        dist[broot] = (dist[a] + k) - dist[b]               # b의 부모에서의 차이값은

while True:
    n = int(input())
    parent = [i for i in range(n + 1)]
    dist = [0 for i in range(n + 1)]                        # dist는 노드와 부모 노드사이의 거리
    for i in range(n):
        a = list(map(str, input().split()))
        find_parent(int(a[0]))
        find_parent(int(a[1]))
        union_parent(int(a[0]), int(a[1]), int(a[2]))
    k = int(input())
    for i in range(k):
        b = list(map(str, input().split()))
        find_parent(int(b[0]))
        find_parent(int(b[1]))
        if parent[int(b[1])] == parent[int(b[2])]:
            print(dist[int(b[2])] - dist[int(b[1])])
        else:
            print("UNKNOWN")

