# 피보나치 함수
input_num = int(input('몇 번재 항: '))

def fivonacci(n) :
  if n <= 0:
    print('0 이하의 값을 입력하셨습니다.')
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else :
    return fivonacci(n-1) + fivonacci(n-2)

print(fivonacci(input_num))
