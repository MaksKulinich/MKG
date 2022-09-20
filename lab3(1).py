num = int(input("Введіть перше число :"))
num2 = int(input("Введіть друге число :"))
first = num//10
last = num%10
first2 = num2//10
last2 = num2%10
print(f"Перше число у зворотньому порядку: {last}{first}")
print(f"Друге число у зворотньому порядку: {last2}{first2}")