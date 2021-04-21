def solution(participant, completion):
    answer = ''
    name = {}
    for i in participant:
        if i not in name:
            name[i] = 1
        else:
            name[i] += 1
    for i in completion:
        name[i] -= 1
    kv = name.items()
    for i in kv:
        if i[1] == 1:
            answer = i[0]
    return answer

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))

# 다른사람의 미친 풀이
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

# 다른사람의 미친 풀이2 (나랑 비슷한데 hash라는 기능을 넣음)
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

# 다른사람의 미친 풀이3 (정렬이 가능했다니...)
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]