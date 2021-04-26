# def solution(numbers, target):
#     if not numbers and target == 0:     # 리스트가 존재하지 않고 target이 0이 되면
#         return 1                        # 1을 출력 -> 카운트
#     elif not numbers:                   # 리스트에 원소가 존재하지 않고 target이 0이 아니면:
#         return 0                        # 0을 출력 -> 노카운트
#     else:                               # 리스트의 원소가 있고 target이 0인 경우, 리스트에 원소 있고 target도 0이 아닌 경우
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
#
#
# # 다른 풀이
# from itertools import product
# def solution(numbers, target):
#     l = [(x, -x) for x in numbers]
#     s = list(map(sum, product(*l)))
#     return s.count(target)
#
# # 다른 풀이
# def solution(numbers, target):
#     q = [0]
#     for n in numbers:
#         s = []
#         for _ in range(len(q)):
#             x = q.pop()
#             s.append(x+n)
#             s.append(x+n*(-1))
#         q = s.copy()
#     return q.count(target)

def dfs(nums, i, n , t):
    ret = 0
    if i == len(nums):
        if n==t: return 1
        else: return 0
    ret += dfs(nums, i+1, n+nums[i], t)
    ret += dfs(nums, i+1, n-nums[i], t)
print(solution([1,1,1,1,1], 3))