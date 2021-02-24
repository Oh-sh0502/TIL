import sys

# a, b의 제한이 100만이므로 find_parent 함수에서 100만번의 재귀가 있을 수 있다.
# 파이썬은 1000번이상의 재귀는 기본적으로 제한하고 있어 setrecursionlimit() 함수로 재귀 제한을 풀어준다.
sys.setrecursionlimit(1000000)

# 입력
input = sys.stdin.readline
m, n = map(int, input().split())

# 찾기(Find) 함수: 부모노드를 기준으로 집합을 정의한다.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

# 합집합(Union) 함수: 집합과 집합간 부모, 자식관계를 확인하고 집합을 하나로 합친다.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 사이클 판별 함수: Find 함수로 두 집합의 부모 노드가 같은지 확인한다. 같다면 같은 부모노드, 같은 집합, 같은 사이클을 의미
def check_cycle(a,b):
    cycle = False
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
    if cycle:
        print("YES")
    else:
        print("NO")

parent = [0] * (m+1)            # 이 문제에서는 0도 원소로 들어간다는 것을 잊지 말것!

for i in range(m+1):            # 이 문제에서는 0도 원소이다!
    parent[i] = i               # 따라서 0번째도 0으로 처리

for i in range(n):
    f, a, b = map(int, input().split())
    if f == 0:
        union_parent(parent, a, b)
    elif f == 1:
        check_cycle(a, b)
