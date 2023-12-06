# 몸무게 추정_문제

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import datasets

# 당뇨병 데이터 세트를 sklearn의 데이터집합으로부터 읽어들인다
diabetes = datasets.load_diabetes()

regr = LinearRegression()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(diabetes.data[:, np.newaxis, 2], diabetes.target, test_size=0.2)

# regr.fit(X, diabetes.target)
regr.fit(X_train, y_train)
print(regr.coef_, regr.intercept_)

y_pred = regr.predict(X_test)

plt.scatter(y_pred, y_test)
plt.show
