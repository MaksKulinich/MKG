from math import cos
import math
def func1(a,x,y,z):
    L = 6*a*math.pow((x),3) + math.sin(y)*math.cos(z) + math.tan(x+math.pi/3)
    return(L)
a = float(input("Введіть значення a"))
x = float(input("Введіть значення x"))
y = float(input("Введіть значення y"))
z = float(input("Введіть значення z"))
L = func1(a,x,y,z)
print("Значення:", L)