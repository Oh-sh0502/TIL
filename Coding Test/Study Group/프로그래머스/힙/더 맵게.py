import heapq


def solution(scoville, K):
    answer = heapsort(scoville, K)
    print(answer)
    return answer


def heapsort(iterable, K):
    h = []
    result = []
    # 모든 원소를 차례로 heap에 넣기(K 이상은 제외)
    for i in iterable:
        heapq.heappush(h, i)
    return mix(h, K)


def mix(h, K):
    cnt = 0
    while h:
        print(h)
        if len(h) == 1:
            if h[0] < K:
                return -1
        first = heapq.heappop(h)
        if first < K:
            second = heapq.heappop(h)
            mix = first + 2 * second
            heapq.heappush(h, mix)
            cnt += 1
        else:
            return cnt


print("----------------------------------------")
print(solution([1, 1, 1], 4), 2)
# print(solution([10, 10, 10, 10, 10], 100), 4)
# print(solution([1, 2, 3, 9, 10, 12], 7), 2)
# print(solution([0, 2, 3, 9, 10, 12], 7), 2)
# print(solution([0, 0, 3, 9, 10, 12], 7), 3)
# print(solution([0, 0, 0, 0], 7), -1)
# print(solution([0, 0, 3, 9, 10, 12], 7000), -1)
# print(solution([0, 0, 3, 9, 10, 12], 0), 0)
# print(solution([0, 0, 3, 9, 10, 12], 1), 2)
# print(solution([0, 0], 0), 0)
# print(solution([0, 0], 1), -1)
# print(solution([1, 0], 1), 1)
print("----------------------------------------")