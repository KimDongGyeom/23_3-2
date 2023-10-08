import turtle
t = turtle.Turtle()
t.shape("turtle")

font_setting = ("Arial", 20, "bold")

t.penup()
t.goto(250, 0)
t.write("X is bigger than y", font=font_setting)
t.goto(0, 0)
t.write("X is equal to Y", font=font_setting)
t.goto(-250, 0)
t.write("Y is bigger than x", font=font_setting)

t.goto(0, 0)
t.pendown()

s1 = turtle.textinput("", "input first number: ")
num1 = int(s1)
s2 = turtle.textinput("", "input second number: ")
num2 = int(s2)

if num1 > num2:
	t.goto(250, 0)
elif num1 == num2:
	t.goto(0, 0)
else:
	t.goto(-250, 0)

turtle.done()
