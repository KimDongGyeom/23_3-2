# 유클리드 호제법을 활용한 최대공약수
def GCD(x, y):
  while(x % y != 0):
    x, y = y, x%y
  return y
print(GCD(10, 12))

# 유클리드 호제법을 활용한 최소공배수
def LCM(x, y):
  result = (x*y) // GCD(x, y)
  return result
print(LCM(10, 12))
