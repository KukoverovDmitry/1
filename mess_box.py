from tkinter import *
from tkinter import messagebox as mb

window = Tk()
def check():
    answer = mb.askyesno(title="Вопрос"
                         , message="Передать данные?")
    if answer:
        s = e.get()
        e.delete(0, END)
        m1["text"] = s

e = Entry(width=50) 
e.pack()

b = Button(text="Click Me", command=check)
b.pack()
m1 = Label(height=10, width=50   )
m1.pack()


window.mainloop()


