import matplotlib.pyplot as plt

# 우리나라의 연간 1인당 국민소득을 각각 years gdp에 저장
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [67.0, 80.0, 257.0, 1686.0, 6505.0, 11865.3, 22105.3]

# 선 그래프를 그린다. x축에서는 years값, y축에는 gdp값이 표시
plt.plot(years, gdp, color='green', marker='o', linestyle='solid')

# 제목 설정
plt.title('GDP per capita')

# x축에 레이블을 붙임
plt.xlabel('year')
# y축에 레이블을 붙인다
plt.ylabel('dooars')

# # png의 형식으로 이미지 저장 // + dpi는 300~600
# plt.savefig('gdp_per_capita.png', dpi=600)

plt.show()
