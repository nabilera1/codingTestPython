import turtle
import random
t = turtle.Turtle()

def square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

square(50)
turtle.done()
# turtle.mainloop()
'''
turtle.done()은 turtle.mainloop()을 호출하는 더 사용자 친화적인 함수입니다. 
즉, turtle.done()을 사용하면 자동으로 turtle.mainloop()가 호출됩니다.
'''