# 어떤 인풋
n = int(input())
# 상태공간트리
s = []

# 원리
def f():
    # 이 부분(for문 앞)에 문제상황에 맞는 조건을 찾는 로직 필요
    if True:
        # 조건 코드 어쩌구 -> 답을 찾고 return
        return
    for i in range(1, n + 1):
      s.append(i)                   # 다음 원소를 추가하고
      f()                           # 함수 재귀를 진행 -> 원하는 바를 찾는다
      s.pop()                       # 함수가 리턴 되면 추가했던 원소를 빼고 백트래킹