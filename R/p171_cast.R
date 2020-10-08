# cast: 세로로 긴 데이터 모양을 가로로!

# dcast: 데이터프레임 형태로 처리 가능
# dcast(데이터 세트, 기준 열 ~ 변환 열)

# 변수명 소문자로 통일하기
names(airquality) <- tolower(names(airquality))
head(airquality)

# melt() 함수 호출하기
aq_melt <- melt(airquality, id = c("month","day"),na.rm = TRUE)
head(aq_melt)

# dcats() 함수 호출하기
aq_dcast <- dcast(aq_melt, month + day ~ variable)
head(aq_dcast)

# 평균구하기
aq_dcast2 <- dcast(aq_melt, month ~ variable, mean)
head(aq_dcast2)


#-------------------------------------------------------------------------------
# acast: 벡터, 행렬, 배열 형태를 변환
# acast(데이터 세트, 기준 열 ~ 반환 열~분리 기준 열)

acast(aq_melt, day ~ month ~ variable)

