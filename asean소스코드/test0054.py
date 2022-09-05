#반복문을 활용하여 레이블 배치하기
from tkinter import *
w = Tk()
#3행 4열
for r in range(3):#0,1,2
    for c in range(4):#0,1,2,3
        Label(w, text='[{}.{}]'.format(r,c), borderwidth=10)\
        .grid(row=r, column=c)
w.mainloop()