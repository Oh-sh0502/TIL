from collections import deque

def solution(tickets):
    visited = [0] * len(tickets)
    route = []
    answer = dfs(tickets, 'ICN', visited,route)
    return answer

def dfs(tickets, airport, visited, route):
    start = airport
    visited[]
    route.append(start)
    if len(route) == len(tickets)+1:
        return route
    order = []
    for i in range(len(tickets)):
        if visited[i] == 1:
            continue
        if tickets[i][0] == start:
            order.append(tickets[i][1])
    print(order)
    if len(order)==0:
        route.pop()
        print("빼기",route)
    else:
        order.sort()
        print(order)
        for i in order:
            result = dfs(tickets,i, visited,route)
            if result:
                return result


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print()
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print()
print(solution([["ICN", "COO"], ["ICN", "BOO"], ["COO", "ICN"]]))
