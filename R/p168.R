#install.packages('reshape2')
# 세트 구조 파악하기
head(airquality)
# 몇 행 몇 열
dim(airquality)
# 상세 구조 확인하기
str(airquality)

# 소문자로 변환한 변수명으로 기존 변수명 대체
names(airquality) <- tolower(names(airquality))
head(airquality)

# 패키지 로드 및 melt()함수 실행
library(reshape2)                   # reshope2 패키지 로드
melt_test <- melt(airquality)
head(melt_test)
tail(melt_test)

# 월과 바람에 따른 오존 확인하기
melt_test2 <- melt(airquality, id.vars = c("month", "wind"), measure.vars = "ozone")
head(melt_test2)

# 선생님 예시: 월과 일에 따른 오존 확인하기
melt_test3 <- melt(airquality, id.vars=c("month", "wind"), measure.vars=c("ozone"))
head(melt_test3)

# 번외: na를 0으로
# melt_test3[is.na(melt_test3)] <- 0
# melt_test3

