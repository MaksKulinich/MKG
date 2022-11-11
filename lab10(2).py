import os
file = 'C\\Microsoft VS Code\\lab\\QUESTIONS'
file1 = open('tiff.txt', 'w')
p = os.listdir(file)
sp = []
sp1 = []
for i in p:
    if ".png" in i:
        sp.append(i)
    if ".jpg" in i:
        sp1.append(i)
    if ".tiff" in i:
        file1.write(i + "\n")
L = len(sp)
print("Кількість файлів '.png' :", L)
print("Файли з розширенням '.jpg' :", sp1)
file1.close()                