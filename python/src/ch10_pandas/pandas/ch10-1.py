import csv

f = open('/Users/gimdong-gyeom/수업정리/3-2/python/src/ch10_pandas/data/csv/weather.csv')
data = csv.reader(f)

for row in data:
  print(row)
f.close
