import math
a = float(input("Введіть значення а "))
b = float(input("Введіть значення b "))
h = float(input("Введіть значення кроку h "))
x = a
sp = []
while x<b:
    y = (math.e**x)/((x**2)+0.11)
    sp.append(y)
    x = x+h
print(sp)
sp.sort(reverse=True)
n = len(sp)
k =int(n/2)
sp1 = sp[0:k]
sp2 = sp[k:n]
print(sp1)
print(sp2)    