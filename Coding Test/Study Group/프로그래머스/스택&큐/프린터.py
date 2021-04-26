from collections import deque
def solution(priorities, location):
    answer = 0
    printer = [False] * len(priorities)
    printer[location] = True
    printer = deque(printer)
    priorities = deque(priorities)
    print_cnt = 0
    while priorities:
        sign = True
        out = priorities.popleft()
        for i in priorities:
            if out < i:
                priorities.append(out)
                printer.append(printer.popleft())
                sign = False
                break
        if sign:
            print_cnt += 1
            if printer[0]:
                answer = print_cnt
                break
            else:
                printer.popleft()
        # print(priorities)
        # print(printer)
    return answer

print(solution([2, 1, 3, 2],2))
print("-----------------------------------")
print(solution([1, 1, 9, 1, 1, 1],0))
print("-----------------------------------")
print(solution([3,3,4,2],3))


# 다른 사람 풀이
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer