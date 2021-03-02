# 3830: 교수님은 기다리지 않는다.

### 문제

상근이는 매일 아침 실험실로 출근해서 샘플의 무게를 재는 일을 하고 있다. 상근이는 두 샘플을 고른 뒤, 저울을 이용해서 무게의 차이를 잰다.

교수님의 마음에 들기 위해서 매일 아침부터 무게를 재고 있지만, 가끔 교수님이 실험실에 들어와서 상근이에게 어떤 두 샘플의 무게의 차이를 물어보기도 한다. 이때, 상근이는 지금까지 잰 결과를 바탕으로 대답을 할 수도 있고, 못 할 수도 있다.

상근이는 결과를 출근한 첫 날부터 공책에 적어 두었다. 하지만, 엄청난 양의 무게가 적혀있기 때문에, 교수님의 질문에 재빨리 대답할 수가 없었다. 이런 상근이를 위해서 프로그램을 만들려고 한다.

상근이가 실험실에서 한 일이 순서대로 주어진다. 어떤 두 샘플의 무게의 차이를 구할 수 있는지 없는지를 알아내는 프로그램을 작성하시오.

---

### 문제풀이

- **Union-Find**를 이용한 문제이다. [동빈나 강의-기타그래프이론](https://www.youtube.com/watch?v=aOhhNFTIeFI&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=8)의 예시코드를 활용하면 유사하게 코드구성은 가능하나, dist라는 추가요소가 존재하기 때문에 좀 더 고민을 해야한다.
- find_parent는 x노드의 루트노드를 찾는 함수이다. 루트노드를 찾는 과정에서 x노드의 부모노드를 찾고, 이를 재귀하여 가장 위의 루트 노드를 찾아낸다. 따라서 바로 루트노드를 찾을 수 있지만, 중간중간에 부모노드를 이용하여 다른 작업을 코딩할 수 있다.

```python
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
        dist[x] += dist[parent[x]]                          # x와 부모노드 사이의 거리에 부모의 부모노드 사이의 거리만큼 더하면 x와 조부모의 거리를 구할 수 있다. 이게 재귀가	되면 x와 루트노드 사이의 거리다.
        parent[x] = r                                       # x의 부모를 루트노드로 설정한다.
        return parent[x]                                    # 그럼 반환되는 건 루트노드이다.
#그렇다 find는 원래 루트노드를 찾는 함수였다..



# 합집합 함수
def union_parent(a, b, k):
    aroot = parent[a]                                       # a의 루트노드를 찾는다.
    broot = parent[b]                                       # b의 루트노드를 찾는다.
    if aroot != broot:                                      # a의 루트노드와 b의 루트노드가 다를 경우
        parent[broot] = aroot                               # b의 루트노드 부모를 a로 한다. 즉, b의 루트노드는 a
        dist[broot] = (dist[a] + k) - dist[b]               # b의 부모에서와 루트노드 aroot와 차이값

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n + 1)]
    dist = [0 for i in range(n + 1)]                        # dist는 노드와 부모 노드사이의 거리
    for i in range(m):
        a = list(map(str, input().split()))
        find_parent(int(a[1]))                              # 시작점의 부모노드를 루트노드로 한다.
        find_parent(int(a[2]))                              # 끝점의 부모노드를 루트노드로 한다.
        if a[0] == "!":                                     # 첫 원소가 ! 라면
            union_parent(int(a[1]), int(a[2]), int(a[3]))   # 유니온 함수 실행: 두 점간의 부모관계를 정립하고 dist 수정
        else:
            if parent[int(a[1])] == parent[int(a[2])]:      # 두 점의 부모(이 시점에서는 루트노드)가 같다면
                print(dist[int(a[2])] - dist[int(a[1])])    # 루트노드간 거리를 서로 빼주면 두 점간의 거리가 됨
            else:
                print("UNKNOWN")


```



---

### 결과

![image-20210226125441819](C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210226125441819.png)

---

### Reference

- 참고: https://pacific-ocean.tistory.com/335

