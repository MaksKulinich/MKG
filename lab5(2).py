import math
A1 = float(input("Введіть абсцису точки A: "))
A2 = float(input("Введіть ординату точки A: "))
B1 = float(input("Введіть абсцису точки B: "))
B2 = float(input("Введіть ординату точки B: "))
C1 = float(input("Введіть абсцису точки C: "))
C2 = float(input("Введіть ординату точки C: "))
A = math.fabs(A2)+math.fabs(A1)
B = math.fabs(B2)+math.fabs(B1)
C = math.fabs(C2)+math.fabs(C1)
if A>B and A>C:
    print("Точка А ")
elif B>A and B>C:
    print("Точка B ")
else:
    print("Точка С ")        