# import tkinter as tk

import os
os.system('cls') 
#f = open("file.txt", "a", encoding="utf - 8") 

#print("Привет", file=f  )

#f.write("\nHello")  

f = open('file.txt', encoding="utf - 8")

#s = f.read()
#s = f.readlines()
s = f.read()
s = s.split('; ')

s = list(map(int, s))

#print(sum(s)/len(s))
c = 0
lts = []

for i in range(len(s)-1):
    if s[i] %3 == 0 or s[i+1] %3 == 0:
        lts.append(s[i] + s[i+1]    )


print(len(lts), max(lts))



