## 2. 변수

> R에세의 데이터 타입의 기본은 벡터(vector)이다. 

* 스칼라

  * 단일 차원의 값
  * 1, 2, 3, 4, ....
  * (1,2)의 경우 2차원 값이므로 스칼라에 해당 x
  * 스칼라 데이터는 길이가 1인 벡터(배열)로 볼 수 있다.

  

* 숫자

  * 정수, 부동소수 등

  * 그냥 변수에 저장해서 변수를 올려넣거나 print() 함수로 출력 가능

  * ```R
    > print(c)
    [1] 7.5
    > c
    [1] 7.5
    
    ```
    
    

* NA

  * Not Available. 상수임

  * '데이터 값이 없음'을 뜻함. 모르는 데이터

  * is.na() 함수를 통해 NA 값이 저장되어 있는지를 알 수 있다.

    ```R
    is.na(
       x # R의 데이터 객체 
    )
    
    # NA가 저장되어 있으면 TRUE, 그렇지 않으면 FALSE
    ```

    ```R
    # 예시
    > one <- 80
    > two <- 90
    > three <- 75
    > four <- NA
    > is.na(four)
    [1] TRUE
    ```

* NULL

  * NULL 객체를 뜻함.

  * 변수가 초기화되지 않았을 때 사용한다.

  * is.null: 변수에 NULL이 저장되어 있는지를 판단

    ```R
    is.null(
       x  # R의 데이터 객체 
    )
    
    # 반환 값은 NULL이 저장되어 있으면 TRUE, 그렇지 않으면 FALSE다.
    ```

    ```R
    > x <- NULL
    > is.null(x)
    [1] TRUE
    > is.null(1)
    [1] FALSE
    > is.null(NA)
    [1] FALSE
    > is.na(NULL)
    logical(0)
    Warning message:
    In is.na(NULL) : is.na() applied to non-(list or vector) of type 'NULL'
    ```

※ NULL과 NA의 차이

NA는 값이 빠져 있는 경우 사용한다. 경측치가 존재하는 이유로는 데이터 입력 중 실수로 값을 입력하지 않은 경우, 값을 어떤 이유로든 관찰되지 못한 경우, 마지막으로 해당 항목에 적절한 값이 없어서 값이 입력되지 않는 경우에 붙는다.

NULL은 프로그래밍의 편의를 위해 미정(undefined) 값을 표현하는 데 사용하는 개념



* 문자열

  * R은 C처럼 한 개의 문자에 대한 데이터 타입이 없이 문자열로 모든 것을 표현
  * 문자열은 작은따옴표('') 또는 큰따옴표("")를 사용

  ```R
  > a <- "hello"
  > print(a)
  [1] "hello"
  > a <- 'hello'
  > print(a)
  [1] "hello"
  ```

* 진리값

  * TRUE, T: 참 값
  * FALSE, F: 거짓 값
  * &(AND), |(OR), !(NOT) 연산자 사용가능

  ```R
  > TRUE & TRUE
  [1] TRUE
  > TRUE & FALSE
  [1] FALSE
  > TRUE | TRUE
  [1] TRUE
  > TRUE | FALSE
  [1] TRUE
  > !TRUE
  [1] FALSE
  > !FALSE
  [1] TRUE
  ```

  - T, F는 원래 변수이므로 사실 T를 FALSE로, F를 TRUE로 할당하여 사용할 수 있다.

  ```R
  > T <- FALSE
  > TRUE <- FALSE		# TRUE는 FALSE로 못 바꿈. 
  Error in TRUE <- FALSE : invalid (do_set) left-hand side to assignment
  ```

  * AND나 OR 연산자에는 &, | 외에도 &&와 ||가 있다.
  *  &, |는 진릿값이 저장된 벡터(배열)끼리 연산할 때 요소별로 계산을 한다. 벡터에 저장된 진릿값 간에 대량으로 논리 연산을 수행할 때 사용한다.
  * &&, ||는 벡터의 요소 간 계산을 하기 위함이 아니라 TRUE && TRUE 등의 경우와 같이 두 개의 진릿값끼리 연산을 하기 위한 연산자다. 한 개의 진릿값만 필요한 if 문 등에서 사용한다.

  ```R
  > c(TRUE, TRUE) & c(TRUE, FALSE)
  [1] TRUE FALSE
  > c(TRUE, TRUE) && c(TRUE, FALSE)
  [1] TRUE
  ```

  * &&, ||는 쇼트서킷short-circuit을 지원한다. 따라서 A && B 형태의 코드가 있을 때 A가 TRUE라면 B도 평가하지만, A가 FALSE라면 B를 평가하지 않는다.



