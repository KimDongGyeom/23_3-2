import csv

f = open('src/data/csv/weather.csv')
data = csv.reader(f)
header = next(data)

max_wind = 0.0
# a_max_wind = 0.0
# count = 0
# a = 0

for row in data:
  if row[3] == '':
    wind = 0
  else :
    wind = float(row[3]) # 평균 풍속의 최대값
  if max_wind < wind :
     max_wind = wind
# for row in data:
#   count += 1
#   if row[2] == '':
#     d_wind = 0
#   else :
#     a += float(row[2]) # 평균 풍속의 최대값
#     a_max_wind = a // count

print('지난 10년간 울릉도의 평균풍속의 최대 풍속은 ', max_wind, 'm/s')
# print('지난 10년간 울릉도의 풍속의 최대 풍속은 ', a_max_wind, 'm/s')

f.close
