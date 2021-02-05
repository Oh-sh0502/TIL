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
