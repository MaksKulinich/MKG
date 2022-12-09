import pandas as pd
massive_txt = open("massive.txt", 'r', encoding='utf-8')
one_txt = open('one.txt', 'w')
sp1 = []
sp2 = []
sp3 = []
for lines in massive_txt:
    x = lines.index(' ')
    y1 = lines[0:x]
    y2 = lines[(x+1):((2*x)+1)]
    y3 = lines[((2*x)+2):-1]
    one_txt.write(y1+" "+ y2+" "+ y3+' ')
    sp1.append(y1)
    sp2.append(y2)
    sp3.append(y3)
pd_S1=pd.Series(sp1)
pd_S2 = pd.Series(sp2)
pd_S3 = pd.Series(sp3)
print(pd_S1)
print(pd_S2) 
print(pd_S3)
one_txt.close()
massive_txt.close()