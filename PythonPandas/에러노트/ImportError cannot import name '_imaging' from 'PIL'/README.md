# ImportError: cannot import name '_imaging' from 'PIL'

### 발생 상황

- [ModuleNotFoundError No module named 'pandas._libs.interval'](ModuleNotFoundError No module named 'pandas._libs.interval') 해결 후, 아래 코드 실행을 발생

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
  File "C:\Users\oh12s\anaconda3\envs\my_first_env\lib\site-packages\matplotlib\pyplot.py", line 36, in <module>
    import matplotlib.colorbar
  File "C:\Users\oh12s\anaconda3\envs\my_first_env\lib\site-packages\matplotlib\colorbar.py", line 44, in <module>
    import matplotlib.contour as contour
  File "C:\Users\oh12s\anaconda3\envs\my_first_env\lib\site-packages\matplotlib\contour.py", line 17, in <module>
    import matplotlib.text as text
  File "C:\Users\oh12s\anaconda3\envs\my_first_env\lib\site-packages\matplotlib\text.py", line 16, in <module>
    from .textpath import TextPath  # Unused, but imported by others.
  File "C:\Users\oh12s\anaconda3\envs\my_first_env\lib\site-packages\matplotlib\textpath.py", line 11, in <module>
    from matplotlib.mathtext import MathTextParser
  File "C:\Users\oh12s\anaconda3\envs\my_first_env\lib\site-packages\matplotlib\mathtext.py", line 27, in <module>
    from PIL import Image
  File "C:\Users\oh12s\AppData\Roaming\Python\Python38\site-packages\PIL\Image.py", line 94, in <module>
    from . import _imaging as core
ImportError: cannot import name '_imaging' from 'PIL' (C:\Users\oh12s\AppData\Roaming\Python\Python38\site-packages\PIL\__init__.py)
```

---

### 원인

 로컬과 아나콘다에 `PIL` 라이브러리가 존재해서 발생

---

### 해결 방법

로컬에 있는 `PIL`을 삭제. 명령 프롬프트에 `pip uninstall PIL`을 했더니 `WARNING: Skipping PIL as it is not installed.`  가 떠서 그냥 로컬의 site-packages 경로에서 PIL 삭제

