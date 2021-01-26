# 9093 단어 뒤집기

### 문제

문장이 주어졌을 때, 단어를 모두 뒤집어서 출력하는 프로그램을 작성하시오. 단, 단어의 순서는 바꿀 수 없다. 단어는 영어 알파벳으로만 이루어져 있다.

---

### 입력

첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있으며, 문장이 하나 주어진다. 단어의 길이는 최대 20, 문장의 길이는 최대 1000이다. 단어와 단어 사이에는 공백이 하나 있다.

---

### 출력

각 테스트 케이스에 대해서, 입력으로 주어진 문장의 단어를 모두 뒤집어 출력한다.

---

### 문제풀이

- 나의 풀이보다 다른 사람들의 풀이에 비해 너무 짧은 것에 놀랐다.
- 나의 방법은 word라는 변수에  각 단어의 알파벳을 하나하나 거꾸로 이어붙인 다음, result 리스트에 append하고 이를 순서대로 출력하는 것이었다.

```python
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sentence = sys.stdin.readline().rstrip().split()
    result = []
    for i in sentence:					# i -> I, am, happy, today
        word = ''
        for j in range(len(i)):			# j -> 0~글자수
            word += i[-1-j]				# 단어의 마지막 알파벳(i[-1])부터 word에 추가 
        result.append(word)				# 거꾸로 배열된 단어를 result에 추가
    for i in result:
        print(i, end=' ')				# 출력
```



- **두 가지**만 알았다면 더 쉽고 빠른 코드를 구성할 수 있었다.

  - `문자열.join()`: 문자열에서 괄호 () 안에 문자에 앞에 문자열을 삽입한 문자를 출력한다. 괄호 ()안이 리스트일 경우 원소 사이에 앞에 문자열을 삽입한 하나의 문자열을 출력한다.

  - `문자열[::-1]`:  콜론 슬라이싱을 이용한 것. 

    - [:] 처음부터 끝까지
    - [start:] start부터 끝까지
    - [:end] 처음부터 end-1까지 
    - [start : end] start부터 end-1 까지
    - [start : end : step] step만큼 문자를 건너뛰면서, 위와 동일하게 추출

    이를 이용하면 `[::-1]`은 **-1만큼 문자를 건너뛰어 처음부터 끝까지!**

  - 두 가지를 알았을 때 코드는 아래와 같다.

```python
n = int(input())

for _ in range(n):
    arr = list(map(list,input().split()))
    for i in arr:
        print("".join(i[::-1]),end=" ")
```



---

### 결과

---

### Reference

- 문자열 삽입(join):https://wikidocs.net/13#_12
- 콜론 슬라이싱: https://vision-ai.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EC%BD%9C%EB%A1%A0-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1-List-Slicing
- 짧은 코드풀이: https://infinitt.tistory.com/230

