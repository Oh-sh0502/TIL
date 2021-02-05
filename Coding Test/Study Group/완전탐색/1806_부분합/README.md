# # 1806: 부분합

### 문제

10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

---

### 문제풀이

- 완전탐색으로는 시간 제한을 만족시킬 수 없다는 것이 핵심이다. [2003번_수들의 합2](../2003_수들의 합2)

에서는 N이 최대 10000이므로 pypy3라도 가능했으나, 이 문제는 N이 최대 100000이다. 따라서 시간복잡도 O(N<sup>2</sup>), 5000050000 번의 탐색으로 본 문제를 해결할 수 없다.

- 위 문제는 **투 포인터 알고리즘**을 사용해서 해결한다. 투 포인터는 시간복잡도 O(N)으로 문제를 해결 가능하다. 알고리즘 원리는 다음과 같다.

<img src="C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210205120000040.png" alt="image-20210205120000040" style="zoom:50%;" />

-  [동빈나님의 투포인터](https://www.youtube.com/watch?v=ttLRltNDiCo&feature=emb_title) 코드 예시에서 interval_sum == m을 interval_sum >=m 로 바꿔주고, 조건을 만족시키는 그룹의 길이를 리스트에 모아서 그 중 최솟값을 구하였다. python3, pypy3 모두 답이 나온다!
   중요한 것은 **길이 리스트의 원소가 0개일 수도 있다는 점을 간과하지 말 것!**

``` python

n, s = map(int, input().split())

seq = list(map(int, input().split()))

# cnt = 0
# sum = 0
# cntlist = []
#
# for i in range(n):
#     sum += seq[i]
#     cnt += 1
#     if sum == s:
#         cntlist.append(cnt)
#     for j in range(i+1,n):
#         sum += seq[j]
#         cnt += 1
#         if sum == s:
#             cntlist.append(cnt)
#     sum = 0
#     cnt = 0
#
# print(min(cntlist))
# 시간 초과가 뜬다 ....

##############################################

# 투포인터 풀이
sum = 0
end = 0
length=[]
for start in range(n):
    while sum < s and end < n:
        sum += seq[end]
        end += 1
    if sum >= s:							# 부분합 s 이상
        length.append(end-start)			# 시작점과 끝점의 차를 length 리스트에 저장
    sum -= seq[start]

if len(length)==0:							# length 리스트에 아무것도 담기지 않을 수 있다.
    print(0)								# 반례: 10 15 /n 1 1 1 1 1 1 1 1 1 1
else:
    print(min(length))						# length 리스트에서 최솟값 출력

```



- 추가적으로 틀린 답을 고쳐나갈 때 **백준의 "질문검색"**에서 반례들을 구해 돌려보는게 좋은 듯하다!

---

### 결과

<img src="C:\Users\oh12s\Desktop\TIL\Coding Test\md-image\image-20210205123827517.png" alt="image-20210205123827517" style="zoom:200%;" />

---

### Reference

- 동빈나 이코테 39강. 투포인터: https://www.youtube.com/watch?v=ttLRltNDiCo&feature=emb_title