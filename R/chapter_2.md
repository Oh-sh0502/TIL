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
    >
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

