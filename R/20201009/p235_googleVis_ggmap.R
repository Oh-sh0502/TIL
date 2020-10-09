#install.packages("googleVis")
library(googleVis)


# 움직이는 차트 생성
library(ggplot2)
# 날짜별(date) 개인 저축률의 변화(pasvert) 값을 구한 후 motion 변수에 할당
motion <- gvisMotionChart(economics, idvar = "psavert", timevar = "date")
# 그래프 그리기
plot(motion)

# 구글 지도 활용: ggmap
# 패키지 설치 및 로드
install.packages("devtools")
library(devtools)
install_github("dkahle/ggmap")
library(ggmap)
library(ggplot2)
# Google API Key 저장
googleAPIkey = "AIzaSyCf0OaMj_2ZLeKlOZO2alwc685pjyRf-Gs";
# 마포구의 위치 정보를 가져온 후 mm 변수에 할당
register_google(googleAPIkey);
mm <- get_googlemap("mapogu", maptype = "roadmap", zoom=12);
# 지도 호출
ggmap(mm)



