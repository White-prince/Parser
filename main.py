import requests
from bs4 import BeautifulSoup

req = requests.get("http://play.anilibria.life")
req2 = requests.get("http://play.anilibria.life/page/2/")
req3 = requests.get("http://play.anilibria.life/page/3/")
html = BeautifulSoup(req.content, 'html.parser')
html2 = BeautifulSoup(req2.content, 'html.parser')
html3 = BeautifulSoup(req3.content, 'html.parser')

title = html.find("title")
print("Название сайта: " + title.text)
print("Аниме на 1 странице")
for el in html.select(".kino-item > .kino-title"):
    content = el.select('h2')
    print(content[0].text)
    while el in html.find_all(".kino-inner > .kino-text"):
        info = el.select(".kino-desc")
        print(info[0].text)

print("Аниме на 2 странице")
for el in html2.select(".kino-item > .kino-title"):
    content = el.select('h2')
    print(content[0].text)
    while el in html.find_all(".kino-inner > .kino-text"):
        info = el.select(".kino-desc")
        print(info[0].text)

print("Аниме на 3 странице")
for el in html3.select(".kino-item > .kino-title"):
    content = el.select('h2')
    print(content[0].text)
    while el in html.find_all(".kino-inner > .kino-text"):
        info = el.select(".kino-desc")
        print(info[0].text)
