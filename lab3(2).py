import sys
sideA = float(sys.argv[1])
sideB = float(sys.argv[2])
sideC = float(sys.argv[3])
k = ("Коефіцієнт пропорційності")
k = 4
sideA1 = sideA*k
sideB1 = sideB*k
sideC1 = sideC*k
print("Трикутник подібний до даного:", sideA1, sideB1, sideC1)