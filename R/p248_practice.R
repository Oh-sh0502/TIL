#install.packages("readxl")
library(readxl)
library(dplyr)
library(reshape2)
#1
middle_mid_exam <- read_excel("C:/R/Rstudy/middle_mid_exam.xlsx")

#2
MATHEMATICS <- middle_mid_exam %>% select(CLASS, ID, MATHEMATICS)
MATHEMATICS <- dcast(MATHEMATICS, ID~CLASS)
MATHEMATICS

ENGLISH <- middle_mid_exam %>% select(CLASS, ID, ENGLISH)
ENGLISH <- dcast(ENGLISH, ID~CLASS)
View(ENGLISH)

#3
middle_mid_exam %>% group_by(CLASS) %>% summarise(SUM_MATH=sum(MATHEMATICS), SUM_ENG=sum(ENGLISH), 
                                                  AVG_MATH=mean(MATHEMATICS),
                                                  AVG_ENG=mean(ENGLISH))
#4
middle_mid_exam %>% group_by(MATHEMATICS) %>% filter(CLASS=='class1'& MATHEMATICS>=80)
filter(MATHEMATICS, class1 >=80) %>% summarise(n())

#5
arrange(middle_mid_exam, MATHEMATICS, desc(ENGLISH))

#6
filter(middle_mid_exam, MATHEMATICS >=80, ENGLISH >=85) %>% summarise(n())
