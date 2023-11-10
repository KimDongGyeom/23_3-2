import matplotlib.pyplot as plt

x = [i for i in range(-10, 11)]
y = [2*i for i in x]

plt.plot(x, y, color='green', marker='o', linestyle='solid')

# 제목 설정
plt.title('y = 2x')

# x축에 레이블을 붙임
plt.xlabel('x')
# y축에 레이블을 붙인다
plt.ylabel('y')

# 그림을 그릴 영역을 지정
plt.axis([-25, 25, -25, 25]) # x축 (-25 ~ 25) / y축 (-25 ~ 25)
plt.show()
