from tkinter import *
import time

window = Tk()
window.geometry('500x200')
window.title('모니터')

label1 = Label(window, text='띵동~')
label1.pack()
label2 = Label(window, text='', font=('나눔고딕', 15))
label2.pack()
label3 = Label(window, text='', font=('나눔고딕', 15))
label3.pack()


def button1_click():
    label2.config(text='택배를 문 앞에 놓아주시면 됩니다.')


button1 = Button(window, text='택배', command=button1_click)
button1.pack()


def button2_click():
    label2.config(text='이 카드로 계산해 주세요.')


button2 = Button(window, text='배달 계산', command=button2_click)
button2.pack()

def win_init():
    label2.config(text='')
    label3.config(text='')

def win_close():
    window.destroy()

button3 = Button(window, text="초기화", fg="red", command=win_init)
button3.pack()
button4 = Button(window, text="종료", fg="red", command=win_close)
button4.pack()

window.mainloop()
