# 문자열
input_hp = '010.1234.5678'

hp = '-'.join(input_hp.split('.'))
print(hp)

hp1 = input_hp.replace('.', '-')
print(hp1)


s = 'Hello, World!'

clist = list(s)
print(clist)
print(''.join(clist))

# split()은 들여쓰기, 줄바꾸기는 모두 생략됨!!!!

print(s.lower()) # 모두 소문자로
print(s.upper()) # 모두 대문자로
print(s.lower().capitalize()) # 첫번째 문자만 대문자로
