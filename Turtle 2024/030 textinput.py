import turtle
t = turtle.Turtle()
t.shape('turtle')
t.speed('fast')
t.color("hotpink")
n = turtle.textinput("모양 입력 받기", "모양을 입력하세요")
if n == 'T':
   for i in range(3):
       t.fd(100)
       t.lt(120)
elif n == 'R':
   for i in range(4):
       t.fd(100)
       t.lt(90)
else:
   # turtle.write("Input is incorrect")
   t.write("Input is incorrect")
turtle.mainloop()
# turtle.done()