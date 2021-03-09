# 정수 N, M을 입력받기 (1<=n<=100, 1<=m<=10000)
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력받기
coin = []
for i in range(n):
    coin.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m+1)

# 다이나믹 프로그래밍: 보텀업
d[0] = 0
for i in range(n):
    for j in range(coin[i], m+1):   # 첫번째 화폐단위부터 최종 M까지.. 첫번째 화폐 이전의 값은 첫번째 화폐로 계산 가
        if d[j-coin[i]] != 10001:   #(i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - coin[i]] +1)

if d[m] == 10001:   # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])

# 입력예시
# 2 15    |      3 4
# 2       |      3
# 3       |      5
#         |      7
# 출력예시
# 5       |      -1