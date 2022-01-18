# ======= 09/12/21================================================== ПАРАДИГМЫ ООП =============== ****************
# ИНКАПСУЛЯПЦИЯ
# НАСЛЕДОВАНИЕ
# ПОЛИФОРМИЗМ

# Класс - тип, описывающий устройство обьектов
# Обькт - экземпляр класса

# свойства = переменные
# методы = функции
# атрибуты = свойства + методы


# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1

# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))


# p1 = Point()
#
# print(type(p1))
# print(type(p1) == Point)  # равен ли экземпляр классу = TRUE, но ссылается на разные области видимости
# print(isinstance(p1, Point))  #

# print(getattr(p1, "x"))
# # Point.x = 100
# # print(p1.x, p1.y)
# # print(id(p1))
# # print(id(Point))
# p1.x = 5
# p1.y = 10
# # p1.z = 20
# setattr(p1, "z", 7)  # Создаем атрибут ( свойства ) экземпляр(класс)-имя свойства-значение
# print(p1.x, p1.y, Point.x)
# print(p1.__dict__)
# # print(Point.__dict__)  # __dict__ = просмотр всех свойств класса или его экземпляра
#
# print(getattr(p1, "z", "False"))  # getattr Доступ к атрибуту обьекта, 3 свойство - отображает по умолчанию
# print(hasattr(p1, "x"))  # hasattr Проверяет существует ли атрибут **************************************************
# print(hasattr(p1, "x"))  # hasattr Проверяет существует ли атрибут **************************************************
#
# p2 = Point
# print(p2.x, p2.y)
#
# delattr(p1, "z")  # удаляет атрибут
#
# print(p1.__dict__)


# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#     def set_coords(self, x, y):  # self  = аргумент содержащий ссылку на наш экземпляр класса ( ничего не принимает ) Обязателен !
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
# p1.set_coords(5, 10)
# p2 = Point()
# p2.set_coords(40, 80)
#
# Point.set_coords(p1, 15, 78)


# ЗАДАНИЕ ****************************************

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00.00.00"
#     country = "country"
#     city = "city"
#     address = "Street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))  # формотирование по центру относительно 40 символов
#         print(f"Имя: {self.name}\nДата рождени: {self.birthday}\nНомер телефона: {self.phone}\nСтрана: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#
#     def input_info(self, name, birthday, phone, country, city, address):
#         self.name = name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_name(self, name):  # Устанавливаем имя
#         """устанавливает имя"""
#         self.name = name
#
#     def get_name(self):
#         """Получаем имя"""
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#
# # h1.name = "Юля"
# # h1.birthday = "23.05.1986"
# # h1.phone = "45-46-98"
# # h1.country = "Россия"
# # h1.city = "Москва"
# # h1.address = "Чистопрудный бульвар"
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Ирина")
# h1.print_info()
# print(h1.get_name())
# h1.set_birthday("19.08.1986")
# h1.print_info()
# print(h1.get_birthday())

# ============================================= ***************************** ===================

# class Car:
#     name = "Car_name"
#     year = "Car_year"
#     model = "Car_model"
#     energe = "Car_energe"
#     color = "Car_color"
#     price = "Car_price"
#
#     def print_info(self):
#         print("Данные автомобиля".center(40, "*"))
#         print(f"Название модели: {self.name}\nГод выпуска: {self.year}\nПроизводитель: {self.model}\n"
#               f"Мощность двигателя: {self.energe}\nЦвет машины: {self.color}\nЦена: {self.price}")
#         print("*" * 40)
#
#     def input_info(self, name, year, model, energe, color, price):
#         self.name = name
#         self.year = year
#         self.model = model
#         self.energe = energe
#         self.color = color
#         self.price = price
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# cars1 = Car()
# cars1.print_info()
# cars1.input_info("ЛАДА", "1202", "СССР", "2 лошади", "ржавый", "0,5$")
# cars1.print_info()
# cars1.set_name("MAZDA")
# cars1.print_info()
# print(cars1.get_name())

# ## ===================================== ***********************************

# class Person:
#     skill = 10  # Квалификация сотрудника
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print(f"Данные сотрудника: {self.name} {self.surname}")
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f"Квалификация сотрудника: {self.name} {self.skill}")
#
#
#
# person1 = Person()
# person1.print_info("Виктор", "Резник")
# person1.add_skill(3)
# print()
# person2 = Person()
# person2.print_info("Анна", "Каренина")


# ==================================================================  14.12.21 ===================

# __магический метод__

# Специальные методы
# Конструктор __new__  # отвечает за выделение памяти
# Инициализатор __init__  #
# Деструктор __del__  #  разрывает связь

# class Point:
#
#     def __new__(cls, *args, **kwargs):
#         print("Конструктор")
#         return super().__new__(cls)
#
#     def __init__(self):
#         print("Инициализатор")
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# p1 = Point()

# ====

# class Point:
#
#     def __new__(cls, *args, **kwargs):
#         print("Конструктор")
#         return super().__new__(cls)
#
#     def __init__(self, x=0, y=0):
#         print("Инициализатор")
#         self.x = x
#         self.y = y
#
#     # def set_coords(self, x, y):
#     #     self.x = x
#     #     self.y = y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p2 = Point()
# print(p2.__dict__)
# p2 = Point(y=2)
# print(p2.__dict__)

# ===


# class Point:
#
#     def __init__(self, x=0, y=0):
#         print("Инициализатор")
#         self.x = x
#         self.y = y
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# Point.__init__(p1, 20)
# print(p1.__dict__)

# === ====================================

# class Point:
#
#     def __init__(self, x=0, y=0):
#         print("Инициализатор")
#         self.x = x
#         self.y = y
#
#     def __del__(self):  # деструктор отрабатывает последним когда все выполнилось
#         print("удаление экземпляра: " + self.__class__.__name__)
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# del p1  # принудительно разоравать связь с экземпляром
# # p1 = 0  # так же прерывает связь
# print(p1.x)

# ============================= СТАТИЧЕСКИЕ ПЕРЕМЕННЫЕ

# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1  # к статической переменной обращаемся через имя КЛАССА ( не экземпляра self )************
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# p2 = Point(2, 3)
# print(p2.__dict__)
# p3 = Point(2, 3)
# p4 = Point(2, 3)
# print(Point.count)
# print(p3.count)


# ========================== ПЕРЕЗАПИСАТЬ КООРДИНАТЫ ============

# class Point:
#     count = 0
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#     def check_value(z):  # статическая функция для проверки на Int и float
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):  # перезаписываем данные переменных
#         if Point.check_value(x) and Point.check_value(y):  # вызываем через имя класса функцию проверки и если верно то: перезаписываем
#             self.x = x
#             self.y = y
#         else:
#             print("координаты должны быть числами")
#
#     def get_coords(self):  # получить данные
#         return self.x, self.y
#
#
# p1 = Point(5, 10)
# p1.set_coords(2.3, 3)
# print(p1.get_coords())
# print(p1.__dict__)


# =========================================================== ЗАДАЧА С РОБОТАМИ =======================**********

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота: ", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#
#         if Robot.k ==0:
#             print(self.name, "Был последний")
#         else:
#             print("Работающих роботов осталось :", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут: ", self.name)
#
#
# droid1 = Robot("R2-D2")
# droid1.say_hi()
# print("Числинность роботов: ", Robot.k)
# droid2 = Robot("C-3PO")
# droid2.say_hi()
# print("Числинность роботов: ", Robot.k)
# droid3 = Robot("U-501")
# droid4 = Robot("BOOOOM")
# print("\nЗдесь роботы могут проделать какую то работу")
# print("Роботы закончили свою работу. Давайте их выключим!")
# del droid1
# del droid2
# del droid3
# del droid4
# print("Численность роботов :", Robot.k)

# =====================================================================================
# ************************************************************************************************************
# ====================================================== ИНКАПСУЛЯЦИЯ =========================================

# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def check_value(z):  # статическая функция для проверки на Int и float
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_value(x) and Point.check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.check_value(x):
#             self.__x = x
#         else:
#             print("координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.check_value(y):
#             self.__y = y
#         else:
#             print("координаты должны быть числами")
#
#     def get_coords(self):  # получить данные
#         return self.__x, self.__y
#
#     def get_coords_x(self):
#         return self.__x
#
#     def get_coords_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# print(p1.get_coords())
# p1.set_coords(20, 74)
# print(p1.get_coords())
# p1.set_coords_x(121)
# p1.set_coords_y(0.22)
#
# print(p1.get_coords())
# print(p1.get_coords_x())
# print(p1.get_coords_y())
#
# print(p1.__dict__)  # просмотреть содержимое
# print(p1._Point__x)  # чтение приватной переменой
# p1._Point__x = 0.75
# print(p1.__dict__)
# # print(p1.__x, p1.__y)
# # p1.__x = 100
# # p1.__y = "abc"
# # print(p1.__x, p1.__y)
#
# # Инкапсуляция
# # x - public
# # _x - protected  = используются для наследования ( изменить можно но не нужно )
# # __x - private  = закрытый режим доступа

# ========================================================== ЗАДАЧА ПРЯМОУГОЛЬНИК ============================
# import math
#
#
# class Rectangle:
#     def __init__(self, length=1, width=1):
#         self.__length = length
#         self.__width = width
#
#     def set_length(self, length):
#         self.__length = length
#
#     def set_width(self, width):
#         self.__width = width
#
#     def get_length(self):
#         return self.__length
#
#     def get_width(self):
#         return self.__width
#
#     def square(self):
#         return self.__length * self.__width
#
#     def perimetr(self):
#         return (self.__length * self.__width) * 2
#
#     def hypo(self):
#         return math.sqrt(self.__length ** 2 + self.__width ** 2)
#
#     def get_draw(self):
#         # for i in range(self.__length):
#         #     print(self.__width * "*")
#         print((self.__width * "*" + "\n") * self.__length)
#
#
# rec1 = Rectangle()
# rec1.set_length(3)
# rec1.set_width(9)
# print("Длина прямоугольника", rec1.get_length())
# print("Ширина прямоугольника", rec1.get_width())
# print("Площадь", rec1.square())
# print("Периметр", rec1.perimetr())
# print("Гипотенуза", round(rec1.hypo(), 2))
# rec1.get_draw()

# =========================================================== МЕТОДЫ ===================

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     # def __getattr__(self, name):  # передаем данные ЕСЛИ ПЕРЕМЕННОЙ НЕ СУЩЕСТВУЕТ,  __getattr__
#     #     return f"В классе {__class__.__name__} отсутствует атрибут: {name}"
#
#     def __getattribute__(self, item):  # ПОЛНОЕ ЗАКРЫТИЕ ДОСТУПА ПЕРЕМЕНОЙ МЕТОДОМ __getattribute__
#         if item == "_Point__x":  # ПО УСЛОВИЮ ПРЯМОГО ДОСТУПА К НЕЙ _Point__x
#             return "Закрытая переменная"
#         else:
#             return object.__getattribute__(self, item)
#
#     def check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.check_val(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.check_val(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def get_coords_x(self):
#         return self.__x
#
#     def get_coords_y(self):
#         return self.__y
#
#     def area(self):
#         return self.__x * self.__y
#
#
# p1 = Point(5, 10)
# # print(p1.__x)
# print(p1._Point__x)  # проверяеМ __getattribute__
# # print(p1.zzz)  # передаем несуществующие данные, проверяем __getattr__
# print(p1.get_coords())
# print(p1.area())

# ============================================


# class Point:
#     WIDTH = 5
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __setattr__(self, key, value):
#         if key == "WIDTH":
#             raise AttributeError
#         else:
#
#
#     def check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_x(self, x):
#         if Point.check_val(x):
#             self.__x = x
#         else:
#             print("Координаты должны быть числами")
#
#     def set_coords_y(self, y):
#         if Point.check_val(y):
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coords(self):
#         return self.__x, self.__y
#
#     def get_coords_x(self):
#         return self.__x
#
#     def get_coords_y(self):
#         return self.__y
#
#     def area(self):
#         return (self.__x * self.__y) + Point.WIDTH
#
#
#
# p1 = Point(5, 10)
# p1.WiDTH = 10
# print(p1.area())


# DZ-15.12.21
# import math
#
#
# class Sphere:
#
#     def __init__(self, r=0, x=0, y=0, z=0):
#         self.r = r
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def set_radius(self, r):
#         self.r = r
#
#     def get_volume(self):
#         return (self.r ** 3) * math.pi * 4 / 3
#
#     def get_square(self):
#         return (self.r ** 2) * math.pi * 4
#
#     def get_radius(self):
#         return self.r
#
#     def get_center(self):
#         return self.x, self.y, self.z
#
#     def set_center(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def is_point_inside(self, x, y, z):
#         if (self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2 <= self.r ** 2:
#             return True
#         return False
#
#
# sp1 = Sphere()
# # sp1.r = 0.6
# sp1.set_radius(0.6)
# print("get_radius: ", sp1.get_radius())
# print("get_volume: ", sp1.get_volume())
# print("get_square: ", sp1.get_square())
# print("get_center: ", sp1.get_center())
# print("is_point_inside:(0, 1.5, 0):", sp1.is_point_inside(0, -1.5, 0))
# sp1.set_radius(1.6)
# print("get_radius: ", sp1.get_radius())
# print("is_point_inside: (0, 1.5, 0):", sp1.is_point_inside(0, -1.5, 0))
#
#
#

# ================================================================ 16.12.21 ===============================
# class Point:
#     __slots__ = ["__x", "__y", "z"]  # закрываем доступ на добавление переменных кроме тех что прописанны
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# print(p1.__dict__)
#
#
#
# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __cheeck_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def __set_coords_x(self, x):  # __ закрываем доступ к методу
#         if Point.__cheeck_value(x):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     def __get_coords_x(self):
#         print("Вызов __get_coords_x")
#         return self.__x
#
#     def __del_coords_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)  # один из способов
#
#
# p1 = Point(5, 10)
# p1.coordX = 100
# print(p1.coordX)
# del p1.coordX
# p1.coordX = 7
# print(p1.coordX)

#
#
# class Point:
#
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __cheeck_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @property  # декоратор ======================================
#     def coords_x(self):  # первым должен быть GETer
#         print("Вызов __get_coords_x")
#         return self.__x
#
#     @coords_x.setter  # прописываем название метода + setter
#     def coords_x(self, x):  # __ закрываем доступ к методу
#         if Point.__cheeck_value(x):
#             self.__x = x
#         else:
#             raise ValueError("Неверный формат данных")
#
#     @coords_x.deleter
#     def coords_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)  # один из способов
#
#
# p1 = Point(5, 10)
# p1.coords_x = 100
# print(p1.coords_x)
# # del p1.coords_x
# p1.coords_x = 7
# print(p1.coords_x)
# print(p1.__dict__)

# ================================================== ЗАДАЧА перевести киллограмы в пуды

# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return  self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print("Киллограмы задаются только числами")
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# w = KgToPounds(12)
# print(w.to_pounds())
# w.kg = 41
# print(w.kg)
# print(w.to_pounds())
# w.kg = "fff"
# print(w.to_pounds())

# ================================================== СТАТИЧЕСКИЙ МЕТОД

# class Point:
#     __count = 0  # закрытая статическая переменная
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod  # статический метод ( можно вызывать и через имя класса и через имя экземпляра )
#     def get_count():
#         return Point.__count
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
#
# print(Point.get_count())
# print(p1.get_count())

#
#
# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))
# q = Change()
# print(q.dec(5), q.inc(5))


# ===================================================== ЗАДАЧА =================================

# class Numbers:
#
#     @staticmethod
#     def max(a, b, c, d):
#         if a > b and a > c and a > d:
#             return a
#         if b > a and b > c and b > d:
#             return b
#         if c > a and c > b and c > d:
#             return c
#         if d > a and d > b and d > c:
#             return d
#
#     @staticmethod
#     def min(a, b, c, d):
#         if a < b and a < c and a < d:
#             return a
#         if b < a and b < c and b < d:
#             return b
#         if c < a and c < b and c < d:
#             return c
#         if d < a and d < b and d < c:
#             return d
#
#     @staticmethod
#     def mid(a, b, c, d):
#         return (a + b + c + d)/4
#
#     @staticmethod
#     def fact(x):
#         fac = 1
#         for i in range(1, x + 1):  # факториал числа
#             fac *= i
#         return fac
#
#
# print(Numbers.max(1, 2, 3, 4))
# print(Numbers.min(1, 2, 3, 4))
# print(Numbers.mid(1, 2, 3, 4))
# print(Numbers.fact(4))

# =============================================

# ================================================= МЕТОДЫ КЛАССА ============================= ПЕРЕСМОТРЕТЬ !!!!

# class Date:
#     def __init__(self, day=0, mont=0, year=0):
#         self.day = day
#         self.mont = mont
#         self.year = year
#
#     @classmethod
#     def from_string(cls, date_as_string):  # cls принимает класс ( self принмает экземпляр )
#         day, mont, year = map(int, date_as_string.split("."))
#         date1 = cls(day, mont, year)
#         return date1
#
#     @staticmethod
#     def is_date_valid(date_as_string):
#         if date_as_string.count('.') == 2:
#             day, mont, year = map(int, date_as_string.split("."))
#             return day <= 31 and mont <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f'{self.year}-{self.mont}-{self.day}'
#
#
# dates = [
#     '30.12.2021'
#     '30-12-2020'
#     '01.01.2021'
#     '12.31.2020'
# ]
#
# for d in dates:
#     if Date.is_date_valid(d):
#         date = Date.from_string(d)
#         db = date.string_to_db()
#         print(db)
#     else:
#         print("Неправильная дата или формат строки с датой")
#
#
#
# # d = "16.12.2021"
# # day, mont, year = map(int, d.split("."))
# # print(day, mont, year)
# # d = Date()
# # date = Date.from_string("16.12..2021")
# # print(date.string_to_db())
# # d1 = Date()
# # date1 = d1.from_string("25.12.2021")
# # print(date1.string_to_db())
# #
# # date2 = Date.from_string("15.10.2110")
# # print(date2.string_to_db())


# ========================================================================= !!!!!

# # ====================== ЗАДАЧА
#
# class Ploshad:
#     count = 0
#
#     @staticmethod
#     def rectangle_geron(a, b, c):
#         perimetr = (a + b + c) / 2
#         return (perimetr * (perimetr - a) * (perimetr - b) * (perimetr - c)) ** 0.5
#
#     @staticmethod
#     def osnovanie_visota(a, h):
#         return 0.5 * h * a
#
#     @staticmethod
#     def ploshad_sq(a):
#         return a ** 2
#
#     @staticmethod
#     def ploshad_pryam(a, b):
#         Ploshad.count += 1
#         return a * b
#
#
# print(Ploshad.rectangle_geron(3, 4, 5))
# print(Ploshad.osnovanie_visota(6, 7))
# print(Ploshad.ploshad_sq(7))
# print(Ploshad.ploshad_pryam(2, 6))
# try_t = Ploshad
# print(try_t.rectangle_geron(1, 2, 3))
# print(Ploshad.count)


# DZ ==== 20.12.21

# class Temp:
#     count = 0
#
#     def cheeck_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     @staticmethod
#     def far_in_cel(x):
#         if Temp.cheeck_value(x):
#             Temp.count += 1
#             return (x - 32) * 5 / 9
#         else:
#             raise ValueError("Неверный формат данных")
#
#     @staticmethod
#     def cel_in_far(x):
#         if Temp.cheeck_value(x):
#             Temp.count += 1
#             return (x * 9/5) + 32
#         else:
#             raise ValueError("Неверный формат данных")
#
#     @staticmethod
#     def col_zap():
#         return Temp.count
#
#
# t1 = Temp
# print(t1.far_in_cel(68))
# print(t1.cel_in_far(0))
# print(t1.col_zap())


# ============================================================= 21.12.21 ================================

# ========================================================

# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname  # фамилия владельца
#         self.num = num  # номер счета
#         self.percent = percent  # процент начисления
#         self.value = value  # сумма в рублях
#         print(f'Счет #{self.num} принадлежащий {self.surname} был открыт')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт')
#
#     def edit_owner(self, surname):
#         """Меняем владельца"""
#         self.surname = surname
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         """Редактирование курса рубля по отношению к доллару"""
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         """Редактирование курса рубля по отношению к евро"""
#         cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         """Конвертация"""
#         return value * rate
#
#     def convert_to_usd(self):
#         """Перевод в доллары"""
#         usd_val = Account.convert(self.value, Account.rate_usd)  # статический метод вызывается через имя класса
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         """Перевод в доллары"""
#         eur_val = Account.convert(self.value, Account.rate_euro)  # статический метод вызывается через имя класса
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def add_persents(self):
#         """начисление процентов"""
#         self.value += self.value * self.percent
#         print("проценты были успешно начислены!!!")
#         self.print_balance()
#
#     def withdraw_money(self, val):  # принимает переменную - сумма которую хотим снять
#         """Снимаем баланс"""
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снято")
#         self.print_balance()
#
#     def add_money(self, val):
#         """Добавляем баланс"""
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def print_info(self):
#         """вывод информации о счете"""
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"#{self.num}\nВладелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")  # .0%  Указываем как отображать %
#         print("-" * 20)
#
#
# acc = Account('Долгих', 12345, 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
#
# acc.add_persents()
# print()
# acc.withdraw_money(700)
# print()
#
# acc.add_money(5000)

# =========================================================== НАСЛЕДОВАНИЕ =============
# БАЗОВЫЙ КЛАСС (родительский)
# ДОЧЕРНИЙ КЛАСС
# DRY (Dont Repeat Youself) - не повторяйся

# public = self.name (открытые переменные )
# protected = self._name (наследование)
# private = self.__name (закрытые переменные )

# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
# # print(issubclass(Point, object))  # проверяем родительский класс - object = TRUE
#
#     def __str__(self):
#         """Преобразовать в строку"""
#         return f"{self.x}, {self.y}"
#
#
# class Line:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         """sp и  ep принимают экземпляры класса Point по две координаты"""
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.width = width
#
#     def draw_line(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# class Rect:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         """sp и  ep принимают экземпляры класса Point по две координаты"""
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.width = width
#
#     def draw_rect(self):
#         print(f"Рисование прямоугольник: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))  # Point экземпляры класса с данными
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()

# Наследование
# Выносим иницилизатор в отдельный класс

# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     # print(issubclass(Point, object))  # проверяем родительский класс - object = TRUE
#
#     def __str__(self):
#         """Преобразовать в строку"""
#         return f"{self.x}, {self.y}"
#
#
# class Prop:  # выносим иницилизатор в отдельный класс
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         """sp и  ep принимают экземпляры класса Point по две координаты"""
#         print("Инициализатор базового класса Prop")
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.width = width
#
#
# class Line(Prop):  # наследуем класс
#     """дочерний класс"""
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")  # Первым отрабатывает инициализатор дочернего класса
#         # Prop.__init__(self, *args)  # при переопределении обращаемся к род классу и передаем аргументы
#         super().__init__(*args)  # можно (чаще используется ) обращаться через super(), self указывать не нужно.
#
#     def draw_line(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# class Rect(Prop):  # наследуем класс
#     """дочерний класс"""
#     def draw_rect(self):
#         print(f"Рисование прямоугольник: {self.sp}, {self.ep}, {self.color}, {self.width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))  # Point экземпляры класса с данными
# line.width = 10
# print(line.width)
# line.draw_line()
# rect = Rect(Point(30, 40), Point(70, 80))
# rect.draw_rect()
# print(rect.width)
#
# print(line.__dict__)

# С ЗАКРЫТЫМИ ПЕРЕМЕННЫМИ

# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     # print(issubclass(Point, object))  # проверяем родительский класс - object = TRUE
#
#     def __str__(self):
#         """Преобразовать в строку"""
#         return f"{self.x}, {self.y}"
#
#
# class Prop:  # выносим иницилизатор в отдельный класс
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         """sp и  ep принимают экземпляры класса Point по две координаты"""
#         print("Инициализатор базового класса Prop")
#         self.sp = sp
#         self.ep = ep
#         self.color = color
#         self.__width = width
#
#     def get_width(self):
#         return self.__width
#
#
# class Line(Prop):  # наследуем класс
#     """дочерний класс"""
#     def __init__(self, *args):
#         print("Переопределенный инициализатор Line")  # Первым отрабатывает инициализатор дочернего класса
#         # Prop.__init__(self, *args)  # при переопределении обращаемся к род классу и передаем аргументы
#         super().__init__(*args)  # можно (чаще используется ) обращаться через super(), self указывать не нужно.
#         self.__width = 5
#
#     def draw_line(self):
#         print(f"Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.get_width()}")
#
#
# class Rect(Prop):  # наследуем класс
#     """дочерний класс"""
#     def draw_rect(self):
#         print(f"Рисование прямоугольник: {self.sp}, {self.ep}, {self.color}, {self.__width}")
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# print(line.__dict__)


# =================================================================== 23.12.21 ===================


# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color, border):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#         self.border = border
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError("Значения ширины должно быть больше нуля")
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError("Значения высоты должно быть больше нуля")
#
#     def border_new(self):
#         return self.border
#
#     def area(self):
#         # return self.color  # обращаемся не к закрытой переменной а к методу def color
#         # return self.__width * self.__height
#         return self.width * self.height
#         # return self.border_new()
#
#
# rect = Rectangle(10, 20, "green", "1px solid gray")
# print(rect.area())
# print(rect.width)  # обращаемся к гетерам
# print(rect.height)  # обращаемся к гетерам
# print(rect.color)  # обращаемся к гетерам
# print(rect.border)  # в данном случае обращаемся к переменной
# rect.width = -50
# print(rect.area())

# ============================================= ЗАДАЧА с ЖИДКОСТЬЮ ==========================

# class Liquid:  # жидкость
#     def __init__(self, name, density):
#         self._name = name  # через одно подчеркивание _name  = переменные наследования
#         self._density = density  # плотность
#
#     def edit_density(self, val):
#         """изменение плотности"""
#         self._density = val
#
#     def calc_v(self, m):  # вычеление объема жидкости, соответствуещего заданной массе
#         res = m / self._density
#         print(f"Объем {m} кг {self._name} равен {res} m^3.")
#         return res
#
#     def calc_m(self, v):  # вычисление массы жидкости, соответствуещего заданному объему
#         res = v * self._density
#         print(f"Вес {v} m^3 {self._name} состовляет {res} кг.")
#         return res
#
#     def print_info(self):
#         print(f"Жидкость{self._name} (плотность = {self._density}kg/m^3.)")
#
#
# class Alcohol(Liquid):
#     def __init__(self, name, density, strength):
#         super().__init__(name, density)
#         self.strength = strength  # крепость
#
#     def edit_strength(self, val):  # изменение крепости
#         self.strength = val
#
#
# a = Alcohol("Wine", 1064.2, 14)
# a.print_info()
#
# a.edit_density(1000)
# a.print_info()
#
# a.calc_v(300)
# a.calc_m(0.5)
#
#
# print(a.strength)
# a.edit_strength(20)
# print(a.strength)

# ==============================

# class Point:  # класс для предоставления точек в трехмерном пространстве
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         else:
#             return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         else:
#             return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисуем линию: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# def set_coords(self, sp: Point, ep: Point):
#     if sp.is_int() and ep.is_int():
#         self._sp = sp
#         self._ep = ep
#     else:
#         print("Координаты должны быть числами")
#
#
# line = Line(Point(1.2, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(3.0, 40), Point(10.0, 200))
# line.draw_line()

#  НАСЛЕДУЕМ МЕТОДЫ ИЗ РОДИТЕЛЬСКОГО

# class Rect:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def show_rect(self):
#         print(f"Прямоугольник: \nШирина: {self.width}\nВысота: {self.height}")
#
#
# class RectFon(Rect):
#     def __init__(self, width, height, background):
#         super().__init__(width, height)
#         self.fon = background
#
#     def show_rect(self):
#         super().show_rect()  # переопределение метода из родительского
#         print("Рамка: ", self.fon)
#
# class RectBorder(Rect):
#     def __init__(self, width, height, border):
#         super().__init__(width, height)
#         self.border = border
#
#     def show_rect(self):
#         super().show_rect()  # переопределение метода из родительского
#         print("Бордер: ", self.border)
#
#
# shape1 = RectFon(100, 200, "Yellow")
# shape1.show_rect()
# print()
# shape2 = RectBorder(600, 300, "1px solid red")
# shape2.show_rect()

# DZ-1
# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname="user", num="####", percent=0.0, value=0):
#         self.__surname = surname  # фамилия владельца
#         self.__num = num  # номер счета
#         self.__percent = percent  # процент начисления
#         self.__value = value  # сумма в рублях
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был открыт')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт')
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def set_num(self, num):
#         self.__num = num
#
#     def set_percent(self, percent):
#         self.__percent = percent
#
#     def set_value(self, value):
#         self.__value = value
#
#     def get_surname(self):
#         return self.__surname
#
#     def get_num(self):
#         return self.__num
#
#     def get_percent(self):
#         return self.__percent
#
#     def get_value(self):
#         return self.__value
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         """Редактирование курса рубля по отношению к доллару"""
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         """Редактирование курса рубля по отношению к евро"""
#         cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         """Конвертация"""
#         return value * rate
#
#     def convert_to_usd(self):
#         """Перевод в доллары"""
#         usd_val = Account.convert(self.__value, Account.rate_usd)  # статический метод вызывается через имя класса
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         """Перевод в доллары"""
#         eur_val = Account.convert(self.__value, Account.rate_euro)  # статический метод вызывается через имя класса
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def add_persents(self):
#         """начисление процентов"""
#         self.__value += self.__value * self.__percent
#         print("проценты были успешно начислены!!!")
#         self.print_balance()
#
#     def withdraw_money(self, val):  # принимает переменную - сумма которую хотим снять
#         """Снимаем баланс"""
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято")
#         self.print_balance()
#
#     def add_money(self, val):
#         """Добавляем баланс"""
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         """вывод информации о счете"""
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"#{self.__num}\nВладелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")  # .0%  Указываем как отображать %
#         print("-" * 20)
#
#
# acc = Account()
# acc.set_surname("Василий")
# acc.set_num("#12345")
# acc.set_percent(0.03)
# acc.set_value(1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# acc.add_persents()
# print()
# acc.withdraw_money(700)
# print()
#
# acc.add_money(5000)

# # var2
# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname="user", num="####", percent=0.0, value=0):
#         self.__surname = surname  # фамилия владельца
#         self.__num = num  # номер счета
#         self.__percent = percent  # процент начисления
#         self.__value = value  # сумма в рублях
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был открыт')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт')
#
#     def edit_owner(self, surname):
#         """Меняем владельца"""
#         self.surname = surname
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.__surname = surname
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, num):
#         self.__num = num
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, percent):
#         self.__percent = percent
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, value):
#         self.__value = value
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         """Редактирование курса рубля по отношению к доллару"""
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         """Редактирование курса рубля по отношению к евро"""
#         cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         """Конвертация"""
#         return value * rate
#
#     def convert_to_usd(self):
#         """Перевод в доллары"""
#         usd_val = Account.convert(self.__value, Account.rate_usd)  # статический метод вызывается через имя класса
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         """Перевод в доллары"""
#         eur_val = Account.convert(self.__value, Account.rate_euro)  # статический метод вызывается через имя класса
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def add_persents(self):
#         """начисление процентов"""
#         self.__value += self.__value * self.__percent
#         print("проценты были успешно начислены!!!")
#         self.print_balance()
#
#     def withdraw_money(self, val):  # принимает переменную - сумма которую хотим снять
#         """Снимаем баланс"""
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято")
#         self.print_balance()
#
#     def add_money(self, val):
#         """Добавляем баланс"""
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         """вывод информации о счете"""
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"#{self.__num}\nВладелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")  # .0%  Указываем как отображать %
#         print("-" * 20)
#
#
# acc = Account()
# acc.surname = "Василий"
# acc.num = "#555555"
# acc.percent = 0.03
# acc.value = 1000
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# acc.add_persents()
# print()
# acc.withdraw_money(700)
# print()
#
# acc.add_money(5000)


# DZ-05.01.21
import math
import re

# class Pair:
#     gip = 0
#
#     def __init__(self, a=0, b=0):
#         self.a = a
#         self.b = b
#
#     def set_a(self, a):
#         self.a = a
#
#     def set_b(self, b):
#         self.b = b
#
#     def get_sum(self):
#         return f"Сумма: {self.a + self.b}"
#
#     def get_proiz(self):
#         return f"Произведение: {self.a * self.b}"
#
#
# class Right_triangle(Pair):
#
#     def __init__(self, a, b):
#         super().__init__(a, b)
#
#     def get_gip(self):
#         gip = ((self.a ** 2) + (self.b ** 2)) ** 0.5
#         return round(gip, 2)
#
#     def get_pr(self):
#         return self.a, self.b, self.get_gip()
#
#     def get_pl(self):
#         return (self.a * self.b) * 0.5
#
#
# alt = Right_triangle(5, 8)
#
# print(f"Гипотенуза АВС: {alt.get_gip()}")
# print(f"Прямоугольный треугольник АВС: {alt.get_pr()}")
# print(f"Площадь АВС: {alt.get_pl()}")
# print()
# print(alt.get_sum())
# print(alt.get_proiz())
#
# print()
# alt.set_a(10)
# alt.set_b(8)
# print(f"Гипотенуза АВС: {alt.get_gip()}")
# alt.set_a(10)
# alt.set_b(20)
# print(f"Гипотенуза АВС: {alt.get_gip()}")
# print(alt.get_sum())
# print(alt.get_proiz())
# print(f"Площадь АВС: {alt.get_pl()}")

# ======================= ONLINE ========================================================== 11.01.2022 ================
# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         self.verify_fio(fio)
#         self.verify_old(old)
#         self.verify_weight(weight)
#         self.verify_ps(ps)
#
#         self.__fio = fio.split()
#         self.__old = old
#         self.__ps = ps
#         self.__weight = weight
#
#         # '''В данном варианте мы в инициализаторе обращаемся к сетерам и там уже делаем закрытые переменные'''
#         # # self.verify_fio(fio)
#         # # self.verify_old(old)
#         # # self.verify_weight(weight)
#         # # self.verify_ps(ps)
#         #
#         # self.fio = fio
#         # self.old = old
#         # self.ps = ps
#         # self.weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError("ФИО должно быть строкой")
#         f = fio.split()  # разбивает строку по пробелам на массив [Фамилия, имя, отчество]
#         if len(f) != 3:  # масиив должен содержать 3 строки
#             raise TypeError("Неверный формат ФИО")
#         letters = "".join(
#             re.findall(r'[a-zа-яё-]', fio,
#                        flags=re.IGNORECASE))  # findall возвращает массив, join возвращает единную строку
#         for s in f:
#             if len(s.strip(letters)) != 0:  # strip удаляет все буквы
#                 raise TypeError("В ФИО можно использовать только буквы и дефис")
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError("Возраст должен быть числом в диапазоне от 14 до 100 лет")
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, (int, float)) or w < 20:
#             raise TypeError("Вес должен быть числом от 20кг и выше")
#
#     @classmethod
#     def verify_ps(cls, ps):
#         if not isinstance(ps, str):
#             raise TypeError("Паспорт должен быть строкой")
#         s = ps.split()  # массив из строковых значений
#         print(s)
#         if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#             raise TypeError("Неверный формат паспорта")
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def ps(self):
#         return self.__ps
#
#     @ps.setter
#     def ps(self, ps):
#         self.verify_ps(ps)
#         self.__ps = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight(weight)
#         self.__weight = weight
#
#
# # Фамилия Имя Отчество
#
#
# p1 = UserDate("Волков Игорь Николаевич", 50, "1234 548965", 80.8)
# p1.fio = "Петров Васька Петрович"
# print(p1.fio)
# p1.ps = "8888 564752"
# print(p1.ps)
#
# print(p1.__dict__)

# ================================== ПЕРЕГРУЗКА МЕТОДОВ ========================================== ************

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#
# class Line(Prop):
#     def draw_line(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#     def __set_one_coords(self, sp):
#         if sp.is_int():
#             self._sp = sp
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def __set_two_coords(self, sp, ep):
#         if sp.is_int() and ep.is_int():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть целыми числами")
#
#     def set_coords(self, sp: Point, ep: Point = None):  # перегрузка методов для одной координаты
#         if ep is None:
#             self.__set_one_coords(sp)
#         else:
#             self.__set_two_coords(sp, ep)
#
#
# line = Line(Point(1, 2), Point(10, 20))
# line.draw_line()
# line.set_coords(Point(30, 40), Point(100, 200))
# line.draw_line()
# line.set_coords(Point(-10, -20))
# line.draw_line()


# ============================================================================= Абстрактный метод

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def is_digit(self):
#         if isinstance(self.x, (int, float)) and isinstance(self.y, (int, float)):
#             return True
#         return False
#
#     def is_int(self):
#         if isinstance(self.x, int) and isinstance(self.y, int):
#             return True
#         return False
#
#
# class Prop:
#     def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
#         self._sp = sp
#         self._ep = ep
#         self._color = color
#         self._width = width
#
#     def set_coords(self, sp, ep):
#         if sp.is_digit() and ep.is_digit():
#             self._sp = sp
#             self._ep = ep
#         else:
#             print("Координаты должны быть числами")
#
#     def draw(self):
#         """Абстрактный метод"""
#         raise NotImplementedError("В дочернем классе должен быть определен метод draw()")  # Абстрактный метод ******
#
#
# class Line(Prop):
#     def draw(self):
#         print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Rect(Prop):
#     def draw(self):
#         print(f"Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# class Ellipse(Prop):
#     pass
#     # def draw(self):
#     #     print(f"Рисование Элипса: {self._sp}, {self._ep}, {self._color}, {self._width}")
#
#
# figs = list()
# figs.append(Line(Point(0, 0), Point(10, 10)))
# figs.append(Line(Point(10, 10), Point(20, 10)))
# figs.append(Rect(Point(50, 50), Point(100, 100)))
# figs.append(Ellipse(Point(-10, -10), Point(10, 10)))
#
# for f in figs:
#     f.draw()


# from abc import ABC, abstractmethod  # *****************************************************************************
#
#
# class Chess(ABC):
#     def draw(self):
#         print("Нарисовал шахматную фигуру")
#
#     @abstractmethod
#     def move(self):
#         print("Метод move() в базовом классе")
#
#
# class Queen(Chess):
#     def move(self):
#         super().move()
#         print("Ферзь перемещен на e2e4")
#
#
# q = Queen()
# q.draw()
# q.move()


# ===========================================================
# from math import pi
#
#
# class Table:
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             self._width = width
#             self._length = length
#         else:
#             self._radius = radius
#
#     def set_radius(self, radius):
#         self._radius = radius
#
#     def set_sides(self, width=None, length=None):
#         if length is None:
#             self._width = self._length = width
#         else:
#             self._width = width
#             self._length = length
#
#     def calc_area(self):
#         raise NotImplementedError("В дочернем классе должен быть определен метод calc_area")
#
#
# class Sq_table(Table):
#     def calc_area(self):
#         return self._width * self._length
#
#
# class Round_table(Table):
#     def calc_area(self):
#         return pi * self._radius ** 2
#
#
# t = Sq_table(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
#
# t1 = Round_table(radius=10)
# print(t.__dict__)
# print(t.calc_area())


# DZ - 13.01.22
from abc import ABC, abstractmethod
import math


# class Root(ABC):
#
#     @abstractmethod
#     def equation(self, a, b, c=None):
#         pass
#
#
# class Linear(Root):
#     def equation(self, a, b, c=None):
#         if a == 0 and b == 0:
#             print('Бесконечность')
#         elif a != 0 and (b == 0 or a <= b):
#             print(f"The root of '3x+7=0' is: {round((-b / a), 2)}")
#         else:
#             raise TypeError('Корней нет')
#
#
# class Quadrate(Root):
#     def equation(self, a, b, c=None):
#         d = b ** 2 + 4 * a * c
#         if d > 0:
#             x1 = (b + math.sqrt(d)) / (2 * a)
#             x2 = (b - math.sqrt(d)) / (2 * a)
#             print(f"The roots of '1x^2-2x-3=0' are: {x1}, {x2}")
#         elif d == 0:
#             x = b / (2 * a)
#             print(f"Корень = {x}")
#         else:
#             print("Корней нет")
#
#
# p1 = Linear()
# p1.equation(3, 7)
#
# p2 = Quadrate()
# p2.equation(1, 2, 3)

# ========================================================= 13.01.22

# from abc import ABC, abstractmethod
#
#
# class Currency(ABC):
#     def __init__(self, value):
#         self.value = value
#
#     @abstractmethod
#     def convert_to_rub(self):
#         pass
#
#     def print_value(self):
#         print(self.value, end=" ")
#
#
# class Dollar(Currency):
#     rate_to_rub = 74.16
#     suffix = "USD"
#
#     def convert_to_rub(self):
#         rub = self.value * Dollar.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Dollar.suffix, end=" ")
#
#
# class Euro(Currency):
#     rate_to_rub = 90.14
#     suffix = "EUR"
#
#     def convert_to_rub(self):
#         rub = self.value * Euro.rate_to_rub
#         return rub
#
#     def print_value(self):
#         super().print_value()
#         print(Euro.suffix, end=" ")
#
#
# d = [Dollar(5), Dollar(10), Dollar(50), Dollar(100)]
# e = [Euro(5), Euro(10), Euro(50), Euro(100)]
# print("*" * 50)
# for i in d:
#     i.print_value()
#     print(f"= {i.convert_to_rub():.2f} RUB")
# print("*" * 50)
# for i in e:
#     i.print_value()
#     print(f"= {i.convert_to_rub():.2f} RUB")

# =======================================================================

# from abc import ABC, abstractmethod
#
#
# class Father(ABC):
#     @abstractmethod
#     def display1(self):
#         pass
#
#     @abstractmethod
#     def display2(self):
#         pass
#
#
# class Child(Father):
#     def display1(self):
#         print("Child Class")
#         print("Display 1 Abstract Method")
#
#
# class GrandChild(Child):
#     def display2(self):
#         print("GrandChild Class")
#         print("Display 2 Abstract Method")
#
#
# gc = GrandChild()
# gc.display1()
# gc.display2()


# ================================================= ВЛОЖЕННЫЕ КЛАССЫ =================================

# class MyOuter:
#     age = 18
#
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def outer_class_method(cls):
#         print("Я - метод внешнего класса")
#
#     def outer_obj_method(self):
#         print("Я являюсь связующим методом объекта внешнего класса")
#
#     class MyInner:  # вложенный класс не видит переменных и методов родительского ( делаем через имя родителя )
#         def __init__(self, inner_name, obj):
#             self.inner_name = inner_name
#             self.obj = obj
#
#         def inner_method(self):
#             print("Я - метод внутреннего класса")
#             MyOuter.outer_class_method()  # вызываем через имя родительского класса
#             out1 = MyOuter("Внешний класс")
#             print(out1.name)
#             print(MyOuter.age)
#             self.obj.outer_obj_method()
#
#
# out = MyOuter("Внешний")
# inner = out.MyInner("Внутренний", out)
# print(inner.inner_name)
# inner.inner_method()

# ======================================

class Employee:
    def __init__(self):
        self.name = "Employee"
        self.intern = self.Intern()
        self.head = self.Head()

    def show(self):
        print("Employee list")
        print("Name", self.name)

    class Intern:
        def __init__(self):
            self.name = "Smith"
            self.id = "657"

        def display(self):
            print("Name: ", self.name)
            print("Degree: ", self.id)

    class Head:
        def __init__(self):
            self.name = "Albina"
            self.id = "007"

        def display(self):
            print("Name: ", self.name)
            print("Degree: ", self.id)


outer = Employee()
outer.show()

d1 = outer.intern
d2 = outer.head
d1.display()
print("*" * 20)
d2.display()


# =================================================

# class Geeksforgeeks:
#     def __init__(self):
#         self.inner = self.Inner()
#
#     def show(self):
#         print("This is an outer class")
#
#     class Inner:
#         def __init__(self):
#             self.inner_inner = self.InnerClass()
#
#         def show(self):
#             print("This is the inner class")
#
#         class InnerClass:
#             def show(self):
#                 print("This is an inner class of inner class")
#
#
# outer = Geeksforgeeks()
# outer.show()
#
# inner1 = outer.inner
# inner1.show()
#
# inner2 = outer.inner.inner_inner
# inner2.show()


# ============================================
# ===========================================
# # class OS:
# #    def system(self):
# #         return "Windows 10"
# #
# #
# # class CPU:
# #     def make(self):
# #         return "Intel"
# #
# #     def model(self):
# #         return "Core-i7"

# # class OS:
# #     def system(self):
# #         return "Windows 10"
# ============================================

# class Computer:
#     def __init__(self):
#         self.name = "PC001"
#         self.os = self.OS()
#         self.cpu = self.CPU()
#
#     class CPU:
#         def make(self):
#             return "Intel"
#
#         def model(self):
#             return "Core-i7"
#
#     class OS:
#         def system(self):
#             return "Windows 10"
#
# comp = Computer()
# my_os = comp.os
# my_cpu = comp.cpu
#
# print(comp.name)
# print(my_os.system())
# print(my_cpu.make())
# print(my_cpu.model())

# ======================================

# class Base:
#     def __init__(self):
#         self.db = self.Inner()  # переменная для доступа из дочернего
#
#     def display(self):
#         print("In Base Class")
#
#     class Inner:
#         def display1(self):
#             print("Inner of Base class")
#
#
# class SubClass(Base):
#     def __init__(self):
#         print("In Subclass")
#         super().__init__()
#
#     class Inner(Base.Inner):  # наследуемся у дочернего класса родителя
#
#         def display2(self):
#             print("Inner of Subclass")
#
#
# a = SubClass()
# a.display()
#
# b = a.db
# # b = SubClass.Inner
# b.display1()
# b.display2()


# ======================================= НАследование от нескольких Родителей *******************

# class Creature:
#     def __init__(self, name):
#         self.name = name
#
#
# class Animal(Creature):
#     def sleep(self):
#         print(self.name + " is sleeping")
#
#
# class Pet(Creature):
#     def play(self):
#         print(self.name + " is playing")
#
#
# class Dog(Animal, Pet):
#     def bark(self):
#         print(self.name + " is braking")
#
#
# b = Dog("Buddy")
# b.bark()
# b.play()
# b.sleep()

# ==============================================

# class A:
#     def __init__(self):
#         print("Инициализатор класса А")
#
#
# class B(A):
#     def __init__(self):
#         print("Инициализатор класса B")
#
#
# class C(A):
#     def __init__(self):
#         print("Инициализатор класса C")
#
#
# class D(B, C):  # если два равных родителя, то в первую очередь отработает тот что прописан первым (в данном случае В)
#     pass
#     # def __init__(self):
#     #     print("Инициализатор класса D")
#
#
# d = D()
# print(D.mro())  # mro -  отображает наследование ********************************************************************


# =====================================

# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x, self.y})"
#
#
# class Styles:
#     def __init__(self, color="red", width=1):
#         print("Инициализатор Styles")
#         self._color = color
#         self._width = width
#
#
# class Pos:
#     def __init__(self, sp: Point, ep: Point, *args):
#         print("Инийиализатор Pos")
#         self._sp = sp
#         self._ep = ep
#         Styles.__init__(self, *args)
#
#
# class Line(Pos, Styles):
#     def draw(self):
#         print(f"Рисование линии: {self._sp, self._ep, self._color, self._width}")
#
#
# l1 = Line(Point(10, 10), Point(100, 100), "green", 5)
# l1.draw()
