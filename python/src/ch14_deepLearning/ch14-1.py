# 몸무게 추정

import numpy as np
from sklearn import linear_model

regr = linear_model.LinearRegression()

X = [[164],[179],[162],[170]]  # 다중회귀에서도 사용할 수 있도록, 다차원배열로 만듬.. -> 대문자 X
y = [53, 63, 55, 59]
regr.fit(X, y)

coef = regr.coef_ # 직선의 기울기
intercept = regr.intercept_ # 직선의 절편
score = regr.score(X, y) # 학습된 직선이 데이터를 얼마나 잘 따르나

print('y =', coef, '* X + ', intercept)
print('The score of this line for the data', score)


input_data = [[180], [185], [168]]
result = regr.predict(input_data)
print('----------')
print(result)
