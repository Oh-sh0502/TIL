# KoNLP 실행을 위해 해야할 것들..
#install.packages("KoNLP")
#install.packages("wordcloud2")
#install.packages("multilinguer")
#install.packages(c("hash", "tau", "Sejong", "RSQLite", "devtools", "bit", "rex", "lazyeval", "htmlwidgets", "crosstalk", "promises", "later", "sessioninfo", "xopen", "bit64", "blob", "DBI", "memoise", "plogr", "covr", "DT", "rcmdcheck", "rversions"), type = "binary")
#install.packages("remotes")
#remotes::install_github('haven-jeon/KoNLP', upgrade = "never", INSTALL_opts=c("--no-multiarch"))
#useSystemDic()
#library(wordcloud2)
#useNIADic()

# 사전 설정하기
library(KoNLP)
useSejongDic()

# 텍스트 파일을 데이터로 가져온 후 word_data 변수에 할당
word_data <- readLines("애국가(가사).txt")
word_data

# 명사만 추출하기
word_data2 <- sapply(word_data, extractNoun, USE.NAMES = F)
word_data2
add_words <- c("백두산","남산","철갑","가을","하늘","달")
buildDictionary(user_dic = data.frame(add_words, rep("ncn", length(add_words))),replace_usr_dic=T)

# 행렬을 벡터로 변환하기
undata <- unlist(word_data2)
undata

# 사용 빈도 확인하기
word_table <-table(undata)
word_table

# 필터링하기
undata2 <- Filter(function(x) { nchar(x) >= 2}, undata) # 두 글자 이상인 단어만 선별
word_table2 <- table(undata2)
word_table2

# 데이터 정렬하기
sort(word_table2, decreasing =T)      # 내림차순 정렬


