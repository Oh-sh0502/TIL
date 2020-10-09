#install.packages('reshape2')

# 함수 정의
stavg <- function(){
  # lib 선언
  library(dplyr)
  library(ggplot2)
  library(reshape2)
  # 자료 불러오기
  st <- read.csv("C:/R/day04/st.txt", header = T, fileEncoding = "utf-8")
  # 데이터 값을 "NAME"을 중심으로 세로 배치 (가로 합이나 가로 평균은 구하기 어렵다.)
  st <- melt(st, id.vars = "NAME")
  # 이름별 평균만을 요약하여 st에 저장
  st <- st %>% group_by(NAME) %>% summarise(TOT=sum(value), AVG=mean(value))
  # 데이터 프레임으로 전환
  sum_avg<- as.data.frame(st)
  return(sum_avg)
}
# java 연동
Rserve::Rserve(args="--RS-enable-remote")