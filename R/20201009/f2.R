#함수 선언
func1 <- function(){
  print("hello")
}
func1                     # 이렇게 실행하면 함수의 정의가 나오고
func1()                   # 이렇게 실행해야 함수가 실행된다.


# 사전 함수 정의
a1 <- function(){
  # 배열 선언
  result <- c(1,2,3,4,5)
  # 출력
  return(result)
}
a2 <- function(){
  # 텍스트 가져오기
  result <- read.csv("C:/R/day04/text.txt", header = T, fileEncoding = "utf-8")
  # 출력
  return(result)
}
a3 <- function(){
  # 배열 선언
  result <- c(7,8,9,4,5)
  # 선언
  return(result)
}

# 자바스크립트 같이 함수 발동기
func1<- function(x){
  if(x ==10){
    # x = 10 이면 함수 a1 출력
    return(a1())
  }else if(x==20){
    # x = 20 이면 함수 a1 출력
    return (a2())             # return 할 때는 괄호를 열닫
  }else if(x == 30){
    # x = 30 이면 함수 a1 출력
    return(a3())
  }
}

result <- func1(10)
result

#java 연동
#install.packages("Rserve")
#Rserve::run.Rserve()          # 연동실행. 잘 안꺼진다. 따라서 나갔다 들어오는게 낫다
#Rserve::Rserve()              # 백그라운드에서 java연동

# 
Rserve::Rserve(args="--RS-enable-remote")
