"""
# 숫자
"""
# print(4*3*2*1)
# print(1/2)
# print(300-100)
# print(423 + 1234)
# print((1/100) * 1234)
# print(3.141592 * 12.0 * 12.0)


"""
# 문자
"""
# print('즐거운 ' + '파이썬 익히기')
# print('학교: ' + '영진전문대학교');
# print('학과: ' + '컴퓨터정보계열 / 일본IT학과');
# print('학번: ' + '1801030');
# print('이름: ' + '김동겸');

"""
# 반복
"""
# print('반가워요' '\n'  * 20)

"""
# 숫자 + 문자
"""
# print('100' + '200')
# print(100 + 200)

"""
거북이 그림판
"""
import turtle
t = turtle.Turtle()
t.shape('turtle')

# 삼각형
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)

# 육각형
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)
# t.forward(100)
# t.left(60)
# t.forward(100)

# 팔각형
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)
# t.left(45)
# t.forward(100)

# 미션

a = int(input('몇각형 인가요?'))

n = int(a)

for i in range(n):
    t.forward(100)
    t.left(360 / n)
turtle.done()
