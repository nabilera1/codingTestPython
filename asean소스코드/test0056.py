#place()로 위젯 배치하기
from tkinter import *
w=Tk()
w.title("My Button")
c=Canvas(height=300, width=600)
Label(c, text='Hello').place(x=10, y=10)
#문제 : 버튼을 x좌표 60, y좌표 90에 배치해 보세요.
Button(c, text="실행").place(x=60, y=90)
c.pack()
w.mainloop()