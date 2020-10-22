#install.packages("readxl")
#install.packages("psych")
#install.packages("descr")
library(readxl)
library(psych)
library(descr)
y16 <- as.data.frame(read_excel("y16.xlsx"))
y17 <- as.data.frame(read_excel("y17.xlsx"))
#View(y16)
#View(y17)



bind_col_full <- full_join(y16,y17,by="ID")
bind_col_full$AREA[is.na(bind_col_full$AREA)]<-'NONE'
bind_col_full$SUM_AMT <- rowSums(bind_col_full %>% select(AMT17, AMT16),na.rm = T) 
bind_col_full$SUM_CNT <- rowSums(bind_col_full %>% select(Y17_CNT, Y16_CNT),na.rm = T)
bind_col_full <- bind_col_full %>% group_by(AREA) %>% summarise(AVG_AMT=mean(SUM_AMT),AVG_CNT=mean(SUM_CNT))
bind_col_full <- as.data.frame(bind_col_full)
bind_col_full <- bind_col_full %>% arrange(desc(AVG_AMT))


bind_col_full
plot(bind_col_full)


describe(bind_col_full)
r5 <- bind_col_full
freq_test <- freq(r5$AREA, plot = T)

hist(bind_col_full$AVG_CNT)

