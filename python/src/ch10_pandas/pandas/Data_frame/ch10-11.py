import numpy as np
import pandas as pd

# df = pd.read_csv('src/data/csv/countries.csv')
df_my_index = pd.read_csv('src/data/csv/countries.csv', index_col=0)
df_my_index['density'] = df_my_index['population'] / df_my_index['area'] # 새로운 열 생성

print(df_my_index)
