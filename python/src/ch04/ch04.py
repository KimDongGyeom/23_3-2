# school = '영진전문대학교'
# adress = '대구 북구 복현동 / 경상북도 칠곡군'
school = input('학교를 입력해주세요: ')
adress = input('주소를 입력해주세요: ')
hp = input('전화번호를 입력해주세요: ')

def print_school_address(school, adress, hp) :
  print('----------------------------')
  print('학교: ', school)
  print('주소: ', adress)
  print('전화번호: ', hp)
  print('----------------------------')

print_school_address(school, adress, hp)


def print_star():
  print('************')

# print_star()
# print_star()
# print_star()
# print_star()
