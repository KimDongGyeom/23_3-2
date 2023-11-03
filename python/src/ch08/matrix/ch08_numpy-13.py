import numpy as np
# bmi = weights / heights(m단위)**2

players = [
  [170, 76.4],
  [183, 86.2],
  [181, 78.5],
  [176, 80.1]
]

np_players = np.array(players)

print('몸무게가 80이상인 선수: ')
print(np_players[np_players[:, 1] >= 80.0])
print('키가 180이상인 선수: ')
print(np_players[np_players[:, 0] >= 180.0])
