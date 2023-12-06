# 몸무게 추정

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

regr = linear_model.LinearRegression()

X = [[164],[179],[162],[170]]  # 다중회귀에서도 사용할 수 있도록, 다차원배열로 만듬.. -> 대문자 X
y = [53, 63, 55, 59]
regr.fit(X, y)

# 학습 데이터와 y 값을 산포도로 그린다
plt.scatter(X, y, color='black')
# 학습 데이터를 입력으로 하여 예측값을 계산한다
y_pred = regr.predict(X)

# 학습 데이터와 예측값으로 선그래프로 그린다
# 계산된 기울기와 y 절편을 가지는 직선이 그려진다
plt.plot(X, y_pred, color='blue', linewidth=3)
plt.show()
