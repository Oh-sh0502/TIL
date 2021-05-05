def solution(answers):
    answers=[0]+answers
    print(answers)
    answer = []
    # 문제의 길이를 구한다
    length = len(answers)
    # 각 수포자의 문제 길이만큼의 답을 뽑는다.
    one = [0,1,2,3,4,5]
    two = [0,2,1,2,3,2,4,2,5]
    three = [0,3,3,1,1,2,2,4,4,5,5]
    cnt_list = [0,0,0,0]
    k=0
    for i in range(1, length):
        if i > 5:
            k = i-(i//5)*5
            if one[k] == answers[i]:
                cnt_list[1] +=1
        else:
            if one[i] == answers[i]:
                cnt_list[1] +=1
    for i in range(1, length):
        print(i)
        if i > 8:
            k = i-(i//8)*8
            if two[k] == answers[i]:
                cnt_list[2] +=1
        else:
            if two[i] == answers[i]:
                cnt_list[2] +=1
    for i in range(1, length):
        if i > 10:
            k = i-(i//10)*10
            if three[k] == answers[i]:
                cnt_list[3] +=1
        else:
            if three[i] == answers[i]:
                cnt_list[3] +=1
    print(cnt_list)
    answer.append(1)
    max = cnt_list[1]
    for i in range(2, 4):
        if max < cnt_list[i]:
            answer = [i]
            max = cnt_list[i]
        elif max == cnt_list[i]:
            answer.append(i)
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
print(solution([5,5,5,1,4,1]))
print(solution([1, 2, 1, 1, 2]))
print(solution([1, 1,1,1]))
print(solution([1,2,5,5,2]))
print(solution([1,3,3,4,5]))