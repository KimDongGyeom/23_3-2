fir_num = int(input('1번째 게임점수를 입력해주세요. : '))
sec_num = int(input('2번째 게임점수를 입력해주세요. : '))

# 일치 하지않는 지
# 큰 값을 고수인지 아닌지
if (fir_num == sec_num):
  print('두 값이 일치합니다.')
else:
  if (fir_num > sec_num):
    print('첫번째 유저가 고수입니다.')
  else:
    print('두번째 유저가 고수입니다.')
