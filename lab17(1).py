import pandas as pd
slovnik = {"Name":['Oleg', 'Gregory', 'Roman', 'Igor'],
        "Phone number":["380633456789", "380967654321", "380931239874", "380679871236"],
        "City":['Kyiv', 'Lviv', 'Chernihiv', 'Poltava'] }
df = pd.DataFrame(slovnik)
df.to_csv("masiv.csv")
tabl = pd.read_csv('masiv.csv')
x = tabl['Name']
sp = []
for name in x:
    sp.append(name)
tabl = pd.DataFrame(slovnik, index=sp)
print(tabl)
write_name = input("Введіть ім'я ")
print(tabl.loc[[write_name],["Phone number", 'City']])