import re

def solution(program, flag_rules, commands):

    flg_dict = {}
    for i in flag_rules:
        a, b = map(str, i.split())
        flg_dict[a] = b
    flg_dict_key = list(flg_dict.keys())
    flg_dict_val = list(flg_dict.values())
    answer = [True] * len(commands)
    cmd = []
    # commands의 문자열 원소를 공백기준으로 잘라 리스트 생성 및 cmd에 추가
    for i in range(len(commands)):
        cmd.append(list(commands[i].split()))

    for i in cmd:
        # 명령문의 첫 원소가 program이 아닐 경우 False를 추가
        if i[0] != program:
            answer.append(False)
            continue
        # program 다음 원소들부터
        j = 1
        while j < len(i):
            print(j)
            for k in range(len(flg_dict_key)):
                if flg_dict_val[k] == 'NULL':
                    continue
                if flg_dict_val[k] == 'NUMBER' or flg_dict_val[k] == 'NUMBERS':
                    if i[j] == flg_dict_key[k]:
                        l = 1
                        while i[j+l] not in flg_dict_key:
                            if not re.compile('[0-9]+').match(i[j+l]):
                                answer[cmd.index(i)] = False
                                break
                            l += 1
                        j = j+l
                        continue
                elif flg_dict_val[k] == 'STRING' or flg_dict_val[k] == 'STRINGS':
                    if i[j] == flg_dict_key[k]:
                        l = 1
                        while i[j+l] not in flg_dict_key:
                            if not (re.compile('[a-z]+').match(i[j+1]) or re.compile('[A-Z]+').match(i[j+1])):
                                answer[cmd.index(i)] = False
                                break
                            l += 1
                        j = j+l
                elif i[j] == '-e':
                    break
                else:
                    answer[cmd.index(i)] = False
                    break
    return answer

print(solution("line",["-s STRINGS", "-n NUMBERS", "-e NULL"],["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]))
print(solution("trip",["-days NUMBERS", "-dest STRING"],["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]))