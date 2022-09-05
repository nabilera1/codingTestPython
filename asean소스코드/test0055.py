# geometry()로 윈도 너비, 높이, 윈도 생성될 위치 지정
# geometry('600x400-200+300')
# -200은 모니터 화면 오른쪽 기준에서 200 위치
# +300은 모니터 화면 위쪽 기준에서 300 위치
from tkinter import *
w=Tk()
w.title("My Program")
w.geometry('600x400-200+300')
c=Canvas(bg='green', width=200, height=100)
c.place(x=30, y=30)
w.mainloop()
