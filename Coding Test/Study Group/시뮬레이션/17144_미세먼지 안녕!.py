import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
# 초기 맵
map_ = list(list(map(int, input().split())) for _ in range(r))
# 미세먼지 농도 변화량을 저장하는 맵
diffusionDifferentialMap = [[0]*c for _ in range(r)]
di = [-1, 1, 0 ,0]
dj = [0, 0, -1, 1]
cleaner = []

# 공기 확산
def diffusionDifferenctial(cleaner):
    # 브루트하게
    for i in range(r):
        for j in range(c):
            # 농도가 0이면 패스
            if map_[i][j] == 0:
                continue
            # 공기청정기면 공기청정기 좌표를 남겨놓고 패스
            elif map_[i][j] == -1:
                cleaner.append((i,j))
                continue
            # 확산하는 먼지량 정의
            dust = map_[i][j] // 5
            # 네 방향 확인
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                # 맵을 벗어나거나 공기청정기면 패스
                if ni < 0 or ni >= r or nj < 0 or nj >=c or map_[ni][nj] == -1:
                    continue
                diffusionDifferentialMap[ni][nj] += dust        # 먼지가 이동한 장소는 먼지 농도가 올라가고
                diffusionDifferentialMap[i][j] -= dust          # 확산 위치 먼지 농도가 내려감
    # 브루트하게 모든 칸을 연산
    for i in range(r):
        for j in range(c):
            # 기존 맵 + 먼지 변화량 = 변화된 먼지량
            map_[i][j] += diffusionDifferentialMap[i][j]
    # 출력은 공기청정기 위치를 리턴한다.
    return cleaner

# 오른쪽
def rightFlow(x,y):
    for i in range(y,0,-1):
        if i == 1:
            map_[x][i] = 0
            continue
        map_[x][i] = map_[x][i-1]
# 왼쪽
def leftFlow(x,y):
    for i in range(y):
        map_[x][i] = map_[x][i+1]
# 아래
def downFlow(x,y,c):
    if c == "up":
        for i in range(x,0,-1):
            if map_[i][y] == -1:
                continue
            map_[i][y] = map_[i-1][y]
    if c == "down":
        for i in range(r-1,x,-1):
            if map_[i][y] == -1:
                continue
            map_[i][y] = map_[i-1][y]
# 위
def upFlow(x,y,c):
    if c == "up":
        for i in range(x):
            if map_[i][y] == -1:
                continue
            map_[i][y] = map_[i+1][y]
    else:
        for i in range(x, r-1):
            if map_[i][y] == -1:
                continue
            map_[i][y] = map_[i+1][y]

# 공기청정기 ON
def clean(cleaner):
    # 공기청정기 위쪽
    up_x, up_y = cleaner[0]
    # 공기청정기 아래쪽
    down_x, down_y = cleaner[1]

    # 위쪽 사이클
    downFlow(up_x,0,"up")           # ↓
    leftFlow(0, c-1)                # ←
    upFlow(up_x,c-1,"up")           # ↑
    rightFlow(up_x,c-1)             # →

    # 아래쪽 사이클
    upFlow(down_x,0,"down")         # ↑
    leftFlow(r-1,c-1)               # ←
    downFlow(down_x,c-1,"down")     # ↓
    rightFlow(down_x,c-1)           # →

for _ in range(t):                                              # 입력한 시간(t)만큼
    diffusionDifferenctial(cleaner)                             # 공기확산
    clean(cleaner)                                              # 공기청정기 가동
    diffusionDifferentialMap = [[0] * c for _ in range(r)]      # 먼지변화량 맵 초기화

# 2차원배열 총합 구하기
result = sum(map(sum, map_))
# 출력
print(result+2)