def solution(clothes):
    answer = 0
    dic = {}
    for i in clothes:
        if dic.get(i[1]) is None:
            dic[i[1]] = 1
        else:
            dic[i[1]] += 1
    print(dic)
    numbers = list(dic.values())
    for i in numbers:
        if answer == 0:
            answer += i+1
        else:
            answer *= (i+1)
    return answer-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))

# 다른사람 풀이

def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer
