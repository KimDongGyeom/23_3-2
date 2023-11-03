import numpy as np

y = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
  [13, 14, 15, 16],
]

np_array = np.array(y)

print(np_array[::2, ::2])
print()
print(np_array[1::2, 1::2])

print('array[::2][::2]')
print(np_array[::2][::2]) # 첫번째 슬라이싱의 결과로, 다시 슬라이싱 -> [1, 2, 3, 4]

print('array[::2,::2]')
print(np_array[::2,::2]) # 첫번째 슬라이싱의 결과로, 다시 슬라이싱 -> [ [1, 3], [9, 11] ]

print('10이상')
print(np_array[np_array >= 10])

print('짝수:')
print(np_array[np_array % 2 == 0])

print('홀수:')
print(np_array[np_array % 2 == 1])
