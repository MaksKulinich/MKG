from bs4 import BeautifulSoup as bs
import requests
url = input("Введіть URL-адресу ")
r=requests.get(url)
file = open("file.txt", 'w', encoding="utf-8")
if r.status_code==200:
    wbs=bs(r.text,'html.parser')
    namelist=wbs.find_all()
    for name in namelist:
        file.write(name.get_text().strip())
file.close()