#  СУБД ( система управления базами данных )
#  SQL  - язык структурированных запросов
#  SQLite
#  SQLiteStudio
# или
# BD Browser for SQLite

#  модуль для питона sqlite3


# СОЗДАЕМ БАЗУ ДАННЫХ =================================================================

# import sqlite3 as sq
#
# # con = sq.connect("profile.db")  # создаем документ и открываем связь с бд
# # cur = con.cursor()  # создает элемент для работоспособности бд
# # cur.execute("""
# # """)
# # con.close()
#
# # *.db, *db3, *.sqlite и *.sqlite3  = расширения баз данных
#
# # второй вариант через with
# with sq.connect("profile.db") as con:  # создаем документ и открываем связь с бд
#     cur = con.cursor()  # создает элемент для работоспособности бд
#     # # cur.execute создаем таблицу
#     # cur.execute("""
#     # CREATE TABLE IF NOT EXISTS user(  # если таблицы нет то ее создаем и называем персон
#     # id INTEGER PRIMARY KEY AUTOINCREMENT,  # присваиваем полю id обязательный ключ (первичный ключ)
#     # name TEXT NOT NULL,  # создаем поле name и присваиваем значение текст не должно быть NULL
#     # summa REAL,
#     # data TEXT
#     # )
#     # """)
#
# # для удаления данных из таблицы :
#     cur.execute("DROP TABLE user")
#
# # Primary key (PK) - первичный ключ ( должен быть изначально хоть в одном поле )
# # - суррогатный (искуственный) ключ
# # - логический ключ


# ==================================================================== 03.03.2022

# import sqlite3 as sq

# with sq.connect("users.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS user(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     phone BLOB NOT NULL DEFAULT +7909000000,
#     age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
#     email TEXT UNIQUE
#     )
#     """)

# DEFAULT- ЗНАЧЕНИЕ ПО УМОЛЧАНИЮ
# UNIQUE - УНИКАЛЬНЫЕ ЗНАЧЕНИЯ
# INTEGER - числовое значение
# TEXT - строчное значение
# BLOB - блок данных
# AUTOINCREMENT - автоматически ставит значение ( по возрастанию )
# PRIMARY KEY поле обязательно к заполнению
# CHECK(age > 0 AND age < 100) - условия от и до

# ==========================================================================

# with sq.connect("users.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     DROP TABLE user_table;
#
#     """)


# ALTER TABLE user - Переименовать
# RENAME TO user_table - на что переименовать
# ADD COLUMN - добавить колонку, если данные уже есть то нужно добавить DEFAULT str
# RENAME COLUMN address TO home_address - переименовать столбец
# DROP COLUMN home_address - удалить столбец
# DROP TABLE user_table - удаляем таблицу

# ==========================================================================


# with sq.connect("users.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     INSERT INTO user
#     VALUEs (10, 'Ольга', '79991112233', 25, 'test@mail.ru')
#
#     """)

# INSERT INTO user
# VALUEs (10, 'Ольга', '79991112233', 25, 'test@mail.ru')  # добавляем данные в уже созданой таблице

# ==================================================================================

# with sq.connect("users.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     INSERT INTO user
#     VALUEs (10, 'Ольга', '79991112233', 25, 'test@mail.ru')
#
#     """)


# ==================================================================================== 08.03.22

# with sq.connect("db_4.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM Ware
#     ORDER BY Price DESC
#     LIMIT 2, 5;
#     """)
#
#     # ====================================== ВЫВОДИМ инфу с БД
#
#     # res = cur.fetchall()  # выводит все данные из базы данных ( в кортеже )
#     # print(res)
#
#     # for res in cur:
#     #     print(res)
#
#     res = cur.fetchone()  # Выводит первый элемент
#     print(res)
#     res2 = cur.fetchmany(3)  # выводим нужно количество записей
#     print(res2)


# ===================================================================================== 15.03.22
import sqlite3 as sq

#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     )
#     """)
#     cur.execute("INSERT INTO cars VALUES(1, 'REnault', 22000)")
#     cur.execute("INSERT INTO cars VALUES(2, 'Лада', 29000)")
#     cur.execute("INSERT INTO cars VALUES(3, 'Волга', 57000)")
#     cur.execute("INSERT INTO cars VALUES(4, 'ИЖ', 35000)")
#     cur.execute("INSERT INTO cars VALUES(5, 'Чайка', 52000)")
#
# # con.commit()  = сохранение изменений в БД
# # con.close()  = закрытие соединения с БД


# ========================================================================

# cars = [
#     ('BWM', 54000),
#     ('TOYOTA', 46000),
#     ('DAEWOO', 38000),
#     ('CITROEN', 29000),
#     ('HONDA', 33000),
# ]
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER)
#     """)

# for car in cars:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)  # ?, ? = в вопросы подставляются данные из списка

# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars)

# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price': 0})  # обновляем данные в таблице (:Price-шаблон)

# executescript = несколько запросов (нельзя использовать шаблоны запросов(? Итд))
# Удаляем данные из таблицы
# Обновляем прайс прибавляя 100

# cur.executescript("""
# DELETE FROM cars WHERE model LIKE 'B%';
# UPDATE cars SET price = price + 100;
# """)


#  BEGIN; - точка отката при rollback()

# cars = [
#     ('BWM', 54000),
#     ('TOYOTA', 46000),
#     ('DAEWOO', 38000),
#     ('CITROEN', 29000),
#     ('HONDA', 33000),
# ]
#
# con = None
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER);
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, 'TTT', 22000);
#     UPDATE cars2 SET price = price + 100;
#     """)
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()  # метод откатывает изменение в БД в исходное состояние и все изменения применятся не будут
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()


# ========================================

# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     last_row_id = cur.lastrowid  # lastrowid свойство создаст id последней записи
#     buy_car_id = 2
#     cur.execute('INSERT INTO cost VALUES("Илья", ?, ?)', (last_row_id, buy_car_id))


# =========================================================

# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     );
#     """)
#
#     cur.execute('SELECT model, price FROM cars')
#
#     # rows = cur.fetchall()  # выводит все записи
#     # rows = cur.fetchone()  # выводит только первую запись
#     # rows = cur.fetchmany(5)  # выводит нужное количество записей
#     # print(rows)
#
#     for res in cur:
#         print(res)


# ====================================================

# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row  # sq.Row = формат записи
#     cur = con.cursor()
#
#     cur.executescript("""
#         CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     );
#     """)
#
#     cur.execute('SELECT model, price FROM cars')

# for res in cur:
#     print(res['model'], res['price'])

# var2

# for model, price in cur:
#     print(model, price)


# ================================================================= загрузили и выгрузили картинку в (из) БД

# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, 'wb') as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#
#     return True
#
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row  # sq.Row = формат записи
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     """)
#
#     cur.execute('SELECT ava FROM users LIMIT 1')
#     img = cur.fetchone()['ava']
#
#     write_ava('out.png', img)
#
#     # img = read_ava(1)
#     # if img:
#     #     binary = sq.Binary(img)
#     #     cur.execute('INSERT INTO users VALUES("Илья", ?, 1000)', (binary,))

# =================================================================================== поднимаем базу данных из файла

# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#
#     # with open('sql_dump.sql', 'w') as f:
#     #     for sql in con.iterdump():  # записываем данные из БД
#     #         f.write(sql)
#
#     # for sql in con.iterdump():  # метод класса cursor, вывели набор команд в консоль с БД
#     #     print(sql)
#
#     with open('sql_dump.sql', 'r') as f:
#         sql = f.read()
#         cur.executescript(sql)


# ============================================================================= Записываем в память


# data = [('car', 'машина'), ('house', 'дом'), ('tree', 'дерево'), ('color', 'цвет')]
#
# con = sq.connect(":memory:")  # :memory: = Пишем в память
# with con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS dict(
#     eng TEXT,
#     rus TEXT
#     )
#     """)
#
#     cur.executemany("INSERT INTO dict VALUES(?, ?)", data)
#
#     cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
#     print(cur.fetchall())


# ===============================
# ======================================================================= WSGI ========== Web Server Gateway Interface

# Фреймверки
# Flask
# Django


# ORM (Object-Relation Mapping)  # работа с записями в БД
# шаблонизатор  # дает возможность сверстать макет один раз (html, css)

# Jinja = модуль для обработки шаблонов
