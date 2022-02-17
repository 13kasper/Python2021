import csv
from bs4 import BeautifulSoup
import requests
import re


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    """чистит от пробелов"""
    res = re.sub(r"\s+", "", s)
    return res


def get_data(html):
    soup = BeautifulSoup(html, "lxml")
    catalog = soup.find('div', id="catalog")
    item = catalog.findAll("div", class_="catalog-item-card")

    """ВОПРОС! почему не выгружаются все карточки товара ??? может это зависить от ленивой загрузки ? как решить"""

    for k in item:
        title = k.find("div", class_="item-all-title").text
        article = k.find('div', class_="article_rating").text
        price = k.find('span', class_="catalog-item-price").text
        link = k.find('a').get('href')

        title = refined(title)
        article = refined(article)
        price = refined(price)
        link = refined(link)

        data = {"title": title, "article": article, "price": price, "link": link}
        write_csv(data)


def write_csv(data):
    with open('rossvik.csv', 'a') as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\r")
        writer.writerow((data['title'], data['article'], data['price'], data['link']))


def main():
    url = 'https://rossvik.ru/catalog/plastyri/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()

with open("rossvik.csv") as f:
    print(f.read())

# ======================   ВОПРОС !!!
# Изначально хотел собрать все линки на сайты где упоминается ключевое слово '' на странице поисковой выдаче гугл.
# Но мне возвращалось None, попробовал на более кратком примере ниже, тоже возвращает None.


# f = requests.get('https://rossvik.ru/').text
# soup = BeautifulSoup(f, "lxml")
# data = soup.find('span', class_="banners-main__item-text small").text
# # data = soup.find('span', text='шин')  # Почему не находит по тексту ? Возвращает None (слово 'шин' в классе выше)
# print(data)

# ===========================================
