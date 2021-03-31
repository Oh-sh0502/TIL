def move(direction):
    if direction == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif direction == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif direction == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif direction == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

def dire(direction):
    if direction == 1 : return 0, 1
    elif direction == 2 : return 0, -1
    elif direction == 3 : return -1, 0
    elif direction == 4 : return 1, 0
n, m ,x, y, k = map(int, input().split())
_map = []
for _ in range(n):
    _map.append(list(map(int, input().split())))
commend = list(map(int,input().split()))
dice = [0, 0, 0, 0, 0, 0, 0]

for i in commend:
    dx, dy = dire(i)
    if 0 <= x + dx < n and 0 <= y + dy < m:
        x += dx
        y += dy
        move(i)
        if _map[x][y] != 0:
            dice[6] = _map[x][y]
            _map[x][y] = 0
        else:
            _map[x][y] = dice[6]
        print(dice[1])
