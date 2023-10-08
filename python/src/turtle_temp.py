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
