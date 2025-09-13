import pandas as pd

df = pd.DataFrame(
    {"id" : [100, 102, 107],
     "math" : [99,100,97],
     "English" : [95, 92, 94]
    },
    index=[1, 2, 3] # index 옵션을 넣지 않으면 행번호가 0부터 시작
)
print(df)

df2 = pd.DataFrame(
    [
        [100, 99, 99],
        [102, 100, 92],
        [107, 97, 94]
    ],
    index=[1, 2, 3],
    columns=["id", "math", "English"]
)
print(df2)