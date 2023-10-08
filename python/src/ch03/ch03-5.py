import turtle, random
t = turtle.Turtle()
t.shape("turtle")

t.width(3)

def hulk():
    t.shapesize(3,3)

def normal():
    t.shapesize(1,1)

for i in range(10):
    screen = turtle.Screen()
    screen.onkeypress(hulk, "h")
    screen.onkeypress(normal, "n")
    screen.listen()
    command = random.randrange(2)
    if command == 1:
        t.left(90)
        t.forward(50)
    if command == 0:
        t.right(90)
        t.forward(50)
