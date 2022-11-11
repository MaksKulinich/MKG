import random
ryadok = input("Введіть рядок ")
punc = ".,:;-!?"
def func1():
    split_rd = ryadok.split(" ")
    r = ''
    for elem in split_rd:
        r+= elem + random.choice(punc)
    print(r)
    return(r)
func1()    
def func2():
    split_rd = ryadok.split(" ")
    povt = ''
    for i in split_rd:
        if split_rd.count(i)>1:
            povt+= i +" "
        c_set = set(povt.split(" "))
    for j in c_set:
        print(j)
func2()