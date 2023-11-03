import numpy as np

y = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
]

np_array = np.array(y)

print(y)
print(np_array)

print(np_array[0][2], np_array[0, 2]) # 동일하게 사용가능함!!

np_array[0, 0] = 12
np_array[2, 2] = 1.234 # 넌파이의 경우 같은 타입만을 저장하기 때문에, 실수가 아닌 정수값이 들어감!!
print(np_array)
print(np_array[0]) # 1첫행만 출력
print(np_array[1, 1:3]) # 5, 6
