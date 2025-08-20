import os
os.system('cls') 

f = open('fruit.txt', 'r', encoding="utf - 8"   )

s = f.read().lower().split()

d = {}

for word in s:
    d[word] = s.count(word)


#print(*d.items(), sep="\n")
sorted_items = sorted(d.items(), key=lambda x: x[1], reverse=True)
print(*sorted_items, sep="\n")
