#install.packages("Rcpp")
#install.packages("dplyr")
library(dplyr)
sh <- read.csv(
  "shop3.txt",
  header=T,
  stringsAsFactors=F,
  fileEncoding = "UTF-8"
)
sh


sh <- rename(sh,ID=TX_ID,NAME=TX_NM,AGE=TX_A,TEMP=TX_T,PRICE=TX_P,QT=TX_Q)

sh$AGE_NY <- ifelse(sh$AGE >= 25,"Y","N")
sh$AGE_HL <- ifelse(sh$AGE >= 30, "H",
                    ifelse(sh$AGE >=25, "M",
                           ifelse(sh$AGE>=20, "L","F")
                    )
)
sh

tt <- sh$PRICE * sh$QT
sh$TOTAL <- tt
sh
sh$GRADE <- ifelse(sh$TOTAL <= 10000,"B",
                   ifelse(sh$TOTAL <= 30000, "S",
                          ifelse(sh$AGE <=300000,"G","F")
                   )
)
sh
sh3 <- sh %>% filter(GRADE == 'G'& AGE_HL == 'Y')

sh4 <- sh %>% arrange(AGE)
sh4 <- sh %>% arrange(desc(AGE),MM)

smr <- sh %>% summarize(TOT = sum(PRICE), AGES = mean(AGE))

smr2 <- sh %>% group_by(NAME) %>% summarise(TOTAVG = mean(PRICE *QT))

smr3 <- as.data.frame(smr2)
