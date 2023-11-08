import pandas as pd

df_apple=pd.read_csv("data/apple/appList.csv")
df_google=pd.read_csv("data/google/appList.csv")


print(df_apple.head())
print(df_apple.isnull.sum())


