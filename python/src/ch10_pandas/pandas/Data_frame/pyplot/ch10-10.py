import matplotlib.pyplot as plt
import pandas as pd

weather = pd.read_csv('src/data/csv/weather.csv', index_col=0, encoding='UTF-8')

# countries_df['population'].plot(kind='bar', color=('b', 'darkorange', 'g', 'r', 'm'))
weather['평균풍속'].plot(kind='hist', bins=15)

plt.show()
