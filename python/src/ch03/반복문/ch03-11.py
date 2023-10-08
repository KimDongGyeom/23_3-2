# num = int(input('숫자를 입력해주세요.: '))
for i in range(1, 10):
  if(i > 1): print('------------')
  for j in range(1, 10):
    print(i, '*', j, '=', i*j)
