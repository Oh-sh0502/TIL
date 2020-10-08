#install.packages("dplyr")
library("dplyr")

# 필요한 데이터 추출하기: select, filter
# select(): 필요한 변수만 별도로 추출할 때 사용
exdata1<- read_excel("C:/R/Rstudy/Sample1.xlsx")
names(exdata1)<-tolower(names(exdata1))
exdata1 %>% select(id)
exdata1 %>% select(id, area, y17_cnt)
exdata1 %>% select(-area)
exdata1 %>% select(-area, -y17_cnt)


# filter(): 필요한 '조건'에 맞는 데이터만 추출하여 분석
exdata1 %>% filter(area=='서울')
exdata1 %>% filter(area == '서울' & y17_cnt >= 10) 


# 데이터 정렬하기: arrange
exdata1 %>% arrange(age)
exdata1 %>% arrange(desc(y17_cnt))
exdata1 %>% arrange(age, desc(y17_cnt))


# 데이터 요약하기: summarise, group by
exdata1
exdata1 %>% summarise(tot_y17_amt=sum(amt17))
# A tribble: 1 x 1 의 의미는 출력되는 데이터 세트가 1행 1열임을 의미한다.

exdata1 %>% group_by(area) %>% summarise(sum_y17_amt = sum(amt17))


