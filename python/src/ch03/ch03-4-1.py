import turtle
t = turtle.Turtle()
t.shape("turtle")

t.width(3)

while True:
	s = input('명령을 입력해주세요.')

	if (s == 'f'):
		t.forward(100)
	if (s == 'h'):
		t.shapesize(10, 10)
	if (s == 'n'):
		t.shapesize(3, 3)
