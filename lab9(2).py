import numpy as np
c_set = {"https://sourceforge.net/projects/numpy/files/NumPy/",
" https://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy",
"https://adic.afke.pp.ua/bat/jak-zrobiti-masiv-numpy.html",
"http://ruslan.rv.ua/python-starter/methods_str/str_methods.html",
"http://pishachok.blogspot.com/p/blog-page_0.html"}
sp = list(c_set)
tuple1 = tuple(c_set)
mas = np.array(c_set)
print("Множина", c_set)
print("Множина у стовпчик:")
for i in c_set:
    print(i)
print("Масив ", mas)
print("Список ", sp)
print("Кортеж ", tuple1)    