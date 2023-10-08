# 재귀함수 _ 팩토리얼
def factorial(n) :
  if n <= 1 :
    return 1
  else :
    return n * factorial(n-1)

print('4! = ', factorial(4))

'''
factorial(4) = 4 * factorial(3)
factorial(3) = 3 * factorial(2)
factorial(2) = 2 * factorial(1)
factorial(1) = 1
'''
