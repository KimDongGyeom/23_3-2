# 몸무게 추정_문제

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets

# 당뇨병 데이터 세트를 sklearn의 데이터집합으로부터 읽어들인다
diabetes = datasets.load_diabetes()


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(diabetes.data[:, np.newaxis, 2], diabetes.target, test_size=0.2)
# test_size=0.2 -> 20%를 테스트에 사용


regr = LinearRegression()
# regr.fit(X, diabetes.target)
regr.fit(X_train, y_train)

score = regr.score(X_train, y_train)

# print('shape of diabetes.data: ', diabetes.data.shape) # 442*10의 형태
# print(diabetes.data)

# 특성
# print('입력데이터의 특성들')
# print(diabetes.feature_names)
# 목표값
# print('target data y:', diabetes.target.shape)
# print(diabetes.target)

# BMI값만 추출
# X = diabetes.data[:, np.newaxis, 2] # np.newaxis를 사용해, 1차원 배열 -> 다차원 배열로 바꿈
# print(X)

# regr.fit(X, diabetes.target)
regr.fit(X_train, y_train)

# score = regr.score(X_train, y_train)
# print(score)
# score = regr.score(X_test, y_test)
# print(score)

y_pred = regr.predict(X_test)

# print(y_pred)
# print(y_test)

count = 0
MSE = 0
for i in range(len(y_pred)):
  MSE += (y_pred[i] - y_test[i])**2
  count += 1
MSE = MSE/count
print(MSE)

print('Mean Squared Error: ', mean_squared_error(y_test, y_pred))
