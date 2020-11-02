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


word_data3 <- readLines("https://www.nongmin.com/news/NEWS/POL/ETC/327549/view", encoding="euc-kr")
word_data3
