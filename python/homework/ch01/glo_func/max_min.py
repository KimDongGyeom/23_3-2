# list 중 가장 큰 값을 리턴
def max_val(data_list):
  num = data_list[0]
  for i in data_list:
    if num < i:
      num = i
  return num

# list 중 가장 작은 값을 리턴
def min_val(data_list):
  num = data_list[0]
  for i in data_list:
    if num > i:
      num = i
  return num
