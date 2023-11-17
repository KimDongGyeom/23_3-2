import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

# weather = pd.read_csv('src/data/csv/weather.csv', encoding='CP949')
weather = pd.read_csv('/Users/gimdong-gyeom/수업정리/3-2/python/src/data/csv/weather.csv', encoding='utf-8')
weather['month'] = pd.DatetimeIndex(weather['일시']).month

# means = weather.groupby('month').mean() # 데이터의 NULL값이 있으므로, err가 발생함
# ->(수정)
numeric_columns = weather.select_dtypes(include=['float64', 'int64'])
means = numeric_columns.groupby(weather['month']).mean() # 데이터의 NULL값이 있으므로, err가 발생함
means['평균풍속'].plot(kind='bar')

plt.show()
