import os
os.system('cls') 

import tkinter as tk

def open_file():
    f = open("books.txt", encoding="utf-8")   
    s = f.read()
    text.insert(tk.END, s)

def count_words():
    f = open("books.txt", encoding="utf-8")
    s = f.read()
    text2.insert(tk.END, len(s.split()))

root = tk.Tk()
root.title("My GUI")    
root.geometry("800x800") 


text = tk.Text(root, height=10, width=50)   
text.pack(pady=40)
text2 = tk.Text(root, height=1, width=50)   
text2.pack(pady=40)

open_btn = tk.Button(root, 
                     text="Open File",
                     command= open_file
                       )
open_btn.pack(pady=20)

open_btn2 = tk.Button(root,
                     text="посчитать слова",
                    command=count_words                     )
open_btn2.pack(pady=20)








root.mainloop()
