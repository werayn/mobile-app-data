import pandas as pd

df_apple=pd.read_csv("data/apple/appList.csv")
df_google=pd.read_csv("data/google/appList.csv")



merged_df=pd.concat([df_apple,df_google])


#display columns and their types
print(merged_df.dtypes)


#display null or empty columns 
print(merged_df.columns[merged_df.isnull().all()])
      






#print(df_apple.head())
#print(df_apple.isnull.sum())


