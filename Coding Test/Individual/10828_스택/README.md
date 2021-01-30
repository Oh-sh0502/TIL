# 10828 스택

### 문제

 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

- push X: 정수 X를 스택에 넣는 연산이다.
- pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
- size: 스택에 들어있는 정수의 개수를 출력한다.
- empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
- top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

---

### 입력

 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

---

### 출력

출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

---

### 문제 풀이

- 조건문으로 각 명령을 코드로 정의. 

- 사용 함수: append(), len(), pop()
- input().split()으로 진행하였을 때, `시간초과`가 발생하였다. 이를 해결하기 위해 `import sys` 라이브러리를 사용하고, `imput().split()` 대신에 `sys.stdin.readline().split()`을 사용하면 더 빠르게 프로그램을 돌릴 수 있다. `sys.stdin.readline()`은 입력문에 자동으로 개행문자 `\n`이 들어가므로 이를 제거하고 싶다면 `sys.stdin.readline().rstrip()` 처럼 rstrip()을 붙여서 개행문자를 제거해준다.

```python
import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    # print(i,"번째 명령을 입력하십시오")
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        stack.append(a[1])
        # print("스택에",stack[len(stack)-1],"이 쌓였습니다. 현재 stack=",stack)
    if a[0] == 'pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
            # print("현재 stack=", stack)
    if a[0]=='size':
        print(len(stack))
    if a[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    if a[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[len(stack)-1])
```

---

### 결과

![image-20210126192508808](C:\Users\oh12s\Desktop\TIL\4차산업 선도인력\image\image-20210126192508808.png)

---

### Reference

- 문제: https://www.acmicpc.net/problem/10828
- 시간초과에 대해 문제해결: https://www.acmicpc.net/board/view/44990

