from bs4 import BeautifulSoup
import requests
import re


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    res = re.sub(r"\D+", "", s)
    return res


def get_data(html):
    price = []
    soup = BeautifulSoup(html, "lxml")
    catalog = soup.find('form', id="list_form1")
    item = catalog.find_all("div", class_="model-price-range")
    for i in item:
        item3 = i.findAll('span')
        for j in item3:
            s = refined(j.text)
            price.append(s)
    list_price(price)


info_page = 0
count_page = 0


def list_price(price):
    summa = 0
    count = 0
    global info_page
    for i in price:
        if i != '':
            summa += int(i)
            count += 1
    info = round((summa / count), 2)
    info_page += info


def main():
    global count_page
    for i in range(0, 15):
        url = f'https://www.e-katalog.ru/list/206/{i}'
        get_data(get_html(url))
        count_page += 1


if __name__ == '__main__':
    main()


print('Средняя цена продаваемых фотоаппаратов:', round(info_page / count_page), 'рублей')
