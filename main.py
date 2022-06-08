import requests
from bs4 import BeautifulSoup

req = requests.get("http://play.anilibria.life")
html = BeautifulSoup(req.content, 'html.parser')

title = html.find("title")
print("Название сайта: " + title.text)
content = html.select("kino-item > kino-title > a > h2")
print(content)
