import random

id = 'ilovepython'
pw = 'mypass1234'
input_id = input('아이디를 입력하시오: ')
input_pw = input('패스워드를 입력하시오: ')


if (input_id == id) and (input_pw == pw): print('환영합니다.')
elif (input_id != id) or (input_id != pw): print('잘못 입력하셨습니다.')
