import csv

f = open('src/data/csv/weather.csv')
data = csv.reader(f)
header = next(data)

for row in data:
# (1)
#   print(row)

# (2)
  print(row[3], end=', ')
f.close
