n, k = map(int,input().split())

# 코인 리스트 담기
coin = []
for _ in range(n):
    coin.append(int(input()))

# 내림차순으로 변경
coin.sort(reverse=True)
cnt = 0                     # 카운트
for i in range(len(coin)):
    if i > k:               # 남은 가치보다 동전단위가 크면 사용 못하므로 패스
        pass

    cnt += k//coin[i]       # 몫은 곧 카운트
    k = k % coin[i]         # 나머지는 곧 남은 가치

print(cnt)                  # 카운트 출력