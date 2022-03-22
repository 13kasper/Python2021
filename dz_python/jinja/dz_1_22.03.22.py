from jinja2 import Template


menu = [
    {'href': '/index', 'link': 'Главная'},
    {'href': '/news', 'link': 'Новости'},
    {'href': '/about', 'link': 'О компании'},
    {'href': '/shop', 'link': 'Магазин'},
    {'href': '/contact', 'link': 'Контакты'},
]

link = """<ul>
{% for i in menu -%}
{% if i.link == 'Главная' -%}
<li><a href="{{ i['href'] }}"class='active'>{{i['link']}}</a></li>
{% else -%}
<li><a href="{{ i['href'] }}">{{i['link']}}</a></li>
{% endif -%}
{% endfor -%}
</ul>
"""

tm = Template(link)
msg = tm.render(menu=menu)
print(msg)