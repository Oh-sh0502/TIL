def solution(v):
    answer = []
    print(v)
    for i in range(3):
        for j in range(3):
            if v[i][0] != v[j][0] and v[i][1] != v[j][1]:
                center = [(v[i][0]+v[j][0])/2, (v[i][1]+v[j][1])/2]
                p1 = i
                p2 = j
            break
    for i in range(3):
        if i == p1 or i == p2:
            continue
        answer.append(2 * center[0] - v[i][0])
        answer.append(2 * center[1] - v[i][1])
    return answer


print(solution([[1, 4], [3, 4], [3, 10]]))
print(solution([[1, 1], [2, 2], [1, 2]]))