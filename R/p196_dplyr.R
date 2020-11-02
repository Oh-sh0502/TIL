# 실습 데이터 확인
nrow(mtcars)
str(mtcars)

# 패키지 로드
install.packages("dplyr")
library(dplyr)

# filter(): 데이터 추출
filter(mtcars, cyl ==4)
filter(mtcars, cyl >=6 & mpg >20)

# arrage(): 정렬
head(arrange(mtcars, wt))
head(arrange(mtcars, mpg, desc(wt)))

# select(): 선택
head(select(mtcars, am,gear))

# mutate(): 열 추가
#mutate(데이터 세트, 추가할 열 이름 = 조건1, ...)
head(mutate(mtcars, years = "1974"))              # years 열을 추가하고 데이터 값에 1974
head(mutate(mtcars, mpg_rank = rank(mpg)))

# distinct(): 중복 값 제거
distinct(mtcars, cyl)
distinct(mtcars, gear)
distinct(mtcars, cyl, gear)

# summarise(): 데이터 요약하기
summarise(mtcars, cyl_mean = mean(cyl), cyl_min = min(cyl), cyl_max = max(cyl))
summarise(mtcars, mean(cyl), min(cyl), max(cyl))  # 열에 이름을 지을지의 차이
# 그륩별 요약
gr_cyl <- group_by(mtcars, cyl)
gr_cyl
summarise(gr_cyl, n())                 # gr_cyl에서 cyl별 개수 요약
summarise(gr_cyl, n_distinct(gear))    # gear 중복 값을 제외하고 cyl별 개수 요약 

# 데이터에서 샘플 추출
sample_n(mtcars, 10)                  # mtcars에서 10개의 샘플 데이터 추출
sample_frac(mtcars, 0.2)              # mtcars에서 20%를 샘플 데이터로 추출출


# %>%: 파이프. 연결하여 연산하는 기능
group_by(mtcars, cyl) %>% summarise(n())
mutate(mtcars, mpg_rank = rank(mpg)) %>% arrange(mp_rank, mpg_rank)
