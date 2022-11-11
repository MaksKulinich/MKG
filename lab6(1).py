import math
a = float(input("Введіть значення а "))
b = float(input("Введіть значення b "))
h = float(input("Введіть значення кроку h "))
x = a
for i in range(5):
    y = (math.e**x)/((x**2)+0.11)
    print("%i  x=%.1f y=%.2f"%(i,x,y))
    x = x+h
    if x>b:
        break