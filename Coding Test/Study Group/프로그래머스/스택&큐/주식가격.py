from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()
        cnt = 0
        for i in prices:
            if c > i:
                cnt += 1
                break
            cnt += 1
        answer.append(cnt)
    return answer

print(solution([1, 2, 3, 2, 3]))