# name = "Andrei"
# print("Hallo", name)
# age = 20
# print(age)
# # a = b = c = 1
# # print(a, b, c)
# a, b, c = 5, "Hello", 9.2  # Какой результат
# print(a, b, c)
# name_new = "Andrei"

# PI = 3.14  # константа пишется в верхнем регистре
# PI = 2
# print(PI)

# a = 1
# b = 2
# c = 1
# a = b
# b = c
# print("a: ", a)
# print("b: ", b)

# print("строку \
# символов")
# print('строку '
#       'символов')
# print('строку \nсимволов')
# print("\tДокумент \"myfirstscript.ru\" находится по заданному пути: \n"
#     "\rD:\Python\projects")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 5)

# print("\"Выполнил задание\n\t\t (Осипов АВ)\n\t\t\t слушатель группы (123)\"")

# a = 1
# b = 2
#
# b = a
# a = a + a
#
#
# print(a, "\n", b)

# a = 2.65165165160005
# print(a)
# print(type(a))

# a = 5
# b = 7
# c = 3
#
# g = 5 * 7 * 3
# h = 5 + 7 + 3
# k = h / 3
# print("Произведение = ", g, "\n", "Сумма = ", h, "\n", "Среднее арифметическое = " k)

# number = 6 + 4 * 5 ** 2 + 7  # ( скобки, степень, деление=умножение, сложение=вычитание, слева направо )
# print(number)

# num = 10
# num -= 5
# print(num)

# a = 9753
# c = a % 10
# d = (a // 10) % 10
# t = (a // 100) % 10
# f = (a // 1000) % 10
#
# print(c, d, t, f)
# ------------------------------------------------------------> Перевернутое число
# num = 9753
# print("Исходное число: ", num)
# res = (num % 10) * 1000
# num = num // 10
# res += (num % 10) * 100
# num = num // 10
# res += (num % 10) * 10
# num = num // 10
# res += num % 10
# # print("num", num)
# print("Обратное число: ", res)

# num1 = "2"
# num2 = 3
#
# print(int(num1) + num2)  # int => Преобразовать в число  // преобразует вещественное число в целое
# print(num1 + str(num2))  # str => Преобразовать в строку
# print(int(3.8))  # 3 // преобразует вещественное число в целое
# print(round(3.8954, 2))  # округляет число до поставленного значения

# a = 5 / 3
#
# print(a)
# print(round(a, 2))

# a = "5.2"
# b = 10
#
# print(float(a) + b)  # преобразовывает дробное число из строки в число


# a = 1
# b = 2
# print("a:", a, "\nb:", b)


# name = "Виктор"
# age = 28
# # print("Меня зовут " + name + ". Мне" + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, " лет.", sep="--", end=" ")
# print("Я учу Питон.")


# name = "Igor"
# age = 28
# grade = 9.2
# print("It` %s, %d. Level: %f" % (name, age, grade))  # % = переменные  s= строка, d= число .2f дробное число


# print("This is a {0}. It`s {1}." .format("ball", "red"))

# name = input("Ваше имя: ")
# city = input("Ваш город: ")
# print("Вас зовут {0}. Ваш город {1}".format(name, city))

# name = input("Введите число 1:")
# pow = input("Введите число 2:")
# print(int(name) ** int(pow))

# a1 = input("Введите число 1:")
# a2 = input("Введите число 2:")
# a3 = input("Введите число 3:")
# a4 = input("Введите число 4:")
# res = float(a1 + a2) / float(a3 + a4)
# print(round(res, 2))
# тоже самое
# a1 = int(input("Введите число 1:"))  # ------>int не примет дробное число, float примет
# a2 = int(input("Введите число 2:"))
# a3 = int(input("Введите число 3:"))
# a4 = int(input("Введите число 4:"))
# res = (a1 + a2) / (a3 + a4)
# print(round(res, 2))


# b1 = True
# b2 = False
#
# print(b1 + 5)
# print(b2 + 5)
# print(bool(""))  # False ---> пустая строка
# print(bool(0))  # False ---> 0 нет значения
# print(bool(False))  # False
# print(bool(None))  # False
# print(bool(0.1))  # True
# print(bool(" "))  # True ---> Пробел не пустая строка
# print(bool("-15"))  # True
# print(bool("Python"))  # True

# test = None
# print(test)  # присваивается нулевое значение
# print(test is None)
# test = 5
# print(test)
# print(test is None)

# print("привет" > "Привет")  # True
#
# print(2 < 4 < 9)  # True
# print(2 * 5 > 7 >= 4 + 3)  # True
# print(3 * 3 <= 7 >= 2)  # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)  # оператор И => and
# print(5 - 3 == 2 or 1 + 2 == 4)  # оператор или => or
# print(not 9 - 9)  # оператор not

# v1 = (0 or 1) and (0 or 1)
# print(v1)
# v2 = 0 or 1 and 0 or 1
# print(v2)
# a = 0
# b = 0
# v3 = (a or 1) and (b or 0)
# print(v3)

# ---------------------------------if

# cnt = 5
# if cnt < 10:
#     cnt += 1  # обязательны 4 пробела
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 15
# b = 5
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("b == a")

# a = int(input("Введите первую сторону 10:"))
# b = int(input("Введите вторую сторону 20:"))
# c = int(input("Введите третию сторону 20:"))
#
# if (a == b) and (a == c):
#     print("Треугольник равносторонний")
# elif (a == b) or (b == c) or (a == c):
#     print("Треугоольник равнобедренный")
# elif (not a == b) or (not a == c):
#     print("Треугольник разносторонний")


# PR-1

# a = int(input("Введите Номер месяца: "))
#
# if ((a <= 2) and (a > 0)) or (a == 12):
#     print("Зима")
# elif(a > 2) and (a < 6):
#     print("Весна")
# elif(a > 5) and (a < 9):
#     print("Лето")
# elif(a > 8) and (a < 12):
#     print("Осень")
# else:
#     print("Ошибка ввода данных")

# PR-2

# a = int(input("Введите количество ворон на ветке от 0 до 9: "))
# b = ""
# if (a < 0) or (a > 9):
#     print("Посчитай еще раз")
#     a = "не может быть столько ворон"
# elif a == 1:
#     b = "ворона"
# elif(a > 1) and (a < 5):
#     b = "вороны"
# elif(a > 4) and (a < 10) or (a == 0):
#     b = "ворон"
#
# print("На ветке {0} {1}".format(a, b))

# DZ-1

# a = input("Как Вас зовут: ")
# b = int(input("Сколько Вам лет: "))
# c = input("Где Вы живете: ")
# print("Меня зовут {0},\nМне {1} лет,\nЯ живу в городе {2}".format(a, b, c))

# DZ-2

# print("Решите пример: 4 * 100 - 54")
# a = int(input("Ваш ответ: "))
# b = 346
# print("Правильный ответ: ", b)
# print("Ваш ответ: ", a)

# DZ-3

# a = int(input("Введите целое число: "))
# if a % 2 == 0:
#     print("Число", a, "- четное")
# else:
#     print("Число", a, "- нечетное")


# ================================>   21.09.21

# day = int(input("Введите день недели (цифрами):"))
# if (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")

# day = int(input("Введите день недели (цифрами):"))
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("Понедельник")
#     if day == 2:
#         print("Вторник")
#     if day == 3:
#         print("Среда")
#     if day == 4:
#         print("Четверг")
#     if day == 5:
#         print("Пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("Суббота")
#     if day == 7:
#         print("Воскресение")
# else:
#     print("Такого дня нет")

# a = int(input("Введите Номер месяца: "))
#
# if 2 >= a > 0 or a == 12:  # ==========================================> Другая запись
#     print("Зима")
# elif(a > 2) and (a < 6):
#     print("Весна")
# elif(a > 5) and (a < 9):
#     print("Лето")
# elif(a > 8) and (a < 12):
#     print("Осень")
# else:
#     print("Ошибка ввода данных")

#  =======================================================================> Тернарные выражения
# a, b = 20, 10
# minim = a if a < b else b
# print(minim)

# a, b = 10, 30
# print("a == b" if a == b else "a > b" if a > b else "a < b")

# ============> На ноль делить нельзя
# a = 2
# c = 0
# b = "На ноль не делим" if c == 0 else a / c
# print(b)

# =========================================================================> Ошибки

# Ошибка значения, синтаксическая ошибка
# 1a = 0
# print(1a)

# ошибка имени
# a = 0
# print(a + b)

# ошибка типа данных
# a = 0
# b = "2"
# print(a + b)  # необходимо преобразовать

# ZeroDivisionError: division by zero  ==> Деление на ноль
# a = 5
# b = 0
# print(a / b)

# Ввод неправильных значений ( строка )
# n = int(input("Ввести целое число: "))
# print((n * 2))

# try:  # попытаться сделать =>
#     n = int(input("Ввести целое число: "))
#     print((n * 2))
# except ValueError:  # Если не полуучится то =>
#     print("Что то пошло не так")

# try:  # попытаться сделать =>
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print((n / m))
# except ValueError:  # Если не полуучится то =>
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:  # попытаться сделать =>
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print((n / m))
# except (ValueError, ZeroDivisionError):  # Если не полуучится то =>
#     print("Нельзя вводить строки")
#     print("Нельзя делить на ноль")
# else:
#     print("Все нормально Вы ввели числа ", n, "и", m)
# finally:
#     print("Конец программы")


# a = input("Введите первое значение: ")
# b = input("Введите второе значение: ")
# try:
#     print(int(a) + int(b))
# except ValueError:
#     print(str(a) + str(b))


# n = input("Введите первое число:  ")
# m = input("Введите второе число:  ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
#     m = str(m)
# finally:
#     print(n + m)


# i = 0
# while i < 5:
#     print("i = ", i)
#     i += 1


# i = 0
# while i < 21:
#     print("i= ", i)
#     i += 2

# a = int(input("Введите количество звездочек: "))
# while a > 0:
#     print("*", end="")
#     a -= 1


# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Не четное")


# n = int(input("Введите начало диапазона: "))
# m = int(input("Введите конец диапазона: "))
# sum = 0
#
# while n < m:
#     if n % 2 != 0:
#         sum += m
#     n += 1
# print("Сумма нечетных:", sum)


# i = 0
# while i < 10:
#     print(i, end=" ")
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")  # до 4-5
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")


# while True:
#     n = int(input("Введите положительное число: "))
#     if not n > 0:
#         break

#
# mas = 1
# while True:
#     n = int(input("Введите положительное число: "))
#     if n == 0:
#         break
#     mas *= n
# print("Результат: ", mas)


# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)


# i = 1
# while i < 5:
#     print("Внешний цикл: i=", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j=", j)
#         j += 1
#     i +=1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i*j, "\t\t", end="")
#         j += 1
#     print()
#     i += 1

# DZ-1
# print("Выберите операцию: \n1 - 'r'\n2 - '+'\n3 - '-'\n4 - '/'\n5 - '*'\n6 - '%'\n7 - '<'\n8 - '>' ")
# a = int(input("Введите цифру: "))
# if a == 1:
#     b = int(input("Введите первое число: "))
#     b = -b
#     print(b)
# else:
#     b = int(input("Введите первое число: "))
#     c = int(input("Введите второе число: "))
#     if a == 4 and c == 0:
#         print("На ноль делить нельзя")
#     elif a == 2:
#         print(b + c)
#     elif a == 3:
#         print(b - c)
#     elif a == 4:
#         print(b / c)
#     elif a == 5:
#         print(b * c)
#     elif a == 6:
#         print(b % c)
#     elif a == 7:
#         if b < c:
#             print(b)
#         else:
#             print(c)
#     elif a == 8:
#         if b > c:
#             print(b)
#         else:
#             print(c)

# DZ-2
# Var1
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# x = a if a > b else b
# y = x if x > c else c
# print("Максимальное значение: ", y)

# Var2
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# print((a if a > c else c) if a > b else (b if b > c else c))


# DZ-3
# a = int(input("Введите количсетво чисел последовательности: "))
# total = 0
# quantity = 0
# maximum = 0
# minimum = 0
# while a > 0:
#     ch = float(input("Введите число: "))
#     if ch > maximum:
#         maximum = ch
#     elif minimum == 0 or ch < minimum:
#         minimum = ch
#     total += ch
#     quantity += 1
#     a -= 1
# x = round(total / quantity, 2)
# print("Количество чисел: {0}\nСреднее арифметическое: {1}\nМинимальное число: {2}\nМаксимальное число: {3}" .format(quantity, x, minimum, maximum))  # почему подсвечивает quantity ?


# DZ-4

# a = int(input("Введите количсетво символов: "))
# b = input("Введите тип символа: ")
# c = int(input("Ориентация линии (0 - горизонтальная, 1 - вертикальная ): "))
# while a > 0:
#     if c > 0:
#         print(b)
#     else:
#         print(b, end=" ")
#     a -= 1


# ====================================================================================> 23.09.21


# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     print(" " * i + "*")  # только в питоне может умножать даже пробелы
#     i += 1

# # тоже самое
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1

# ========================================================================> FOR

# for element in collections:
#     print(element)

# for i in "Hello":
#     print(i)

# j = 1
# for color in 'red', 'orange', 'yellow', 'green', 'cyan', 'blue':
#     print(j, 'color:', color)
#     j += 1  # для нумерации


# for i in 'one', 'two', 1, 20, 0.3:
#     print(i)

# for i in range(n):
#     тело цикла

# range(start, stop, step)

# for i in range(9):  # stop если одно значение
#     print(i, end=" ")

# for i in range(2, 9):  # start, stop
#     print(i, end=" ")

# for i in range(2, 9, 3):  # start, stop, step
#     print(i, end=" ")

# for i in range(9, 2, -1):  # start, stop, step
#     print(i, end=" ")

# a = int(input("Введите целое число: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")


# for i in range(11, 100, 11):
#     print(i, end=" ")


# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(10):
#     print(i, end=" ")
#     if i == 5:
#         break  # при break = else выводиться не будет
# else:
#     print("\nDone!")


# for i in range(3):  # Вложенный for
#     print("+++")
#     for j in range(2):
#         print("------")

# a = int(input("Введите ширину прямоугольника: "))
# b = int(input("Введите высоту прямоугольника: "))
#
# for i in range(b):
#     for j in range(a):
#         print("*", end=" ")
#     print()

# a = int(input("Введите ширину прямоугольника: "))
# b = int(input("Введите высоту прямоугольника: "))
#
# for i in range(b):
#     for j in range(a):
#         if (i == 0 or i == b - 1) or (j == 0 or j == a - 1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# ================================================> [результирующие выражения | цикл | опциональные цсловия]
# print([i * 2 for i in "Hello"])
# print([i for i in range(30) if i % 2 == 0])
#
# num = [i ** 3 for i in range(30) if i % 2 == 0]
# print(num)

# a = 12
# c = 0
# v = 0
# for i in range(1000):
#     b = int(input("Введите число от 1 до 100: "))
#     if 12 > b:
#         print("Загаданное число меньше")
#         c += 1
#     elif 12 < b:
#         print("Загаданое число больше")
#         v += 1
#     else:
#         f = c + v
#         print("Вы угадали с ", f, "раза")
#         break
#     i += 1

# ========================================================>******************* СПИСКИ ***************************
# num = [8, 3, 9, 4, 1]
# print(id(num))
# print(num)
# # print(type(num))
# # print(type(["one", "two", 2, 3.5, [1, 2, 3]]))
# print(num[0])
# print(num[-3])  # можно задавать с отрицательным индексом справа налеево
# num[1] = 256
# print(num)
# num[3] += 100
# print(num)
# print(id(num))
#
# print("Длина списка: ", len(num))  # ==================================> длина списка

# s = []
# s = [5, 6]
# print(s)

# s = [5] * 6
# print(s)
# b = list("Hello")
# print(b)

# n = list(range(10))  # list преобразовать в список =================
# print(n)

# n = list(range(2, 10, 2))
# print(n)

# a = [0 for i in range(5)]  # генерация списков ================
# print(a)

# a = [i ** 2 for i in range(5)]  # генерация списков ================
# print(a)

# n = 5
# a = [i ** 2 for i in range(1, n+1)]  # +1
# print(a)

# c = [i * 3 for i in "list"]
# print(c)

# a = [1, 2, 3]  # Объединение списков ========================
# b = [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))  # ввод списка пользователем ===========
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# сокращенная запись
# a = [input("->") for i in range(int(input("кол-во: ")))]
# print(a)

# a = [input("->") for i in range(int(input("кол-во: ")))]  # Вывод списка =======================
# print(a)
#
# for i in range(len(a)):
#     print(a[i])

# a = list(range(10, 2, -2))
# print(a)
#
# for i in range(len(a)):
#     print(a[i], end=" ")
#
# print()
#
# for j in a:
#     print(j, end=" ")


# =======> DZ-1
# a = int(input("Введите число: "))
# c = int(0)
# b = a
# while b > 0:
#     c = c * 10 + b % 10
#     b = b // 10
# if c == a:
#     print("Число {0} полиндром".format(a))
# else:
#     print("Число {0} НЕ полиндром".format(a))


# ========> DZ-2 var1
# a = int(input("Начало диапазона: "))
# b = int(input("Конец диапазонао: "))
# print([i for i in range(a, b+1) if i % 2 != 0])

# var2
# a = int(input("Начало диапазона: "))
# b = int(input("Конец диапазонао: "))
# for i in range(a, b+1):
#     if i % 2 != 0:
#         print(i, end=" ")


# =======>DZ-3
# a = 8
# for i in range(a):
#     print("*" * a, end=" ")
#     print()
#     a -= 1

# var2
# a = 8
# while a > 0:
#     print("*" * a, end=" ")
#     print()
#     a -= 1


# =======>DZ-4
# for i in range(8):
#     print("*" * i, end=" ")
#     print()
#     i += 1

# var2
# b = 1
# while b < 8:
#     print("*" * b, end=" ")
#     print()
#     b += 1

# ===============================================================>28.09.21

# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# print("------------------------")

# for i in my_list:  # значения без скобок
#     print(i**2, end=" ")
# print("\n-------------------------")

# for i in range(len(my_list)):  # цикл проходит по длине списка
#     my_list[i] = my_list[i] ** 2
#     print(my_list[i], end=" ")  # с индексом выводит значения по одному
#
# for i in range(len(my_list)):
#     my_list[i] += 5
#     print(my_list)  # без индекса выводит списко ( в скобка )

# summa = 0
# a = [int(input("->")) for i in range(int(input("n = ")))]
# for i in range(len(a)):
#     if a[i] < 0:
#         summa += a[i]
# print(summa)

# summa = k = 0
# a = [int(input("->")) for i in range(int(input("n = ")))]
# for i in range(len(a)):
#     if a[i] != 0:
#         summa += a[i]
#         k += 1
# print(summa/k)

# ====>Срезы - получение какой то части списка, которая в свою очередь тоже является списком

# s = [5, 9, 3, 7, 1, 8]
# print(s[2:3])  # от и до
# print(s[2:])  # От заданного до конца
# print(s[:5])  # От 0 до заданого
# print(s[:])  # Весь список
# print(s[::2])  # Шаг (через сколько)
# print(s[5:0:-1])  # 0 пятерку не включит, справа налево
# print(s[-2:2:-1])  # 2 тройку не включит, справа налево
# print(s[-1:4:-1])  # получим 8
# print(s[10:20])  # ничего не найдет

# s = [1, 2, 3, 4, 5, 6, 7]
# s[1:3] = [0, 0, 0, 0]  # заменит индексы 1 и 2 на 4 индекса с 0
# s[1:2] = [20]
# s[19:20] = [18]  # можем добавлять, даже если такого индекса нет, только срезами ( приплюсовать еще индекс )
# print(s)

# ==================================================================> МЕТОДЫ

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s.append(99)  # Добавляет элемент в конец списка
# print(s)
#
# s1 = []
# s1.extend([1, 2, 3])  # Добавляет множество элементов
# print(s1)
# s1.extend("add")
# print(s1)

# ---------------------------------------------------------------
# Сформировать список квадратов чисел от 1 до 10
# num_array = []
# for i in range(1, 11):
#     num_array.extend([i ** 2])
# print(num_array)

# Тоже самое сокращенно
# s = []
# s.extend(([i ** 2 for i in range(1, 11)]))
# print(s)
# ---------------------------------------------------------------

# s = [1, 2, 3, 4, 5, 6, 7]
# s.insert(1, 100)  # добавляем новое значение сдвигом индексов, 1 парметр = номер индекса, 2 параметр = само значение
# print(s)

# ---------------------------------------------------------------
# s1 = []
# n = int(input("n = "))
# for i in range(n):
#     x = int(input("-> "))
#     s1.append(x)
# print(s1)

# a = int(input("Введите количсетво запросов "))
# s = []
# for i in range(a):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3")
# print(s)


# Область пересечения списков
# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:  # Если i уже в списке с
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# -----------------------------------------------------
# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# i = 0
# while i < len(a):
#     c.append(a[i])
#     c.append(b[i])
#     i += 1
# print(c)
# ------------------------------------------------------


# s = [1, 2, 3, 0, 5, 6, 7, 5, 0, 0]
# s[7:] = []  # удаляет значения в заданном периоде
# print(s)
# s.remove(0)  # Удаляет элемент из списка с заданным значением,
# # если элементов несколько, то удалится только  самый первый
# print(s)
# s.remove(3)
# print(s)
#
# s[3:5] = []
# print(s)
#
# last = s.pop()  # возвращает элемент на указанной позиции, удаляя его из списка
# print(last)
# print(s)
# #
# # s.clear()  # Удаляет из списка все имеющиеся значения
# # print(s)
# #
# del s[:]
# print(s)


# s = [1, 20, 3, 4, 5, 6, 7, 3, 0, 0]
# num = s.count(3)  # Считает количество значений "3" в списке
# print(num)
#
# ind = s.index(20)  # Указывает положение первого индекса по значению
# print(ind)
#
# ind = s.index(3, 3)  # Указывает положение индекса в заданном диапазоне
# print(ind)
#
# s_copy = s.copy()  # Возвращает копию списка
# print(s)
# print(s_copy)
#
# a = [1, 2, 3]
# b = a
# print("a = ", a)
# print("b = ", b)
# a.append(20)  # при присваивании изменения затронут обе переменные
# print("a = ", a)
# print("b = ", b)
#
# s.append(120)
# print(s)
# print(s_copy)  # в копию изменения не идут
#
# s.reverse()  # перестраивает элементы списка в обратном порядке
# print(s)

# s.sort()  # сортирует значения по возрастанию
# print(s)

# s.sort(reverse=True)  # сортирует значения по убыванию
# print(s)


# sorted_s = sorted(s)  # пересохраняет сортировку в новую переменную
# print(sorted_s)
# print(s)

# sorted_s = sorted(s, reverse=True)  # пересохраняет сортировку в новую переменную по убыванию
# print(sorted_s)
# print(s)

# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len)  # Сортировка по длине символов
# # s2.sort(key=len, reverse=True)
# print(s2)

# -----------------------------------------------------------------ИМПОРТ МОДУЛЕЙ
# import random
# print(random.random())  # [0.0, 1,0] возвращает случайное  число в данном диапазоне не включая 1

# from random import random, randint, randrange
# print(random())  # [0.0, 1,0] возвращает случайное  число в данном диапазоне не включая 1
# print(randint(0, 9))  # [0, 9] возвращает случайное целое число в данном диапазоне включая указанные
# print(randrange(0, 10, 2))  # [0, 10, шаг] возвращает случайное целое число в данном диапазоне не включая последнее
# import math
# import random
# import random as r  # псевдоним метода (random)
#
# print(r.randint(0, 5))
# print(r.randrange(0, 5, 2))
#
# cities = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(r.choice(cities))  # случайный выбор из списка
#
# s = [55, 66, 77, 88, 99]
# print(r.choice(s))
#
# s = [55, 66, 77, 88, 99, 45, 63, 21]
# print(r.sample(s, 3))  # 1 = из какого списка, 2 = количество элементов
# print(r.choices(s, k=3))
# r.shuffle(s)  # перемешивает список случайным образом
# print(s)
# print(round(r.uniform(10.5, 20.5), 2))  # генерирует вещественное число в заданном диапазоне
#
# mas = [r.randint(0, 100) for i in range(10)]  # генерация случайного списка от 0 до 100 из 10 элементов
# print(mas)

# =------------------------------------------------------------------------------------------30.09.21
# import copy
# import random as r

# lst = [5, 3, 2, 4, 1]
# print("Длина списка", len(lst))
# print("Минимальная значение", min(lst))
# print("Максимальное значение", max(lst))
# print("Сумма", sum(lst))


# mas1 = [r.randint(0, 100) for i in range(10)]
# print(mas1)
# max_1 = max(mas1)
# print("Max: ", max_1)
# mas1.remove(max_1)
# print(mas1)
# mas1.append(max_1)
# print(mas1)

# mas1 = [r.randint(-20, 20) for i in range(10)]
# print(mas1)
# mas1.sort(reverse=True)
# print(mas1)

# a = [r.randint(0, 100) for i in range(10)]
# print(a)
# min_1 = min(a)
# print(min_1)
# print("Min: ", min_1)
# min_2 = a.index(min_1)
# print("Index_min: ", min_2)
#
# del a[0:min_2]
# # print(a[min_2:])  # второй вариант
# print(a)

# in = Оператор принадлежности =-----------------------------------------------------------------
# not in =--- Не содержится ли
# x = list('1a2asd32asda32')
# print(x)
# print("a" in x)
# print("a" not in x)

# lst = []
# if lst:
#     print("True")
# else:
#     print("False")

# lst = [1, 's', 'a', 'f', 5, 8, 'y']
# if 'a' in lst:
#     print("True")
# else:
#     print("False")

# a = int(input("Введите размер первого списка: "))
# b = int(input("Введите размер первого списка: "))
# list1 = [r.randint(0, 10) for i in range(a)]
# list2 = [r.randint(0, 10) for j in range(b)]
# list3 = list1 + list2
# print(list1)
# print(list2)
# # print(list3)
#
# list3 = []  # ============== первый вариант  проверяет есть ли в другом спике идентичные значения и не выводит их
# print(list3)
# for i in list1:
#     repeat = False
#     for j in list2:
#         if i == j:
#             repeat = True
#     if not repeat:
#         list3.append(i)
# for i in list2:
#     repeat = False
#     for j in list1:
#         if i == j:
#             repeat = True
#     if not repeat:
#         list3.append(i)
# print(list3)

# list3 = []  # ============= второй вариант
# for i in range(len(list1)):
#     if list1[i] not in list3:  # проверяет нет ли в списке 3 и проверяет 1 список на дубли
#         list3.append(list1[i])
# for i in range(len(list2)):
#     if list2[i] not in list3:  # проверяет нет ли в списке 3 и проверяет 2 список на дубли
#         list3.append(list2[i])
# print("Элементы обоих списков без повторений: ", list3)

# ================================================= 3 Вариант Владислав
# import random
# listVal1 = [random.randint(0, 10) for i in range(int(input("Введите размер первого списка: ")))]
# listVal2 = [random.randint(0, 10) for j in range(int(input("Введите размер первого списка: ")))]
# listVal3 = listVal1 + listVal2
# print(listVal1)
# print(listVal2)
#
# print("Список без повторений:")
# listVal5 = []
# listVal5 += [i for i in listVal1 if listVal1.count(i) == 1]
# listVal5 += [i for i in listVal2 if listVal2.count(i) == 1]
# print(listVal5)
# print("Общие элементы")
# listVal6 = [i for i in listVal1 if i in listVal2]
# print(listVal6)
# =================================================

# list3 = []
# for i in range(len(list1)):  #=========Ю вывести элементы которые повторяются в двух списках
#     if list1[i] in list2 and list1[i] not in list3:
#         list3.append(list1[i])
# print(list3)


# =========================================================================>

# users1 = ["Игорь", "Владимир", "Алла"]
# users2 = users1
# users2.append("Виктория")
# print(users1)
# print(users2)
# # is = возвращает True если оба операнда указывают на один и тот же обьект
# # is not = возвращает True если оба операнда указывают разные обьекты
# print(users1 is users2)

# import copy

# users1 = ["Игорь", "Владимир", "Алла"]
# users2 = copy.deepcopy(users1)  # Копирует обьект
# users2.append("Виктория")
# print(users1)
# print(users2)
# print(users1 is users2)
# =======================================================================>

# ==============================================ВЛОЖЕННЫЕ СПИСКИ МАТРИЦА
# m = [
#     [1, 2, 3, 4],  # строка 0
#     [5, 6, 7, 8],  # строка 1
#     [9, 10, 11, 12]  # строка 2
# ]
# print(m[1][2])
# # m[row][col]  # Номер строки и номер столбца
# print(m)
#
# # Вывод
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
#
# # тот же самый вывод
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()

# Возведем в квадрат
# for row in m:
#     for x in row:
#         print(x ** 2, end="\t")
#     print()
# сокращено
# square = [[x ** 2 for x in row] for row in m]
# for row in square:
#     for x in row:
#         print(x, end="\t")
#     print()

# =====>
# w, h = 5, 3
# m = [[0 for x in range(w)] for y in range(h)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()


# m = [[x for x in range(y, y+10)] for y in range(10)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# for x, y in [[1, 2], [3, 4, ], [5, 6], [7, 8]]:  # первое значение будет Х, второе будет У
#     print(x, "+", y, "=", x + y)

# Преобразовать матрицу таким образом, что бы строки с нечетными индексами были упорядочены по убыванию,
# а с четными по возрастанию

# m = [
#     [2, 5, 8],
#     [8, 5, 6],
#     [9, 4, 1],
#     [1, 2, 4],
#     [7, 5, 6]
# ]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
#
# for i in range(len(m)):
#     if i % 2 == 0:
#         m[i].sort()
#     else:
#         m[i].sort(reverse=True)
#     print()
#
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()


# w, h = 5, 4  # генератор матрицы
# m = [[r.randint(1, 30) for x in range(w)] for y in range(h)]
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# =========================== ---------------------------------->
# Вывести матрицу от -20 до 10 и посчитать количесвто отрицательных чисел
# w, h = 3, 4
# m = [[r.randint(-20, 10) for x in range(w)] for y in range(h)]
# for row in m:
#     for x in row:
#         print(x, end="\t\t")
#     print()
# s = 0
# for i in m:
#     for x in i:
#         if x < 0:
#             s += 1
# print()
# print("Количсевто отрицательных чисел", s)


# DZ-1
# a = []
# b = int(input("Введите элементы списка: "))
# for i in range(b):
#     x = int(input("-> "))
#     a.append(x)
# v = a[::2]
# for i in v:
#     print(i, end=" ")

# DZ-2
# a = []
# b = int(input("Введите элементы списка: "))
# for i in range(b):
#     x = int(input("-> "))
#     a.append(x)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# DZ -3
# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(a)
# for i in range(len(a)):
#     for x in range(len(a)):
#         if i != x and a[i] == a[x]:
#             break
#     else:
#         print(a[i], end=" ")

# 03.10.21
# DZ-1
# import copy
# import random as r
#
# a = [int(input("->")) for i in range(int(input("n = ")))]
# b = int(input("Введите число: "))
# print("b = ", b)
# for i in a:
#     if b in a:
#         print("Число присутствует в элементах списка")
#         break
#     else:
#         print("Такого числа нет в элементах списка")
#         break

# DZ-2

# summa = 0
# a = [r.randint(0, 100) for x in range(20)]
# print(a)
# for i in a:
#     summa += i
# print("Summa: ", summa)

# DZ-3
# a = [r.randint(0, 100) for x in range(10)]
# print(a)
# a2 = sorted(a, reverse=True)
# print(a2)

# a = [r.randint(-100, 100) for x in range(10)]
# print(a)
# a2 = sorted(a, reverse=True)
# print(a2)
# a2 = []
# a3 = []
# for i in range(len(a)):
#     if a[i] > 0:
#         a2.append(a[i])
#     else:
#         a3.append(a[i])
# a2.sort(reverse=True)
# print(a3)
# print(a2)
# a4 = a2 + a3
# print(a4)


# a = [r.randint(-100, 100) for x in range(10)]
# print(a)
# e = []
# v = 0
# for i in range(len(a)):
#     while i >= 0:
#         v = max(a)
#         e.append(v)
#         a.remove(v)
#         break
# print(e)


# ===================================================================================> 05.10.21

# import math as m
# from math import sqrt, ceil, floor  # указываем какие методы вызываем, не нужно прописывать math перед каждым методом
# import locale
# from math import *  # любые методы из math

# num = sqrt(2)  # Квадратный корень
# print(num)
# num1 = ceil(3.8)  # Округление в верхнюю сторону
# print(num1)
# num2 = floor(3.8)  # Округление в нижнюю сторону
# print(num2)
#
# print(pi)  # Константа ПИ

# radius = 2
# print(pi * (radius ** 2))

# a = int(input("Введите радиус окружности: "))
# print(round((pi * 2 * a), 2))

# num = -5.24
# print("Модуль числа: ", fabs(num))  # Модуль числа

# a = 8
# b = 20
# c = 10
# print("Наибольший общий делитель: ", gcd(a, b, c))  # Наибольший делитель


# num_list1 = [0.3, 0.3, 0.3]
# print("Сумма элементов списка: ", fsum(num_list1))  # сумма списка всегда вещественное
# print("Сумма элементов списка: ", sum(num_list1))  # сумма списка целые числа
# # decimal  Даёт более точные значения

# print(degrees(3.12159))  # перевод из радианов в градусы
# print(radians(180))  # перевод из градусов в радианы
# print(cos(radians(60)))  # косинус грудусов
# print(sin(radians(90)))  # синус градусов
# print(tan(radians(0)))  # Тангенсы

# # Вывести гипотенузу треугольника по двум катетам
# x = 8
# y = 6
# q = (x**2) + (y**2)
# print(sqrt(q))

# # Вычисление фигур
# a = int(input("Выбор фигуры: 1 - треугольник, 2- Прямоугольник, 3-Круг: "))
# g = 0
# if a == 1:
#     b = float(input("Введите сторону а: "))
#     c = float(input("Введите сторону а: "))
#     f = float(input("Введите сторону а: "))
#     print((b + c + f) /2)
# if a == 2:
#     b = float(input("Введите сторону а: "))
#     c = float(input("Введите сторону а: "))
#     print(b * c)
# if a == 2:
#     b = float(input("Введите радиус круга: "))
#     print(pi * (b ** 2))

# import time


# sec = time.time()
# print("Секунды с начала эпохи", sec)
# local_time = time.ctime(sec)
# print("Местное время", local_time)
# res = time.localtime(sec)
# print("Local time: ", res)
# print("Год", res.tm_year)
# print("Месяц", res.tm_mon)
# print("День месяца", res.tm_mday)
# print("Часы", res.tm_hour)  # с 0 до 23
# print("Минуты", res.tm_min)  # c 0 по 59
# print("Секунды", res.tm_sec)  # с 0 по 61
# print("День недели", res.tm_wday)  # с 0 по 6  # нумерация с нуля
# print("День года", res.tm_yday)  # с 1 по 366
# print("Учет перехода на летнее время", res.tm_isdst)  # 0 или 1 или -1
#
#
# print(time.strftime("Today id %B %d, %Y", time.localtime(456127987)))  # формировать в строке данные в нужном формате
# print(time.strftime("%m/%d/%Y, %H:%M:%S"))

# pause = 5
# print("Программа запустилась....")
# time.sleep(pause)
# print(str(pause) + " second.")

# ЗАДАЧА РЕШЕНА ?  НАПОМИНАЛКА ==========================================>
# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут напомнить ? "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.time()
# time.sleep(2)
# finish = time.time()
# res = finish - start
# print("Program time: " + str(res) + "second.")

# тоже самое без погрешности
# start = time.monotonic()  # без дробных
# time.sleep(1)
# finish = time.monotonic()
# res = finish - start
# print("Program time: " + str(res) + " second.")

# print(time.strftime("Сегодня: %B %d, %Y "))

# import time
# import locale
# locale.setlocale(locale.LC_ALL, "")
#
# sec = time.time()
# local_time = time.ctime(sec)
# print("Местное время: ", local_time)
#
# print(time.strftime("Сегодня: %B %d, %Y "))  # locale.LC_ALL работает с сокращенными


# ============================================================================>>>>>>> ФУНКЦИИ


# def hello(name, word):
#     print("Hello,", name, ". Say " + word, sep="")  # функция должна быть ограждена двумя пустыми строками
#
#
# hello("Irina", "hi")
# hello("Ivan", "hello")


# def get_sum(a, b):  # кэмэл кейс нельзя, только нижний регистор, писать по змеиному
#     print(a + b)
#
#
# x, y = 2, 3
# get_sum(x, y)
# get_sum(2.6, 4.3)
# get_sum("abc", "def")
# get_sum(str(x), "def")


# def symb_ol(a, b, c):
#     for i in range(a):
#         if i % 2 == 0:
#             print(b, end="")
#         else:
#             print(c, end="")
#     print()
#
# symb_ol(9, "+", "-")
# symb_ol(7, "X", "O")
#
# # тоже самое
# def paint_my(n, first, second):
#     for i in range(n):
#         print(first if i % 2 == 0 else second, end="")
#     print()
# paint_my(9, "+", "-")
# paint_my(7, "X", "O")


# def get_sum(a, b):  # ======================================================================/////////
#     return a + b
#     # print()  # ПОД РЕТУРНОМ НИЧЕГО РАБОТАТЬ НЕ БУДЕТ
#
#
# x = 2
# y = 3
# res = get_sum(x, y)
# print(res)
# print(get_sum(2.6, 4.3))


# DZ-1

# x1 = float(input("Введите x1: "))
# y1 = float(input("Введите y1: "))
# x2 = float(input("Введите x2: "))
# y2 = float(input("Введите y2: "))
#
#
# def distance(a, b, c, d):
#     kor = ((a - b) ** 2) + ((c - d) ** 2)
#     res = sqrt(kor)
#     return round(res, 2)
#
#
# print("Растояние между точками: ", distance(x1, y1, x2, y2))


# DZ-2
# print("Найти площадь треугольника по сторонам и углу между ними")
# a = int(input("Сторона 1: "))
# b = int(input("Сторона 2: "))
# c = int(input("Угол: "))
#
#
# def square(side1, side2, injection):
#     s = 0.5 * a * b * sin(radians(c))
#     return s
#
#
# print("Площадь треугольника: ", square(a, b, c))


# ==============================================================================> 07.10.21


# def maxmin(x, y):
#     if x > y:
#         return x
#     else:
#         pass  # =====> элемент заглушки
#
#
# print(maxmin(10, 5))
# print(maxmin(10, 15))


# Написать функцию, нахождения разности, если a > b или сумму, если a < b. a и b вводятся с клавиатуры

# a = int(input("Сторона 1: "))
# b = int(input("Сторона 2: "))
#
#
# def c(n1, n2):
#     if n1 > n2:
#         return n1 - n2
#     else:
#         return n1 + n2
#
#
# print(c(a, b))

# Вывести куб всех чисел от 1 до 10 ( функция, которая принимает один параметр и возвращает значение )


# def kub(a):
#     return  a ** 3
#
#
# for i in range(1, 11):
#     print(i, "число в кубе =", kub(i))

# ================================================================================> Ряд фибоначчи


# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         a, b = b, a + b  # a присваиваем b, а в b присваиваем a+b
#     print()
#
# fib(22)
# fib(61)
#
#
# # тоже самое расписанное уже только с доп переменной
# def fib(n):
#     с = 0
#     a, b = 0, 1
#     while a < n:
#         print(a, end=" ")
#         # a, b = b, a + b  # a присваиваем b, а в b присваиваем a+b
#         c = a + b
#         a = b
#         b = c
#     print()
#
# fib(22)
# fib(61)

# заменить местами первый с последним элементы
# def change(lst):
#     # temp = lst[0]  # вариант 1
#     # print(temp)
#     # lst[0] = lst[-1]
#     # print(lst[0])
#     # lst[-1] = temp
#     # print(lst)
#
#     # lst[0], lst[-1] = lst[-1], lst[0]  #===> второй способ, принт в вызове фнкции
#     # return lst
#
#     start = lst.pop()  # 3 ВАРИАНТ
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))


# def get_sum(a, b, c=0, d=1):  # аргументы по умолчанию должны назначаться с конца ( право налево)
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 2))
# print(get_sum(1, 5, 2))  # если параметров меньше чем в функции, то можно допистаь значение по умолчанию (=1 или другое)
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=6))  # именнованый параметр (ключевые), указывать что имено нужно перезаписать ( ключ=значение),
# # начиная с конца ( право налево)


# def change(n=20, f="-"):
#     for i in range(n):
#         print(f, end=" ")
#     print()
#
#
# change(15, "^")
# change(10, "+")
# change(15)
# change()


# def check_passwd(username, password, min_lenght=8, check_username=True):
#     if len(password) < min_lenght:
#         print("Пароль слишком короткий")
#         return True
#     elif check_username and username in password:
#         print("Пароль содержит имя пользователя")
#         return False
#     else:
#         print("Пароль для пользователя", username, "прошел все проверки")
#         return True
#
#
# check_passwd("Igor", "12345")
# check_passwd("Igor", "12345Igor")
# check_passwd("Igor", "12345name")

#

# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         a = n % 10
#         if even and a % 2 == 0:
#             s += a
#         elif not even and a % 2 != 0:
#             s += a
#         n //= 10
#     return s
#
#
# print("Сумма четных элементов: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетных элементов")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))

#

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age, "\n")
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")
# display_info("Igor", age=23, name="Ira")  # Ошибка
# display_info(age=23, "Igor")  # Ошибка

#

# def func(a, ln=[]):  # сохраняет значения в список при каждом вызове, так быть не должно
#     ln.append(a)
#     return ln
#
#
# print(func(1))
# print(func(2))
# print(func(3))


# def func(a, ln=None):  # решение ( обход ) примера выше
#     if ln is None:
#         ln = []
#     ln.append(a)
#     return ln
#
#
# print(func(1))
# print(func(2))
# print(func(3))


# a1 = [1, 2, 3]
# a2 = [1, 2, 3]
# print(type(a1))
# print(type(a2))
# print(id(a1))
# print(id(a2))
# print(a1 == a2)
# print(a2 is a1)
#
# a3 = 5
# a4 = 5
# print(a3 == a4)
# print(a4 is a3)

# a1 = [1, 2, 3]
# print(id(a1))
# a1.append(4)
# print(a1)
# print(id(a1))
# a1[1] = "Hello"
# print(a1)
# print(id(a1[1]))

# Строки и числа неизменяемые тип данных ( id разное, занимает новую ячейку памяти при изменении )
# s = 5
# print(id(s))
# s = 9
# print(s)
# print(id(s))


# st = "Hello"
# print(id(st))
# st = st[1: -1]  # Пересохраняет данные в новую ячейку
# print(st)
# print(id(st))


# a1 = [1, 2, 3]
# a2 = [1, 2, 3]
# print(id(a1))
# print(id(a2))
# y = a1  # сохраняет список в ту же ячейку
# print(a1 is a2)
# print(a1 is y)  #
#
# a1[0] = 0
# print(a1)
# print(y)  # при изменении списка, изменяется и в пересохраненной переменной


# x = [1, 2, 3]
# y = x[:]  # через срез создается новая ячейка памяти
# print(y)
# y[0] = 0
# print(y)
# print(x)
# print(id(y))
# print(id(x))


# x = [1, 2, 3]
# print(id(x))
# x += [4, 5]  # список = изменяемый тип данных, id не меняется
# print(x)
# print(id(x))


# def add_number(n):
#     print("Внутри функции: ", n, "=", id(n))
#     n += 1
#     print("После присваивания: ", n, "=", id(n))
#
#
# x = 1
# print(x, "=", id(x))
# add_number(x)
# print(x, "=", id(x))

# =====================================================>
# def add_number(n):
#     print("Внутри функции: ", n, "=", id(n))
#     n += [4]  # список не изменит id  в сокращеном виде записи, мы изменяем список
#     n = n + [4]  # список изменит id  мы создаем новый список с новым id и записываем туда n + [4]
#     print("После присваивания: ", n, "=", id(n))
#
#
# x = [1, 2, 3]
# print(x, "=", id(x))
# add_number(x)
# print(x, "=", id(x))


# DZ_11.10.21
# DZ - 1 # немного эксперементов

# a = int(input("1-прямоугольник\n2-треугольник\n3-круг\nВведите номер фигуры: "))
#
# if a == 1 or a == 2:
#     b = int(input("Основание: "))
#     c = int(input("Высота: "))
# else:
#     b = int(input("Радиус: "))
#
# if a == 1:
#     def n(o, v):
#         s = o * v
#         print("Площадь прямоугольника: ", s)
# elif a == 2:
#     def n(o, v):
#         s = 0.5 * o * v
#         print("Площадь треугольника: ", s)
# elif a == 3:
#     def n(o):
#         s = (o ** o) * pi
#         print("Площадь круга: ", s)
#
# if a == 3:
#     n(b)
# else:
#     n(b, c)

# DZ-2

# a = [6, 3, 8, 5, 7, 9, 3, 6, 5, 13, 1]
# b = []
# c = []
#
# for i in a:
#     if i != 1:
#         for j in range(2, i):
#             if (i % j) == 0:
#                 b.append(i)
#                 break
#         else:
#             c.append(i)
# print(c)
# print(b)
# print("Min", min(c))
# print("Max", max(b))


# DZ-3

# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         a = n % 10
#         if even and a % 2 == 0:
#             s += a
#         elif not even and a % 2 != 0:
#             s += a
#         n //= 10
#     return s
#
#
# print("Сумма четных элементов: ")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетных элементов")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# ==============================================================================> 12.10.21
# ==============================================================================> КОРТЕЖ (typle)
# lst = [10, 20, 30]  # список
# tpl = (10, 20, 30)  # кортеж
#
# a = ()
# print(type(a))
# b = tuple()
# print(type(b))
#
# # упаковка кортежа
# a1 = (5, )
# print(type(a1))
# c = 1, 2, 3  # неизменяемый тип данных
# # c = tuple((1, 2, 3))
# print(type(c))
#
#
# t1 = tuple("hello")
# print(t1)

# a = tuple((1, 2, 3, 4, 5))
# print(a)
# print(a[3])
# print(a[1:3])
# a[1] = 3  # не изменяется

# s1 = tuple(int(input("-> ")) for i in range(5))
# print(s1)

# s = input("Введите по порядку, без пробелов элементы кортежа: ")
# a = tuple(s)
# print(a)  # получаем строковые значения
# print(int(a[0]))  # преобразовать одно из значений в число

import random as r

# mas = tuple([r.randint(0, 100) for i in range(10)])
# print(mas)


# mas = tuple([2 ** i for i in range(1, 13)])
# print(mas)
# кортеж поддерживает только два метода ==> count и index
# t1 = tuple("hello")
# t2 = tuple(" world")  # пробел считает как отдельный символ
# t3 = t1 + t2
# print(t3)
# print(len(t3))  # длина кортежа
# print(t3.count("l"))  # считаем заданные элементы
# print(t3.count("a"))
# print(t3.index("l"))  # отображает первый индекс заданного элемента
# # если значения нет в кортеже то index возваращает ошибку, для этого нужно условие:
# if 'a' in t3:
#     print(t3.index('a'))
# else:
#     print("Такого символа нет ")
#
# for i in t3:
#     if i == " ":  # удаляем пробел внутри кортежа
#         continue
#     print(i, end=" ")

#  Найти значения в кортеже и вывести срез от и до значения


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             f = tpl.index(el)
#             s = tpl.index(el, f+1)  # +1
#             return tpl[f:s + 1]  # или тут
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# def ran(a, b):
#     mas = tuple([r.randint(a, b) for i in range(10)])
#     return mas
#
#
# tpl = ran(0, 5)
# print(tpl)
# tpl2 = ran(-5, 0)
# print(tpl2)
#
# tpl3 = tpl + tpl2
# print(tpl3)
# print("0= ", tpl3.count(0))

# t = (10, 11, [1, 2, 3], [5, 6, 7], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# t[4].append("hi")
# print(t, id(t))


# вывечти уникальные числа из списка и вывести в кортеже в обратном порядке
# a = [1, 2, 3, 3, 2]
# b = [2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]
# c = []
#
# def fun(g):
#     for i in g:
#         if i not in c:
#             c.append(i)
#             c.sort(reverse=True)
#     d = tuple(c)
#     return d

# t = fun(a)
# r = fun(b)
# print(t)
# print(r)

# тоже самое == > верный
# def func(lst):
#     a = []
#     [a.append(i) for i in reversed(lst) if i not in a]
#     return tuple(a)
#
#
# print(func([1, 2, 3, 3, 2]))
# print(func([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))

# ========================================> РАСПАКОВКА КОРТЕЖА
# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# тоже самое ( диструктуризация )
# x, y, z = t  # Должно совпадать количество значений
#
# print(x, y, z)

# Возврат нескольких значений и доступ к каждому элементу из кортежа
# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# print(user[1])
# print(user[2])

# ========================УДАЛИТЬ КОРТЕЖ
# индекс кортежа удалить не можем, только весь кортеж
# a = tuple((1, 2, 3, 4, 5))
# del a
# print(a)

# lst = [1, 2, 3, 4, 5]
# a = tuple(lst)
# print(a)
#
# ls = list(a)  # ПЕРЕЗАПИСЫВАЕМ КОРТЕЖ в СПИСОК ( преобразуем )
# print(ls)

# ВЛОЖЕННЫЕ КОРТЕЖИ
# contries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# # распоковка
# print(contries)
# for country in contries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "население = ", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород:", city_name, "население = ", city_population)


# 14.10.21
# DZ-1

# a = [2, 7, 0, 3, 1, 5, -13, 100]
# b = [2, 7, 0, 3, 1, 5, -13, 13]
# c = [26]
# d = [99, 99, 100, 34, -39]
# w = [99, 39, 26, 99, 100, 39, 34]
#
#
# def ch(lst):
#     g = []
#     for i in lst:
#         if i > 0 and i % 13 == 0:
#             g.append(i)
#     if not g:
#         return " no numbers"
#     u = max(g)
#     return u
#
#
# print("{0} -> {1} ".format(a, ch(a)))
# print("{0} -> {1} ".format(b, ch(b)))
# print("{0} -> {1} ".format(c, ch(c)))
# print("{0} -> {1} ".format(d, ch(d)))
# print("{0} -> {1} ".format(w, ch(w)))


# DZ -2
# a = ('ab', 'abcd', 'cde', 'abc', 'def')
# b = 0
# s = 'ab'
# if s in a:
#     print("YES")
#     print(a.index(s))
#     b = a[0]
#     print(b)


# DZ-3
# a = input("Введите значение 253523651: ")
# s = tuple(a)
# lst = []
# print(s)
# for i in s:
#     if i not in lst:
#         print(i, "=",  s.count(i))
#     lst.append(i)

# ==========================================================> МНОЖЕСТВА - set ( сохраняет уникальные значения в списке )
# неупорядочная коллекция уникальных данных
# По индексу обращаться нельзя ( не упорядочный )


# s = {"banana", "apple", "orange", "apple", "orange"}
# print(type(s))
# print(s)
# print(len(s))
#
# a = {}  # пустой будет не set ( не множество )
# print(type(a))
#
# b = set("hello")  # разбивает элемент по буквам исключая дубли
# print(a)
#
# c = ["red", "green", "green", "blue", "purple"]
# col = set(c)
#
# print(col)


# s = {x for x in range(10)}
# s = {x * x for x in range(10)}
# print(s)

# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# num = set(numbers)  # преобразуем в множество
# print(num)

# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# num = {i for i in numbers if i % 2 == 0}  # # преобразуем в множество
# print(num)
#
# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]  # преобразование назад в список
# num = list({i for i in numbers if i % 2 == 0})
# print(num)


# a = 'я обычная строка'
# b = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
#
#
# def to_set(s):
#     d = set(s)
#     return d, len(d)  # при передачи нескольких значений возвращается КОРТЕЖ
#
#
# print(to_set(a))
# print(to_set(b))

# c = {"red", "green", "blue", "purple"}
# print("green" not in c)  # узнаем есть ли значение в множестве


# pr = {1, 2, 3, 5, 7, 7, 11}
# for i in pr:
#     print(i, end=" ")


# r = ["ab_1", "ac_2", "bc_1", "bc_2"]
# a = {i for i in r if "a" in i}  # ======================= ПРОВЕРЯЕМ ЕСТЬ ЛИ БУКВА В ЭЛЕМЕНТАХ
# print(a)

# справа можем пистаь только IF,   if else используем справой стороны
# r = ["ab_1", "ac_2", "bc_1", "bc_2"]
# a = {"A" + i[1:]
#      if i[0] == 'a' else 'B' + i[1:]  # ======================= ЗАМЕНЯЕМ ЭЛЕМЕНТЫ
#      for i in r
#      if i[1] == 'c'}  # выводим с условием что вторая буква с
# print(a)

# a = {0, 1, 2, 3}
# a.add(4)  # ДОБАВИТЬ ЭЛЕМЕНТ В ПРОИЗВОЛЬНЫЙ ИНДЕКС
# print(a)
# a.remove(4)  # УДАЛИТЬ ЗАДАННЫЙ ЭЛЕМЕНТ
# print(a)
# b = 2
# if b in a:  # ПРОВЕРЯЕМ ЕСТЬ ЛИ ЭЛЕМЕНТ В МНОЖЕСТВЕ И УДАЛЯЕМ ЧЕРЕЗ УСЛОВИЕ
#     a.remove(2)
# # a.remove(6)  # если удалить не существующий элемент == ошибка ключа
# print(a)
#
#
# a.discard(6)  # удаление элемента без генерации исключения если элемент отсутствует
# print(a)
#
# a.pop()  # удаление первого элемента
# print(a)
#
# a.clear()
# print(a)

# ==================================================================================> МЕТОДЫ МНОЖЕСТВ
# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)  # Обьединение множеств
# c = b | a  # # Обьединение множеств = тоже самое сокращенный
# a.update(b)  # в список 1 положили список 2
# b |= a  # тоже самое сокращенно
# c = a.intersection(b)  # возвращает множество являющееся пересечением а и b
# c = a & b  # # тоже самое сокращенно
# a &= b  # Оставляет в множестве А только те элементы которые есть в множестве В
# c = a - b  # возвращает разность множеств а и b ( элементы входящие в А но не входящие в B )
# a -= b  # удаляет из множества А все элементы входящие в множество В
# c = a ^ b  # возвращает симметрическую разность множеств А и В (элементы, входящие в А или в В, но не в оба из них одновременно)
# a ^= b  # Записывает в А симметрическу. разность множеств А и В
# c = a <= b  # возвращает true,  если А является подмножеством В
# c = a >= b  # возвращает true,  если B является подмножеством A
# c = a < b  # Эквивалентно A <= B and A != B
# c = a > b  # Эквивалентно A >= B and A != B
# c = a.copy()  # создает копию
# print(c)
# print(a)
# print(b)


# # ЗАДАЧА===========================<<<
# #
# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# ob = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(ob)
# s_max = max(ob)
# s_min = min(ob)
# print("Длина элементов: ", len(ob))
# print("Максимальное значение: ", s_max)
# print("Минимальное значение: ", s_min)

# ======== ЗАДАЧА
# Найдите общие буквы в двух разных строках

# Введите первую строку: Hello
# Введите вторую строку: How are you
# Общими буквами являются:
# e o H
# =>
# y = input("Введите первую строку: Hello")
# x = input("Введите первую строку: How are you")
# c = set(y) & set(x)
# print(c)
# for i in c:
#     print(i, end=" ")

# ======================================>
# ris = {"Марина", "Женя", "Света"}
# mus = {"Женя", "Костя", "Илья"}
# one = ris ^ mus
# two = ris & mus
# draw = ris - two
#
# # one_hobby = ris | mus  # мое
# # two_hobby = ris & mus  # мое
# # one_hobby -= two_hobby  # мое
#
# print(one_hobby)
# print(two_hobby)
# print(draw)

# =======================================================ТИП FROZENSET (замороженное множество )
# его изменять и как то повлиять не можем
# s = frozenset([1, 2, 3, 4, 5])
# print(s, len(s))
# print(2 in s)

# s = frozenset({i ** 2 % 4 for i in range(10)})
# print(s, len(s))
# print(2 in s)

# ==============================================================>
# r1 = set('ABCD')
# b = {frozenset({i + j for j in r1.difference({i})}) for i in r1}
# print(b, end="\t")

# ЗАДАЧА №7======================================================
# def superset(s1, s2):
#     if s1 > s2:
#         print("Объект", s1, "является чистым супермножеством")
#     elif s1 == s2:
#         print("Множества равны")
#     elif s1 < s2:
#         print("обьект", s2, "является чистым супермножеством")
#     else:
#         print("Супермножество не обнаружено")
#
#
# set_1 = {1, 8, 3, 5}
# set_2 = {3, 5}
# set_3 = {5, 3, 8, 1}
# set_4 = {90, 100}
#
# superset(set_1, set_2)
# superset(set_1, set_3)
# superset(set_2, set_3)
# superset(set_4, set_2)


# DZ- 16.10.21
# DZ-1
# Найдите все буквы в первой строке, которые отсутствуют во второй
# a = set(input("Введите первую строку: "))
# b = set(input("Введите вторую строку: "))
# a -= b
# print("Искомыми буквами являются: ")
# for i in a:
#     print(i, end=" ")

# DZ-2
# Посчитайте гласные буквы в строке
#  а, и, е, ё, о, у, ы, э, ю, я
# a = input("Введите строку: ")
# b = set("аиеёщныэюя")
# c = 0
# for i in a:
#     if i in b:
#         print(i, end=" ")
#         c += 1
# print()
# print("Количсетво гласных: ", c)

# DZ-3
# Найдите все буквы, присутствующих хотя бы в одной строке

# a = set(input("Введите первую строку: "))  # test
# b = set(input("Введите вторую строку: "))  # string
# a |= b
# for i in a:
#     print(i, end=" ")

# DZ-4
# Вывод уникальтных букв из двух строк
# a = set(input("Введите первую строку: "))  # hello
# b = set(input("Введите вторую строку: "))  # world
# c = a ^ b
# for i in c:
#     print(i, end=" ")

# DZ-5

# mat = {"Матвей", "Евгения", "Михаил", "Максим", "Наталья"}
# fiz = {"Максим", "Матвей", "Александр"}
# al = list(mat) + list(fiz)
# print("Все призёры: ", al)
# two = mat & fiz
# print("Призёры обеих команд: ", two)
# mat &= fiz
# print("Обновленный список призеров по математике: ", mat)
# fiz.clear()
# print(fiz)


# DZ-6

# list1 = [1, 1, 3, 3, 1]
# list2 = [5, 5, 5, 5, 5, 5, 5]
# list3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
#
#
# def set_gen(lst):
#     c = []
#     v = set()
#     for i in lst:
#         c.append(i)
#         if i not in v:
#             v.add(i)
#         if i in v and c.count(i) >= 2:
#             i = str(i) * c.count(i)
#             v.add(i)
#     return v
#
#
# print(set_gen(list1))
# print(set_gen(list2))
# print(set_gen(list3))

# 19.10.21 ==============================================================>>>> СЛОВАРИ = dict

# a = [1, 2, 3, 4]
# b = {"one": 1, "two": 2}  # КЛЮЧ и ЗНАЧЕНИЕ
# print(b)

# d = {}  # Пустой словарь
# print(d)
# print(type(d))
# d1 = dict()  # Пустой словарь
# print(d1)
#
# d3 = dict.fromkeys(["a", "b"], 100)  # если указаны ключи без значений, то через запятую 100 будет значение
# print(d3)

# a = [1, 2, 3, 4]
# c = dict(a)  # так преобразовать в словарь НЕЛЬЗЯ
# print(c)


# user = [
#     ['igor@gmail.com', 'Igor'],  # из списка
#     ['irina@gmail.com', 'Irina'],
#     ['anna@gmail.com', 'Anna']
# ]

# user = (
#     ('igor@gmail.com', 'Igor'),  # из кортежа, должны быть парные ( кортеж или список) в 1 упадет ключ и 2 значение
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna')
# )
# print(user)
# d_user = dict(user)
# print(d_user)

# d4 = {str(a): a ** 2 for a in range(2, 7)}  # ГЕНЕРАТОР СЛОВАРЯ строки
# print(d4["2"])  # Вывод значения словаря по имени ключа

# d4 = {a: a ** 2 for a in range(2, 7)}  # ГЕНЕРАТОР СЛОВАРЯ цифры
# print(d4)
# print(d4[2])  # Вывод значения словаря по имени ключа
# d4[2] = 15  # записали новое значение
# print(d4)
# d4[5] = 4**2  # можно сразу вычисления записать
# print(d4)

# d5 = {0: 'text', 'one': 40, (1, 2.3): 'кортеж', 42: [2, 3, 4, 7], True: 1}  # КЛЮЧ ДОЛЖНО БЫТЬ НЕ ИЗМЕНЯЕМОЕ ЗНАЧЕНИЕ, список в виде ключа не может
# print(d5)
# print(d5[42][1])  # доступ = в первых скобках доступ к ключу, 2 индекс списка
# print(d5[(1, 2.3)])  # Ключ в виде кортежа
# del d5[(1, 2.3)]  # удаляется и ключ и значение
# print(d5)
#
# print("one" in d5)  # True  = есть ли клюс в словаре
# print("a" in d5)
#
# print(d5.keys())  # отображает все ключи
#
# if 'one' in d5:  # ищет совпадение ключей
#     print("TRUE")
# if 'one' in d5.keys():  # тоже самое только медленей, сперва перебирает все ключи
#     print("TRUE")

# d6 = {'one': 1, 'two': 2, 'three': 3}
# print(d6["four"])  # на несуществующий ключ = ошибка
# key = "four"
# key = "two"  # УДАЛИТСЯ

# if key in d6:  # удаляем через проверку
#     del d6[key]

# try:
#     del d6[key]
# except KeyError:
#     print('Элемента с заданным ключем "' + key + '"нет в словаре')
# print(d6)


# d6 = {'one': 1, 'two': 2, 'three': 3}
# for key in d6:
#     print(key, "=", d6[key])  # Вывод ключей и значений


# ДАН СЛОВАРЬ с числовыми значениями. Необходимо их все перемножить и вывести на экран
# a = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# b = a['x1'] * a['x2'] * a['x3'] * a['x4']
# print(b)


# # ЗАДАЧА
# # d = {i: input("-> ") for i in range(1, 5)}  # тоже самое  через генератор
#
# d = dict()
#
# # for k in range(1,5):  # Тоже самое  через фор
# #     d[k] = input("-> ")
#
# d[1] = input('-> ')
# d[2] = input('-> ')
# d[3] = input('-> ')
# d[4] = input('-> ')
# print(d)
# d2 = int(input("Какой элемент удалить: "))
# del d[d2]
# print(d)


# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
# print(capitals)  # добавляем ключи и значения
#
# countries = ['Россия', "Италия", "Франция", "Испания"]
#
# for country in countries:
#     if country in capitals:
#         # print('Столица страны: ', country, ': ', capitals[country])
#         print('Столица страны: ' + country + ': ' + capitals[country])
#         # print('Столица страны: ' + str(country) + ': ' + str(capitals[country]))
#
#     else:
#         print('В базе нет страны из списка', country)


# product = dict()
# product[1] = ['Core-i3-4330', 9, 4500]
# product[2] = ['Core-i5-4670k', 3, 8500]
# product[3] = ['AMD FX-6300', 6, 3700]
# product[4] = ['Pentium G3220', 8, 2100]
# product[5] = ['Core-i5-3450', 5, 6400]
#
# for key in product:
#     print(key, ') ', product[key][0], ' - ', product[key][1], " шт. по ", product[key][2], 'руб', sep="")
# trig = 1
# while True:  # бесконечный цикл
#     trig = int(input('Введите номер товара: '))
#     if trig == 0:
#         break
#     product[trig][1] = input("Количсетво = ")
#
# for key in product:
#     print(key, ') ', product[key][0], ' - ', product[key][1], " шт. по ", product[key][2], 'руб', sep="")


#
#
#
#
# d = {'A': 1, 'B': 2, 'C': 3}  # в список ВЫВОДИТ КЛЮЧИ
# x = iter(d)
# print(x)
# lst = list(x)
# print(lst)
#
# d.clear()  # ОЧИСТИТЬ СЛОВАРЬ
# print(d)


# d = {'A': 1, 'B': 2, 'C': 3}
# d2 = d.copy()  # независимая копия ( новый обьект )
# print('d =', d)
# print('d2 =', d2)
#
# d2['B'] = 5
# d['E'] = 7
# print('d =', d)
# print('d2 =', d2)


# d = {'A': 1, 'B': 2, 'C': 3}
# value = d.get('A')  # получение значения по ключу
# # value = d.get('E', 'FF')  # что бы не получать none, пишем любое 2 значение
# print(value)
# print(d)
#
# new = d.items()  # возвращает список пар ключей и значений ( в кортеже)
# print(new)
#
# new1 = dict.items(d)
# print(new1)
#
# a = d.keys()  # получаем список ключей СЛОВАРЯ
# print(a)
#
# # item = d.pop('B')  # Обязательно указываем индекс , удаляет и ключ и значениe
# item = d.pop('G', 5)  # если ключа нет, то ошибка ключа
# # если ключ не найден то вернет значение по умолчанию
#
# print(item)  # сохранит только значение
# print(d)


# d = {'A': 1, 'B': 2, 'C': 3}
# item = d.popitem()  # удаляет случайным образом 1 пару ключ-значение
# print(item)
# print(d)


# d = {'A': 1, 'B': 2, 'C': 3}
# item = d.setdefault('E', 5)  # Устанавливает элемент которого нет, по умолчанию значение none, если передаем то через запятую.
# print(item)
# print(d)


# d = {'A': 1, 'B': 2, 'C': 3}
# d.update([('R', 7), ('Q', 9)])  # Добавляет (если их нет) пару ключ-значение через кортеж
# print(d)
# d.update([('A', 20), ('B', 40)])  # если значения есть, обновляет их
# print(d)


# ОБЪЕДИНЕНИЕ СЛОВАРЕЙ
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# c = {'q': 5, 'b': 10}

# z = x | y | c  # оператор сложения словарей, то же самое что решение ниже, перезапишется последний указаный

# z = x.copy()
# print(z)
# z.update(y)  # если ключи повторяются он перезаписывает значение, если нет ключа то добавляет
# print(z)

# Тоже самое
# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {i: d[i] for d in [x, y] for i in d}
# print(z)

# ===================================================ВЫВОД ЗНАЧЕНИЙ
# d = {'A': 1, 'B': 2, 'C': 3}
# v = d.values()  # выводим список значений
# print(v)
# # конвертируем в список значений
# lst = list(v)
# print(lst)

#
# print(list(d.values()))  # тоже самое сразу


# ВЫНЕСТИ В НОВЫЙ СЛОВАРЬ ИМЯ И ЗАРПЛАТУ
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')  # удаляет из d и возвращает в new_d
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)

# # Вариант Юрия == == = >
# slov = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New York"}
# new_s = {}
# print(slov)
# new_s.update([('name', slov.pop("name"))])
# new_s.update([("salary", slov.pop("salary"))])
# print(slov)
# print(new_s)

# DZ-20.10.21
# DZ-1 # объеденить три словаря в один
# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
#
# d = a | b | c
# print(d)

# DZ-2
# Дан словарь
# a = {
#         'emp1': {'name': 'Jhon', 'salary': 7500},
#         'emp2': {'name': 'Emma', 'salary': 8000},
#         'emp3': {'name': 'Brad', 'salary': 6500}
# }
#
# # Измените значение зарплаты Брэда с 6500 до 8500
# print(a['emp3'])
# print(a['emp3']['salary'])
# a['emp3']['salary'] = 8500
#
# for i in a:
#     print(i)
#     for j in a[i]:
#         print(j, ':', a[i][j])

# DZ-3
# чет намудрил )))
# s = 0
# slv = dict()
# for i in range(5):
#     print(i+1, "- й ", end="")
#     a = input('Студент: ')
#     b = int(input("Балл: "))
#     slv[a] = b
# for j in slv:
#     s += slv[j]
# s = s / 5
# lst = set()
# for g in slv:
#     if slv[g] > s:
#         lst.add(g)
# print('Средний бал:', round(s), '. Студенты с баллом выше среднего:')
# for i in lst:
#     print(i)


# ======================================================================================21.10.21
# ВЫВОД ВЛОЖЕНЫХ СЛОВАРЕЙ
# a = {
#     "First": {
#         1: "one",
#         2: "two",
#         3: "three"
#     },
#     "Second": {
#         4: "four",
#         5: "five"
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ':', a[x][y])

# a = {
#     'John': {
#         'N': 3056,
#         'S': 8463,
#         'E': 8441,
#         'W': 2694
#     },
#     'Tom': {
#         'N': 4832,
#         'S': 6786,
#         'E': 4737,
#         'W': 3612
#     },
#     'Anne': {
#         'N': 5239,
#         'S': 4802,
#         'E': 5820,
#         'W': 1859
#     },
#     'Fiona': {
#         'N': 3904,
#         'S': 3645,
#         'E': 8821,
#         'W': 2451
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ':', a[x][y])
#
# b = input("Имя: ")
# c = input("Регион: ")
# print()
# print(a[b][c])
# a[b][c] = int(input("Новое значение: "))
# print(a[b][c])
# # print(f'{a[b][c]}')

# ================================================ГЕНЕРАТОРЫ

# Поменяли местами ключи с значением
# a = {'один': 1, 'два': 2, 'три': 3}
# d = {value: key for key, value in a.items()}
# print(d)


# a = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# d = {value: key for key, value in a.items()}  # в форе две переменных = ключ, значение, items() возвращает ключ-значение
# # слева пишем что хотим получить value: key
# print(d)

# a = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# d = {key: value for key, value in a.items() if value <= 2}  # условия справа
# print(d)

# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)


# s = "Hello"
# b = {i: i * 3 for i in s}
# print(b)  # выводится уникальные элементы


# value = input('-> ')
# lst = [1, 2, 3, 4]
# d = {k: value for k in lst}  # k выступает в виде ключа по списку lst, индекс = ключ
# print(d)

# =====================================================РАЗРЯЖАННАЯ МАТРИЦА

# m = dict()
# m[(0, 1)] = 1
# m[(1, 2)] = 3
# m[(2, 0)] = 2
#
# print(m.get((2, 1), 0))
# print(m.get((2, 0), 0))

# if (1, 2) in m:
#     print(m[(1, 2)])
# else:
#     print(0)

# try:
#     print(m[(2, 0)])
# except KeyError:
#     print(0)


# SciPy = научная библиотека для питона

# List()
# a = {1: 'Rectangle', 2: 'Triangle', 3: 'Circle'}
# value = list(a)
# print(value)
#
# value = list(a.values())  # список значений словаря
# print(value)
#
# k = list(a.keys())  # список ключй словаря
# print(k)
#
# par = list(a.items())  # список пар ( ключ = значение)
# print(par)

# ЗАДАЧА
# Преобразовать список в словарь, так, что бы строковые значени ябыли ключами, а числовые - значениями.
# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
# print(d)


# ========================================= ФУНКЦИЯ zip

# d = list(zip([1, 2, 3], ['one', 'two', 'three']))  # список кортежей
# print(d)

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))  # обьединяет словари, количество должно быть одинаковым в двух.
# print(d)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# d = dict(zip(a, b))
# print(d)

# a = ['Dec', 'Jan', 'Feb']  # zip  в генераторе
# b = [12, 1, 2]
# # d = {k: v for (k, v) in zip(b, a)}
# d = zip(a, b)
# print(d)
# print(type(d))

# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# d = zip(a)
# print(d)
# print(list(d))  # будет работать с одним значением, dict не будет


# a = ['Dec', 'Jan', 'Feb']
# b = [12, 1, 2]
# c = [4.6, 4.0, 9.2]
# d = zip(a, b, c)
# print(d)
# print(list(d))  # будет работать с 3 значением, dict не будет


# print(list(zip(range(5), range(100))))

# ================================================================================
# a = {12: 'Dec', 1: 'Jan', 2: 'Feb'}
# b = {3: 'Math', 4: 'April', 5: 'May'}
#
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)
# ===============================================================================

# РАСПАКОВКА
# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# a, b = zip(*pairs)  # получаем кортеж с данными
# print(a)
# print(b)

# # ПАРАЛЕЙНАЯ СОРТИРОВКА
# ls = [2, 1, 4, 3]
# n = ['b', 'd', 'a', 'c']
#
# # a = sorted(zip(ls, n))
# # print(a)
#
# a = list(zip(ls, n))
# print(a)
# a.sort()
# print(a)
# a = list(zip(n, ls))
# print(a)
# a.sort()
# print(a)
# print(dict(a))


# ЗАДАНИЕ

# month = ['January', 'February', 'March']
# total = [52000.00, 51000.00, 48000.00]
# prod = [46800.00, 45900.00, 43200.00]
#
# for t, p, m in zip(total, prod, month):
#     profit = t - p
#     print("Общая прибыль в", m, '=', profit)

# =======================================================> ** ОПЕРАТОР РАСПАКОВКИ

# one = {'apple': 0.04, 'orange': 0.35}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**one, **two})  # просто обьеденить через скобки не можем, оператор распаковки ** дает такую возможность

# one = {'apple': 0.04, 'orange': 0.35, 'pepper': 0.25}
# two = {'pepper': 0.20, 'onion': 0.55}
# print({**one, **two})  # сотрет дубли и запишет последние значения
#
# for k, v in {**one, **two}.items():  # получаем доступ к распакованным элементам и выводим их
#     print(k, '->', v)


# =============================================================> enumerate ( переменная нумерация ( for ) )

# data = [5, 6, 7, 8, 9, 4, 1]
# for i, val in data:
#     print(i, ':', val)  # ошибка типа что мы не можем взять не итерируемый обьект

# data = [5, 6, 7, 8, 9, 4, 1]
# for i, val in enumerate(data, 1):  # enumerate добавляет числовые значения, 2 значение = start
#     print(i, ':', val)

# data = {1: 5, 2: 6, 3: 7, 4: 8, 5: 9, 6: 4, 7: 1}
# for i, val in enumerate(data, 1):
#     print(i, ':', val)  # в словаре возьмет ключи

# data = {1: 5, 2: 6, 3: 7, 4: 8, 5: 9, 6: 4, 7: 1}
# for i, val in enumerate(data, 1):
#     print(i, ':', data[val])  # в словаре возьмет pyfxtybz
#
# d = {1: {'a': 1, 'b': 2, 'c': 3},
#      2: {'a': 10, 'b': 20, 'c': 30}}
# for i, k in enumerate(d):
#     print(i, ") key =", k, ", value =", d[k], sep="")


# DZ-22.10.21
# DZ - 1
# a = ["red", "green", "blue"]
# b = ["#FF0000", "#008000", "#0000FF"]
# d = dict(zip(a, b))
# print(d)

# DZ-2
# Создайте словарь, в котором ключами будут числа от 1 до 10, а значениями эти же числа, возведенные в куб
# a = {i: i ** 3 for i, key in enumerate(range(10), 1)}
# print(a)

# DZ-3
# a = ['color', 'fruit', 'pet']
# b = ['blue', 'apple', 'dog']
# d = {i: g for i, g in zip(a, b)}
# print(d)

# DZ-4
# Без * но хоть что то )
# a = (10, 9)
# b = (2, 3, 4)
# c = (3, 5, 10, 6)
#
#
# def bug(h):
#     f = []
#     for i in h:
#         f.append(i)
#     return min(f)
#
#
# print(bug(a))
# print(bug(b))
# print(bug(c))

# DZ-5
# Без * но хоть что то )
# a = (3, 9, 1)
# b = (2, 5, 4, 2)
# c = (3, 5, 10, 6, 3)
#
#
# def bug(h):
#     f = []
#     g = 0
#     for i in h:
#         g = i + g
#         f.append(g)
#     for j in f:
#         print(j, end=" ")
#     return f
#
#
# bug(a)
# print()
# bug(b)
# print()
# bug(c)


#  ===============================================================================> 26.10.21

# lst = [1,2,3,4,5]
# itr = iter(lst)  # итератор (метод)
# print(itr)
# print(next(itr))  # функция next выводит по 1 индексу каждый вызов (следующий эл по очереди )
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr, "STOP"))  # если значений больше выйдет ошибка, второе значение выводим по умолчанию.


# lst = [1, 2, 3, 4, 5]
# b = enumerate(lst)
# c = next(b)
# print(c)
# print(type(c))
# print(next(b))


# a = [1, 2, 3]
# b = [4, *a, 5, 6]  # * распаковывает данные, в данном случает список а
# print(b)

# ===================================================================> * ОПЕРАТОР
# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, "abc"))


# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#     # return sum(params)  # суммирование без цикла
#
#
# print(summa(1, 2, 3, 4, 5))
# print(summa(3, 5, 1))


# def func(*args):
#     a = {i: i for i in args}
#     return a
#     # return {i: i for i in args}  # или так
#
#
# print(func(1, 2, 3, 4, 5))


# ======= ЗАДАЧА
# найти среднее арифметическое передаваемых аргументов, вывести его и списком все число меньше его
# def func(*args):
#     a = sum(args) / len(args)
#     print(a)
#     return [i for i in args if i < a]
#
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))


# def print_scores(student, *scores):  # несколько параметров с * ( простые параметры ставятся перед параметром с *)
#     print("Имя студента: ", student)  # здесь один аргумент
#     for s in scores:  #  в цикле выводим множество значений
#         print(s, end=" ")
#     print()
#
#
# print_scores("Валентин", 100, 90, 88, 92, 99)
# print_scores("Роман", 96, 20, 33, 56)


# ЗАДАЧА
# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])  # преобразуем в число и разворачиваем через срез
#
#
# def func(*args, only_add=False):
#     res = []
#     for i in args:
#         if not only_add or (only_add and i % 2 != 0):  # первое условие для 1 варианта, 2 для 2-го
#             res.append(reverse_num(i))  # вызываем другую функцию где разворачивам i
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_add=True))


# def func(a, b, *args):
#     return a, b, args
#
#
# print(func(1, 2))
# print(func(1, 2, 3, "abc"))


# def func(**kwargs):  # =======================> передаем  с **
#     return kwargs
#
#
# print(func(a=1, b=3, c=5))
# print(func())
# print(func(w="Python"))


# def func(*args, **kwargs):  # ======================= * и **
#     return args, kwargs
#
#
# print(func(4, 6, a=1, b=3, c=5))
# print(func())
# print(func(w="Python"))


# def info(**data):
#     for k, v in data.items():  # проходимся по паре = ключ, значение
#         print(k, "is", v)
#     print()
#
#
# info(firstname="Irina", lastname="Sharma", age=22, phone="1234567898")
# info(firstname="Igor", lastname="Wood", email="igor@mail.ru", country="Russia", age=22, phone="8548356789")


# my_dict = {"one": "first"}
#
#
# def db(**kwargs):
#     my_dict.update(**kwargs)  # добавляем ключ значение в словарь
#     return my_dict
#
#
# print(db(k1=22, k2=33, k3=44))
# print('my_dict = ', db(name='bob', age=31, weigt=61, eyes='grey'))


# ====================================================================================
# def func(name, *args, odd=False,
#          **kwargs):  # odd=False должен быть до **kwargs, иначе он его запишет его как ключ и значение
#     return name, args, odd, kwargs  # **kwargs должен быть в конце
#
#
# print(func("Irina", 1, 2, 3, 4, odd=True, one="1", two="3"))
# =====================================================================================


# def func(name, *args, **kwargs):
#     print(args[2])  # получаем аргументы по индексу
#     print(kwargs['one'])  # получаем значение по ключу
#
#
# func("Irina", 1, 2, 3, 4, one="1", two="3")


# def pet_names(name, *args, **kwargs):  # выводим через 3 параметра
#     print("Name: ", name)
#     for pet, name in kwargs.items():
#         print(pet, ";", name)
#
#
# pet_names("Jonathan", dog='Brock', fish=['Larry', 'Curly', 'Molly'], turtle='Sheldon')


# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = {**x, 'one': 1, 'two': 2, **y}  # b перезапишет значение
# print(z)


# ============================================================================== ТИПЫ ПЕРЕМЕНЫХ и global
# name = "Tom"
# print(name)
#
#
# def hi():
#     global name  # глобал устанавливает переменой глобальное значение
#     name = "Sam"
#     print("Hello", name)
#
#
# def bye():
#     print("Good bye", name)
#
#
# print(name)  # до вызова функции где ставим глобал = будет ТОМ
# hi()
# print(name)  # после вызова функции будет SAM
# bye()


# i = 5
#
# def func(arc=i):  # если в функции используем переменную, то она должна быть выше
#     print(arc)
#
#
# i = 6  # не перезапишет, т.к. должна быть выше функции
# func()


# def add_two(a):
#     x = 2
#     return a + x
#
#
# print(add_two(3))
# print(x)


# def add_five(a):
#     x = 2
#
#     def wrap():
#         print("x = ", x)
#         return a + x
#     return wrap()
#
# print(add_five(5))


# import builtins
#
# names = dir(builtins)
#
# for i in names:
#     print(i)


# DZ-28.10.21
# DZ-1
# import math
#
#
# def figure_type(name, **kwargs):
#     print(name, end=" ")
#     lst = []
#     for key, i in kwargs.items():
#         lst.append(i)
#     if name == 'rhombus':
#         print(lst[0] * lst[1] / 2)
#     elif name == 'square':
#         print(lst[0] ** 2)
#     elif name == 'trapezoid':
#         s = 0.5 * (lst[0] + lst[1]) * lst[2]
#         print(s)
#     elif name == 'circle':
#         print((lst[0] ** 2) * math.pi)
#     else:
#         print('invalid data')
#
#
# figure_type('rhombus', d1=10, d2=8)
# figure_type('square', a=5)
# figure_type('trapezoid', a=12, b=3, h=6)
# figure_type('circle', r=18)
# figure_type('unknown', a=1, b=2, c=3)


# ===================================================================== 28.10.21

# def outer_func(who):
#     def inner_func():
#         print('Hello', who)
#
#     inner_func()
#
#
# outer_func('world')
# outer_func('star')
# # inner_func()  # вызов вложенной функции выдаст ошибку

# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print('Сумма внутренней функции: ', a + b)
#
#     fun2(4)
#     print('Значение внешней переменной a: ', a)
#
#
# fun1()

# =================================================

# x = 25
#
#
# def fn():
#     global t
#     a = 30
#     print('Global: ', x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('Nonelocal: ', a)
#         return
#     inner()
#     t = a
#     return
#
#
# fn()
#
# z = x + t
# print(z)
# ==================================================


# def fn1():
#     x1 = 25
#
#     def fn2():
#         x1 = 33
#
#         def fn3():
#             nonlocal x1  # перезапишет на новое знач. область на уровень выше (на один уровень где обьявлена переменная)
#             x1 = 55
#
#         fn3()
#         print('fn2.x1 =', x1)
#
#     fn2()
#     print('fn1.x1 =', x1)
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b  # изнутри без nonlocal переменные не видны
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# result = outer(2, 3, -1, 4)
# print('result: ', result)


# МУТНАЯ ЗАДАЧА -+-+-+-+-+-+-+-+-+-+-+-+-+-
# def rect_paral_square(a, b, c):
#     s = 0
#
#     def rect_square(i, j):
#         nonlocal s
#         s += i * j
#
#     rect_square(a, b)
#     rect_square(a, c)
#     rect_square(c, b)
#     return 2 * s
#
#
# print(rect_paral_square(2, 4, 6))
# # print('s =', s)
# print(rect_paral_square(5, 8, 2))
# # print('s =', s)
# print(rect_paral_square(1, 6, 8))
# # print('s =', s)
# -+-+-+-+-+-+-+-+-+-+-+-+-+--+-+-+-+-+-+-+-+-+-+-+-+-+-

# def increment(number):
#     def inner_increment():
#         return number + 1
#     return inner_increment()
#
#
# print(increment(10))

# ===

# def increment(n):
#     def inner_increment(x):
#         return n + x
#     return inner_increment(5)
#
#
# print(increment(10))

# ====================================================================================== CLOSURE (ЗАМЫКАНИЕ)

# def increment(n):
#     def inner_increment(x):
#         return n + x
#     return inner_increment  # без скобок, ничего не передаем
#
#
# a = increment(12)
# print(a(5))
# # print(increment(12)(5))  # другой способ, тоже самое, обычно не используется ( нехороший тон )


# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# ================================================= ЗАДАЧА с ЗАМЫКАНИЕМ

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()

# ======================================  СОРТИРОВКА ЧЕРЕЗ ВСТРОЕННУЮ ФУНКЦИЮ

# studens = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Ella': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classfilter(lower, upper):
#     def class_student(exem):
#         return {k: v for (k, v) in exem.items() if lower <= v <= upper}
#
#     return class_student
#
#
# a = make_classfilter(80, 100)
# b = make_classfilter(70, 80)
# c = make_classfilter(50, 70)
# d = make_classfilter(0, 50)
# print(a(studens))
# print(b(studens))
# print(c(studens))
# print(d(studens))

# ===========================================
# ============ Калькулятор========================================ИНТЕРЕСНО
# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print()
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
#
# obj1 = func(5, 2)
# print(obj1.sub())
#
# obj1 = func(5, 2)
# print(obj1.mul())
# ================================================

# =======================================================================LAMBDA == АНОНИМНАЯ ФУНКЦИЯ (lambda)

# print((lambda x, y: x + y)(1, 2))
#
#
# func = lambda x, y: x + y  # сохраняем в переменную и аргументы передаем уже при вызове
# print(func(1, 2))
# print(func('a', 'b'))

# =============

# print((lambda x, y: (x ** 2) + (y ** 2))(2, 5))

# ============

# summ = lambda a=1, b=2, c=3: a + b + c
# print(summ(10))

# ================

# func1 = lambda *args: args
# print(func1(1, 2, 3, 4))
# print(func1('a', 'b', 'c', 'd'))

# ===================================

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
# for t in c:
#     print(t('abc'))

# ===================================

# def inc(n):
#     return lambda x: x + n
#
# f = inc(42)
# print(f(0))
# print(f(3))

# =================================
# d = 55
# inc = (lambda n: (lambda x: x + n))  # тоже самое что выше ( вложенная lambda )
#
# f = inc(d)
# print(f(10))
# print(f(3))

# =================================

# print((lambda n: (lambda x: x + n))(42)(3))  # сокращенная запись

# ===============================

# print((lambda x: (lambda y: (lambda z: x + y + z)))(2)(4)(6))  # вложенные lambda для 3 значений
# print((lambda x: lambda y: lambda z: x + y + z)(2)(4)(6))  # без скобок
# sum3 = (lambda x: lambda y: lambda z: x + y + z)  # через переменную
# print(sum3(2)(4)(6))

# объяснение на обычных функциях:
# def f1(x):
#     def f2(y):
#         def f3(z):
#             return x + y + z
#
#         return f3
#
#     return f2
#
#
# print(f1(2)(4)(6))
# ===============================

# 1436 (import)
# DZ-01.11.21
# from math import *

# ===========================================
# def quadratic(a, b, c):
#     d = b * b - 4 * a * c
#     lst = []
#     if d > 0:
#         x1 = (-b - sqrt(d)) / (2 * a)
#         x2 = (-b + sqrt(d)) / (2 * a)
#         lst.append(x1)
#         lst.append(x2)
#         return lst
#
#
# print(quadratic(2, 3, -5))
# ===========================================


# # тесты/эксперементы
# d = ((lambda a: (lambda b: (lambda c: b * b - 4 * a * c)))(2)(3)(-5))
# x1 = ((lambda a: (lambda b: (lambda c: (-a - sqrt(b)) / (2 * c))))(3)(d)(2))
# x2 = ((lambda a: (lambda b: (lambda c: (-a + sqrt(b)) / (2 * c))))(3)(d)(2))
# lst = [x1, x2]
# print(lst)


# # тесты тесты
# d = ((lambda a: (lambda b: (lambda c: b * b - 4 * a * c)))(2)(3)(-5))
# x1 = (lambda n: (lambda a, c: (-a - sqrt(n)) / (2 * c)))
# x2 = (lambda n: (lambda a, c: (-a + sqrt(n)) / (2 * c)))
# f = x1(d)
# f2 = x2(d)
# lst = [f(3, 2), f2(3, 2)]
# print(lst)


# ===========================================================================02.11.21


# ====================================== Сортировка через лямбда

# d = {'b': 15, 'a': 10, 'c': 4}
# # list_d = list(d)  # получим только ключи
# list_d = list(d.items())  # получим список кортежей
# print(list_d)
# list_d.sort(key=lambda i: i[1])  # будет сортировать по индексу кортежа, сорт работает только со списком
# print(list_d)
# print(dict(list_d))


# players = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#        {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#        {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#        {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}]
#
#
# # d_players = list(players.items())  # ошибка
# # print(d_players)
#
# res = sorted(players, key=lambda item: item['last name'])  # сортед сортирует любой тип данных
# res1 = sorted(players, key=lambda item: item['raiting'])
# res2 = sorted(players, key=lambda item: item['raiting'], reverse=True)
#
# print(res)
# print(res1)
# print(res2)

# ============================================================================

# a = [
#     (lambda x, y: x + y),
#     (lambda x, y: x - y),
#     (lambda x, y: x * y),
#     (lambda x, y: x / y),
# ]
#
# b = a[0](5, 12)  # по индексу выбираем кортеж с лямбда
# print(b)

# ======================================================

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 1]
#
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# ======================================================

# d = {
#     1: lambda: print('Monday'),  # ЕЛСИ НЕТ ПРИНИМАЕМОГО АРГУМЕНТА, сразу :
#     2: lambda: print('Tuesday'),
#     3: lambda: print('Wednesday'),
#     4: lambda: print('Thursday'),
#     5: lambda: print('Friday'),
#     6: lambda: print('Saturday'),
#     7: lambda: print('Sunday'),
# }
#
# d[2]()  # вызвали как функцию

# ====================================================
import re
from math import *

# d = {
#     'circle': lambda x: math.pi * (x * x),
#     'quadro': lambda x, y: x * y,
#     'trap': lambda x, y, c: ((x + y) / 2) * c,
# }
#
# print('Площадь окружности: ', d['circle'](2))
# print('Площадь Прямоугольника: ', d['quadro'](2, 5))
# print('Площадь Трапеции: ', d['trap'](2, 10, 15))

# ====================================================

# ========================================================== ТЕРНАРНЫЕ ВЫРАЖЕНИЯ
# TRUE if условие else FALSE

# maximum = lambda a, b: a if a > b else b
# print(maximum(15, 12))
# print(maximum(5, 13))

# maximum = lambda a, b, c: a if a < b and a < c else b if b < a and b < c else c
# print(maximum(9, 8, 5))

# ======================================================== ФУНКЦИЯ MAP ==========================================


# def mul(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# lst2 = list(map(mul, lst))  # map проходится по всему списку
# print(lst2)

# ТОЖЕ САМОЕ
# def mul(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# lst2 = list(map(lambda t: t * 2, lst))
# print(lst2)
# ================================================

# t = (2.88, -1.75, 100.55)
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)

# ==========================================

# lst = ['1', '2', '3', '4', '5', '6', '7']
# lst2 = list(map(int, lst))  # преобразование строки в цифры
# print(lst2)

# ========================================

# areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.000135]
# # res = list(map(round, areas))  # round без второго параметра округлил по умолчанию
# res = list(map(round, areas, range(1, 7)))  #
# print(res)

# ======================================= создание кортежей, списков из двух списков

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# res = list(map(lambda x, y: (x, y), st, num))  # (x, y) что получаем, если dict то сразу в словарь
# print(res)

# =======================================

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# res = list(map(lambda x, y: (x + y), l1, l2))
# print(res)

# ======================================

# st = 'hello'
# res = list(map(lambda x: x * 3, st))
# print(res)

# ================================================================== ФУНКЦИЯ FILTER

# t = ('adsd', 'sdd', 'dsdsdsd', 'sd', 'dwwdddwwwww')
# t2 = tuple(filter(lambda s: len(s) == 3, t))  # работает по условию, в данном случае вернет если длина равна 3
# print(t2)

# ===============================================

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# =============================================

# lst = [random.randint(1, 40) for i in range(10)]
# lst2 = list(filter(lambda s: 10 <= s <= 20, lst))
# print(lst)
# print(lst2)

# ============================================
# # извлеките числа делимые на 15
# lst = [45, 55, 60, 37, 100, 105, 220]
# lst2 = list(filter(lambda s: s % 15 == 0, lst))
# # lst2 = list(filter(lambda s: not s % 15, lst))  # второй вариант
# print(lst)
# print(lst2)

# ========================================== СОВМЕЩЕННЫЕ MAP и FILTER

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, range(10))))
# print(m)

# =====================================================================ПОЛИНДРОМ с лямбда == ЧЕРЕЗ СРЕЗ

# k = ('madam', 'fire', 'tomato', 'book', 'kiosk', 'mom')
# m = list(filter(lambda x: x == x[::-1], k))
# print(m)

# ==================================================================================== ДОКУМЕНТИРОВАНИЕ

# def square(n):
#     """принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)

# a = """Тройные двойные кавычки"""
# b = '''Тройные двойные кавычки'''
# print(a)
# print(b)

# def cylinder(r, h):
#     """
#     вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основе заданной высоты и радиуса основания
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(3, 6))
# print(cylinder.__doc__)
# print(max.__doc__)

# DZ-03.11.21
# DZ-1

# def func(x):
#     def func2(y):
#         return x * y
#     return func2
#
#
# res = func(2)
# print(res(15))
# print(res(20))
# res = func(3)
# print(res(15))
# print(res(20))


# DZ-2

# sum3 = (lambda x: (lambda y: (lambda z: x + y + z)))
# print(sum3(2)(4)(6))

# DZ-3

# s = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
#
# res = sorted(s, key=lambda i: i['name'])
# print(res)
# res = sorted(s, key=lambda i: i['final'], reverse=True)
# print(res)

# DZ-4

# s = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nikolas', 'final': 98},
# ]
# d = []
# for i in s:
#     d.append(i['final'])
# for j in s:
#     if j['final'] == min(d):
#         print(j)
#     elif j['final'] == max(d):
#         print(j)
#
#
# # а так нельзя схитрить ? )
# res = tuple(filter(lambda x: x['final'] != 95, s))
#
# print(res)


# ========================================================================= 04.11.21 ДЕКОРАТОРЫ

# def hello():
#     return 'Hello, I am func "hello"'
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)

# ===========================================

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello  # в переменную записали имя функции и потом вызываем по переменной со скобками
# print(test())

# =============================================

# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()  # тут вызывается func_test
#         print('Code after')
#     return func_wrapper
#
# @my_decorator
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# # test = my_decorator(func_test)
# # test()
# func_test()

# ==========================================

# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#     return wrap
#
#
# @bold  # очередность применения сверху вниз
# @italic
# def hello():
#     return 'text'
#
#
# print(hello())

# =========================================

# def deco(fn):
#     counter = 0
#     def wrapper():
#         nonlocal counter
#         fn()
#         counter += 1
#         print('Вызов функции', counter)
#
#     return wrapper
#
#
# @deco
# def hello():
#     print('Hello')
#
#
# hello()
# hello()
# hello()

# =======================================

# def args_decoration(fn):
#     def wrap(*arg1, **arg2):
#         print("args: ", arg1)
#         print("kwargs: ", arg2)
#         fn(*arg1, **arg2)  # тут вызывает print_full_name
#
#     return wrap
#
#
# @args_decoration
# def print_full_name(a, b, c='Viktor', study='Python'):
#     print(a, b, c, 'изучают', study, '\n')
#
#
# print_full_name("Ирина", "Елизавета", "Светлана", study='JavaScript')
# print_full_name("Владимир", "Екатерина")

# ===================================

# def args_decoration(fn):
#     def wrap(*args, **kwargs):
#         print('*' * 20)
#         print(args, kwargs)
#         fn(*args, **kwargs)  #
#         print('*' * 20)
#
#     return wrap
#
#
# @args_decoration
# def one(a, b):
#     print(a + b)
#
#
# @args_decoration
# def two(a, b, c=3):
#     print(a * b * c)
#
#
# one(2, 3)
# two(2, 3, 4)
# two(2, 3, c=5)

# =================================

# def args_decorator(arg1, arg2):
#     print('Я создаю декоратор. Аргументы: ', arg1, arg2)
#
#     def my_decorator(func):
#         print("Я- декоратор. Аргументы", arg1, arg2)
#
#         def wrapper(func_arg1, func_arg2):
#             print('Я - обертка вокруг декорируемой функции')
#             func(arg1, arg2)
#             return func(func_arg1, func_arg2)
#
#         return wrapper
#
#     return my_decorator
#
#
# @args_decorator("Игорь", "Нефедов")
# def print_full_name(first, last):
#     print('Меня зовут: ', first, last)
#
#
# print_full_name("Ирина", "Лаврова")

# ================================

# def args_decorator(decorator_text):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     return my_decorator
#
# @args_decorator(decorator_text='Hello, ')
# def hello_world(text):
#     print(text)
#
#
# hello_world('World')

# ====================================

# def one(num_dec):
#     def two(func):
#         def res(args):
#             return str(func(args) * num_dec)
#
#         return res
#
#     return two
#
#
# @one(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# =============================================  ПРОВЕРКА НА СООТВЕТСТВИЕ ( указанное )

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwards):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:  # если тип(type) не соответствует, то выводим ошибку
#                     raise TypeError("Типы данных не соответветствуют")  # raise вызывает исключения
#             for k in kwargs:
#                 if type(f_kwards[k]) != kwargs[k]:  # если тип(type) не соответствует, то выводим ошибку
#                     raise TypeError("Типы данных не соответветствуют")  # raise вызывает исключения
#             return fn(*f_args, **f_kwards)
#
#         return wrap
#
#     return wrapper
#
#
#
# @ typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, 6))
# print(typed_fn2("Hello, ", "world", "!"))
# print(typed_fn3("Hello, ", "world! ", z=5))

# =================================================================


# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end="")
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text="Hello, ")
# def hello_world2(text):
#     print(text)
#
#
# hello_world('HI!')
# hello_world2('world!')

# ==============================================================

# ============================================================================09.11.21

# print(int('100', 2))  # второй параметр указывает систему исчесления, в которую пересчитывает первый параметр
# print(int('100', 8))
# print(int('100', 16))

# print(bin(19))  # двоичная система
# print(oct(19))  # восьмиричная
# print(hex(19))  # шестнадцатеричная
#
# print(0b1010)  # обратно в десятичные из двоичных
# print(0o12)  # обратно в десятичные из восьмиричных
# print(0xFF)  # обратно в десятичные из шестнадцатеричной


# q = "Pyt"
# w = 'hon'
# e = q + w
# print(e)
# print(e * -3)  # на отрицательное число будет пустая строка
#
#
# print(e in 'I am learn Python')  # True
# print(e in 'I am learn Java')  # False
#
# s = "Hello"
# print(s[1])
# print(s[1:6])
# print(s[2:len(s)-2])
# print(s[:])
# print(s[2:2])
# print(s[-5:-2])
# print(s[4:0:-1])  # H не включится, т.к. в условии среза 0 не включается ( end )
# print(s[::-1])  # разворачиваем строку полностью

# ========================== ====================================================== МЕТОД SLICE

# s = "abcdefgh"
# print(s[slice(2, 5)])
# print(s[slice(5, None)])  # срез от 5 до конца
# print(s[slice(5, None, -1)])  # срез от 5 до конца в реверсе
# print(s[slice(None, None)])  # каждый второй элемент в пустом срезе

# ========================================================================

# s = "python"
# print(id(s))
# # s[3] = 't'  # так записать нельзя
# s = s[:3] + 't' + s[4:]
# print(id(s))
# print(s)

# ===================================================
# ЗАДАЧА ЗАМЕНИТЬ БУКВЫ В СТРОКЕ


# def change_char(s, c_old, c_new):
#     s2 = ''
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i += 1
#     return s2
#
#
# str1 = 'Я изучаю Nuthon. мне нравится Nuthon. Nuthon очень интересный язык программирования.'
# str2 = change_char(str1, "N", "P")
# print(str1)
# print(str2)

# ======================================================
# Второй вариант через срез

# str1 = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования"
# def renam(stroka, start, chenge):
#     a = ""
#     for i in range(len(stroka)):
#         if stroka[i] == start:
#             a = a[:i] + chenge
#         else:
#             a = a[:i] + stroka[i]
#     return a
#
#
# print(str1)
# print(renam(str1,"N","P"))

# ========================================================
# Третий вариант
# print(str1.replace('Nuthon', 'Python'))
# ================================================================= ПРЕФИКСЫ

# print(u"Hello")
# print('I\'m Learning\nPython')
# print('C:\\file.txt')
# print(r'C:\file.txt')  # префикс r позволяет не экранировать текст
# print(r'C:\file.txt\\'[:-1])  # срез убирает символ ( слэш ) в конце
# print(r'C:\file.txt' + '\\')  # второй способ слэша в конце
# print('C:\\file.txt\\')  # третий способ
# print(b'a1b2c3')
# print(b'a1b2c3'[1])  # 1 переводит код в десятичное значение
# print(b'\xff\xfe\xfd'[1])  # свыше 128 бит

# ================================================================= F строки

# name = 'Дмитрий'
# age = 25
# print(f'Меня зовут {name}, мне {age} лет.')

# import math
# print(f'Значение числа pi: {math.pi:.2f}')  # :.2f (float) сокращаем значение до 2 после точки
#
# x = 10
# y = 5
# print(f'{x} x {y} / 2 = {x * y / 2}')

# planets = ['Меркурий', 'Венера', 'Земля', 'Марс']
# print(f'Мы живем на планете {planets[2]}')
#
# planet = {"name": 'Земля', "radius": 6378000}
# print(f'Планета {planet["name"]}. Радиус {planet["radius"] / 1000}км.')
#
# print(f'13 / 3 = {round(13 / 3)}')


# name = 'Друг'
# prof = 'программист'
# lang = 'Python'
#
# message = (
#     f'Привет {name}.'
#     f'ты {prof}.'
#     f'На языке {lang}.'
# )
#
# print(message)

# a = 74
# print(f'{{{a}}}')

# =============================================================== Fr

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print("home\\" + dir_name + '\\' + file_name)  # обычный вариант

# =============================================================


# s = """Hello"""
# print(s)

# s = 5
# print('мне ' + str(s) + " лет")

# s = 'Hello'
# s1 = 'hel'
# print(max(s, s1))  # отработает s1, т.к. в кодировке ASCII находиться выше


# print(ord('a'))  # ord  возвращает код символа
# print(ord('#'))
# print(ord('к'))

# проверка кода символа
# while True:
#     n = input('->')
#     if n != "-1":
#         print(ord(n))
#     else:
#         break
# ==============================

# ============ ЗАДАЧА

# mystr = "Test string for me"
# arr = [ord(x) for x in mystr]
# print("ASCII коды: ", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое", arr)
# arr += [x for x in [ord(x) for x in (input('->'))[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:  # если последний элемент есть в списке не включая последний элемент. то
#     print("Количество последних элементов: ", arr.count(arr[-1])-1)
# arr.sort(reverse=True)
# print(arr)

# =============================================================================

# получить из кода символа = символ

# print(chr(97))  # a
# print(chr(35))  # '#'

# =============================
# вывести все символы в кодировке между a и b
# a = 122
# b = 97

# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

# Вариант в одну строку
# print(*(chr(x) for x in range(a, b + 1)) if a < b else (chr(x) for x in range(b, a + 1)))

# Второй вариант через срез

# DZ-10.11.21
# DZ-1
# Замена символа на другой символ в строке на парных позициях
# def change_char(s, c_old, c_new):
#     s2 = ''
#     i = 0
#     while i < len(s):
#         if (s[i] == c_old) and (i % 2 == 0):
#             s2 = s2 + c_new
#         else:
#             s2 = s2 + s[i]
#         i += 1
#     return s2
#
#
# str1 = 'Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования.'
# str2 = change_char(str1, "N", "P")
# print(str1)
# print(str2)

# DZ-2
# s = '0123456789'
# s2 = s[:4] + s[5:]
# print(s2)

# DZ-2 не пойму задание, вариант №2

# s = '0123456789'
# n = input("Число: ")
#
# for i in s:
#     if i == n:
#         s2 = s[slice(None, int(n))] + s[slice(int(n)+1, None)]
#         print(s2)

# DZ-3

# s = '012345363738494'
# print(*(i for i in s if i != '3'))

# DZ-4


# def func(num):
#     d = []
#     while num > 0:
#         if num % 2 == 0:
#             d.append(0)
#             num = num // 2
#         elif num % 2 == 1:
#             d.append(1)
#             num = num // 2
#
#     for i in d[::-1]:
#         print(i, end="")
#     print()
#
#
#
# while True:
#     s = int(input('Введите число (Выход = 0): '))
#     func(s)
#     if s == 0:
#         break


# ======================================================================= 11.11.21

# список
# кортеж
# словарь
# множество

# s = 'hello, WORLD! I am learning Python. 123!@'
# print(s.capitalize())  # возвращает копию строки с 1 символом в верхнем регистре, остальные в нижнем.
# print(s.lower())  # преобразует все символы в нижний регистр
# print(s.upper())  # преобразует все символы в верхний регистр
# print(s.swapcase())  # меняет регистр символов на противоположный
# print(s.title())  # преобразует первые буквы всех слов в заглавные
#
# print(s.count('he'))  # возвращает количество вхождений подстроки в строку
# print(s.count('l', 3))  # второй параметр с откуда искать
# print(s.lower().count('i'))  #
# print(len(s))
# print(s.count('l', 3, 15))  # 1 - символ, 2-старт, 3 до какого
# print(s.find('l'))  # возвращает индекс первго вхождения
# print(s.find('Python', 3))  # вернет индекс вхождения данной строки
# rfind начинает поиск справа налево ==========================================================
# print(s.rfind('l', 3, 16))
# print(s.rindex('in'))

# ======================================================

# s = input('Введите два слова через пробел: ')
# s2 = s[s.find(' ') + 1:]
# s3 = s[:s.find(" ")]
# print(s2)
# print(s3)
# print(s2 + " " + s3)

# ЗАДАЧА вытащить числа из строки
# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if i == '1' or i == '2' or i == '5' or i == '9' or i == '7':
#         digits.append(int(i))
# print(digits)

# тоже самое через FIND
# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     if '1234567890'.find(i) != -1:
#         digits.append(int(i))
# print(digits)

# От Артема
# num = "ab12c59p7dq"
# digits = []
# for i in num:
#     if 48 <= ord(i) <= 57:  # если элемент есть в списке ASCII
#         digits.append(int(i))
# print(digits)

# От АРТЕМА
# s = 'ab12c59p7dq'
# digits = []
# for i in s:
#     try:
#         digits.append(int(i))  # TRY проверяет на целые числа
#     except ValueError:
#         pass
# print('digits =', digits)

# =============================================================

# s = 'hello, WORLD! I am learning Python. 123!@'
# print(s.index('Python'))  # возвращает первый индекс, который соответствует элементу, начиная с начала строки,
# # и возвращает ValueError если совпадение не найдено
# print(s.index('cPython'))


# ЗАДАЧА ==================================================================

# s = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# first = s.index('(')
# second = s.index(')')
# print(s[first + 1:second])

# вариант 2
# s = "Дана ст(рока символов ,среди которых есть одна открыв)ающаяся"
# print(s[s.find('(') + 1:s.find(')')])

# ЗАДАЧА
# если символ f встречается в строке 1 раз, то вывести его вхождение, если 2 и более 2 раз,
# то вывести первое и послднее вхождение, если нет то ничего не выводить

# s = 'aaaaaaaaaaafaaaaaaaaaaafaaaaaaa'
# if s.count('f') == 1:
#     print(s.find('f'))
# elif s.count('f') >= 2:
#     print(s.find('f'), s.rfind('f'))

# вариант через фор
# h = 'Send heri yulio hertino ftfdf'
# jjj = []
# j = -1
# for i in h:
#     j += 1
#     if i == 'f':
#         jjj.append(j)
# print(jjj)

# ================================================

# s = 'hello, WORLD! I am learning Python. 123!@'
# print(s.endswith('123!@'))  # определяет, заканчивается ли строка заданной подстрокой
# print(s.endswith('on.', 3, 35))  # 3-диапазон, 35 с какого индекса проверять.
# print(s.endswith('WORLD!', 0, 13))  # 0-диапазон, 13 с какого индекса проверять.

# ================================================

# print('abc123'.isalnum())  # isalnum определяет, состоит ли строка из букв или цифр ( другие символы будет FALSE )
# print('AAAAdddd'.isalnum())
# print('45645'.isdigit())  # определяет состоит ли строка из ЦИФР
# print('asd1'.isidentifier())  # является ли строка допустимым индитификатором в ПИТОН
#
# print('abc'.islower())  # проверяет являются ли буквы строчными
# print('\n   \t  '.isspace())  # проверяет, состоит ли строка из пробельных символов ( включая \n \t )
#
# print('Hello'.istitle())  # определяет начинается ли строка с заглавной буквы
# print('Hello'.istitle())  # определяет начинается ли строка с заглавной буквы
# print('HELLO'.isupper())  # определяет состоит ли строка из всех заглавных букв
#
# print('py'.center(10, '='))  # Выравнивает строку по центру (2-символ вместо пробела)
#
# print('http://www.python.org/'.lstrip('/:pths'))  # обрезает заданные символы с левой стороны
# # останавливается при первом не указанном символе
# # если символы не указаны, то удаляет все пробелы с левой стороны
# print('http://www.python.org/'.rstrip('org/'))  # тоже самое справа
# print('http://www.python.org/'.rstrip('org/').lstrip('/:pths'))  # с двух сторон совмещенное
# print('http://www.python.org/'.strip())  # с двух сторон

# =======================================================================================

# s = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования"
# print(s.replace('Nuthon', 'Python'))  # заменяет вхождение в подстроке в строке

# ==================================================================================

# ЗАДАЧА
# s = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последнего вхождения.'
# print(s[:s.find('о') + 1] + s[s.find('о') + 1:s.rfind('о')].replace('о','О') + s[s.rfind('о'):])
#
#
# # ==var2
# stroka = "Замените в этой строке все появления буквы 'о' на букву 'О', кроме первого и последнего вхождения"
# first = stroka.find("о")
# last = stroka.rfind("о")
# stroka = stroka[:first + 1] + stroka[first + 1:last].replace("о", "О") + stroka[last:]
# print(stroka)

# ==============================================

# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))  # обьеденяет список в строку с разделителем
#
# print("..".join(['1', '2']))
#
# print(":".join("Hello"))
#
# print("Строка разделенная пробелами".split())  # разделяет строку по пробелам ( или символам ) в список
# print('www.python.org.tttt.hhhh'.split('.', 2))  # второй параметр количсетво вхождений
# print('www.python.org.tttt.hhhh'.rsplit('.', 2))  # rsplit, тоже самое с правой стороны


# a = input("-> ").split()  # записывает сразу в список разделяя по пробелу
# print(a)

# ЗАДАЧА
# Введите ФИО - Никонов Валерий Анатолий
# Никонов В. А.

# stroka = input("Введите ФИО - ").split()
#
#
# def ren(inp):
#     return inp[0] + " " + inp[1][0] + ". " + inp[2][0]+"."
#
#
# print(ren(stroka))

# ====================================


# DZ-15.11.21
# DZ-1

# s = 'I am learning Python. hello, WORLD!'
# print(s[:s.find('h')] + s[s.rfind('h')+1:])

# DZ-2

# s = 'I am learning Python. hello, WORLD!'
# f = s[s.find('h')+1:s.rfind('h')]
# print(s[:s.find('h')+1] + f[::-1] + s[s.rfind('h'):])

# DZ-3

# a = input('Введите строку: ')
# b = input('Введите что хотите заменить: ')
# c = input('Введите на что заменить: ')
# f = a.replace(b, c)
# print(f)

# DZ-4
# s = 'Ежевику для ежат\nПринесли два ежа.\nЕжевику ели-ели\nЕжата возле ели съели.'
# f = s.split()
# g = []
# for i in f:
#     if i[0] == 'Е' or i[0] == 'е':
#         g.append(i)
#
# print(s, '\nКоличество слов: ', len(g))

# ===================================================================== 16.11.21 ====== RE (регулярное выражение )

# import re

# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счёта.'
# reg = 'я'
# print(s.find(reg))  # find() - в строке будет искать шаблон и возвращать индекс первого вхождения подстроки в строке
# # если шаблон не найден, то будет возвращать '-1'
# print(reg in s)  # проверка есть ли шаблон в строке
#
#
# print(re.findall(reg, s))  # метод возвращает список содержащие ВСЕ совпадения с регулярного выражения, регистрозависимый
# print(re.findall('12', s))  # если не находит совпадения, возвращает пустой список
#
# print(re.search(reg, s))   # месторасположение первого совпадения объекта, индексы от начала и какием заканчивается
# print(re.search(reg, s).span())  # получаем кортеж с индексами
# print(re.search(reg, s).start())  # выводит первое значение
# print(re.search(reg, s).end())  # выводит второе значение
# print(re.search(reg, s).group())  # получаем само значение
#
#
# print(re.match(reg, s))  # поиск по заданному шаблону  в НАЧАЛЕ строки ( не используется )
# reg = r'\.'  # точку нужно экранировать, слежебный символ заменит все символы
# print(re.split(reg, s, 1))  # возвращает список, в котором строка разбита по шаблону, 3 параметр = количество разделений
# # количество всегда будет +1, все что не разделено будет в нем
#
# print(re.sub(reg, '!', s))  # находит регулярное выражение и заменяет его символом заданным 2 параметром


# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счёта. 1986'
# reg = '[2021]'  # если в виде списка вернет совпадения всех символов в списке ( включая повторяющиеся )
# reg = '[0-9]'  # ищет все цифры в заданном диапазоне
# reg = '[а-я]'  # все буквы
# reg = '[0-9][0-9][0-9][0-9]'  # будет искать 4 цифры подряд
# reg = '[12][0-9][0-9][0-9]'  # первую цифру ищет или 1 или 2 [12]
#
# reg = '[А-Я а-яё]'  # ё идет по символам после я, регистрозависимый А-а
#
# s = 'Ели[-ели].'
# reg = '[А-Яа-яё.\[\]-]'  # скобки и точку нужно экранировать, символ дефиса указываем последним
# reg = '[А-Яа-яё.\[\]-].'  # точка снаружи это будет абсолютно любой символ, будет выводить попарно
#
# print(re.findall(reg, s))

# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счёта. 1986'
# reg = r'[^0-9]'  # [^abc] в квадратных скобках - Находит все символы кроме заданных ( отрицание )
# print(re.findall(reg, s))


# ЗАДАНИЕ ======================

# s = 'Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09.'
#
# reg = '[0-2][0-9][\:][0-5][0-9]'
# print(re.findall(reg, s))

# =====================================

# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счёта. 1986'
# reg = r'\d'  # \d - это одна любая цифра [0-9]
# reg = r'\w'  # \w - это одна любая буква, цифра, символ подчеркивания ( без пробелов, точек ) [0-9]
# reg = r'\s'  # \s - один пробельный символ, включая табуляцию и перенос (\n, \t )
# reg = r'\D'  # \D - все кроме цифр
# reg = r'\W'  # \W - все кроме цифр, букв, символов подчеркивания (_)
# reg = r'\S'  # \S - все кроме кроме пробелов
# reg = r'\A'  # \A - ищет набор символов в начале строки
# reg = r'1986\Z'  # \Z - ищет набор символов в конце строки == устанавливаем в конце ( символ $ тоже самое )
# reg = r'ния\b'  # \b - ищет набор символов в начале или в конце ПОДСТРОКИ
# reg = r'ния\B'  # \B - ищет набор символов НЕ в начале и НЕ в конце ПОДСТРОКИ
# print(re.findall(reg, s))

# ============

# s = 'Я ищу совпадения в 2021 году. И я их найду в 2 счёта. 25_65'
# reg = r'20*'
# print(re.findall(reg, s))

# количество повторений
# + от 1 до бесконечности
# * от 0 до бесконечности = символа может не быть, а может быть до бесконечности
# ? от 0 до 1

# =============================================================================================== ? НУЖНО

# d = "Цифры: 7, +17, -42, 0013, 0.3"
# print(re.findall(r'[+-]?\d+', d))  # в скобках [] указываем какие символы должны присутствовать, ? = не исключает остальные символы

# ====================================================================================================================
#
# s = "05-03-1987 # Дата рождения"
# print("Дата рождения: ", re.sub("#.*", "", s))  # .* в данном случае выбирает любые символы до бесконечности
# print("Дата рождения: ", re.sub("-", ".", s))
# print("Дата рождения", re.sub("-", ":", re.sub("#.*", "", s)))

# ========================================

# s = "12 сентября 2021 года"
# reg = r"\d{2,4}"  # максимальное значение {}
# print(re.findall(reg, s))

# =======================

# s = "МИ Д - Министерство иностранных дел, ГЭ С - гидроэлектростанция, ФСБ - Федеральная служба безопасности"
# # reg = r"[А-ЯЁ]{2,}"  # ищем аббривиатуру от 2 до бесконечности символов
# reg = r"[А-ЯЁ]{2,}\s*[А-ЯЁ]"  # включили что в аббривиатуре могут быть пробелы а могут не быть.
# print(re.findall(reg, s))

# ================================================================================= ПРОВЕРКА НОМЕРА +7

# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# reg = r"\+?7[0-9]{10,}"
# print(re.findall(reg, s))

# ==============================================================================ПЕРЕСМОТРЕТЬ

# s = "Я ищу совпадения в 2021 году. И я их найду в 20000 счёта"
# reg = r"^\w+\s\w+"
# print(re.findall(reg, s))

# s = "45 78 456 78"
# reg = r'^\d+\s+\d+'
# print(re.findall(reg, s))

# s = "+7 900 sdsdsdd"
# reg = r'^\+\d+\s+\w+'
# print(re.findall(reg, s))

# ============================================================================================ ФЛАГИ


# s = "Я ищу совпадения в 2021 году. И я их найду в 20000 счёта"
# reg = r'я'
# print(re.findall(reg, s, flags=re.I))  # re.I или re.IGNORECASE  = игнорирует регистр, атрибут flags=
#
# print(re.findall(r'\d+', '12 + ۴'))
# print(re.findall(r'\d+', '12 + п', flags=re.ASCII))  # проверяет на кодировку ASCII

# ================================

# re.DEBUG
# re.LOCALE
# re.DOTALL

# text = r'''
# Торт
# с вишней1
# вишней2
# '''
# print(re.findall(r'Торт.с', text))
# print(re.findall(r'Торт.с', text, flags=re.DOTALL))
# print(re.findall(r'виш\w+', text, flags=re.MULTILINE))


# ====================================================== ПРОВЕРЯЕМ @mail
# re.VERBOSE

# print(re.findall(r'''
#                     [\w\.-]+
#                     @ # разбиваем по @
#                     [\w\.-]+
#                     ''', "test@mail.ru", re.VERBOSE))  # позволяет форматировать, оставлять комментарии.


# DZ-18.11.21
# DZ-1
# Найти адрес электронной почты
# s = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru login.3-67@i.ru, 1ogin@ru.name.ru"
# reg = r'[\w\.-]+@+[\w\.-]+'
# print(re.findall(reg, s))


# ====================================================================================== 18.11.2021


# s = r'author=Пушкин А.С.; title = Евгений Онегин; price     =200; year= 1831'
# reg = r'\w+\s*=[^;]+'
# print(re.findall(reg, s))

# ==================================================================================

# def validate_name(name):
#     return re.findall(r'^[a-z0-9_-]{3,16}$', name, re.IGNORECASE)
# # ^ - ограничивает допуск при несовпадении символов в начале строке
# # $ - ограничивает допуск при несовпадении символов в конце строке
#
# print(validate_name('Python_master000%'))

# ===================================================================================


# ============ ЖАДНЫЕ (greedy) - захватывают максивмально возможное число символов
# ===   ?   ==== ЛЕНИВЫЕ (lazy) - захватывают минимальное возможное число символов
# *?, +?, ??  - ленивые используются в связке
# {n,m}?, {,m}?, {n,}?


# text = '<body>Пример жадного соответствия регулярных выражений</body>'  # ЖАДНОЕ РЕГУЛЯРНОЕ выражение
# print(re.findall('<.*>', text))
# print(re.findall('<.*?>', text))  # ленивое выражение
# print(re.search('<.*?>', text).group())  # вывели первое совпадение тега

# ========================================

# s = "<p>Изображение <img scr='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*?>'
# reg = r'<img[^>]*>'
# print(re.findall(reg, s))

# =======================================

# text = "Python[16] (питон[17] или пайтон[22]"
# reg = r'\[.*?]'
# print(re.findall(reg, text))

# ======================================

# s = "Петр, Ольга и Виталий отлично учатся!"
# reg = "Петр|Ольга|Виталий"  # | - ИЛИ
# print(re.findall(reg, s))


# s = "Word2016, PS6, AI5"
# reg = r"([a-z]+)(\d*)"  # получаем группировки данных в кортеже
# print(re.findall(reg, s, re.I))
# print(re.search(reg, s, re.I).group())


# s = '5 + 7*2 -4'
# reg = r'\s*[+*-]\s*'  # отработает как разделители
# reg = r'\s*([+*-])\s*'  # операторы выгрузит в список при ()
# print(re.split(reg, s))

# ==================================================
# import re
# s = input('Введите дату в формате dd-mm-YYYY: ')
# reg = r'([0-2][0-9]|[3][01])-([0][1-9]|[1][0-2])-([1][9][0-9][0-9]|[2][0][0-9][0-9])'
# print(re.findall(reg, s))

# ==================================================

# s = '127.0.0.1'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'  # ?: шаблон для повторений
# print(re.findall(reg, s))

# =====================================================

# s ="Базовый JS прост. Продвинутый Python сложен. Базовый Python прост."
# reg = r"[а-яё]+(?= Python)"
# reg = r"Базовый(?! Python)"
# reg = r"(?<=Базовый )\w{2,6}"
# reg = r"(?<!Продвинутый )Python"
# print(re.findall(reg, s, re.I))


# ===================================ЛЮДОВИКИ

# s = "КарлIV, КарлIX, КарлV, КарлVI, КарлVII, КарлVIII, ЛюдовикIX, ЛюдовикVI, ЛюдовикVII, ЛюдовикVIII, ЛюдовикX, ..., " \
#     "ЛюдовикXVIII, ФилиппI, ФилиппII, ФилиппIII, ФилиппIV, ФилиппV, ФилиппVI"

# reg = r"Людовик(?=VI)\w+"
# reg = r"\w+(?<=Людовик)VI"
# reg = r"\w+(?<!Людовик)VI"
# print(re.findall(reg, s, re.I))

# ===========================================

# ==================================================================== ЗАДАНИЕ
# найти цифры рядом с которой нет цифр
# s = "1X, Text ABC 123 A1B2C3"
# reg = r"(?<!\d)\d(?!\d)"
# print(re.findall(reg, s, re.I))
#
# # Найти текст между СТАРТ И ЕНД
# s2 = "text from #START# till #END#"
# reg2 = r"(?<=#START#).*(?=#END#)"
# print(re.findall(reg2, s2, re.I))
#
# # вывести цифру с одним подчеркиванием
# s3 = "12_34__56"
# reg3 = r"\d+(?=_(?!_))"
# print(re.findall(reg3, s3, re.I))

# =======================================================================

# s = "Я ищу совпадения в 2021 году. И я их найду в 20000 счёта"
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s, re.I).group())
# m = re.search(reg, s)
# print("Строка: ", m[0])  # по 0 индексу получаем полный запрос
# print("Цифра: ", m[1])  # 1 индекс будет что искали в первых скобках ( сейчас цифры )
# print("Буквы: ", m[2])  # 2 индекс будет что искали во вторых скобках ( сейчас НЕ цифры )

# ============================================================================

# s = "Самолет прилетает 10/23/2021. Будем вас рады видеть после 10/24/2021"
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r'\2.\1.\3', s))  # заменяем через индексы ( скобки )

# ==============================================================================

# ===============================================================================
# s = "google.com and google.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r'http://\1', s))

# ================================================================================ ПРОВЕРКА РИМСКИХ ЧИСЕЛ


# def is_roman_namber(num):
#     pattern = r'^M{0,3}(CD|CM|D?C{0,3})?(XC|XL|L?X{0,3})?(IX|IV|V?I{0,3})?$'
#     if re.search(pattern, num):
#         return True
#     return False
#
#
#
# print(is_roman_namber('MMDCCLXXIII'))
# print(is_roman_namber('CCCMMVIIVV'))
# print(is_roman_namber('IV'))

# =======================================================================================

# DZ-23.11.21
# DZ-1
# import re
#
# s = input('Введите пароль: ')
# reg = r'(^[a-z@\d\-]{6,18}$)'
# print(re.findall(reg, s, re.I))

# DZ-2

# s = 'В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021 были зафиксированы максимумы ежемесячных осадков.'
# reg = r'\d+/\d+/\d+'
# print(re.findall(reg, s))

# DZ-3
# Валидация номеров
# s = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7(499) 456-45-78'
# reg = r'(?:\+?7|8)\s?[0-9.*]{2,10}.*'
# print(re.findall(reg, s))


# ============================================================================= 23.11.21 РЕКУРСИЯ

# def elevator(n):
#     if n == 0:
#         print('Вы в подвале')
#         return
#     print('->', n)
#     elevator(n - 1)  # функция вызывает себя
#     print(n, end=' ')
#
#
#
# n1 = int(input('На каком вы этаже: '))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res = res + i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# ========
# def sum_list(lst):
#     if len(lst) == 1:
#         # print(lst, "=> lst[0]: ", lst[0])
#         return lst[0]
#     else:
#         print(lst, "=> lst[0]: ", lst[0])
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))

# ====================================== Калькулятор систем исчесления

# def to_str(n, base):
#     convert = '0123456789'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
#
# print(to_str(769, 10))

# ==================================

# def to_str(n, base):
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(255, 16))

# ============================================================================ РЕКУРСИЯ и вложеные списки


# names = ['Adam', ['Bob', ['chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
#
#
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#             print(count)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# print(type(names) == list)
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
#
#
# print(len(names))

# ======================================================================================= БЕЗ РЕКУРСИИ

# names = ['Adam', ['Bob', ['chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# #
# #
# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             for i in item:
#                 if isinstance(i, list):
#                     for k in i:
#                         count += 1
#                 else:
#                     count += 1
#
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# =========================================================================== "Выпрямление списка"


# def union(s):
#     if not s:  # s == []
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:])
#
#
# names = ['Adam', ['Bob', ['chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(union(names))

# ===========================================================================

# def remove(text):
#     if not text:
#         return ""
#     if text[0] == '\t' or text[0] == ' ':
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("    Hello \tWorld Hi   "))

# ========================================================================   ЛИНЕЙНАЯ СОРТИРОВКА
# ЗАДАЧА, узнаем есть ли элемент в списке
# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#
#         else:
#             if s[pos] > item:  # работает только с отсортированным списком !!!!!!!!!!!!!!!!
#                 stop = True
#             else:
#                 pos = pos + 1
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))

# =====================================================================
# вариант в форе
# def seq_search(s, item):
#     for i in s:
#         if i == item:
#             return True
#     else:
#         return False

# lst = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(seq_search(lst, 3))
# print(seq_search(lst, 13))

# =================================================================   БИНАРНЫЙ СОРТИРОВКА

# def binary_search(s, item):
#     first = 0
#     last = len(s) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2  # получаем середину списка
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:  # если позиция до середины до уменьшаем длину -1
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# lst = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# # print(binary_search(lst, 3))
# print(binary_search(lst, 8))

# ====================================================

# # def binary_search(s):  # Бинарная сортировка с лямбда
# #     if len(s) <= 1:
# #         return s
# #     midpoint = (len(s)-1) // 2
# #     elem = s[midpoint]
# #     left = list(filter(lambda x: x < n, a))
# #     right = list(filter(lambda x: x > n, a))
# #center = [i for i in s if i == elem]
# #     return binary_search(left) + center + binary_search(right)
# #
# # r = [97, 63, 14, 42, 39, 6, 15, 71, 34, 10]
# # print(binary_search(r))

# =====================================================================================

# DZ-25.11.21
# DZ-1 Используйте алгоритм бинарного поиска.


# def binary_search(s, item):
#     s.sort()
#     first = 0
#     last = len(s) - 1
#     found = False
#     text = f'Число {bi} отстутствует в списке'
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#             text = f"Число {bi} присутствует в списке "
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return text
#
#
# bi = int(input("Введите число 15: "))
# s = [97, 63, 14, 42, 39, 6, 15, 71, 34, 10]
# print(binary_search(s, bi))

# DZ-2


# def count_items(lst):
#     if lst == []:
#         return 0
#     else:
#         count = count_items(lst[1:])
#         print(lst)
#         if lst[0] < 0:
#             count = count + 1
#
#         return count
#
#
# names = [-2, 3, 8, -11, -4, 6]
# print(count_items(names))

# ===============================

# ===============================================================ПУЗЫРЬКОВАЯ СОРТИРОВКА
import random as r

#
#
# def bubble(array):
#     for i in range(len(array)-1):
#         print(i)
#         for j in range(len(array)-1-1):  # -i будет сортировка в обратную сторону
#             print(j, '*')
#             if array[j] > array[j+1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
#
#
# a = [r.randint(1,99) for i in range(10)]
# print(a)
# bubble(a)
# print(a)

# =================================================================================

# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#     l = merge_sort(a[:n // 2])
#     r = merge_sort(a[n // 2:n])
#     i = j = 0
#     res = []
#
#     while i < len(l) or j < len(r):
#         if not i < len(l):
#             res.append(r[j])
#             j += 1
#         elif not j < len(r):
#             res.append(l[i])
#             i += 1
#         elif l[i] < r[j]:
#             res.append(l[i])
#             i += 1
#         else:
#             res.append(r[j])
#             j += 1
#     return res
#
#
# array = [9, 5, 3, 8, 6]
# print(array)
# array = merge_sort(array)
# print(array)

# ===================================================== СОРТИРОВКА ШЕЛЛА

# ==========================================

# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#
#         gap //= 2
#         print(gap, "Список: ", s)
#     return s
#
#
# a = [10, 44, 26, 14, 67, 21, 9, 87]
# print(a)
# shell_sort(a)
# print(a)


# ===========================
# =======================================
# =====================================================
# =============================================================== РАБОТА С ФАЙЛАМИ
# метод open
# f = open(r"C:\Users\Пользователь\Dropbox\Андрей работа 2020\УЧЕБА\Академия ШАГ\ONLINE\PYTHON\ONLine\text.txt", "r")
# print(*f)  # содержимое файла
# print(f)
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# print(f.read(3))  # получить содержимое файла, можно указать количество символов
# print(f.read())  # следующий запрос будет уже с 4 символа
# f.close()  # закрываем файл

# ===================================

# f = open("text.txt", "r")
# try:
#     print(f.read())
# finally:
#     f.close()

# ===================================

# f = open("test.txt", 'r')
# print(f.read())
# print(f.readline())  # считывание построчно
# print(f.readline(8))  # считывание построчно с количеством символов
# print(f.readline())  # продолжение строки
# print(f.readline())  # 3 строка

# print(f.readlines())  # список всех строк

# # ============
# i = 0
# for line in f:
#     i += 1
# print(i)
# f.close()
#
# # ================
#
# t = f.readlines()
# print(t)
# print("в документе", len(t), "строк")
#
# # =====================


# f = open('xyz.txt', 'w')  # W создаем/записываем файлы
# f.write('Hello \nWorld')
# f.write('NewText')
# f.close()

# f = open('xyz.txt', 'a')  # A ДОзаписываем файлы
# print(f.write('New text.'))
# f.close()

# ================================

# f = open('xyz.txt', 'a')
# lines = ['This is list 1', 'This is line 2']  # дозаписываем массив элементов
# f.writelines(lines)
# f.close()

# ======================= Генерация спика  в файл, записывать можно только строки ( преобразовать в str )

# f = open('xyz.txt', 'a')
# lst = [str(i) + str(i - 1) for i in range(1, 20)]
# print(lst)
# for index in lst:
#     f.write(index + "\t")
# f.close()

# ============================================
# ЗАДАЧА ЗАМЕНЫ СТРОКИ ==== VAR1

# f = codecs.open('text2.txt', 'r', encoding='utf-8')  # чей то файл, ошибка адреса
# lst = f.readlines()
# lst[1] = 'Hello world!\n'
# print(lst)
# f.close()
# f = codecs.open('text2.txt', 'w', encoding='utf-8')
# f.writelines(lst)
# f.close()

# ЗАДАЧА ЗАМЕНЫ СТРОКИ ==== VAR2

# my_file = open("E:\\u4\\pythonProject\\t11.txt", "r")  # чей то файл, ошибка адреса
# read_file = my_file.readlines()
# print(read_file)
# for i in range(len(read_file)):
#     if read_file[i] == "изменить строку в списке;\n":
#         read_file[i] = "Hello World\n"
# print(read_file)
# my_file.close()
# my_file = open("E:\\u4\\pythonProject\\t11.txt", "w")
# my_file.writelines(read_file)
# my_file.close()

# DZ 29.11.21
# DZ-1

# f = open('dz.txt', 'r')
# gen = f.readlines()
# pos = 1
# gen.pop(pos)
# f.close()
#
# f1 = open('dz.txt', 'w')
# f1.writelines(gen)
# f1.close()
# f2 = open('dz.txt', 'r')
# print(*f2)


# DZ-2
# f = open('dz.txt', 'r')
# gen = f.readlines()
# pos1 = 1
# pos2 = 2
# print(gen)
# for i in range(len(gen)):
#     rut = gen[pos1]
#     if i == pos1:
#         gen[pos1] = gen[pos2]
#         gen[pos2] = rut
# print(gen)
# f.close()
#
# f1 = open('dz2.txt', 'w')
# f1.writelines(gen)
# f1.close()
# f2 = open('dz.txt', 'r')
# print(*f2)


# DZ-3
# f = open('dz3.txt', 'r')
# gen = f.readlines()
# rev = gen[::-1]
# print(gen)
# print(rev)
# f.close()
# f = open('dz3.txt', 'w')
# f.writelines(rev)
# f.close()


# ======================================================================================== 30.11.21
#
# f = open('text.txt', 'r')
# print(f.read(3))
# print(f.tell())  # возвращает текущую позицию курсора в памяти ( в файле ) #3
# print(f.seek(1))  # перемещает курсор на необходимую позицию
# print(f.read())
#
# f.close()

# =====================

# f = open('text.txt', 'r+')
# print(f.write("I am learning Python"))
# print(f.seek(3))  # перемещаем курсор с какой позиции нужно записать или удалить данные
# print(f.write("-new string-"))  # перезаписываем кусок содержимого
# print(f.tell())
# f.close()

# ==================================== WITH менеджер контента ( не требует закрытия документа )

# with open('text.txt', 'w+') as f:  # ====================== записываем
#     print(f.write('0123456789\nfsefsefgsegesgsg'))
#
# with open('text.txt', 'r') as f:  # ================= считываем
#     for line in f:
#         print(line)

# ==============================    ЗАПИСЫВАЕМ В ДОКУМЕНТ СПИСОК ВЕЩЕСТВЕННЫХ ЧИСЕЛ

# file_name = "res_1.txt"
# lst = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))  # через map преобразовываем в строку
#     return " ".join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
#
# print("Done!")

# ================================================================
# ЗАДАЧА в обратном порядке из строки сделать список с вещественными числами

# with open(file_name, 'r') as f:
#     file_lst = f.read().split(' ')
#     print(file_lst)
#     print(len(file_lst))

# ==================================== ЗАДАЧА  var1

# def find_in_file(file_name):
#     max_l = 0
#     temp_res = []
#     res = []
#     c = 0
#     with open(file_name, "r") as new_file:
#         temp_file = new_file.read().split()
#         for i in temp_file:
#             temp_res.append(len(i))
#             if len(i) > max_l:
#                 max_l = len(i)
#         for j in temp_res:
#             if j == max_l:
#                 res.append(temp_file[c])
#             c += 1
#     return res
#
#
# print(find_in_file("poisk.txt"))

# ======================================== ЗАДАЧА  var2

# file_name = 'res_1.txt'
# lst = ['один', 'два', 'три', 'четыре', 'пять', 'шесть!']
#
# with open(file_name, 'w', encoding='utf-8') as f:
#     f.write(' '.join(lst))
#
#
# def open_file_and_find_max(file):
#     with open(file, 'r', encoding='utf-8') as f:
#         file_lst = f.read().split(' ')
#         max_len = max(len(i) for i in file_lst)
#         new_lst = []
#         for i in file_lst:
#             if len(i) == max_len:
#                 new_lst.append(i)
#         return new_lst
#
#
# print(open_file_and_find_max(file_name))

# ========================================= ЗАДАЧА  var3

# with open('res_1.txt', 'r') as f:
#     lst = f.read().split()  # разбиваем список строк
#     print(lst)
#     m = max(len(i) for i in lst)  # находим максимальный элемент
#     print([i for i in lst if len(i) == m])  # при условии если длина равна максимальному значению (м), выводим тоже

# ======================================================================================================
# ==============================================================================================
# ================================================================================

# Создать новый файл на основе существующего с изменениями

# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open("one.txt", 'w') as f:
#     f.write(text)
#
# read_file = "one.txt"
# write_file = "two.txt"
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:  # сразу два открытия документа
#     for line in fr:
#         line = line.replace("Строка", "Линия - ")
#         fw.write(line)
#
# with open(write_file, 'r') as fr:
#     for line in fr:
#         print(line, end="")

# ========================================= ============= МЕТОДЫ   os, os.path  ===========================================

import os

# print("Текущая директория", os.getcwd()) # Возвращает текущую директорию ( там где файл *.ру)
# print(os.listdir())  # возвращает все что находится в директории
# print(os.listdir(".."))  # возвращает список директорий и файлов на уровень выше или в директори по указанному пути
#
# os.mkdir("folder")  # создает директорию по указанному пути, папку с таким же именем создать нельзя
# os.makedirs("folder1/folder2/folder3")  # создает набор вложенных директорий ( создаст конечную директорию с промежуточными папками )

# os.remove("xyz.txt")  # удаляет файл
# os.rename("folder", "tetttttt")  # переименовывает файлы и директории ( папки ) ( если такого названия нет ), может и перемещать
# os.renames("text.txt", "text/new_text/tx.txt")  # переименовывает и перемещает файл, создавая промежуточные директории
#
# os.rmdir("text")  # удаляет пустую директорию. Если директория не существует будет ошибка


# os.walk = возвращает имена обьектов в дереве директорий, обходя это дерево сверху вниз ( topdown=True) или снизу вверх (topdown=False)
# for root, dirs, files in os.walk("folder1", topdown=True):
#     print("Root:", root)
#     print("Subdirs:", dirs)
#     print("Files:", files)

# ===============================================

# ====ЗАДАЧА===== удалить папку в которой нет файлов===========================================
# for root, dirs, files in os.walk("Work", topdown=False):
#     if len(dirs) == 0 and len(files) == 0:
#         print("Deriktoriya " + root + " udalena")
#         os.rmdir(root)
# ================

# ================ от учителя ===========================
# for root, dirs, files in os.walk("Folder", topdown=True):
#     if not os.listdir(root):
#         os.rmdir(root)
#         print(f"Директория {root} удалена.")

# ===============================================


# DZ-02.11.21
# DZ-1
# with open("a1.txt", 'r') as v, open("a2.txt", 'r') as v2, open("a3.txt", 'a+') as v3:
#     v3.write('\n')
#     v3.writelines(v)
#     v3.write('\n')
#     v3.writelines(v2)
#
# f = open('a3.txt', 'r', encoding='utf-8')
# print(f.read())

# DZ-2

# with open("DZ-2.txt", 'r', encoding='utf-8') as v:
#     reg = 0
#     for line in v:
#         kol = len(line.split(' '))
#         reg = line.count('')-1
#         print(f' {line}  {reg} симв. {kol} сл.')


# =========================================================== 02.12.21 ===== OS.PATH

# import os.path

# print(os.path.split(r'D:\rr\rrr\rrrr\r5\text_r5.txt'))
# # разбивает путь на кортеж который состоит из двух состовляющих (head, tail) голова и хвост =====
# print(os.path.dirname(r'D:\rr\rrr\rrrr\r5\text_r5.txt'))
# # возвращает имя директории ========
# print(os.path.basename(r'D:\rr\rrr\rrrr\r5\text_r5.txt'))
# # возвращает имя файла ====
#
# print(os.path.join(r'\rr\rrr', r'text_r5.txt'))
# # соединяет один или несколько компонентов пути с учетом особенности OS

# =======================================================ДЕРЕВО======================================ДЕРЕВО====

# dirs = [r'Work\F1', r'Work\F2\F21']  # создаем папки ( дерево ) х==============================================*****
# for dir1 in dirs:
#     os.makedirs(dir1)
#
# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for dir1, files in files.items():  # добавляем файлы в папки
#     for file in files:
#         file_path = os.path.join(dir1, file)  # создаем пути
#         open(file_path, 'w').close()

# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f'some sample text for {file} file')
#
# def print_tree(root, topdown):  # обход папок и файлов
#     print(f'Обход {root} {"сверху вниз" if topdown else "снизу вверх" }')
#     for root, dirs, files in os.walk(root, topdown=topdown):  # topdown=topdown == что попадет то и выведет (TRUE, False)
#         print(root)
#         print(dirs)
#         print(files)
#     print("-" * 50)
#
#
#
#
# print_tree('Work', topdown=False)
# print_tree('Work', topdown=True)

# print(os.path.exists(r'Work\F2\F21\f211.txt'))  # EXISTS  проверяет путь на существование ( true и false )
#
# print(os.path.getctime(r'Work\F2\F21\f211.txt'))  # Возвращает время создания файла
# print(os.path.getatime(r'Work\F2\F21\f211.txt'))  # Возвращает время последнего изменения файла
# print(os.path.getsize(r'Work\F2\F21\f211.txt'))  # размер файла в байтах


import time  # ============================================================= ДАННЫЕ ПО ФАЙЛАМ

# path = r"text.txt"
# size = os.path.getsize(path)
# kb = size / 1024
# atime = os.path.getatime(path)
# mtime = os.path.getmtime(path)
#
# print("Размер: ", kb, "KB")
# print("Дата последнего использования: ", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(atime)))
# print("Дата последнего редактирования: ", time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(mtime)))

# print(os.path.normcase('/User/admin/Document'))
# # нормализует регистр пути и слеши ========================
# print(os.path.relpath(r'Work\F2\F21\f211.txt'))
# # возвращает относительный путь
#
# print(os.path.isfile(r'Work\F2\F21\f211.txt'))
# # Возвращает TRUE, если концом пути является существующий файл
# print(os.path.isdir(r'Work\F2\F21'))
# # Возвращает TRUE, если концом пути является существующая директория


# ============================================== ИЩЕМ ВСЕ ФАЙЛЫ И ПАПКИ И ВЫВОДИМ НАЗВАНИЯ эелемента и размер файла
# var 1
# dir_name = 'Work'
#
# objs = os.listdir(dir_name)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     if os.path.isfile(p):
#         print(f"{obj} - file - {os.path.getsize(p)} bytes")
#     elif os.path.isdir(p):
#         print(f"{obj} - dir")

# var2
# def print_tree(root):
#     for rot, dirs, files in os.walk(root, topdown=True):
#         if rot == root:
#             for i in dirs:
#                 print(i, "-dir")
#             for j in files:
#                 print(j, "-file",os.path.getsize(rot+"\\"+j), "byte")
# print_tree("Work")

# ============================================================================*****  GIT HAB  *****=================

# git --help
# git init    (иницилизирует проект)
# git status  (отображает статус файлов)
# add -A (--a)  (все файлы)
# *.py  ( любой фАЙЛ С РАСШИРЕНИЕМ PY )
# . (все файлы в текущей директории )
# git commit -m "first commit"   ( создаем точку версионности документа)
# git config --global user.name "kas"
# git config --global user.email "andrei.rossvik@gmail.com"
# .gitignore   ( создание файла игнорирования )
# git branch  ( на какой ветке мы находимся )
# git branch test ( новая ветка )
# git branch -D test  ( удаление ветки )
# git checkout readme ( перейти на другую ветку, readme- название ветки )
# git checkout -b readme ( создание ветки и переход на нее )
# readme.md ( документ для описания проектов )
# git merge readme (объединяет ветки )


# DZ-07.12.21
# DZ-1
import os.path

# dir_name = r'test_dir/f1'
# file = '4.txt'
# search = os.listdir(dir_name)
# for i in search:
#     mp = os.path.join(dir_name, i)
# if file in search:
#     print(f"{file} ({dir_name}) - last access time  {os.path.getatime(mp)} sec")
# else:
#     print('Тут рыбы нет')


# DZ-2
# dir_name = 'files'
# file = []
# dirs = []
# search = os.listdir(dir_name)
# for i in search:
#     mp = os.path.join(dir_name, i)
#     if os.path.isfile(mp):
#         file.append(dir_name + '//' + i)
#     elif os.path.isdir(mp):
#         dirs.append(dir_name + '//' + i)
#
# out = file + dirs
# print(out)


# DZ-3
# os.makedirs('Work\empty_files')
# for root, dirs, files in os.walk('Work'):
#     for i in files:
#         mp = os.path.join(root, i)
#         if os.path.getsize(mp) > 0:
#             print(f'{root}\\{i} {os.path.getsize(mp)}')
#         else:
#             gen = os.path.basename(i)
#             os.replace(mp, f"Work/empty_files/{gen}")



# ============================================================================== 07.12.21 =========================
# Токен личного доступа (PAT)

# cd.. ( выйти в папку на уровень выше )
# cd name_folder ( выйти в папку по имени (folder пример) )
# mkdir new-git (новая папка)
# cd new-git ( войти в новую папку )
# git clone ( +ссылка- копируем репризиторий )



# ======================================================= Внесли изменения =================================

