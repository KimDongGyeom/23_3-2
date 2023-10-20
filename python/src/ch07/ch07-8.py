import random
import string

up_str = string.ascii_uppercase
low_str = string.ascii_lowercase

n_digits = int(input('몇 자리의 비밀번호를 원하십니까?: '))

otp = ''
for i in range(n_digits) :
  otp += str(random.randrange(0, 10))
  otp += up_str[random.randrange(0, len(up_str))]
  otp += low_str[random.randrange(0, len(low_str))]

print(otp)
