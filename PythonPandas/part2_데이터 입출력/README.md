# Part2. 데이터 입출력

### 1. 외부 파일 읽어오기

- 판다스는 다양한 형태의 외부 파일을 읽어와서 데이터프레임으로 변환하는 함수를 가지고 있다.

- **read_csv(), read_excel(), read_json()**

   ```python
   # CSV파일 -> 데이터프레임
   pandas.read_csv("파일경로(이름)")
   
   pandas.read_csv("파일경로(이름)", header=0)			# 기본값: 0행을 열 지정
   pandas.read_csv("파일경로(이름)", header=n)			# n행을 열 지정
   pandas.read_csv("파일경로(이름)", header=None)			# 행을 열 지정하지 않음
   
   pandas.read_csv("파일경로(이름)", index_col=False)		# 인덱스 지정하지 않음
   pandas.read_csv("파일경로(이름)", index_col='c0')		#'c0' 열을 인덱스 지정
   
   # Excel파일 -> 데이터프레임(read_csv와 동일한 옵션 사용가능)
   pandas.read_excel("파일경로(이름)")
   
   # JSON파일 -> 데이터프레임
   pandas.read_json("파일경로(이름)")
   ```

### 2. 웹(web)에서 가져오기

​	**2-1. HTML 웹 페이지에서 표 속성 가져오기**

​	read_html() 함수는 HTML 웹 페이지에서 <table> 태그에서 표 형식의 데이터를 모두 찾아서 데이터 프레임으로 변환한다.

   ```python
   # HTML 표 속성 읽기
   pandas.read_html("웹 주소(URL)" 또는 "HTML 파일경로(이름)")
   ```

​	**2-2. 웹 스크래핑(scraping)**

​	웹 서버에 저장된 데이터를 가져오는 행위를 말하며, BeautifulSoup 등의 도구로 수집한 데이터를 데이터프레임으로 정리한다. [2.5_us_etf_list](../Study Code & File/2.5_us_etf_list)를 참고한다.

### 3. 데이터 저장하기

   ```python
   # CSV 파일로 저장
   df.to_csv("파일 이름(경로)")
   
   # JSON 파일로 저장
   df.to_json("파일 이름(경로)")
   
   # Excel 파일로 저장
   df.to_excel("파일 이름(경로)")
   
   # 데이터프레임 여러 개를 Excel 파일로 저장(Excel 워크북 객체를 생성한다.)
   pandas.ExcelWriter("파일 이름(경로)")
   ```

---

## +α

### 1. 외부파일 읽어오기 `read_xxx()` 함수들의 옵션

<img src="C:\Users\oh12s\Desktop\TIL\Machine Learning\image\image-20210116214407141.png" alt="image-20210116214407141" style="zoom: 67%;" />

### 2. 라이브러리 

   **2-1. BeautifulSoup**

   - 프로그래밍 언어 html의 데이터를 추출할 수 있게 도와준다. 
   - 즉, html 코드들을 파이썬이 인지하게 도와준다.

   ```python
   # 라이브러리 불러오기
   from bs4 import BeautifulSoup
   ```

   

   **2-2 . requests**

   -  Python 기본 라이브러리인 urllib보다 간결한 코드로 다양한 HTTP 요청 가능

   - 크롤링할 때 요청에서 requests 이용


   ```python
   # 라이브러리 불러오기
   import requests
   # 사용방법(출처: https://rednooby.tistory.com/97)
   response = requests.get('https://www.naver.com')
                       .post
                       .put
                       .delete
                       .head
                       .options
                       .trace
   ```

​	**2-3. re**

-  정규표현식을 지원하는 라이브러리

  ``` python
  import re
  p 
  ```

  

- 정규식을 이용하여 문자열을 검색할 수 있다.

  - match(): 문자열의 처음부터 정규식과 매치되는지 조사
  - search(): 문자열 전체를 검색하여 정규식과 매치되는지 조사
  - findall(): 정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려줌
  - finditer(): 정규식과 매치되는 모든 문자열(substring)을 반복 가능한 객체로 돌려줌

- 예를 들어 공부해보자

  ``` python
  from bs4 import BeautifulSoup
  import requests
  import re
  
  resp = requests.get(url)
  soup = BeautifulSoup(resp.text, 'lxml')
  rows = soup.select('div > ul > li')
  
  for row in rows:
  	etf_name = re.findall('^(.*) \(NYSE', row,text)
      print(etf_name)
  ```

  


  ###  **※ HTTP? Get? Post?** 

   - HTTP: 웹 상에서 **클라이언트와 서버 간에 요청/응답으로 데이터를 주고 받는 프로토콜**

   ​	* 프로토콜: 공통의 데이터 교환 방법 및 순서에 대해 정의한 **의사소통 약속, 규약**

   - GET 요청: 서버로부터 **정보를 조회하기 위해 설계**된 메소드. 요청할 때 **쿼리스트링**을 통해 전송
   - POST 요청: **리소스를 생성/변경하기 위해 설계**된 메소드. **HTTP 메시지의 Body**에 담아 전송
   - Get과 Post 차이점
     - **Get**은 **Idempotent(멱등)**하도록 설계되었다. 멱등이란 `연산을 여러 번 적용하더라도 결과가 달라지지 않는 성질`로, Get으로 **서버에게 동일한 요청을 여러 번 전송한다면 동일한 응답이 돌아와야한다**. 이러한 설계원칙에 따라 **주로 조회할 때 사용**해야한다.
     - **Post**는 **Non-idempotent**하다. **서버에게 동일한 요청을 여러 번 전송하면 응답은 다를 수 있다**. 따라서 POST는 **서버의 상태나 데이터를 변경시킬 때 사용**된다. 가령 게시글 저장이나 삭제에 POST를 사용.

### ※ 정규표현식 & 메타문자

- 정규표현식: 특정한 규칙을 가진 문자열의 집합을 표현하는데 사용하는 형식 언어 

- 메타문자: 표현식 내부에서 특정한 의미를 갖는 문자

- 메타문자 문자 종류: https://brownbears.tistory.com/62

- 예를 들어서 공부해보자!

  ```
  '^(.*) \(NYSE'	-> 	'모든문자 (NYSE' 를 의미. 
  	^: 입력문자열이 시작 부분에서 위치
  	.: New Line을 제외한 모든 문자
  	*: *기호 앞의 문자나 부분식을 찾아냄
  	(.*): 소괄호는 그랩핑을 의미. 따라서 .과* 합쳐져 "모든문자열(아무 글자?)"를 의미
      \: 특수문자를 사용할 때 앞에 붙이면 그대로 사용 가능
  ```

  <img src="C:\Users\oh12s\Desktop\TIL\Machine Learning\image\image-20210116225853954.png" alt="image-20210116225853954" style="zoom:67%;" />

---

## Reference

- BeautifulSoup 관련 정보:  https://m.blog.naver.com/PostView.nhn?blogId=tjsqjavmfh&logNo=221312333469&categoryNo=75&proxyReferer=https:%2F%2Fwww.google.com%2F
- requests 관련 정보: https://rednooby.tistory.com/97
- HTTP? GET? POST?: https://hongsii.github.io/2017/08/02/what-is-the-difference-get-and-post/
- 프로토콜?: https://m.blog.naver.com/PostView.nhn?blogId=on21life&logNo=221509574568&proxyReferer=https:%2F%2Fwww.google.com%2F
- re 관련 정보: https://wikidocs.net/4308#match
- 메타문자 문자 종류: https://brownbears.tistory.com/62


   ```

   ```