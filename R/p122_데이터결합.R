# 세로결합: bind_row()

# 엑셀 파일 불러오기
library(readxl)
m_history <- read_excel("C:/R/Rstudy/Sample2_m_history.xlsx")
f_history <- read_excel("C:/R/Rstudy/Sample3_f_history.xlsx")
View(m_history)
View(f_history)

#데이터 세트를 세로로 결합하기
exdata_bindjoin <- bind_rows(m_history, f_history)
exdata_bindjoin

# 가로 결합, left_join(), inner_join(), full_join()
library(readxl)
jeju_y17_history <-read_excel("C:/R/Rstudy/Sample4_y17_history.xlsx")
jeju_y16_history <-read_excel("C:/R/Rstudy/Sample5_y16_history.xlsx")
View(jeju_y17_history)
View(jeju_y16_history)
bind_col <- left_join(jeju_y17_history, jeju_y16_history, by = "ID")
bind_col_inner <- inner_join(jeju_y17_history, jeju_y16_history, by = "ID")
bind_col_full <- full_join(jeju_y17_history, jeju_y16_history, by = "ID")
