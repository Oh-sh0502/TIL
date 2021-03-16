
# 순열 이용
# from itertools import permutations
#
# n, m = map(int, input().split())
#
# result = list(permutations(range(1,n+1), m))
#
# for i in result:
#     for j in range(m):
#         print(i[j], end= ' ')
#     print()


# 백트래킹
n, m = map(int, input().split())        # n개의 수열, 길이 m

s = []                                  # 상태공간트리
def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):             # 재귀를 할꺼니까 안에 for문 필요
    if i in s:                          # 서브 조건: 중복 불가 (ex. [1,1] [3,3,3])
      continue
    s.append(i)                         # 상태 공간 트리에 추가
    f()                                 # 추가한 원소 다음 원소를 찾으러 재귀(DFS)
    s.pop()                             # 재귀함수가 위에 if문을 만나 return이 일어나고 나면 끝에 원소를 뺌
                                        # ex. n = 4 m = 3인 수열을 찾을 때, [1,2,3] [1,2,4] 찾고 끝 원소를 뺌 -> [1,2]
                                        # 그리고 다음 for문에 의해 [1,3,?]을 또 찾을 수 있음
f()

# 다른 풀이
n, m = map(int, input().split())

def f(s):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    f(s + [i])                          # 이부분을 자유롭게 할 줄 알아야함.

f([])