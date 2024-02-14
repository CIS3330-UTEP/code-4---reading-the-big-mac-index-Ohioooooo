import pandas as pd

df = pd.read_csv('big-mac-full-index.csv')

print(df)
print(df.columns)
print(type(df.columns))
print(len(df.columns))
