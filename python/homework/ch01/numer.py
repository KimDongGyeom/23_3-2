import random
# 함수 파일 위치: ./glo_fuc/ *
from glo_func import max_min
from glo_func import sort

array = random.sample(range(1, 101), 10)
# 1~100까지 10개의 원소를 가진 정렬되지 않은 list 출력
print('정렬 전: ', array)

# 최대 & 최소값 출력
print(' 최소값: ', max_min.min_val(array))
print(' 최대값: ', max_min.max_val(array))

# 정렬된 list 출력
print('오름차순 정렬:', sort.sort_ASC(array))
print('내림차순 정렬:', sort.sort_DESC(array))
