import requests 
from bs4 import BeautifulSoup as bs
import json
tag = input("Введіть тег ")
url = input("Введіть URL-адресу ")
url_r = requests.get(url)
for i in range(1):
    if url_r.status_code== 200:
        continue
    else:
        print("Задана Web-сторінка не працює")
file = open("web.json", 'a+', encoding='utf-8')
if url_r.status_code==200:
    wbs=bs(url_r.text,'html.parser')
    numb = wbs.find_all(tag)
    L_numb = len(numb)
    K = {tag:L_numb}
    json.dump(K, file)
file.close()