# 라이브러리 불러오기
import seaborn as sns

# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')

# for 반복으로 각 열의 NaN 개수 계산하기
missing_df = df.isnull()
print(missing_df)
for i in missing_df.columns:
    missing_count = missing_df[i].value_counts()            # 각 열의 데이터 개수 파악
    print(missing_count)
    try:
        print(i, ': ', missing_count[True])                 # NaN 값이 있으면 개수 출력
    except:
        print(i, ': ', 0)                                   # NaN 값이 없으면 0개 출력


# NaN 값이 500개 이상인 열을 모두 삭제 - deck 열(891개 중 688개의 NaN 값)
df_thresh = df.dropna(axis=1, thresh=500)

# age 열에 나이 데이터가 없는 모든 행 삭제 - age 열(891개 중 177개의 NaN 값)
df_age = df.dropna(subset=['age'], how='any', axis=0)
print(len(df_age))

