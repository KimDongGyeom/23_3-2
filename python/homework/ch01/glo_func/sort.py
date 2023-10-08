# 오름차순 정렬된 list를 리턴
def sort_ASC(data_list):
  for i in range(len(data_list)):
    list_length = len(data_list) - i
    for j in range(1, list_length):
      if data_list[j-1] >= data_list[j]:
        temp = data_list[j-1]
        data_list[j-1] = data_list[j]
        data_list[j] = temp
  return(data_list)

# 내림차순 정렬된 list를 리턴
def sort_DESC(data_list):
  for i in range(len(data_list)):
    list_length = len(data_list) - i
    for j in range(1, list_length):
      if data_list[j-1] <= data_list[j]:
        temp = data_list[j-1]
        data_list[j-1] = data_list[j]
        data_list[j] = temp
  return(data_list)
