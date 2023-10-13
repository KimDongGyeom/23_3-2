def get_divisors(num):
  divisors = set()
  for i in range(2, num // 2 + 1) :
    if num % i == 0:
      divisors.add(i)
      divisors.add(num // i)
  return divisors
x = 48
print(x, get_divisors(x))
y = 60
print(y, get_divisors(y))
