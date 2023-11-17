import matplotlib.pyplot as plt
import pandas as pd

weather = pd.read_csv('src/data/csv/weather.csv', index_col=0, encoding='UTF-8')

print(weather.describe())
print('평균 분석:', weather.mean())
print('표준편차 분석:', weather.std())
print('count:', weather['최대풍속'].count())
print('count:', weather[['최대풍속', '평균풍속']].count())
