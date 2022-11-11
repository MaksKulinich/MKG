sp = []
s1 = input("Введіть рядок ")
for i in s1:
    if i.isdigit():
        sp.append(int(i))
dob = 1
for i in sp:
    dob = dob*i
print("Сума ", sum(sp))
print("Добуток ", dob)            