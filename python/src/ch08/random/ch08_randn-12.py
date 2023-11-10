import numpy as np
import random

average_height = 175
average_weight = 70
average_age = 22

sigma = 10

# 100행 3열의 행렬의 데이터를 0으로 채워줌
players = np.zeros((100, 3))
players_heights = players[:, 0] = sigma * np.random.randn(100) + average_height
players_weights = players[:, 1] = sigma * np.random.randn(100) + average_weight
players_ages = players[:, 2] = np.floor(sigma * np.random.randn(100)) + average_age


print('신장 평균값: ', np.mean(players_heights))
print('신장 중앙값: ', np.median(players_heights))

print('체중 평균값: ', np.mean(players_weights))
print('체중 중앙값: ', np.median(players_weights))

print('나이 평균값: ', np.mean(players_ages))
print('나이 중앙값: ', np.median(players_ages))
