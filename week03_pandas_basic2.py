import seaborn as sns
import pandas as pd

# df = sns.load_dataset('mpg')
# print(df) # drop, dropna, fillna를 각각 언제 사용해야할지 왜 써야되고 어떨 때 적용해야하는지 알고있어야 함

df1 = pd.read_csv('csv_files/bike_rentals.csv')
# print(df1.info())
# print(df1.describe())
# print(df1.describe(include='object'))

df2 = pd.read_csv('csv_files/Bookings.csv')

print(df2.info())
print(df2.describe())
print(df2.describe(include='object'))
print(df2['Review'])
