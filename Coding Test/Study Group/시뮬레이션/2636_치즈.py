import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())

# 치즈 맵
map_ = list(list(map(int, input().split())) for _ in range(n))
# 치즈의 안과 밖을 구분하는 새로운 맵
inout = [[False]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]

# 안과 밖을 구별하는 bfs 함수
def bfs(x,y):
    q = deque()
    if map_[x][y] == 1 or inout[x][y] == True:                      # 치즈이거나 바깥이면
        return                                                      # 멈춰!
    else:                                                           # 아니라면
        inout[x][y] = True                                          # 바깥은 True 표시
        q.append((x,y))                                             # 출발
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue
                if map_[nx][ny] == 1 or inout[nx][ny] == True:
                    continue
                inout[nx][ny] = True
                q.append((nx,ny))


# 치즈 녹이기
def melt():
    cheese = 0
    for i in map_:
        cheese += i.count(1)
    cheese_after = 0
    #브루트하게
    for i in range(n):
        for j in range(m):
            x = i
            y = j
            # 먼저 방문여부를 확인. 여기서 방문여부란 진짜 들렀거나, 치즈가 녹은 경우
            if visited[i][j] == True:
                continue
            # 그럼 여기서부터는 방문하지 않거나, 치즈가 안 녹은 경우겠지
            # 우선 방문처리하고
            visited[i][j] == True
            # 맵에 있는 값을 확인해. 만약 0이면 그 주변에 1이 있는지를 찾아본다.
            if map_[i][j] == 0:
                if inout[i][j] == False:
                    continue
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m:
                        continue
                    # 1이 만약에 있다? 그 값을 0으로 만들고(녹여버리고) 방문처리(녹였음표시)
                    if map_[nx][ny] == 1:
                        map_[nx][ny] = 0
                        cheese_after += 1
                        visited[nx][ny] = True
            else:
                continue
    # 처음 치즈 상태가 녹은 후와 같다면 다 녹았다고 인지
    if cheese == cheese_after:
        return cheese
    # 그게 아니라면 치즈상태에 변화가 있다고 인지.
    else:
        return 'F'


cnt = 0             # 치즈가 다 녹은 시간
finalcheese = 0     # 마지막으로 남았던 치즈 개수


while True:
    bfs(0,0)                                            # 안과 밖을 나눈다
    finalcheese = melt()                                # 치즈를 녹이고
    cnt += 1                                            # 그게 아니라면 치즈를 녹인 시간에 1초 추가
    if finalcheese == 'F':                              # 치즈가 덜 녹았다면
        inout = [[False] * m for _ in range(n)]         # 변수 초기화
        visited = [[False] * m for _ in range(n)]
    else:                                               # 치즈가 다 녹았다면
        break                                           # 멈춰!

print(cnt)
print(finalcheese)


