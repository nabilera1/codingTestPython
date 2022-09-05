from tkinter import *
w = Tk()
w.geometry('300x200')
lbl = Label(w, text="My program", bg="green")
lbl.pack()

c = Canvas(w, width=200, height=100, bg="red")
c.place(x=50, y=50)

# btn = Button(w, text='Click!', command=w.destroy)
# btn.place(x=65, y=100)

Button(w, text='Click!', command=w.destroy).place(x=65, y=100)

w.mainloop()