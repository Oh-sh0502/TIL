from collections import deque

n = int(input())
indegree = [0] * (n+1)                          # 진입차수 0으로 초기화

graph = [[] for i in range(n+1)]                # 간선 연결 리스트 초기화
cost = [0] * (n+1)                              # 각 건물 건설 비용을 의미하며 일단 0으로 초기화

for i in range(1, n+1):
    info = list(map(int, input().split()))      # 정보 입력
    before = info[1:info.index(-1)]             # 건물을 짓기 전에 먼저 지을 건물 번호를 따로 모은다
    cost[i] = info[0]                           # info의 첫번째 원소는 건물을 건설 비용
    for j in before:                            # 먼저 지을 건물번호을 차례대로
        graph[j].append(i)                      # "j에서 i로 테크트리 업"을 의미
        indegree[i] += 1                        # 상위건물 진입차수 1 증가

spendTime = [0] * (n+1)                         # 건물을 짓는데 걸리는 총 시간을 나타냄

# 위상 정렬 함수
def topology_sort():
    q = deque()                                 # deque 만들고
    for i in range(1, n+1):
        if indegree[i] == 0:                    # 1번 건물부터 진입차수가 0인 건물을 차례로 확인
            q.append(i)                         # 0이라면 deque에 추가
    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()                       # deque에서 하나 뺌. 그 번호의 건물에 대해
        spendTime[now] += cost[now]             # 총 소요시간에 건물의 건축 시간을 우선 더해준다.
        for i in graph[now]:                    # 그 건물의 상위 건물을 차례로 확인
            indegree[i] -= 1                    # 상위 건물 진입차수 -1
            # 총 소요시간은 상위건물의 총소요시간과 현재 지정 건물의 총 소요시간을 비교하여 최댓값. 사실 상위건물의 시간을 이전 건물의 시간으로 갱신 시켜주는 것.
            spendTime[i] = max(spendTime[i], spendTime[now])
            if indegree[i] == 0:                # 아까 진입차수를 -1하고 0이 되었다면
                q.append(i)                     # 상위 건물 번호를 deque에 추가. 루프

topology_sort()
for i in spendTime[1:]:
    print(i)


