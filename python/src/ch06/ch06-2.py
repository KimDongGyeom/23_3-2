items = {
  '커피음료': '7',
  '펜': '3',
  '종이컵': '2',
  '우유': '1',
  '콜라': '4',
  '책': '5'
}

input_data = int(input('메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료: '))

# 재고 조회
if(input_data == 1) :
  input_data = (input('물건의 이름을 입력해주세요: '))
  print('재고: ', items[input_data])
  input_data = int(input('메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료: '))

if(input_data == 2) :
  종류, 재고 = input('물건의 이름과 수량을 입력하시오: ').split()
  items[종류] = int(items[종류]) + int(재고)

  print(items[종류])
  input_data = int(input('메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료: '))

if(input_data == 3) :
  종류, 재고 = input('물건의 이름과 수량을 입력하시오: ').split()
  items[종류] = int(items[종류]) - int(재고)
  print(items[종류])
  input_data = int(input('메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료: '))

if(input_data == 4) :
  print('프로그램을 종료합니다.')

