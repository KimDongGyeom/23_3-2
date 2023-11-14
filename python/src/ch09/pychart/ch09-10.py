import matplotlib.pyplot as plt

hours = [8, 8, 3, 5]

hourlabels = ['Sleep', 'Study', 'Eat', 'Play']

# autopct로 백분율을 표시할 때 소수점 2번째까지 표시
# labes 매개 변수에 hourlabels list를 전달
plt.pie(hours, labels = hourlabels, autopct = '%.2f')
plt.show()
