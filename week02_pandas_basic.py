import pandas as pd
import seaborn as sns

df = pd.DataFrame(
    {"id" : [100, 102, 107],
     "math" : [99,100,97],
     "English" : [95, 92, 94]
    },
    index=[1, 2, 3] # index 옵션을 넣지 않으면 행번호가 0부터 시작
)
# print(df)

df2 = pd.DataFrame(
    [
        [100, 99, 99],
        [102, 100, 92],
        [107, 97, 94]
    ],
    index=[1, 2, 3],
    columns=["id", "math", "English"]
)
# print(df2)

df3 = pd.melt(df2)
# print(df3)

df3 = pd.melt(df2).rename(columns={'variable':'var', 'value':'val'}) # melt 후 칼럼 명을 변경하기
# print(df3)

df3 = pd.melt(df2).rename(columns={'variable':'var', 'value':'val'}).query('val>95') # val값이 95가 넘는 값만 출력할 수 있도록
# print(df3)

df1 = pd.DataFrame(
    {
        'date' : ['2025-09-13', '2025-09-13', '2025-09-14', '2025-09-15'], # 2025-09-14 -> 2025-09-15 변경 시 결측치 발생함.
        'city' : ['seoul', 'incheon', 'seoul', 'incheon'], # 15일에 해당하는 서울이 없고, 14일에 해당하는 인천이 없기 때문
        'temp' : [25, 24, 27, 24]
    },
    index=[1, 2, 3, 4]
)
# print(df1)

df2 = df1.pivot(index='date', columns='city', values='temp')
# print()
# print(df2)

df = sns.load_dataset('mpg') # mpg는 seaborn 패키지에서 제공하는 데이터셋
# print(df.tail()) # tail은 아래서부터 5개, head는 위에서부터 5개
# print(df) # 397행, 9개 열

# print(df.sort_values('mpg')) # mpg(연비) 기준으로 오름차순
# print(df.sort_values('mpg', ascending=False)) # mpg기준으로 내림차순
# print(df.drop(columns=['mpg', 'cylinders'])) # 보기 싫은 컬럼을 삭제하기


print(sns.get_dataset_names()) # seaborn 에서 제공하는 데이터셋들의 이름을 출력
titanic = sns.load_dataset('titanic')
# print(titanic)
# print(titanic[['sibsp', 'parch', 'fare']])
# print(titanic.columns)

print(titanic[titanic.age > 70]) # 70세 이상의 행만 남김
print(titanic.sample(n=7)) # 랜덤하게 7개 추출
print(titanic.nsmallest(4, 'age')) # 가장 나이가 어린 4명
print(titanic.nlargest(4, 'age')) # 가장 나이가 많은 4명

