def solution(numbers, hand):
    answer = ''
    left_button = [1, 4, 7]
    center_button = [2, 5, 8, 0]
    right_button = [3, 6, 9]
    phone = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    visited = [[0] * 3 for _ in range(4)]
    left_thumb = '*'
    right_thumb = '#'
    for i in numbers:
        if i in left_button:
            answer += 'L'
            left_thumb = i
        elif i in right_button:
            answer += 'R'
            right_thumb = i
        else:
            for i in range(4):
                for j in range(3):
                    if phone[i][j] == left_thumb:
                        left_start_x = i
                        left_start_y = j
                    elif phone[i][j] == right_thumb:
                        right_start_x = i
                        right_start_y = j
            left_length = dfs(left_start_x, left_start_y, i, phone, visited, 0)
            right_length = dfs(right_start_x, right_start_y, i, phone, visited, 0)
            print(left_length)
            print(right_length)
            if left_length > right_length:
                answer += 'L'
                left_thumb = i
            elif left_thumb < right_thumb:
                answer += 'R'
                right_thumb = i
            else:
                if hand == 'left':
                    answer += 'L'
                    left_thumb = i
                else:
                    answer += 'R'
                    right_thumb = i
    return answer


def dfs(x, y, end, phone, visited, length):
    if phone[x][y] == end:
        return length
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx > 3 or ny < 0 or ny > 2 or visited[nx][ny]:
            continue
        length += 1
        print(dfs(nx, ny, end, phone, visited, length))
    return 0


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))