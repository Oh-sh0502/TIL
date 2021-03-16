def Solution(m,k):
    result = []
    d = [0] * len(k)                                # k가 나왔는지 방문여부
    alphabet = list(m)                              # 리스트로 쪼갬
    for i in alphabet:
        if not i in k:
            result.append(i)
        else:
            idx = k.index(i)
            if idx == 0 and d[idx] == 0:
                d[idx] = 1
                continue
            elif idx != 0 and d[idx] == 0:
                if 0 in d[:idx]:
                    result.append(i)
                else:
                    d[idx] = 1
            else:
                result.append(i)
    return ''.join(result)

print(Solution("kkaxbycyz", "abc"))
print(Solution("acbbcdc","abc"))
