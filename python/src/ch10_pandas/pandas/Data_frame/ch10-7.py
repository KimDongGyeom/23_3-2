import numpy as np
import pandas as pd

# df = pd.read_csv('src/data/csv/countries.csv')
df = pd.read_csv('src/data/csv/countries.csv', index_col=0) # index를 자동생성하지 않고, 첫 번째 열을 index로 사용
print(df)
