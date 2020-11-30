sum(1:10)
mean(1:10)

d<- matrix(1:9, ncol=3) # 방향은 열벡터방향이 우선적이다
d
e<-apply(d, 1, sum)     # 행의 합
f<-apply(d, 2, sum)     # 열의 합

g<-rbind(d,총합=f)
g
str(g)


# 아이리스 데이터의 Sepal.Length, Sepal.Width, Petal.Length, Petal.Width 컬럼의 합을 구해보자. 

head(iris)
apply(iris[,1:4],2,sum)

# 리스트를 반환하는 특징의 apply 계열함수
(result <- lapply(1:3, function(x){x*2}))
result[1] 
unlist(result)  # unlist는 리스트를 벡터로 변환한다.

# lapply()는 리스트를 인자로 받을 수 있다.
x <- list(a=1:3, b=4:6)
x
lapply(x, mean)

# 데이터 프레임도 적용 가능
lapply(iris[,1:4],mean)

#colMeans(): 각 컬럼의 평균을 구하는 또 하나의 방법
colMeans(iris[,1:4])
