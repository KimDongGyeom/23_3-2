# 몸무게 추정_문제

import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

regr = linear_model.LinearRegression()

X = [[164, 1],[167, 1],[165, 0],[170, 0], [179, 0], [163, 1], [159, 0], [166, 1]]  # 다중회귀에서도 사용할 수 있도록, 다차원배열로 만듬.. -> 대문자 X
y = [43, 48, 47, 66, 67, 50, 52, 44]
regr.fit(X, y)

print('계수:', regr.coef_)
print('절편:', regr.intercept_)
print('점수:', regr.score(X, y))
print('은지와 동민이의  추정 몸무게:', regr.predict([[166, 1], [166, 0]]))

