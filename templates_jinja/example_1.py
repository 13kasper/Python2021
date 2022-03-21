from jinja2 import Template

# {{ }} -выражение для вставки конструкции Python  в шаблон
# {% %} - спецификатор шаблона
# {# #} - блок коментариев
# # ## - строковый комментарий

# =================

# name = "Игорь"
# age = 28
# tm = Template("Привет {{ n.upper() }}.  Мне {{ a*2 }} лет.")  # экземпляр класса
# msg = tm.render(n=name, a=age)
# print(msg)

# ============

# per = {'name': 'Игорь', 'age': 28}  # через словарь
# tm = Template("Привет {{ p['name'] }}.  Мне {{ p['age'] }} лет.")  # экземпляр класса
# msg = tm.render(p=per)
# print(msg)

# ===========================


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Person("Игорь", 28)
#
# # tm = Template("Привет {{ p['name'] }}.  Мне {{ p['age'] }} лет.")
# tm = Template("Привет {{ p.get_name() }}.  Мне {{ p.get_age() }} лет.")  # через геттеры
# msg = tm.render(p=per)
# print(msg)


# ====================

# data = """Модуль Jinja вместо
# определения {{ name }}
# подставит соответствующее значение
# """
#
# tm = Template(data)
# msg = tm.render(name="Игорь")  # вставили в шаблон в data
# print(msg)
#
# # {%raw%}...
# #  {%endraw%} # сохраняет шаблон таким как он написан, ставится в конце


# link = "<a href='#'>Ссылка</a>"
# tm = Template("{{link | e}}")  # | e = экранирование внутри шаблона
# msg = tm.render(link=link)
# print(msg)

# {% for <выражение> %}  # =====================================================ЦИКЛЫ
# <повторяющийся фрагмент>
# {% endfor %}


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Житомир'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
# # минус в {% -%}удаляет пробелы
# link = """<select name="cities">
# {% for c in cities -%}
#     {% if c.id > 3 -%}
#         <option value="{{ c['id'] }}">{{ c['city'] }}</option>
#     {% elif c.city == 'Москва' -%}
#         <option>{{ c['city'] }}</option>
#     {% else -%}
#         {{c['city']}}
#     {% endif -%}
# {% endfor -%}
# </select>
# """
#
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)
#
# # {% if <условие> %} ========================================================== IF
# #        <фрагмент при истинности условия>
# # {% endif %}


# ===================================================== Задача ======> СДЕЛАТЬ

# menu = [
#     {'href': '/index', 'link': 'Главная'},
#     {'href': '/news', 'link': 'Новости'},
#     {'href': '/about', 'link': 'О компании'},
#     {'href': '/shop', 'link': 'Магазин'},
#     {'href': '/contact', 'link': 'Контакты'},
# ]
#
# link = """
#
# """
#
# tm = Template(link)
# msg = tm.render(menu=menu)
# print(msg)


# ===================================

cars = [
    {'model': 'Audi', 'price': 23000},
    {'model': 'Skoda', 'price': 17000},
    {'model': 'Renault', 'price': 44000},
    {'model': 'WV', 'price': 21000},
]

# tpl = "Суммарная цена автомобилей {{ cs | sum(attribute='price') }}"  # sum - выводим сумму всех авто по аттрибуту
# tpl = "Суммарная цена автомобилей {{ cs | max(attribute='price') }}"  # max - выводим словарь с максимальной ценой
# tpl = "Суммарная цена автомобилей {{( cs | max(attribute='price')).model }}"  # выводим саму модель машины ( в скобка)
# tpl = "Суммарная цена автомобилей {{cs | random }}"  # выводим рандомную модель
tpl = "Суммарная цена автомобилей {{cs | replace('model', 'brand') }}"  # заменяем ключи model на brand

tm = Template(tpl)
msg = tm.render(cs=cars)
print(msg)

# ========================

# lst = [1, 2, 3, 4, 5, 6]
#
# tpl = "Суммарная цена автомобилей {{ cs | sum }}"  # sum - выводим сумму всех авто из списка
#
# tm = Template(tpl)
# msg = tm.render(cs=lst)
# print(msg)

# =========================