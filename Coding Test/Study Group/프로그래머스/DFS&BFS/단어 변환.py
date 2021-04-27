
def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    visited = [0] * len(words)
    answer += dfs(begin, target, words, 0, visited)
    return answer

def dfs(b,t,w, cnt, v):
    # print(b,"||", t,"||", w,"||", cnt,"||",v)
    if b == t:
        return cnt-1
    else:
        b_alphabet = list(b)
        w_list = []
        for i in range(len(w)):
            marking = [0] * len(b)
            if v[i] == 1:
                continue
            for j in range(len(b)):
                if b_alphabet[j] == w[i][j]:
                    marking[j] += 1
            if sum(marking) == len(b)-1:
                w_list.append(w[i])
                v[i] = 1
        # print(w_list)
        if t in w_list:
            return cnt+1
        else:
            for i in w_list:
                return dfs(i, t, w, cnt+1, v)

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))
print(solution("hit","hhh",["hhh", "hht"]))
print(solution("hot","lot",["hot", "dot","dog","lot","log"]))