# 학생 별 과목별 성적 평균을 구하시오
library(reshape2)
grade <- read.table('day03.txt',fileEncoding = 'utf-8', header=T, sep=',')
grade
str(grade)
names(grade) <- tolower(names(grade))
grade

grade2 <- melt(grade, id="name")
grade2

grade_d <- dcast(grade2, name ~ variable, mean)
grade_d

grade_d2 <- dcast(grade2, ko ~ variable, mean)