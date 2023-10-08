import random

print('1~100까지의 숫자를 맞추시오')
num = 0
count = 0
a = random.randint(1, 100)
while num != a:
  num = int(input('숫자를 입력하세요: '))
  count += 1
  if(num > a): print('입력 수 보다 작음')
  if(num < a): print('입력 수 보다 큼')
if num == a: print('축하합니다.', '총 횟수: ',count)
