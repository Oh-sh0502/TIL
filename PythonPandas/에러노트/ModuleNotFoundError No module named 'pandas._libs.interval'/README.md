# ModuleNotFoundError: No module named 'pandas._libs.interval'

### 발생원인

- [[WinError 193] %1은(는) 올바른 Win32 응용 프로그램이 아닙니다](../[WinError 193] %1은(는) 올바른 Win32 응용 프로그램이 아닙니다) 해결 후, 아래와 같은 코드를 실행함

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
  File "C:\Users\oh12s\AppData\Roaming\Python\Python38\site-packages\pandas\__init__.py", line 30, in <module>
    from pandas._libs import hashtable as _hashtable, lib as _lib, tslib as _tslib
  File "C:\Users\oh12s\AppData\Roaming\Python\Python38\site-packages\pandas\_libs\__init__.py", line 13, in <module>
    from pandas._libs.interval import Interval
ModuleNotFoundError: No module named 'pandas._libs.interval'
```

---

### 원인

역시나 로컬과 아나콘다에 각각 pandas 패키지가 있었기 때문에 발생하였다.

---

### 해결방법

로컬에 있는 pandas를 삭제하였다.

```
pip uninstall pandas
```

---

