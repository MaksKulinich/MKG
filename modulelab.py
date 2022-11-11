def module():
    numb = input("Введіть число ")
    str_numb = str(numb)
    sum1 = 0
    for i in range(len(str_numb)):
        sum1+= int(str_numb[i])
    print("Сума ", sum1)
    max1 = max(numb)
    min1 = min(numb)
    print("Максимальна цифра ", max1)
    print("Мінімальна цифра ", min1)
    return(module)
module()        