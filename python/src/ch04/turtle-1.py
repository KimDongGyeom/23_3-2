import turtle
t = turtle.Turtle()
t.shape('turtle')

def n_polygon(n, length):
  for i in range(18):
    for i in range(n):
      t.forward(length)
      t.left(360 / n)
    t.right(20)

n_polygon(6, 100)
turtle.done()
