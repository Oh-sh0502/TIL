# 다른사람의 미친 풀이2 (나랑 비슷한데 hash라는 기능을 넣음)
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    print(dic)
    print(temp)
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))