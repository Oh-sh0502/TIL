from collections import deque

test = int(input())

for i in range(test):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    idx = deque(list(range(n)))
    result = [0] * n
    cnt = 1
    while queue:
        front = queue.popleft()
        front_idx = idx.popleft()
        if not queue:
            result[front_idx] = cnt
            break
        # queue 안의 최대보다 맨앞 원소가 크거나 같으면 cnt번째 인쇄실시
        if front >= max(queue):
            result[front_idx] = cnt
            cnt += 1                    # 인쇄 후 카운트 +1
        # queue 안에 맨앞 원소보다 큰 원소가 있다면 앞 원소를 뒤로 이동동
       else:
            queue.append(front)
            idx.append(front_idx)
    print(result[m])