from collections import deque
# NxN
n = int(input())
_map = [[0]*n for i in range(n)]

# 사과의 위치
k = int(input())
apple_map = [[False] * n for _ in range(n)]
apple_location = []
for i in range(k):
    apple_x, apple_y = map(int, input().split())
    apple_location.append((apple_x, apple_y))
    apple_map[apple_x - 1][apple_y - 1] = True

# 뱡향 전환 횟수
l = int(input())
curve = []
for i in range(l):
    curve.append(tuple(map(str, input().split())))

# 오아왼위
dx = [0,1,0,-1]
dy = [1,0,-1,0]

def bfs(start):
    x, y = start
    snake = deque()         # 뱀 큐 생성
    q = deque()             # 큐 생성
    q.append(start)         # 큐에 (0,0) 추가
    snake.append(start)
    time = 0                # 시간
    turn = 0                # dx, dy 전환을 위한 turn
    while q:
        x, y = q.popleft()
        # 다음칸
        nx = x + dx[turn]
        ny = y + dy[turn]
        # 벽에 부딪혔을 때 종료
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            return time+1
        # 뱀이 자기 몸에 부딪혔을 때 종료
        for i in list(snake):
            snake_x, snake_y = i
            if nx == snake_x and ny == snake_y:
                return time+1
        # 뱀이 사과를 먹었을 때, 꼬리는 그대로 머리만 전진
        if apple_map[nx][ny] == True:
            time += 1
            apple_map[nx][ny] = False
            snake.append((nx,ny))
            q.append((nx,ny))
        # 뱀이 사과를 안 먹었다면, 꼬리와 머리 모두 전진
        else:
            time += 1
            snake.popleft()
            snake.append((nx,ny))
            q.append((nx,ny))
        # 시간이 지난 후 방향 전환
        for i in curve:
            second, direction = i
            # 시간이 방향 전환 시간과 일치할 경우
            if time == int(second):
                # 전환방향이 왼쪽이면 turn -1
                if direction == 'L':
                    turn -= 1
                    if turn == -5:
                        turn = -1
                # 전환방향이 오른쪽이면 turn 1
                elif direction == 'D':
                    turn += 1
                    if turn == 4:
                        turn = 0
print(bfs((0,0)))

