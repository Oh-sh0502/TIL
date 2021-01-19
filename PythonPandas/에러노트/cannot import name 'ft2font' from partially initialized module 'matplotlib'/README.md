# cannot import name 'ft2font' from partially initialized module 'matplotlib'

### 발생원인

- [ModuleNotFoundError No module named 'pandas._libs.interval'](../ModuleNotFoundError No module named 'pandas._libs.interval') 해결 후,  아래와 같은 코드 실행

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('./시도별 전출입 인구수.xlsx', fillna = 0, header = 0)
print(df)
```

---

### 에러문

```python
Traceback (most recent call last):
  File "C:/Users/oh12s/PycharmProjects/Pandas/example/part4/4.1_matplotlib_line1.py", line 2, in <module>
    import matplotlib.pyplot as plt
  File "C:\Users\oh12s\AppData\Roaming\Python\Python38\site-packages\matplotlib\__init__.py", line 174, in <module>
    _check_versions()
  File "C:\Users\oh12s\AppData\Roaming\Python\Python38\site-packages\matplotlib\__init__.py", line 159, in _check_versions
    from . import ft2font
ImportError: cannot import name 'ft2font' from partially initialized module 'matplotlib' (most likely due to a circular import) (C:\Users\oh12s\AppData\Roaming\Python\Python38\site-packages\matplotlib\__init__.py)
```

---

### 원인

 로컬과 아나콘다에 모두 패키지가 다운로드 되어 있어 발생

---

### 해결 방법

로컬에서 matplotlib을 삭제한다.

```
pip uninstall matplotlib
```

