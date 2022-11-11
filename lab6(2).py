import math
a = float(input("Введіть значення а "))
b = float(input("Введіть значення b "))
h = float(input("Введіть значення кроку h "))
x = a
while x<b:
    y = (math.e**x)/((x**2)+0.11)
    print("%i  x=%.1f y=%.2f"%(x,y))
    x = x+h