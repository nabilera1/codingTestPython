from tkinter import *
w=Tk()
w.title("My Button")
Label(w, text="Hello").grid()
Button(w,text="실행").grid()
# Label(w, text="Hello").grid(row=0, column=0)
# Button(w,text="실행").grid(row=0, column=1)
w.mainloop()
