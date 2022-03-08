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

import sqlite3 as sq

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

with sq.connect("users.db") as con:
    cur = con.cursor()
    cur.execute("""
    INSERT INTO user
    VALUEs (10, 'Ольга', '79991112233', 25, 'test@mail.ru')

    """)