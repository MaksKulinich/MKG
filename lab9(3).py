sl = {"Лев":"lion",
"Жираф":"giraffe",
"Кіт":"cat",
"Собака":"dog",
"Слон":"elephant",
"Ведмідь":"bear",
"Лисиця":"fox",
"Кролик":"rabbit",
"Білка":"squirrel",
"Кінь":"horse",}
x = sl.keys()
y = sl.values()
slov1 = {m:n for (m,n) in zip(y,x)}
print(slov1)