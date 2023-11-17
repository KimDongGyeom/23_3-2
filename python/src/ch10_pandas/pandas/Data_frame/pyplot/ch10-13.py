import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

# weather = pd.read_csv('src/data/csv/weather.csv', encoding='CP949')
weather = pd.read_csv('/Users/gimdong-gyeom/수업정리/3-2/python/src/data/csv/weather.csv', encoding='utf-8')
monthly = [ None for x in range(12)] # 달별로 구분된 12개의 데이터 프레임
monthly_wind = [ 0 for x in range(12)] # 각 달의 평균 퐁속을 담을 리스트

weather['month'] = pd.DatetimeIndex(weather['일시']).month

for i in range(12) :
  monthly[i] = weather[weather['month'] == i + 1] # 달별로 분리
  monthly_wind[i] = monthly[i]['평균풍속'].mean() # 개별 데이터 분석
m = range(1, 13)
plt.title('Monthly Average Wind speed')
plt.xlabel('Month')
plt.ylabel('Average Wind Speed')
plt.plot(m, monthly_wind, 'ro-')
plt.show()
