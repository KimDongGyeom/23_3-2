import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

# weather = pd.read_csv('src/data/csv/weather.csv', encoding='CP949')
weather = pd.read_csv('/Users/gimdong-gyeom/수업정리/3-2/python/src/data/csv/weather.csv', encoding='utf-8')

missing_data = weather [weather['평균풍속'].isna()] # isna() 결손값이 있을 경우, 출력 할 수 있음
print(missing_data)
