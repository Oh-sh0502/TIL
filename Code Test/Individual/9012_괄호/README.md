# 9012_괄호

### 문제

 괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다. 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

---

### 입력

 입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다. 각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

---

### 출력

 출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 

---

### 문제 풀이

- 세 가지 풀이가 있다

  - 풀이 1:

    괄호를 문자열로 입력 받은 후, 여는 괄호 `(`가 나오면 변수 sum에 1을 더하고, 닫는 괄호 `)`가 나오면 1을 빼준다. 만약 `sum = -1`이면, NO를 출력하고 for문을 나온다. **`(`와 `)`의 개수가 같아서 sum이 0이 되어야 하므로** sum이 양수가 나온다면 NO, 그리고 0일때는 YES를 출력시킨다.

    ```python
    a = int(input())
    for i in range(a):
        b = input()
        s = list(b)
        sum = 0
        for i in s:
            if i == '(':
                sum += 1
            elif i == ')':
                sum -= 1
            if sum < 0:
                print('NO')
                break
        if sum > 0:
            print('NO')
        elif sum == 0:
            print('YES')
    ```

  - 풀이 2:

    괄호를 문자열로 입력 받은 후에 첫 번째 원소를 검사한다. 원소가 닫는 괄호 `)`라면 VPS가  될 수 없으므로 NO를 출력한다. 그 다음 `(`가 리스트에 있다면, `(`과 `)`를 하나씩 삭제한다. 모두 삭제했을 때 리스트의 원소가 없으면 YES를 출력한다.

    ```python
    
    num = int(input())
    
    for i in range(num):
        vps = list(input())
        while len(vps) != 0:
            if vps[0] == ')':
                print('NO')
                break
            else:
                if ')' in vps:
                    vps.remove(')')
                    vps.remove('(')
                else:
                    print("NO")
                    break
        if len(vps)==0:
            print("YES")
    
    ```
  
- 풀이 3:
  스택 구조를 이용한다. 여는 괄호 `(`를 리스트에 append하고 닫는 괄호`)`를 발견하면 리스트에서 `(` 를 pop으로 제거한다. `)`를 발견했는데 리스트에 `(`가 없다면 `)`가 앞에 있는 경우와 `(`보다 많이 남아있는 경우를 모두 대변한다. NO와 YES를 리스트에 따로 담아 마지막에 출력해주면 끝.

   그리고 **`double_break`라는 boolean 값을 통해서 for문에서 빠져나가는 방법**이 인상적이었다. 필요한 스킬!

  ```python
    case = int(input())
    result = []
    
    for i in range(case):
        bracket = list(input())
        bracket_stack = []
        double_break = True
        
        for j in range(len(bracket)):
            if bracket[j] == "(":
                bracket_stack.append(bracket[j])
            else:
                try:
                    if bracket_stack.pop() == "(":
                        pass
                except:
                    result.append("NO")
                    double_break = False
                    break
    
        if len(bracket_stack):
            result.append("NO")
            continue
            
        if double_break:
            result.append("YES")
            
            
    for i in result:
        print(i)
  ```

- 느낀 점

  - 괄호가 서로 소거되야한다는 것은 유추했으나 이것을 표현해내는 것에 어려움이 있었다. 
  - 개인적으로 2번째 풀이는 remove() 함수에서 `(`가 맨 앞의 괄호가 없어지는 것이기 때문에 알맞은 쌍의 괄호가 소거되는 것이 아니어서 약점으로 보인다.
  - 풀이 1번은 간단명료하게 풀이해서 아이디어가 좋은 풀이라 생각하고, 풀이 3의 경우 코테준비를 위해 스택&큐를 자주 사용하는 입장에서 필요한 발상풀이라고 생각했다.


---

  ### 결과

![image-20210127010745230](C:\Users\oh12s\Desktop\TIL\Code Test\md-image\image-20210127010745230.png)

---

### Reference

- 풀이 1: https://pacific-ocean.tistory.com/70
- 풀이 2: https://parkssiss.tistory.com/35
- 풀이 3: https://claude-u.tistory.com/118
- 리스트 제거: https://ponyozzang.tistory.com/587

