n = int(input())
w = [0]
for i in range(n):
    w.append(int(input()))

d = [0] * (n+1)
d[1] = w[1]
if n > 1:
    d[2] = w[1] + w[2]
for i in range(3, n+1):
    d[i] = max(d[i-1], d[i-3] + w[i-1] + w[i], d[i-2]+w[i])
print(d[n])

# 이건 왜 안될까?
# if n == 1:
#     print(d[1])
# else:
#     d[2] = w[1] + w[2]
# -> 와인수를 1로 하고 해봤더니 6이 두번 출력되네.. ㅋㅋㅋㅋ 이걸로 20분을 ㅜㅜ

# 이건 왜 안될까?
# if문 없이
# d[1] = w[1]
# d[2] = w[1] + w[2]
# -> w[2]가 없음..