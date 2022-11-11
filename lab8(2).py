import numpy as np 
n = int(input("Введіть розмірність масиву "))
k = int(n**(1/2))
print(k)
x = 1
masA = np.zeros((k,k))
for i in range(k-1,-1,-1):
    for j in range(k):
        masA[j][i]=x
        x = x+1
print(masA)        