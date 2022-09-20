import math
def func1(a,x,y,z):
    L = 6*a*math.pow((x),3) + math.sin(y)*math.cos(z) + math.tan(x+math.pi/3)
    return(L)
a1 = float(input("Введіть значення a"))
x1 = float(input("Введіть значення x"))
y1 = float(input("Введіть значення y"))
z1 = float(input("Введіть значення z"))
L = func1(a1,x1,y1,z1)
print("Значення:", L)
