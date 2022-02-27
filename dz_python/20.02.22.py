from bs4 import BeautifulSoup
import requests
import re


# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def refined(s):
#     res = re.sub(r"\D+", "", s)
#     return res
#
#
# def get_data(html):
#     price = []
#     soup = BeautifulSoup(html, "lxml")
#     catalog = soup.find('form', id="list_form1")
#     item = catalog.find_all("div", class_="model-price-range")
#     for i in item:
#         item3 = i.findAll('span')
#         for j in item3:
#             s = refined(j.text)
#             price.append(s)
#     list_price(price)
#
#
# info_page = 0
# count_page = 1
#
#
# def list_price(price):
#     summa = 0
#     count = 0
#     global info_page
#     for i in price:
#         if i != '':
#             summa += int(i)
#             count += 1
#     info = round((summa / count), 2)
#     info_page += info
#
#
# def main():
#     global count_page
#     for i in range(4):
#         url = f'https://www.e-katalog.ru/list/206/{i}'
#         get_data(get_html(url))
#         count_page += 1
#
#
# if __name__ == '__main__':
#     main()
#
#
# print('Средняя цена продаваемых фотоаппаратов:', round(info_page / count_page), 'рублей')


# Через класс ============================================ > СВОЙ ВАРИАНТ
# class Parser:
#     soup = ""
#     res = []
#     all_p = 0
#
#     def __init__(self, url):
#         self.url = url
#
#     def refined(self, s):
#         chek = re.sub(r"\D+", "", s)
#         return chek
#
#     def get_html(self, url):
#         req = requests.get(self.url).text
#         self.soup = BeautifulSoup(req, 'lxml')
#         self.parsing()
#
#     def parsing(self):
#         catalog = self.soup.find('form', id="list_form1")
#         item = catalog.find_all("div", class_="model-price-range")
#         for i in item:
#             item3 = i.findAll('span')
#             for j in item3:
#                 s = self.refined(j.text)
#                 self.res.append(s)
#             for x in self.res:
#                 if x != "":
#                     print(x)
#                     self.all_p += int(x)
#         print(self.all_p)
#         # print(self.res)
#
#     # def all_page(self):
#     #     self.all_p.append(self.parsing())
#     #     print(self.all_p)
#
#
# for i in range(0, 15):
#     link = f'https://www.e-katalog.ru/list/206/{i}'
#     pars = Parser(link)
#     print(pars.__dict__)
#     # pars.url_page()
#     pars.get_html(link)


# ================================================= От учителя по 1 странице
#
# class Parser:
#     html = ""
#
#     def __init__(self, url):
#         self.url = url
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     def parsing(self):
#         elements = self.html.find_all("div", class_="model-price-range")  #
#         prices = []
#         for element in elements:
#             pr1 = element.find_all('span')[0].text
#             price_1 = re.sub(r"\D", "", pr1)
#             pr2 = element.find_all('span')[1].text
#             price_2 = re.sub(r"\D", "", pr2)
#             if price_2.isnumeric():  # .isnumeric() =  проверка содержит ли строка только числа
#                 prices.append((int(price_1) + int(price_2)) / 2)
#             else:
#                 prices.append(int(price_1))
#         print(prices)
#         print(f"Средняя цена: {round(sum(prices) / len(prices))} руб.")
#
#     def run(self):
#         self.get_html()
#         self.parsing()
#
#
# pars = Parser(f"https://www.e-katalog.ru/list/206/")
# pars.run()

# ======================================= От учителя все страницы  НЕВЕРНЫЙ === выводит среднее крайней страницы

# class Parser:
#     html = ""
#
#     def __init__(self, url):
#         self.url = url
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     def parsing(self):
#         elements = self.html.find_all("div", class_="model-price-range")  #
#         prices = []
#         for element in elements:
#             pr1 = element.find_all('span')[0].text
#             price_1 = re.sub(r"\D", "", pr1)
#             pr2 = element.find_all('span')[1].text
#             price_2 = re.sub(r"\D", "", pr2)
#             if price_2.isnumeric():  # .isnumeric() =  проверка содержит ли строка только числа
#                 prices.append((int(price_1) + int(price_2)) / 2)
#             else:
#                 prices.append(int(price_1))
#         return prices
#
#     def run(self):
#         self.get_html()
#         return self.parsing()  # ======================================= обязательно вернуть
#
#
# av = []
# for i in range(15):
#     pars = Parser(f"https://www.e-katalog.ru/list/206/{i}/")
#     av = pars.run()
#     # print(av)
#
# print(f"Средняя цена: {round(sum(av) / len(av), 2)} руб.")  # НЕВЕРНО !!!!! выводит среднее крайней страницы


# ================================================  ВЕРНЫЙ

# class Parser:
#     html = ""
#
#     def __init__(self, url):
#         self.url = url
#
#     def get_html(self):
#         req = requests.get(self.url).text
#         self.html = BeautifulSoup(req, 'lxml')
#
#     def parsing(self):
#         elements = self.html.find_all("div", class_="model-price-range")  #
#         prices = []
#         for element in elements:
#             pr1 = element.find_all('span')[0].text
#             price_1 = re.sub(r"\D", "", pr1)
#             pr2 = element.find_all('span')[1].text
#             price_2 = re.sub(r"\D", "", pr2)
#             if price_2.isnumeric():  # .isnumeric() =  проверка содержит ли строка только числа
#                 prices.append((int(price_1) + int(price_2)) / 2)
#             else:
#                 prices.append(int(price_1))
#         return round(sum(prices) / len(prices))
#
#     def run(self):
#         self.get_html()
#         return self.parsing()  # ======================================= обязательно вернуть
#
#
# j = 0
# av = []
# for i in range(4):
#     pars = Parser(f"https://www.e-katalog.ru/list/206/{i}/")
#     av.append(pars.run())
#
#     print(f"{j} Средняя цена: {av} руб.")
#     j += 1
# print(av)
# print(f"Средняя цена: {round(sum(av) / len(av), 2)} руб.")

# =============================================================================================================

