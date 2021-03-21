def solution(table, languages, preference):
    answer = ''
    _max = 0
    dictionary = {}
    for i in range(len(languages)):
        dictionary[languages[i]] = preference[i]
    print(dictionary)
    for i in range(len(table)):
        column = list(table[i].split())
        score = 0
        for j in column[1:]:
            if j in dictionary.keys():
                print("yes!!")
                score += dictionary.get(j)*(6-column.index(j))
                print(j,": ",score)
        if _max == 0:
            _max += score
            answer = column[0]
            print(answer)
        else:
            if _max < score:
                _max = score
                answer = column[0]
            elif _max == score:
                i = 0
                while True:
                    if answer[i] == column[0][i]:
                        continue
                    elif answer[i] > column[0][i]:
                        answer = column[0]
                        break
                    else:
                        break
    return answer

a = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
b = ["PYTHON", "C++", "SQL"]
c = [7, 5, 5]
print(solution(a,b,c))