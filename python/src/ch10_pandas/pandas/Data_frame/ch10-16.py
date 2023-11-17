import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

# weather = pd.read_csv('src/data/csv/weather.csv', encoding='CP949')
weather = pd.read_csv('/Users/gimdong-gyeom/수업정리/3-2/python/src/data/csv/weather.csv', index_col=0, encoding='utf-8')

new_data = weather[:]

# new_data.dropna(axis = 0, how='any', inplace=False)
# new_data.fillna(0, inplace=False)
new_data.fillna(weather['평균풍속'].mean(), inplace=True)

print(new_data.isna())
