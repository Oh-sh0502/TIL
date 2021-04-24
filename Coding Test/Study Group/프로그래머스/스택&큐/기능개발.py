import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        remainder = 100 - progresses[i]
        days.append(math.ceil(remainder/speeds[i]))

    days = deque(days)
    print(days)
    while days:
        front = days.popleft()
        cnt = 1
        for i in days:
            if front >= i:
                cnt += 1
            else:
                break
        if cnt > 1:
            for _ in range(cnt - 1):
                days.popleft()
        answer.append(cnt)
    return answer

print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))
print(solution([93],[1]))
print(solution([40, 93, 30, 55, 60, 65],[60, 1, 30, 5 , 10, 7]))
print(solution([93, 30, 55, 60, 40, 65],[1, 30, 5 , 10, 60, 7]))
print(solution([5, 5, 5],[21, 25, 20]))


# 다른 사람 풀이
def solution(progresses, speeds):
    Q=[]
    for p, s in zip(progresses, speeds):
        if len(Q)==0 or Q[-1][0]<-((p-100)//s):
            Q.append([-((p-100)//s),1])
        else:
            Q[-1][1]+=1
    return [q[1] for q in Q]
