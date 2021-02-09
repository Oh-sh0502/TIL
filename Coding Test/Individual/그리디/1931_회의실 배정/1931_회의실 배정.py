n = int(input())
time = []                                       # 시간표리스트
for _ in range(n):
    start, end = map(int, input().split())
    time.append([start,end])                    # [시작, 끝] 리스트를 time에 저장

# 정렬방법 1
time.sort(key=lambda time: time[0])
time.sort(key=lambda time: time[1])

# 정렬방법 2

time.sort(key=lambda time:(time[0],time[1]))

cnt = 0                                         # 카운트
endtime = 0                                     # 이전 타임 끝나는 시간

for start,end in time:
    if start >= endtime:                        # 시작시간보다 이전 타임의 끝나는 시간 크거나 같으면
        cnt += 1                                # 카운트 +1
        endtime = end                           # 끝나는 시간 체인지

print(cnt)                                      # 카운트 출력