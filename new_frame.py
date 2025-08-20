import os
os.system('cls') 

import tkinter as tk

################
root = tk.Tk( )
root.title("ОКНО НА 3 ФРЕЙМА")

root.configure()
root.attributes("-alpha",1)

#################
frame1 = tk.Frame(root,  width=100, height=100)
frame1.pack()
frame2 = tk.Frame(root, width=100, height=100)
frame2.pack()
frame3 = tk.Frame(root,  width=100, height=100)
frame3.pack()

####################

metka = tk.Label(frame1, text="Ведите имя",  font=("Arial", 20))
metka.pack(side="left")
metka1 = tk.Label(frame2, text="Ведите отчество",  font=("Arial", 20))
metka1.pack(side="left")
metka2 = tk.Label(frame3, text="Ведите фамилию",  font=("Arial", 20))
metka2.pack(side="left")

e = tk.Entry(frame1,  font=("Arial", 20))
e.pack(side="left")
e2 = tk.Entry(frame2,  font=("Arial", 20))
e2.pack(side="left")
e3 = tk.Entry(frame3,  font=("Arial", 20))
e3.pack(side="left")

b = tk.Button(frame1, text="Ввод", font=("Arial", 20))
b.pack(side="left")
b2 = tk.Button(frame2, text="Ввод", font=("Arial", 20))     
b2.pack(side="left")   
b3 = tk.Button(frame3, text="Ввод", font=("Arial", 20))
b3.pack(side="left")


root.mainloop()
