import turtle
t = turtle.Turtle()
t.shape('turtle')
t.speed('fast')
t.color("hotpink")
t.begin_fill()
for i in range(5):
   t.fd(100)
   # t.rt(288)
   t.lt(72)
   t.fd(100)
   t.rt(144)
t.end_fill()
turtle.mainloop()