import turtle

t = turtle.Turtle()
t.shape('turtle')
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)

side_length = 100
angle = 360/4

for i in range(4):
  t.forward(side_length)
  t.right(angle)





turtle.done()

