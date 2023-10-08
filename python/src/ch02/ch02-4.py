# 초 -> 시 분 초로 바꾸기
s = int(input('여성이면 1, 남성이면 0을 입력해주세요: '))
height = int(input('키를 입력해주세요: '))
waist = int(input('허리 둘레를 입력해주세요: '))

RFM = 64 - (20 * (height / waist)) + 12 * s

print('당신의 RFM은', s, ' 입니다.')

