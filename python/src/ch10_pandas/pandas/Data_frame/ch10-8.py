import numpy as np
import pandas as pd

# df = pd.read_csv('src/data/csv/countries.csv')
df_my_index = pd.read_csv('src/data/csv/countries.csv', index_col=0)
df_no_index = pd.read_csv('src/data/csv/countries.csv')

# print(df_my_index['population'])
# print(df_no_index['population'])

# print(df_my_index[ ['area', 'population'] ])

# print('1')
# print(df_my_index.head())
# print('2')
# print(df_my_index.tail())
# print('3')
# print(df_my_index[:2])

print('1')
print(df_my_index.loc['KR'])
print('2')
print(df_my_index['population'][:3])
print('3')
print(df_my_index.loc['US', 'capital'])
print('4')
print(df_my_index['capital'].loc['US'])
