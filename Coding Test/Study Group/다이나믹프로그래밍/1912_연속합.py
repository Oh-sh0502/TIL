# 입력
n = int(input())
seq = list(map(int, input().split()))

# sum dp테이블 생성
_sum = [0] * n
# 첫 원소 대입
_sum[0] = seq[0]

# 점화식 입력
for i in range(1, n):
    _sum[i] = max(seq[i], _sum[i-1]+seq[i])

#출력
print(max(_sum))