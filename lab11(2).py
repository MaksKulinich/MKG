import json
Cities_file = open('Cities.txt', 'r', encoding='utf-8')

city = input("Введіть місто ")
slovnik = json.load(Cities_file)
print("Населення міста ", slovnik["Cities"][city])

for i in sorted(slovnik['Cities'].items(), key=lambda para:para[1]):
    print(i)

x = input("Введіть місто ")
y = int(input("Введіть населення "))
new = {x:y}
Cities_write = open('Cities.txt', 'a+', encoding='utf-8')
json.dump(new, Cities_write, ensure_ascii=False, indent=2)
Cities_file.close()
Cities_write.close()    