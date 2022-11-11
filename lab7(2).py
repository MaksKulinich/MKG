import random
N = int(input("Введіть кількість рядків :"))
for i in range(N):
    r1 = input("Ввудіть рядок кратний 3: ")
    L = len(r1)
    first = int(L/3)
    sec = int((L/3)+ first)
    s1 = r1[0:first]
    s2 = r1[first:sec]
    s3 = r1[sec:L]
    emptly = ''
    p = [s1]+[s2]+[s3]
    random1 = random.sample(p,3)
    emptly1 = emptly.join(random1)
    print("Відповідь ", emptly1)