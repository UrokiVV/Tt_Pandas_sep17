# Tt_Class_v3_sep22.py
import pandas as pd

df0 = pd.DataFrame({
    'ФИО       ': ['Петров А.   ', 'Ларичев Ю.  ', 'Иванов И.   ', 'Смирнов К.  ', 'Владимиров А',
                   'Машуков Д.  ', 'Попович А.  ', 'Абаковский Ю', 'Михаилов И. ', 'Кузьмин К.  '  ],
    'Математика': [   3,            4,               5,             3,             4,
                      2,            2,               2,             3,             3 ],
    'Иностр.яз.': [   5,            5,               3,             2,             0,
                      1,            1,               2,             1,             2 ],
    'Литература': [   5,            5,               5,             5,             5,
                      5,            3,               3,             5,             5 ],
    'История':    [   5,            4,               5,             5,             5,
                      3,            3,               3,             3,             3],
    'Спорт':      [   5,            5,               5,             5,             5,
                      5,            5,               5,             5,             5 ]
} )

print("----------- 1) Оценки учеников  ------------")
print(df0)

df = df0.sort_values(by="ФИО       ")
df.reset_index(drop=True, inplace=True)
print("----------- 2) Оценки учеников (Отсортированные ФИО) ------------")
print(df)
print("-----------------------")

x_mat = df['Математика'].mean()
print(f"Среднее зачение по Математике: {x_mat:.2f}")

df_mean = df.iloc[0:10, 1:7]  # срез: все ученки, оценки по всем предметам
# print("df_mean()")
print("----------- 3) среднее зачение по предметам ------------")
print(df_mean.mean())   # среднее зачение по предметам
print("----------- 4) математич. величины по предметам ------------")
print(df.describe())
print("----------- 5) медианное зачение по предметам ------------")
# print("df_median()")
print(df_mean.median())

# print("\n --- dx_res ---")
dx_res = df.describe()

dx1 = dx_res.iloc[1]  # mean
dx5 = dx_res.iloc[5]  # median
dx4 = dx_res.iloc[4]  # Q1 = 25%
dx6 = dx_res.iloc[6]  # Q3 = 75%
dx2 = dx_res.iloc[2]  # std
dx4.name = "Q1(25%)         "
dx6.name = "Q3(75%)         "
dx5.name = "median          "
for i1 in range(5):
    val = float(dx2.iloc[i1])
    dx2.iloc[i1] = round(val, 2)
    # print(dx2.iloc[i1])

# print(dx1)
# print(dx5)
# print(dx2)
dx_con = pd.concat( [dx1, dx5, dx4, dx6, dx2], axis=1)
# print("----------- 6) Объединение мат. величин по предметам ------------")
# print(dx_con)

dict_result = dx_con.to_dict('list')  # DataFrame ==> dictionary
# print("---------- dict_result --------------")
# print(dict_result)

dict2 = dict_result
df3 = pd.DataFrame(dict2, index = [ 'Математика',
                                   'Иностр.яз',  'Литература',
                                   'История',   'Спорт' ] )

df3['IQR(Q3-Q1)'] = df3["Q3(75%)         "] - df3["Q1(25%)         "]
# print("------------ df3 + IQR: ----------- ")
# print(df3)

df3_T = df3.T   # Транспонирование
print("----------- Результат: Набор данных и все мат. величины по предметам ------------")
print(df)
print(df3_T)
