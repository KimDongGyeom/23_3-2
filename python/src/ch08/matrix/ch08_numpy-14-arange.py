import numpy as np

# arange == array + range
# np.arange([start,] stop, [step])

# np.array(range(5)) == np.arange(5)


# linsplace() : Linearly Spaced (선형 간격으로 배열 생성)
# np.linspace(start, stop, num=50)
  # start: 생략 불가능
  # stop: stop까지 생성_stop-1(X)
  # num: 기본값은 50개

a = np.linspace(0, 49)
print(a)

# logspace()
# np.logspace(start, stop, num=50)
  # start: 생략 불가능 // 10**start
  # stop: stop까지 생성_stop-1(X) // 10**stop
  # num: 기본값은 50개

logspace_array = np.logspace(0, 5, 10)
print(logspace_array)


# reshape(행갯수, 열 갯수) ->
# flatten() -> 1차원 배열로 변경
