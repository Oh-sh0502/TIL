import re

def solution(program, flag_rules, commands):
    answer = []
    cmd = []
    for i in range(len(commands)):
        cmd.append(list(commands[i].split()))
    for i in cmd:
        if i[0] != 'line':
            answer.append(False)
            continue
        for j in range(1,len(i) ,2):
            if i[j] == '-n':
                if not re.compile('[0-9]+').match(i[j+1]):
                    answer.append(False)
                    break
            elif i[j] == '-s':
                if not (re.compile('[a-z]+').match(i[j+1]) or re.compile('[A-Z]+').match(i[j+1])):
                    answer.append(False)
                    break
                else:
                    answer.append(True)
                    break
            elif i[j] == '-e':
                answer.append(True)
                break
            else:
                answer.append(False)
                break
    return answer

print(solution("line",["-s STRING", "-n NUMBER", "-e NULL"],["line -n 100 -s hi -e", "lien -s Bye"]))
print(solution("line",["-s STRING", "-n NUMBER", "-e NULL"],["line -s 123 -n HI", "line fun"]))