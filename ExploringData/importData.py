import pandas as pd

df = pd.read_csv('./ExploringData/data/literary_birth_rate.csv')

# firts lines
print(df.head())
# last lines
print(df.tail())
# column index
print(df.columns)
# amount of rows and columns
print(df.shape)
# info from dataframe
print(df.info())