# Tt_Salary_dz_sep17.py  17.09.2024  средняя зарплата по городу
import pandas as pd

df = pd.read_csv('dz.csv')
df['City'] = df['City']. fillna ("Xxxx") # Заменили город=Nan на Xxxx
groups = df.groupby('City')

for City, df_City in groups:
    print("\n City=", City)
    print("Salary.mean=", df_City.Salary.mean())
