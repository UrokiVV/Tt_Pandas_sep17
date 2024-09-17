#  Tt_Pandas_IT_Jobs_sep17  17.09.2024
import pandas as pd

df = pd.read_csv('it_jobs_2030.csv')
print(df.head())

print("\n---- df.info(): ------")
print(df.info())

print("\n------df.describe(): -----")
print(df.describe())
