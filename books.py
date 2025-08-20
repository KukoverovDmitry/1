import os
os.system('cls') 

f = open("books.txt", encoding="utf - 8")


for _ in range(3):
    s = f.readline().strip()

f.seek(0)    
s = (f.read()
    .replace(",","")
    .replace("\"","")
    .split())
print(max(s, key=len)   )