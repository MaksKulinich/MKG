from array import *
mas = array('i',[])
for i in range(10):
    y = int(input("Введіть eлементи масиву "))
    mas.append(y)
sum = 0
for i in range(10):
    sum = sum+ mas[i]
ser = sum/10
print("Середнє значення ", ser)
print("Масив ", mas)
mas1 =array('i',[])
for i in range(10):
    if mas[i]>ser:
        mas1.append(mas[i])
print("Масив 1", mas1)        