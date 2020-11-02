#install.packages('wordcloud')
#install.packages('tm')
#install.packages('RCurl')
#install.packages('RColorBrewer')


library(wordcloud2)
library(wordcloud)
library(tm)
library(RCurl)
library(RColorBrewer)
# wordcloud(데이터, 옵션)
# 기본형 워드클라우드 생성
wordcloud2(word_table2)   #word_table2는 아까 2글자 이상인 단어들을 모은 것


# 배경 등 색상 변경하기
wordcloud2(word_table2, color = "random-light", backgroundColor = "black")
wordcloud2(word_table2, fontFamily ="맑은 고딕", size =1,2, color = "random-light",
           backgroundColor = "black", shape="star")



# Viewer에 나온 워드클라우드를 플롯으로 만들어 파일에 넣기
jpeg(filename = "1p.jpg", width = 300, height = 300, quality = 120)
palate <- brewer.pal(9,"Set1")    # 색깔(9가지 색상, 색칠세트 이름)
wordcloud(names(word_table2),
          freq=word_table2,
          scale=c(5,0,5),
          rot.per=0.35,
          min.freq=1,
          random.order=F,
          random.color=T,
          colors=palate
          )
dev.off()
