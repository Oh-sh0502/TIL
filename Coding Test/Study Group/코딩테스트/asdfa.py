def solution(enter, leave):
    answer = []
    i = 0
    j = 0
    room = []
    seen = [set() for _ in enter]
    while True:
        room.append(enter[i])
        if len(room) > 1:
            for x in range(len(room)):
                for y in range(i+1,len(room)):
                    seen[x].add(y)
                    seen[y].add[x]
                    i += 1
        while leave[0] in room:
            room.remove(leave[0])
    return answer

print(solution([1,3,2],[1,2,3]))