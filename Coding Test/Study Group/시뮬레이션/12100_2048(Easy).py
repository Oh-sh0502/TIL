import numpy as np

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

def left(board):
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                temp_j = j
                while board[i][temp_j-1]==0:
                    board[i][temp_j-1] = board[i][temp_j]
                    board[i][temp_j] = 0
                    temp_j -= 1
            else:
                continue

            if board[i][j-1] == board[i][j]:
                board[i][j-1] += board[i][j]
                board[i][j] = 0
                print(np.array(board))
            else:
                x = i
                y = j
                if board[x][y-1] == 0:
                    continue
                while board[x][y-1] == 0:
                    board[x][y-1] = board[x][y]
                    board[x][y] = 0
                    print(np.array(board))
                    y -= 1
    return board


def right(board):
    before = board.copy()
    for i in range(n):
        for j in range(n-2,-1,-1):
            if board[i][j] == board[i][j+1]:
                board[i][j+1] += board[i][j]
                board[i][j] = 0
                print(np.array(board))
            else:
                x = i
                y = j
                while board[x][y + 1] == 0:
                    board[x][y + 1] = board[x][y]
                    board[x][y] = 0
                    print(np.array(board))
                    y += 1
    return board

def up(board):
    before = board.copy()
    for i in range(n):
        for j in range(1, n):
            if board[j-1][i] == board[j][i]:
                board[j-1][i] += board[j][i]
                board[j][i] = 0
                print(np.array(board))
            else:
                x = i
                y = j
                while board[y-1][x] == 0:
                    board[y-1][x] = board[y][x]
                    board[y][x] = 0
                    print(np.array(board))
                    y -= 1
    return board

def down(board):
    print(np.array(board))

    for i in range(n):
        for j in range(n-2,-1,-1):
            if board[j][i] == board[j+1][i]:
                board[j+1][i] += board[j][i]
                board[j][i] = 0
                print(np.array(board))
            else:
                x = i
                y = j
                while board[y+1][x] == 0:
                    board[y + 1][x] = board[y][x]
                    board[y][x] = 0
                    print(np.array(board))
                    y += 1
    return board


results = []
def dfs(brd):

    if brd == up(brd):
        max_up = max(map(max, brd))
        results.append(max_up)
    else:
        dfs(up(brd))
    print("------------------------------------------------------")
    if brd == down(brd):
        max_down = max(map(max, brd))
        results.append(max_down)
    else:
        dfs(down(brd))
    print("------------------------------------------------------")
    if brd == left(brd):
        max_left = max(map(max, brd))
        results.append(max_left)

    else:
        dfs(left(brd))
    print("------------------------------------------------------")
    if brd == right(brd):
        max_right = max(map(max, brd))
        results.append(max_right)

    else:
        dfs(right(brd))

dfs(board)
print(max(results))