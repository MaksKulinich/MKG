import math
x = float(input("Введіть значення х :"))
def f1(x1):
    rez = math.e**3.27*math.fabs(x1-9)+1
    return(rez)
def f2(x2):
    rez = math.cos(x2)+(math.cos(x2)/math.sin(x2))+ math.pow(math.fabs(x2-7.84),1/2)
    return(rez)
def f3(x3):
    rez = math.sin(math.fabs(x3-0.7))+ 3.33*2**x3
    return(rez)
y = 0.0
if x>=5.2:
    y = f1(x)
elif x>0.19:
    y = f2(x)
else:
    y = f3(x)
print(y)    