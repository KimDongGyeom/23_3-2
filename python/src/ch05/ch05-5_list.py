seoul = 9765
Busan = 3441
Inchenon = 2954
city_pop = [seoul, Busan, Inchenon]

Daejeon = 1531
city_pop.append(Daejeon)

print(city_pop)
print('최대 인구: ', max(city_pop))
print('최소 인구: ', min(city_pop))
print('평균 인구: ', (sum(city_pop)) / len(city_pop) )

