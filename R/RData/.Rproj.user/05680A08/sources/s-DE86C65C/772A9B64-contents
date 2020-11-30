x<-read.csv("a.csv");
x;
str(x);  #tr(객체) : 데이터 구조, 변수 개수, 변수 명, 관찰치 개수, 관찰치의 미리보기

(y<-read.csv("b.csv",header = FALSE))  # 겉에 괄호를 치면 실행결과도 같이 나옴
y
names(y)<-c("id","name","score")
y
str(y)
y$name<-as.character(y$name)
str(y)

z<-read.csv("a.csv", stringsAsFactors = FALSE)
z
str(z)

# score  컬럼이 팩터가 아닌 int형 데이터가 되게하는 방법
(m<-read.csv("c.csv", na.strings=c("NIL")))
str(m)
is.na(m$score)

write.csv(m, "d.csv",row.names=FALSE) # 행 이름은 제외하고 파일에 저장
n<-read.csv("d.csv")
n

write.csv(x, "e.csv") # 첫 번째 컬럼이 행 번호 1,2,3을 의미. 그러나 꼭 필요한 정보가 아니면 생략하자.
(l<-read.csv("e.csv"))




