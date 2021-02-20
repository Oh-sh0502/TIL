# read_excel() got an unexpected keyword argument 'fillna'

### 발생 상황

- [ImportError: cannot import name '_imaging' from 'PIL'](../ImportError: cannot import name '_imaging' from 'PIL') 해결 후, 아래의 코드 입력 후 발생

```python
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('./시도별 전출입 인구수.xlsx',fillna=0, header = 0)
print(df)
```

---

### 에러문

```python
Traceback (most recent call last):
  File "C:/Users/oh12s/PycharmProjects/Pandas/example/part4/4.1_matplotlib_line1.py", line 3, in <module>
    df = pd.read_excel('./시도별 전출입 인구수.xlsx',fillna=0, header = 0)
  File "C:\Users\oh12s\anaconda3\envs\my_first_env\lib\site-packages\pandas\util\_decorators.py", line 296, in wrapper
    return func(*args, **kwargs)
TypeError: read_excel() got an unexpected keyword argument 'fillna'
```

----

### 원인

- read_excel() 함수에 **`fillna`란 옵션은 없다**. 내가 공부하고 있는 책의 코드를 그대로 썼는데 정작 옵션에 `fillna`는 없다.
- 책은 아나콘다와 함께 스파이더라는 IDE를 사용하고 있다. 나는 파이참을 사용하고 있는데 그 차이가 아닐까? 아니면 이전 버전에서 바뀌었을 수도 있다.

---

### 해결 방법

- 데이터프레임에 `fillna()`라는 함수가 있다.

```python
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_excel('./시도별 전출입 인구수.xlsx', header = 0).fillna(0)
print(df)
```

---

### Reference

https://stackoverflow.com/questions/64641467/whats-the-problem-read-excel-got-an-unexpected-keyword-argument-fillna