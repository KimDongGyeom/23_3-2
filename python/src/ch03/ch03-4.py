import turtle
t = turtle.Turtle()
t.shape("turtle")

t.width(3)

while True:
	s = input('명령을 입력해주세요.')
	if (s == 'r'):
		t.right(90)
		t.forward(100)
	if (s == 'l'):
		t.left(90)
		t.forward(100)
