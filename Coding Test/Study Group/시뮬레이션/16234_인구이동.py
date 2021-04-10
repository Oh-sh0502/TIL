import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, l ,r = map(int, input().split())
world = []


for i in range(n):
    world.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def open(x,y,num,dp):
    q = deque()
    if dp[x][y] == 0:
        dp[x][y] = num
    else: return 0
    q.append((x,y))
    stack.append((x,y))
    room_sum = world[x][y]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or dp[nx][ny] != 0:
                continue
            if l <= abs(world[x][y] - world[nx][ny]) <= r:
                dp[nx][ny] = num
                room_sum += world[nx][ny]
                stack.append((nx,ny))
                q.append((nx,ny))
    room_avg = room_sum // len(stack)
    return room_avg


def change(x,y, avg_list, dp, shared_room):

    for i in range(1, shared_room+1):
        if dp[x][y] == i:
            if avg_list[i] == 0:
                continue
            world[x][y] = avg_list[i]


sol = 0


def solution(sol):
    global stack

    shared_room = 1
    avg_list = [0]
    dp = [[0] * n for _ in range(n)]

    sol += 1
    m = world[:]

    for i in range(n):
        m[i] = world[i][:]
    stack = []
    for i in range(n):
        for j in range(n):
            avg = open(i, j, shared_room, dp)
            if avg:
                for x, y in stack:
                    world[x][y] = avg
                    # print(np.array(world))
                shared_room += 1
            stack = []


    if m == world:
        print(sol -1)
        return
    else:
        return solution(sol)


solution(sol)