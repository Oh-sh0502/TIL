# [WinError 193] %1은(는) 올바른 Win32 응용 프로그램이 아닙니다

### 발생 상황: 

- 아래와 같은코드를 실행함

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./시도별 전출입 인구수.xlsx', fillna = 0, header = 0)
print(df)
```

- http://blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221559824175 사이트를 참고하여 conda 가상환경을 생성하고 파이참에 연결했었음

---

### 에러문

```python
[WinError 193] %1은(는) 올바른 Win32 응용 프로그램이 아닙니다
```

---

### 원인

로컬에 다운로드한 numpy와 아나콘다의 numpy 2개가 존재하여 발생. 

---

### 해결 방법

로컬에 있는 numpy를 삭제.

```
pip uninstall numpy
```

---

### 추가 내용

- 아나콘다에 있는 패키지와 로컬에 있는 패키지 경로는 다음과 같다.
  - 아나콘다: `C:\Users\user\anaconda3\envs\가상환경\lib\site-packages`
  - 로컬: `C:\Users\user\AppData\Roaming\Python\Python38\site-packages`

---

### Reference

: https://ebbnflow.tistory.com/131