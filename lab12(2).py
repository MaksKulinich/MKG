import random
def nomer():
    letter = "AEUFQRZW"
    numb = [3]+[6]+[12]
    cifr = "01123456789"
    x = random.choice(letter)
    y = random.choice(cifr)+random.choice(cifr)+random.choice(cifr)+random.choice(cifr)+random.choice(cifr)+random.choice(cifr)+random.choice(cifr)+random.choice(cifr)
    z = str(random.choice(numb))
    random_nomer = x + y + "-" + z
    return(random_nomer)
file = open('nomers.txt', 'w')
N = int(input("Введіть кількість номерів "))
for i in range(N):
    file.write(nomer() + "\n")
file.close()        