import sys

sys.setrecursionlimit(1000000)


def U(k, num):
    if k - num < 0:
        return 0
    return k - num


def D(n, k, num):
    if k + num > n - 1:
        return n - 1
    return k + num


def C(board, k, num, deleted):
    deleted.append((k, board[k]))
    if k == len(board) - 1:
        board = board[:len(board) - 1]
        k = k - 1
    else:
        board.pop(k)
    return (k, deleted, board)


def Z(k, deleted, board):
    k_before, val = deleted.pop()
    board.append(val)
    board.sort()
    if k_before < k:
        k += 1
    return (k, board)


def solution(n, k, cmd):
    answer = ''
    board = list(range(n))
    board_before = board[:]
    deleted = []
    for i in cmd:
        if len(i) == 1:
            al = i
        else:
            al, num = i.split()
            num = int(num)
        if al == 'U':
            k = U(k, num)
        elif al == 'D':
            k = D(n, k, num)
        elif al == 'C':
            k, deleted, board = C(board, k, num, deleted)
        elif al == 'Z':
            k, board = Z(k, deleted, board)

    for i in board_before:
        if i in board:
            answer += 'O'
        else:
            answer += 'X'

    return answer

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))