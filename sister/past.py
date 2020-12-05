from konlpy.tag import Okt
from collections import Counter
import csv

filename = "e:\wordcloud\data.txt"
f = open(filename, 'r', encoding='utf-8')
jeju = f.read()

# okt 객체 생성

okt = Okt()
noun = okt.nouns(jeju)
for i, v in enumerate(noun):
    if len(v) < 2:
        noun.pop(i)
count = Counter(noun)
f.close()

# 명사 빈도 카운트
noun_list_jeju = count.most_common(100)
for v in noun_list_jeju:
    print(v)

# txt 파일에 저장

with open("noun_list_jeju.txt", 'w', encoding='utf-8') as f:
    for v in noun_list_jeju:
        f.write(" ".join(map(str, v)))  # 튜플 int값을 str 타입으로 전환 후 조인
        f.write("\n")

# csv 파일에 저장
with open("noun_list_jeju.csv", "w", newline='', encoding='euc-kr') as f:
    csvw = csv.writer(f)
    for v in noun_list_jeju:
        csvw.writerow(v)


def visualize(noun_list_jeju):
    wc = WordCloud(font_path='c:\\Windows\\Fonts\\08seoulNamsanb_0.ttf',
                   background_color="white",
                   width=1000,
                   height=10000,
                   max_words=100,
                   max_font_size=300)


wc.generate_from_frequencies(dict(noun_list_jeju))
wc.to_file('keyword.png')