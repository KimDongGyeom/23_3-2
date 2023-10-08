import random

player1 = input('Player1의 이름: ')
player2 = input('Player2의 이름: ')
print('.....주사위를 굴립니다.....')

num1 = random.randint(1, 6)
num2 = random.randint(1, 6)

print(player1, '의 주사위 번호는', num1)
print(player2, '의 주사위 번호는', num2)

if num1 == num2: print('비겼습니다.')
if num1 > num2:
  print(player1,'이/가 이겼습니다.')
else:
  print(player2,'이/가 이겼습니다.')
