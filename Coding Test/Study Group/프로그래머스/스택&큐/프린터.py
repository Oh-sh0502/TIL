from collections import deque
def solution(priorities, location):
    answer = 0
    printer = [False] * len(priorities)
    printer[location] = True
    printer = deque(printer)
    priorities = deque(priorities)
    while priorities:
        sign = True
        out = priorities.popleft()
        for i in priorities:
            if out < i:
                priorities.append(out)
                printer.append(printer.popleft())
                # sign = False
                break
        # if sign:
        #     printer.append(out)

    print(printer)
    answer = printer.index(True) + 1
    return answer

print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))