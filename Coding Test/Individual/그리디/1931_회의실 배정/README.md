# # 1931: 회의실 배정

### 문제

 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다. 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자. 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다. 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

<br>

---

### 문제풀이

<br>

- 시작하는 시간과 끝나는 시간의 정렬이 중요한 문제였다. 시작하는 시간과 끝나는 시간 모두 오름차순 정렬을 해야하는데, **끝나는 시간의 오름차순이 우선되어야한다.** 
   **시작하는 시간에 상관없이 끝나는 시간이 오름차순으로 정렬**되어 있어야한다. 그리고 **끝나는 시간이 일치하는 경우들에 한해서, 시작하는 시간을 비교하고 오름차순으로 정렬**한다.
-  정렬을 완성시킨 다음, 시작시간이 이전의 끝나는 시간보다 크거나 같을 때 카운트를 해주면 문제가 해결된다.

```python
n = int(input())
time = []                                       # 시간표리스트
for _ in range(n):
    start, end = map(int, input().split())
    time.append([start,end])                    # [시작, 끝] 리스트를 time에 저장

# 정렬방법 1
# time.sort(key=lambda time: time[0])           
# time.sort(key=lambda time: time[1])

# 정렬방법 2
time.sort(key=lambda time:(time[1],time[0]))

cnt = 0                                         # 카운트
endtime = 0                                     # 이전 타임 끝나는 시간

for start,end in time:
    if start >= endtime:                        # 시작시간보다 이전 타임의 끝나는 시간 크거나 같으면
        cnt += 1                                # 카운트 +1
        endtime = end                           # 끝나는 시간 체인지
        
print(cnt)                                      # 카운트 출력
```

<br>

- 여기서 코드에 따른 정렬 방식을 분석해보자.
  - ![image-20210210015842736](https://user-images.githubusercontent.com/71415474/115832992-8161b280-a44e-11eb-87fa-7eb0806ad5d2.png)
     
     <br>
      sort함수를 2번 활용한 경우 구본동작으로 적용된다. 따라서, 시작시간으로 오름차순 했다가 끝나는 시간으로 오름차순하여 결과적으로 **끝나는 시간 중심의 오름차순 정렬이 완성된다.**
     <br>
     
  - ![image-20210210020058347](https://user-images.githubusercontent.com/71415474/115833006-86266680-a44e-11eb-9ecd-d7d422df0445.png)
     <br>
    lambda에서 적용할 함수가 2개 이상일 때, 튜플에 저장하여 사용한다. 앞에 함수부터 순서대로 적용하는데, 중요한 것은 **"앞의 함수가 실행된 결과를 기준으로"**가 ㅈ적용된다. 따라서 **끝나는 시간을 오름차순한 결과를 기준으로 시작시간을 오름차순한다는 뜻이다.** 백준의 예시에서, **끝나는 시간이 모두 다르므로 오름차순 정렬은 고정되고 시작시간은 오름차순은 앞의 함수의 룰을 깰 수 없으므로 정렬이 더 이상 바뀌지 않는다.**
    <br>
    
  - ![image-20210210021042305](https://user-images.githubusercontent.com/71415474/115833021-8aeb1a80-a44e-11eb-8623-33402886a92c.png)
    <br>
    앞의 내용을 이해했다면 다음 코드가 다른 정렬을 뽑아내는 것을 알 수 있다. 위의 경우, **시작시간 오름차순을 우선으로하고 끝나는 시간의 오름차순을 적용한다.**
     **시작시간의 오름차순은 바뀌지 않으며, 시작시간이 같은 경우에만 끝나는 시간을 고려하게 된다.**
     위의 결과로 코드를 돌리면 **출력값이 3이나와 오답**이 나오게 된다.

---

### 결과

- ```python
  coin.sort(key=lambda time:(time[1], time[0]))
  ```

![image-20210210014442016](https://user-images.githubusercontent.com/71415474/115833050-93435580-a44e-11eb-863c-b3c4179a6c3f.png)



- ```python
  coin.sort(key=lambda time: time[0])
  coin.sort(key=lambda time: time[1])
  ```

![image-20210210001743773](https://user-images.githubusercontent.com/71415474/115833059-96d6dc80-a44e-11eb-898d-97a5f237b192.png)

---

### Reference

- 풀이 1: https://pacific-ocean.tistory.com/236
- 풀이 2: https://covenant.tistory.com/126
- lambda: https://wikidocs.net/64
- sort(key=lambda 인수: 함수) & 다중조건: https://dailyheumsi.tistory.com/67



