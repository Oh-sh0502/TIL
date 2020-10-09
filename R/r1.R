sh <- read.csv(
  "shop.txt",
  header=FALSE,
  stringsAsFactors=F,
  fileEncoding = "UTF-8"
)

#colnames(sh) <- c("ID","Name","AGE","TEMP","PRICE","QT")
sh
tt <- sh$PRICE * sh$QT
tt

sh$TOTAL <- tt
sh

write.csv(
  sh,
  file="shoptotal.csv",
  row.names = T
)

save(
  sh,
  file="shoptotal.rda"
)
sht <- load("shoptotal.rda")
sht
str(sh)

tt <- sum(sh$TOTAL)
tt <- rowSums(sh[,c(4:7)],na.rm = T)
sh <- sh[]
sg
sh
