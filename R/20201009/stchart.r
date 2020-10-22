#install.packages('reshape2')

# 함수 정의
stchart <- function(){
  # lib 선언
  library(dplyr)
  library(ggplot2)
  library(reshape2)
  # 자료 불러오기
  st <- read.csv("C:/R/day04/st.txt", header = T, fileEncoding = "utf-8")
  # 데이터 값을 "NAME"을 중심으로 세로 배치 (가로 합이나 가로 평균은 구하기 어렵다.)
  st <- melt(st, id.vars = "NAME")
  # 이름별 평균만을 요약하여 st에 저장
  st <- st %>% group_by(NAME) %>% summarise(AVG=mean(value))
  # 데이터 프레임으로 전환
  average<- as.data.frame(st)
  # 이미지 판 생성 (이미 폴더에 생겨있다)
  jpeg(filename = "stchart50.jpg", width=300, height=300, quality= 120)       # 번외: 이미지파일로 만들기
  # 그래프 그리기
  p<-ggplot(average, aes(x=NAME, y=AVG)) + geom_col(color="red")
  # 그래프 붙이기
  print(p)
  # 연결 끊기
  dev.off()
}
# java 연동
Rserve::Rserve(args="--RS-enable-remote")
