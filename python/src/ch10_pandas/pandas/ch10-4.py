import csv
import matplotlib.pyplot as plt
import numpy as np

f = open('src/data/csv/weather.csv')
data = csv.reader(f)
header = next(data)

monthly_wind = [0 for x in range(12)]
days_counted = [0 for x in range(12)]

for row in data:
  month = int(row[0][5:7]) # 월에 해당하는 값을 추출
  if row[3] != '' :
    wind = float(row[3])
    monthly_wind[month -1] += wind # 추출은 1~12이나, index는 0부터 시작해서, -1을 해주어야 함!
    days_counted[month -1] += 1

for i in range(12):
  monthly_wind[i] /= days_counted[i]

x = range(1, 13)
plt.xticks(x)

plt.plot(x,monthly_wind, 'bo-')

plt.show()

f.close
