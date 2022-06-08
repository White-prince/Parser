import requests
from bs4 import BeautifulSoup

req = requests.get("http://play.anilibria.life")
html = BeautifulSoup(req.content, 'html.parser')

title = html.find("title")
print("Название сайта: " + title.text)
print("Аниме на 1 странице")
for el in html.select(".kino-item > .kino-title"):
    content = el.select('h2')
    print(content[0].text)
