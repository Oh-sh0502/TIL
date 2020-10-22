# ggplot2는 R 시각화 1순위 패키지다. ggplot()함수를 이용해서 틀을 만들고, 그 안에 이미지 객체 레이어를 포개는 방식
#install.packages("ggplot2")
library(ggplot2)
str(airquality)
ggplot(airquality, aes(x = Day, y = Temp))

# 산점도: geom_point()
#jpeg(filename = "gg1.jpg", width=300, height=300, quality= 120)       # 번외: 이미지파일로 만들기
ggplot(airquality, aes(x = Day, y = Temp)) + geom_point()
#dev.off()

ggplot(airquality, aes(x = Day, y = Temp)) + geom_point(size = 3, color = "red")


# 꺾은선 그래프: geom_line()
ggplot(airquality, aes(x = Day, y = Temp)) + geom_line()
#둘다 붙여보자
ggplot(airquality, aes(x = Day, y = Temp)) + geom_point(size = 3, color = "red")+ geom_line


# 막대그래프: geom_bar()
ggplot(mtcars, aes(x = cyl)) +                # x축이 자연수로 연속적이게 ( 4,5,6,7,8)
  geom_bar(width = 0.5)

ggplot(mtcars, aes(x = factor(cyl))) +        # factor로 보여진 레벨만 (4, 6, 8)
  geom_bar(width = 0.5)

ggplot(mtcars, aes(x=factor(cyl))) +          # 누적 막대그래프. factor(gear) 부분은 반드시 factor를 사용. 비어있는 값이 있으면 안됨
  geom_bar(aes(fill = factor(gear)))


