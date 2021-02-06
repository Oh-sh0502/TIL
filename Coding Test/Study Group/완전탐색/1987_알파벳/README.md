# #1987: 알파벳

### 문제

세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

---

### 문제풀이

-  좌측 상단에서부터 확장하는 방법으로 BFS를 선택하였다. [동빈나의 DFS&BFS 강의](https://www.youtube.com/watch?v=7C9RgOcvkvo)의 코드예시를 참고하여 풀었다. 그러나, 코드 예시처럼 위치(nx, ny)만 queue에 저장하면 탐색이 제대로 되지 않는다. 
   DFS처럼 이전 위치와 알파벳에서 연장하여 탐색해야하는데, for문에서 상하좌우 블록을 우선적으로 저장하다보니 아직 탐색하지 않을 위치까지 감안하여 경로를 탐색하게 된다.
   따라서 위치와 알파벳을 같이 저장하여 연장탐색이 가능하게 해야한다.
-  동빈나 BFS 코드예시에서는 deque()를 사용한다. 그러나 이 문제에서 deque()를 사용한다면 **메모리 초과**가 발생한다. 따라서 다른사람의 풀이를 참고하여 **deque를 set으로 바꿔서 풀었더니 문제가 해결되었다.**
   **deque가 여러 개의 메모리 단위로 데이터를 저장하고, 새로운 메모리 단위를 할당하여 요소를 추가하는 방식이기 때문에 메모리를 더 차지하는게 아닌가 싶다. **

```python
from collections import deque
import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    answer = 1
    # queue = deque()
    # queue.append((x,y,board[x][y]))
    queue = set([(x, y, board[x][y])])

    while queue:
        # x, y, ans = queue.popleft()
        x, y, ans = queue.pop()
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            # print(nx,"행 ",ny,"열: ")
            if nx < 0 or nx >= r or ny < 0 or ny >= c or board[nx][ny] in ans:
                continue
            else:
                # queue.append((nx,ny,ans + board[nx][ny]))
                queue.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)

    return answer

board = []
r, c = map(int,sys.stdin.readline().split())
for i in range(r):
    board.append(list(sys.stdin.readline().rstrip()))

result = bfs(0,0)
print(result)

```

---

### 결과

![image-20210205135928345](C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210205135928345.png)

---

### Reference

- 동빈나 이코테 강좌_DFS&BFS: https://www.youtube.com/watch?v=7C9RgOcvkvo
- 풀이 참고: https://devjin-blog.com/boj-1987-alphabet/

