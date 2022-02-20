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
import json
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

# class Employee:
#     def __init__(self):
#         self.name = "Employee"
#         self.intern = self.Intern()
#         self.head = self.Head()
#
#     def show(self):
#         print("Employee list")
#         print("Name", self.name)
#
#     class Intern:
#         def __init__(self):
#             self.name = "Smith"
#             self.id = "657"
#
#         def display(self):
#             print("Name: ", self.name)
#             print("Degree: ", self.id)
#
#     class Head:
#         def __init__(self):
#             self.name = "Albina"
#             self.id = "007"
#
#         def display(self):
#             print("Name: ", self.name)
#             print("Degree: ", self.id)
#
#
# outer = Employee()
# outer.show()
#
# d1 = outer.intern
# d2 = outer.head
# d1.display()
# print("*" * 20)
# d2.display()


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


# ============================================================== 18.01.22

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(self.name, end="")
#
#     class Notebook:
#         def __init__(self):
#             self.brand = "HP"
#             self.cpu = "i7"
#             self.ram = 16
#
#         def show(self):
#             print(f"=> {self.brand}, {self.cpu}, {self.ram}")
#
#
# s1 = Student("Roman")
# s2 = Student("Vladimir")
#
# s1.show()
# s2.show()

# +======================================================== МИКСИНЫ (mixins) / ПРИМЕСИ ++++++++++++++++++++++++++

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=""):
#         super().log(message, filename="subclasslog.txt")
#
#
# sub = MySubClass()
# sub.display("Эта строка будет отображаться и записываться в файл")

# ==========================

# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print("Init Goods")
#         self.name = name
#         self.wight = weight
#         self.price = price
#
#     def print_info(self):
#         print(f"{self.name}, {self.wight}, {self.price}")
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print("Init MixinLog")
#         self.ID += 1
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f"{self.id}: Товар был продан в 00:00 часов")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# n = NoteBook("HP", 1.5, 35000)
# n.print_info()
# n.save_sell_log()
# print(NoteBook.mro())

# ======================================================= ПЕРЕГРУЗКА ОПЕРАТОРОВ ================================
# __add__ / __sub__ / __mul__ / __truediv__ / __floordiv__  / __mod__
# ФОрмотирование времени *************************

# class Clock:
#     __DAY = 86400  # 86400 сек в сутках = 24*60*60
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.__secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.__secs % 60  # секнды
#         m = (self.__secs // 60) % 60  # минуты
#         h = (self.__secs // 3600) % 24  # часы
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):  # add=Перезагрузка, self = c1, other = c2
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый оперант должен быть типом Clock")
#
#         return Clock(self.__secs + other.__secs)
#
#
# c1 = Clock(100)
# c2 = Clock(200)
# c3 = Clock(300)
#
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c3.get_format_time())
# c4 = c1 + c2 + c3
# print(c4.get_format_time())

# ======================


# class Clock:
#     __DAY = 86400  # 86400 сек в сутках = 24*60*60
#
#     def __init__(self, secs: int):
#         if not isinstance(secs, int):
#             raise ValueError("Секунды должны быть целым числом")
#
#         self.__secs = secs % self.__DAY
#
#     def get_format_time(self):
#         s = self.__secs % 60  # секнды
#         m = (self.__secs // 60) % 60  # минуты
#         h = (self.__secs // 3600) % 24  # часы
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __mul__(self, other):  # add=Перезагрузка, self = c1, other = c2
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый оперант должен быть типом Clock")
#
#         return Clock(self.__secs * other.__secs)
#
#     def __eq__(self, other):
#         if self.__secs == other.__secs:
#             return True
#         return False
#
#     def __ne__(self, other):
#         return not self.__eq__(other)  # противоположное значение __eq__
#
#
# c1 = Clock(200)
# c2 = Clock(200)
# c3 = Clock(300)
# # c1 *= c2 * c3  # ====================================== второй вариант
# print(c1.get_format_time())
# print(c2.get_format_time())
#
# # ============================= ПРОПИСАТЬ ВСЕ МЕТОДЫ ПЕРЕЗАГРУЗКИ =================================
#
# if c1 == c2:
#     print("Время одинаково")
#
# if c1 != c3:
#     print("Время разное")


# ======================================================================= 20.01.22 ====================
# Перезагрузка методов продолжение, перегрузка квадратных скобок

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = list(marks)  # указываем список
#
#     def __getitem__(self, item):  # __getitem__ перегрузили возможность получения данных в квадратных скобках
#         if 0 <= item < len(self.marks):  # проверка на верный индекс ( существующий )
#             return self.marks[item]
#         else:
#             raise IndexError("Неверный индекс")
#
#     def __setitem__(self, key, value):  # __setitem__
#         if not isinstance(key, int) or key < 0:
#             raise TypeError("Индекс должен быть целым неотрицательным числом")
#
#         if key >= len(self.marks):
#             off = key + 1 - len(self.marks)  # если ключ больше чем длина списка
#             self.marks.extend([None] * off)  # пишем None в места пропусков индекса, новое значение записываем в конец
#
#         self.marks[key] = value  # устанавливаем в какой то ключ какое то значение
#
#     def __delitem__(self, key):  # удаление значения по ключу
#         if not isinstance(key, int):
#             raise TypeError("Индекс должен быть целым числом")
#         del self.marks[key]
#
#
# s1 = Student("Сергей", [5, 8, 4, 3, 2])
# # print(s1.marks[2])
# # print(s1[2])
# # print(s1[12])  # выходим за рамки списка-индекс не существует
# # s1[2] = 22  # пытаемся записать в список
# # s1["2.5"] = 22  # пытаемся записать неверный индекс
# # print(s1[2])
# s1[10] = 33  # записываем значение в несуществующий индекс с пропуском промежуточных
# del s1[2]  # удаляем элемент
# print(s1.marks)


# ================================== ЗАДАЧА напишите класс  Point3D сложение 3 координат итд

# class Point3D:
#     CH = "Координата должна быть числом"
#     RIGHT = "Правый оперант должен быть типом Point3D"
#
#     def __init__(self, x=0, y=0, z=0):
#         self.x = x  # будут поступать сеттеры х
#         self.y = y
#         self.z = z
#
#     def __str__(self):
#         return f"{self.x}, {self.y}, {self.z}"  # вызывается геттер
#
#     @staticmethod  # проверяем на int и float
#     def __check_value(v):
#         return isinstance(v, int) or isinstance(v, float)  # isinstance(v, (int, float)) Тоже самое
#
#     @staticmethod
#     def __check0(exemplar):
#         if exemplar.x == 0 or exemplar.y == 0 or exemplar.z == 0:
#             raise ZeroDivisionError("ни одна из координат второго операнда не должна быть равна 0")
#
#     @property
#     def x(self):
#         return self.__x
#
#     @x.setter
#     def x(self, value):
#         if self.__check_value(value):
#             self.__x = value
#         else:
#             print(self.CH)
#
#     @property
#     def y(self):
#         return self.__y
#
#     @y.setter
#     def y(self, value):
#         if self.__check_value(value):
#             self.__y = value
#         else:
#             print(self.CH)
#
#     @property
#     def z(self):
#         return self.__z
#
#     @z.setter
#     def z(self, value):
#         if self.__check_value(value):
#             self.__z = value
#         else:
#             print(self.CH)
#
#     def __add__(self, other):  # Перегрузка методов на сложение
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x + other.x, self.__y + other.y, self.__z + other.z)
#
#     def __sub__(self, other):  # Перегрузка методов на вычитание
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x - other.x, self.__y - other.y, self.__z - other.z)
#
#     def __mul__(self, other):  # Перегрузка методов на умножение
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return Point3D(self.__x * other.x, self.__y * other.y, self.__z * other.z)
#
#     def __truediv__(self, other):  # Перегрузка методов на деление = other делитель
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         self.__check0(other)
#         return Point3D(self.__x / other.x, self.__y / other.y, self.__z / other.z)
#
#     def __eq__(self, other):  # Перегрузка методов на равенство
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         return self.__x == other.x and self.__y == other.y and self.__z == other.z
#
#     def __getitem__(self, item):  # проверяем на строковые значения в индексе
#         if not isinstance(item, str):
#             raise ValueError("Ключ должен быть строкой")
#         elif item == "x":
#             return self.__x
#         elif item == "y":
#             return self.__y
#         elif item == "z":
#             return self.__z
#         else:
#             print("Неверное значение ключа")
#
#     def __setitem__(self, key, value):
#         if not isinstance(key, str):
#             raise ValueError("Ключ должен быть строкой")
#         if self.__check_value(value):
#             if key == "x":
#                 self.__x = value
#             if key == "y":
#                 self.__y = value
#             if key == "z":
#                 self.__z = value
#         else:
#             print("координаты должны быть числами")
#
#
# pt = Point3D(12, 15, 18)
# pt2 = Point3D(6, 3, 9)
# print(f"Координаты 1-й точки {pt}")
# print(f"Координаты 2-й точки {pt2}")
#
# pt3 = pt + pt2  # складываем xyz + xyz
# print(f"Сложение координат ({pt3})")
# pt4 = pt - pt2
# print(f"Вычитание координат ({pt4})")
# pt5 = pt * pt2
# print(f"Умножение координат ({pt5})")
# pt6 = pt / pt2
# print(f"Деление координат ({pt6})")
# print(f"Равенство координат {pt == pt2}")
#
# print('x=', pt["x"], 'x1=', pt2["x"])
# print('y=', pt["y"], 'y1=', pt2["y"])
# print('z=', pt["z"], 'z1=', pt2["z"])
#
# pt['x'] = 20
# print("Запись значения в координату x:", pt['x'])
# print(f"Координаты 1-й точки {pt}")


# =============================================================

# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per_rect(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_per_sq(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# print(r1.get_per_rect(), r2.get_per_rect())
# s1 = Square(10)
# s2 = Square(20)
# print(s1.get_per_sq(), s2.get_per_sq())
#
# shape = [r1, r2, s1, s2]
#
# for g in shape:
#     if isinstance(g, Rectangle):
#         print(g.get_per_rect())
#     else:
#         print(g.get_per_sq())

# тоже самое с полиморфизмом ( другая реализация с одним названием метода )
# class Rectangle:
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_perimetr(self):
#         return 2 * (self.w + self.h)
#
#
# class Square:
#     def __init__(self, a):
#         self.a = a
#
#     def get_perimetr(self):
#         return 4 * self.a
#
#
# r1 = Rectangle(1, 2)
# r2 = Rectangle(3, 4)
# s1 = Square(10)
# s2 = Square(20)
# shape = [r1, r2, s1, s2]
#
# for g in shape:
#     print(g.get_perimetr())

# ======================================
# аналог сложения чисел и строк ==== ПОЛИМОРФИЗМ ======================================
# class Number:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return self.value + int(a)
#
#
# class Text:
#     def __init__(self, value):
#         self.value = value
#
#     def total(self, a):
#         return len(self.value + str(a))
#
#
# t1 = Number(10)
# t2 = Text("Python")
# print(t1.total(35))
# print(t2.total(35))

# ========================================================= ПОЛИМОРФИЗМ ====================

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Я собака. Меня зовут {self.name}. Мой возраст {self.age}")
#
#     def make_sound(self):
#         print(f"{self.name} мяукает")
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Я кот. Меня зовут {self.name}. Мой возраст {self.age}")
#
#     def make_sound(self):
#         print(f"{self.name} гавкает")
#
#
# cat = Cat("Пушок", 0.5)
# dog = Dog("Мухтар", 4)
#
# for animal in (cat, dog):
#     animal.info()
#     animal.make_sound()

# ===================================================== МЕТОД REPR

# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):  # обязательно возвращает строковое выражение (f"")
#         """служебная информация (техническая)"""
#         return f"{self.__class__}:{self.name}"  # выводим информацию к какому классу относится и информацию переменной
#
#     def __str__(self):  # первым отрабатывает __str__
#         return f"{self.name}"
#
#
# cat = Cat("Пушок")
# print(cat)

# DZ_24_01_22

# from abc import ABC, abstractmethod
# import math
#
#
# class Shape(ABC):
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#     @abstractmethod
#     def square(self):
#         pass
#
#     @abstractmethod
#     def painting(self):
#         pass
#
#     @abstractmethod
#     def print_info(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, x=0, y=0, color='red'):
#         self.x = x
#         self.y = y
#         self.color = color
#
#     def perimeter(self):
#         return 2 * (self.x + self.y)
#
#     def square(self):
#         return self.x * self.y
#
#     def painting(self):
#         for pain in range(self.x, 0, -1):
#             print(self.y * '*')
#
#     def print_info(self):
#         print(f"Сторона: {self.x}\nЦвет: {self.color}\nПлощадь: {self.square()}\nПериметр: {self.perimeter()}")
#
#
# class Rectangle(Shape):
#     def __init__(self, x=0, y=0, color='red'):
#         self.x = x
#         self.y = y
#         self.color = color
#
#     def perimeter(self):
#         return 2 * (self.x + self.y)
#
#     def square(self):
#         return self.x * self.y
#
#     def painting(self):
#         for pain in range(self.x, 0, -1):
#             print(self.y * '*')
#
#     def print_info(self):
#         print(
#             f"Сторона: {self.x}\nШирина: {self.y}\nЦвет: {self.color}\nПлощадь: {self.square()}\nПериметр: {self.perimeter()}")
#
#
# class Triangle(Shape):
#     def __init__(self, x=0, y=0, z=0, color='red'):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.color = color
#
#     def perimeter(self):
#         return (self.z + self.y + self.x) / 2
#
#     def square(self):
#         d = self.perimeter()
#         return round(math.sqrt(d * (d - self.x) * (d - self.y) * (d - self.z)), 2)
#
#     def painting(self):
#         for pain in range(0, self.y+1):
#             print(' ' * (self.y - pain), '* ' * pain)
#
#         # print('\n'.join([f"{' ' * (self.y - x - 1)}{'*' * (2 * x + 1)}" for x in range(0, self.y)]))
#
#     def print_info(self):
#         print(
#             f"Сторона 1: {self.x}\nСторона 2: {self.y}\nСторона 3: {self.z}\nЦвет: {self.color}\nПлощадь: {self.square()}\nПериметр: {self.perimeter()}")
#
#
# var = Square(3, 3)
# var1 = Rectangle(3, 7, "green")
# var2 = Triangle(11, 6, 6, "yellow")
#
# for i in (var, var1, var2):
#     i.perimeter()
#     i.square()
#     i.print_info()
#     i.painting()
#     print()


# ========================================================== 25.01.22 ==============================================

# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f"{self.last_name} {self.first_name} {self.age}")
#
#
# class Student(Human):
#     def __init__(self, spec, group, rating, last_name, first_name, age):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         print(f"{self.speciality} {self.group} {self.rating}", end=" ")
#         super().info()
#
#
#
# class Teacher(Human):
#     def __init__(self, spec, experience, last_name, first_name, age):
#         super().__init__(last_name, first_name, age)
#         self.speciality = spec
#         self.experience = experience
#
#     def info(self):
#         print(f"{self.speciality} {self.experience}", end=" ")
#         super().info()
#
#
# class Graduate(Student):
#     def __init__(self, topic, spec, group, rating, last_name, first_name, age):
#         super().__init__(spec, group, rating, last_name, first_name, age)
#         self.topic = topic
#
#     def info(self):
#         print(f"{self.topic}", end=" ")
#         super().info()
#
#
# group = [
#     Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5),
#     Graduate("Шугани", "Сергей", 15,  "РПО", "PD_011", 5, "Защита персональных данных"),
#     Teacher("Башкиров", "Алексей", 45,  "Разработка приложений", 20)
# ]
#
# for i in group:
#     i.info()

# ================================================

# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
#
# p = Point(1, -2, -7)
# print(len(p))
# print(p.__dict__)
# print(abs(p))

# ===============================
import math

# class Point:
#     __slots__ = ('x', 'y', '__length')  # прописываем какие переменные разрешены
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)  # ТУТ вызываем метод
#
#     @property
#     def length(self):
#         return self.__length  # инициализируем переменную ТУТ
#
#     @length.setter
#     def length(self, value):
#         self.__length = value
#
#
# p = Point(5, 9)
# print(p.length)
# # p.z = 5
# # print(p.__dict__)


# ==============================================  __sizeof__ смотрим размер памяти =========================*****

# class Point:
#     __slots__ = ('x', 'y')  # прописываем какие переменные разрешены
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point(1, 2)
# pt2 = Point2D(1, 2)
# print("pt =", pt.__sizeof__())  # __sizeof__ смотрим размер памяти
# print("pt =", pt2.__sizeof__() + pt2.__dict__.__sizeof__())


# ==================================================


# class Point:
#     __slots__ = ('x', 'y')  # прописываем какие переменные разрешены
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):  # __slots__  на дочерний класс не действует
#     pass
#
#
# pt3 = Point3D(10, 20)
# pt3.z = 30
# print(pt3.__dict__)

# =========================================

# class Point:
#     __slots__ = ('x', 'y')  # прописываем какие переменные разрешены
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point3D(Point):
#     __slots__ = 'z'  # можем указать отдельно в дочернем классе
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt3 = Point3D(10, 20, 30)
# # pt3.z = 30
# print(pt3.x, pt3.y, pt3.z)


# ======================================================== ФУНКТОРЫ ==== экземпляры используются как функции __call__

# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#         return self.__counter
#
#
# c1 = Counter()
# c1()
# c1()
# c2 = Counter()
# c2()
# c2()
# c2()

# ===============================

# class StripsChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):  # args[0] если передаем 1 значение то указываем индекс (0)
#             raise ValueError("аргумент должен быть строкой")
#         return args[0].strip(self.__chars)
#
#
# s1 = StripsChars("?:!.; ")  # пробел на конце обязателен
# print(s1("  .  ?Hello World! "))
#
#
# # это же через функцию :
#
# def strip_string(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError("Аргумент должен быть строкой")
#         return string.strip(chars)
#
#     return wrap()
#
#
# s1 = StripsChars("?:!.; ")
# print(s1("    ?Hello World! "))


# ===================================================== Декораторы  ==================================

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self):
#         print('Перед вызовом функции')
#         self.func()
#         print('После вызова функции')
#
#
# @MyDecorator
# def function():
#     print("func")
#
#
# function()

# ===================

# class MyDecorator:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         print('Перед вызовом функции')
#         res = self.func(a, b)
#         print('После вызова функции')
#         return res
#
#
# @MyDecorator
# def function(a, b):
#     return a * b
#
#
# print(function(2, 5))


# ====================================== Задание ===============================

# class Power:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, a, b):
#         res = self.func(a, b)
#         return res ** 2
#
#
# @Power
# def function(a, b):
#     return a * b
#
#
# print(function(2, 3))

# =================================

# class Power:
#     def __init__(self, arg):
#         self.name = arg
#
#     def __call__(self, func):
#         def wrap(a, b):
#             print('ПЕРЕД')
#             print(self.name)
#             func(a, b)
#             print("ПОСЛЕ")
#
#         return wrap
#
#
# @Power('test2')
# def function(a, b):
#     print(a, b)
#
#
# function(2, 3)


# DZ_27.01.22


# ============================================================== 27.01.22 ==================================

# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrapper(a, b):
#             res = func(a, b)  # func  вызывает multuple
#             print(res)
#             return res ** self.arg
#
#         return wrapper
#
#
# @Power(5)
# def multuplr(a, b):
#     return a * b
#
#
# print("результат", multuplr(2, 2))

# ==================================================== Наружные декораторы ======

# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# ========


# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
#     def dec(fn):
#         def wrap(*args, **kwargs):
#             print("*" * 20)
#             fn(*args, **kwargs)
#             print("*" * 20)
#
#         return wrap
#
#     @dec
#     def info(self):
#         print(f"{self.name} {self.surname}")
#
#
# p1 = Person("Виталий", "Карасев")
# p1.info()

# ============================================ Декораторы классов, декорируем сам класс
# можем использовать методы из класса декоратора в экземпляре основного класса

# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print("Init ActualClass")
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
# print(obj.quad(4))
# print(obj.doubler(4))

# =======================================================

# class Message:
#     _REGISTERY = {}
#
#     def __init__(self, text):
#         self.text = text
#
#     @classmethod
#     def registr(cls, name):
#         def decorator(klass):
#             cls._REGISTERY[name] = klass
#             return klass
#
#         return decorator
#
#     @classmethod
#     def create(cls, message_type, text):
#         klass = cls._REGISTERY.get(message_type)
#         if klass is None:
#             raise ValueError("Такого мессенджера нет")
#         print(text, end=" ")
#         return klass(text)
#
#
# @Message.registr('Telegram')
# class TelegramMessage(Message):
#     def send(self):
#         print("(Telegram)")
#
#
# @Message.registr('WhatsApp')
# class WhatsAppMessage(Message):
#     def send(self):
#         print("(WhatsApp)")
#
#
# # # m1 = TelegramMessage("text")
# # # m1.send()
# # # m2 = WhatsAppMessage("new text")
# # # m2.send()
# m1 = Message.create("Telegram", "text")
# m1.send()
# m2 = Message.create("WhatsApp", "new text")
# m2.send()

# =============================== ДИСКРИПТОР (класс у которого определенны магические методы ( set, get, del )
# __get__() / __set__() / __delete__()  / __set_name__()
# Дискриптор данных или data descriptor
# non-data descriptor (дескриптор не данных ) - только для __get__

# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, value):
#         self.__surname = value
#
#
# p = Person("Иван", "Николаев")
# print(p.surname)
# print(p.name)

# ============= это же =>

# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)  # экземпляр класса
#         self.surname = String(surname)  # экземпляр класса
#
#
# p = Person("Иван", "Николаев")
# print(p.name.get())
# p.name.set("Игорь")
# print(p.name.get())


# ================================================
# __get__() / __set__() / __delete__()  / __set_name__()

# class ValidString:
#     def __set_name__(self, owner, name):  # owner = ссылка на класс Person
#         self.__name = name
#
#     def __get__(self, instance, owner):  # owner = ссылка на класс Person, instance = ссылка на экземпляр класса
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f"{self.__name} должно быть строкой")
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()  # экземпляр класса
#     surname = ValidString()  # экземпляр класса
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person("Иван", "Николаев")
# print(p.name)
# p.name = "Игорь"
# print(p.name)
# print(p.surname)

# == ЗАДАЧА
# Дискриптор данных или data descriptor
# class NoNegative:
#     def __set_name__(self, owner, name):  #
#         self.__name = name
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError("Значение должно быть положительным")
#         instance.__dict__[self.__name] = value
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#
# class Order:
#     price = NoNegative()
#     quantity = NoNegative()
#
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def total(self):
#         return self.price * self.quantity
#
#
# apple = Order('apple', 5, 10)
# print(apple.total())
# apple.price = -10

# ======================================================= МЕТТАКЛАССЫ - класс который создает другие классы

# a = 5
# print(type(a))
# print(type(int))

# =============================

# class MyList(list):  # если наследуется от list, можем применять методы списков (append())
#     def get_length(self):
#         return len(self)
#
#
# lst=MyList()
# lst.append(1)
# lst.append(2)
# lst[0] = 3
# print(lst, lst.get_length())

# тоже самое =>
# # MyList = type(
# #     'MyList',
# #     (list,),
# #     dict(get_length=lambda self:len(self))
# # )

# ===============

# class MyMetaclass(type):
#     def __new__(mcs, name, bases, attr):  # Конструктор,  mcs = метакласс, имя, bases-от чего наследуем, аттрибуты
#         print("Создание нового объекта", name)
#         return super(MyMetaclass, mcs).__new__(mcs, name, bases, attr)
#
#     def __init__(cls, name, bases, attr):  # первым параметром cls
#         print("Инициализация класса", name)
#         super(MyMetaclass, cls).__init__(name, bases, attr)
#
#
# class Student(metaclass=MyMetaclass):
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# stud = Student("Анна")
# print(stud.get_name())
# print(type(stud))
# print(type(Student))


# ================================================================== 01.02.2022 =============

# ============================================== СОЗДАНИЕ МОДУЛЕЙ =====================================

# import math
#
# print(math.pi)
#
# from math import pi
#
# print(pi)

# import rect, sq, trian  # не желательно разные модули импортировать в одной строке ( но можно )
# import пакет.модуль  # вид записи = r1 = geometry.rect.Rectangle(1, 2)
# import geometry.rect
# import geometry.sq
# import geometry.trian

# from geometry import rect, sq, trian  # вид записи r1 = rect.Rectangle(1, 2)


# from geometry import *  # для такого импорта прописываем список имен модулей в файл __init__


# r1 = rect.Rectangle(1, 2)
# r2 = rect.Rectangle(3, 4)
# # print(r1)
#
# s1 = sq.Square(10)
# s2 = sq.Square(20)
#
# t1 = trian.Triangle(1, 2, 3)
# t2 = trian.Triangle(4, 5, 6)
#
# shape = [r1, r2, s1, s2, t1, t2]
#
# for g in shape:
#     print(g.get_perimetr())


# if __name__ == __main__:
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#     # print(r1)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())


# def main():
#     r1 = rect.Rectangle(1, 2)
#     r2 = rect.Rectangle(3, 4)
#     # print(r1)
#
#     s1 = sq.Square(10)
#     s2 = sq.Square(20)
#
#     t1 = trian.Triangle(1, 2, 3)
#     t2 = trian.Triangle(4, 5, 6)
#
#     shape = [r1, r2, s1, s2, t1, t2]
#
#     for g in shape:
#         print(g.get_perimetr())
#
#
# if __name__ == '__main__':
#     main()


# from car import carclass, electrocar
#
#
# class Person:
#     def show(self):
#         print('Hello')
#
#
# def main():
#     e = electrocar.Electrocar("Tesla", "T", 2018, 99000)
#     e.show_car()
#     e.description_battery()
#
#
# if __name__ == '__main__':
#     main()


# ==================================== 03.02.22 ======= УПАКОВКА ДАННЫХ ===================
# Сериализация (кодирование) - запись данных  на диск
# Десериализация (декодирование) - это чтение данных

# Стандартной библиотеке Python:
# - marshal = для поддержки старых форматов файлов питон
# - pickle
#    # dump()- метод для сохранения данных в файл (нечитабельные)
#    # load()- считывает данные из файла
#    # dumps()- сохраняет данные в оперативную память
#    # loads()- считывает данные из оперативной памяти
# - json


import pickle

# filename = 'basket.txt'
#
# shop_list = {
#     'фрукты': ["яблоки", "манго"],
#     'овощи': ["морковь"],
#     'бюджет': 1000
# }
#
# with open(filename, 'wb') as fh:
#     pickle.dump(shop_list, fh)  # 1) что записываем в файл, 2) в какой файл (имя)
#
# with open(filename, 'rb') as fh:
#     print(pickle.load(fh))


# class Test:
#     a_number = 35
#     a_string = 'привет'
#     a_list = [1, 2, 3]
#     a_tuple = (22, 23)
#     a_dict = {"first": "a", "second": 2, "third": [1, 2, 3]}
#
#     def __str__(self):
#         return f"Число: {Test.a_number}\nСтрока: {Test.a_string}\n" \
#                f"Список: {Test.a_list}\nКортеж: {Test.a_tuple}\nСловарь: {Test.a_dict}"
#
#
# obj = Test()
# my_obj = pickle.dumps(obj)
# print(f"Сериализация в строку:\n{my_obj}\n")
#
# l_obj = pickle.loads(my_obj)
# print(f"Десериализация в строку:\n{l_obj}\n")


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __getstate__(self):  # Переопределяет
#         attr = self.__dict__.copy()  # копируем все данные self в переменную
#         print(attr)
#         del attr['c']  # даляем по индексу переменную
#         print(attr)
#         return attr
#
#     def __setstate__(self, state):  # state-
#         self.__dict__ = state
#         self.c = lambda x: x * x
#         # print(self.__dict__)
#         # print(state)
#
#     def __str__(self):
#         return f"{self.a} {self.b} {self.c(2)}"  # self.c(2) передаем в значение x lambda
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# # print(item3.__dict__)
# print(item3)


# ==========================

# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename, encoding='utf-8')
#         self.count = 0
#
#     def red_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith("\n"):  # endswith - если строка заканчивается - (указать)
#             line = line[:-1]
#         return f"{self.count}: {line}"
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)  # update обновить данные
#         file = open(self.filename, encoding='utf-8')
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
# reader = TextReader("hello.txt")
# print(reader.red_line())
# print(reader.red_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.red_line())


# =========================== JSON

# import json

# data = {
#     "firstName": "Jane",
#     "lastName": "Djo",
#     "hobbies": ("running", "sky diving"),
#     "age": 5,
#     20: "one"
# }
#
# # with open("data_file.json", 'w') as fw:
# #     json.dump(data, fw)
#
# # with open("data_file.json", 'w') as fw:
# #     json.dump(data, fw, indent=4)  # indent сдвигает на 4 таббуляции ( форматирование данных )
# #
# # with open("data_file.json", 'r') as fw:
# #     print(json.load(fw))
#
# st = json.dumps(data)  # сохраняем в память
# data = json.loads(st)
# print(data)

# ===================


# x = {
#     "name": "Виктор"
# }
# y = {
#     "name": "Виктор"
# }
#
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))  # ensure_ascii = правит кодировку


# ===================

# ================================================= ГЕНЕРАТОР СПИСКОВ =====

# import json
# from random import choice
#
#
# def gen_persom():
#     name = ''
#     tel = ''
#
#     letters = ['a', "b", 'b', 'd', 'e', 'f', 'e', 'g']
#     num = ['1', "2", '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)  # choice = берет случайным индекс из списка
#     # print(name)
#
#     while len(tel) != 7:
#         tel += choice(num)  # choice = берет случайным индекс из списка
#     # print(tel)
#
#     person = {
#         'name': name,
#         "tel": tel
#     }
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open('person.json'))  # если у нас нет файла то except,
#         # data сохраняет данные, и добавляет новые при след запуске
#     except FileNotFoundError:
#         data = []
#
#     data.append(person_dict)  # в пустой список мы добавляем данные из gen_person
#     with open('person.json', 'w') as f:  # открываем файл
#         json.dump(data, f, indent=2)  # добавляем данные
#
#
# # gen_persom()
# # print(gen_persom())
# # for i in range(5):
# #     print(gen_persom())
#
# # persons = []
#
# # for i in range(5):  # группируем словари в список
# #     persons.append(gen_persom())
# # print(persons)
#
# # with open('person.json', 'w') as f:
# #     json.dump(persons, f, indent=2)
#
# for i in range(5):
#     write_json(gen_persom())


# =============================================================== 08.02.22 =============================
# Задача с студентами и оценками
# import json
#
#
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#
#     def __str__(self):
#         a = ''
#         for i in self.marks:  # преобразуем список в строку ( числа + пробел с , )
#             a += str(i) + ', '
#         return f"Студент {self.name}: {a[:-2]}"
#
#     def add_mark(self, mark):  # добавляем оценки
#         self.marks.append(mark)
#
#     def delete_mark(self, index):  # удаляем оценки
#         self.marks.pop(index)
#
#     def edit_mark(self, index, new_mark):  # изменяем оценку
#         self.marks[index] = new_mark
#
#     def average_mark(self):  # выводим среднее арифметическое
#         return round(sum(self.marks) / len(self.marks), 2)
#
#     @classmethod  # записываем данные в словарь для записи в json файд
#     def dump_to_json(cls, stud, filename):
#         try:
#             data = json.load(open(filename))
#         except FileNotFoundError:
#             data = []
#
#         data.append({'name': stud.name, 'marks': stud.marks})
#         with open(filename, 'w') as f:
#             json.dump(data, f, indent=2)
#
#     @classmethod  # метод загрузки json файла
#     def load_from_file(cls, filename):
#         with open(filename, 'r') as f:
#             print(json.load(f))
#
#
# class Group:
#     def __init__(self, student, group):
#         self.student = student
#         self.group = group
#
#     def __str__(self):
#         a = ''
#         for i in self.student:
#             a += str(i) + "\n"
#         return f"Группа: {self.group}\n{a}"
#
#     def add_student(self, student):
#         self.student.append(student)
#
#     def remove_student(self, index):
#         return self.student.pop(index)
#
#     @classmethod
#     def change_group(cls, group1, group2, index):  # удаляем студента из одной группы и переводим в другую.
#         return group2.add_student(group1.remove_student(index))  # добавляем того студента что удалили
#
#     @classmethod
#     def dump_group(cls, file, group):
#         try:
#             data = json.load(open(file))
#         except FileNotFoundError:
#             data = []
#
#         with open(file, 'w') as f:
#             stud_list = []
#             for i in group.student:
#                 stud_list.append([i.name, i.marks])
#             tmp = {'Student': stud_list}
#             data.append(tmp['Student'])
#             json.dump(data, f, indent=2)
#
#     @classmethod
#     def upload_joinal(cls, file):
#         with open(file, 'r') as f:
#             print(json.load(f))
#
#
# st1 = Student('Bodny', [5, 4, 3, 4, 5, 3])
# st2 = Student('Nikolaenko', [2, 3, 5, 4, 2])
# st3 = Student('Birukov', [3, 5, 3, 2, 5, 4])
#
# # Student.dump_to_json(st1, 'student.json')
# Student.dump_to_json(st2, 'student.json')
# Student.load_from_file('student.json')
#
# sts = [st1, st2]
# my_group = Group(sts, 'ГК Python')
# print(my_group)
#
# # Group.dump_group('group.json', my_group)  # Вызов записи группы
#
# my_group.add_student(st3)
# print(my_group)
# my_group.remove_student(1)
# print(my_group)
#
# group22 = [st2]
# my_group2 = Group(group22, "ГК Web")
# Group.change_group(my_group, my_group2, 0)
# print(my_group)
# print(my_group2)
# # Group.dump_group('group.json', my_group2)  # Вызов записи группы
#
# Group.upload_joinal('group.json')
#
# # # делалось первым
# # print(st1)
# # st1.add_mark(4)
# # print(st1)
# # st1.delete_mark(3)
# # print(st1)
# # st1.edit_mark(2, 15)
# # print(st1)
# # print(st1.average_mark())


# ================================ Модуль Request =========================== ++++++
# pip install requests
# python -m pip install --upgrade pip  # обновить среду разработки

import requests
import json

# response = requests.get('https://jsonplaceholder.typicode.com/todos')  # получили доступ
# todos = json.loads(response.text)  # записали в переменную
#
# todos_by_user = {}
#
# for todo in todos:
#     if todo['completed']:  # по свойству 'completed' делаем проверку на TRue и False
#         try:
#             todos_by_user[todo['userId']] += 1
#         except KeyError:
#             todos_by_user[todo['userId']] = 1
#
# print(todos_by_user)
#
# top_users = sorted(todos_by_user.items(), key=lambda x: x[1],
#                    reverse=True)  # сортируем словари по значению и кладем в кортеж
# print(top_users)
#
# max_complite = top_users[0][1]  # находим максимальный результат по индексам
# print(max_complite)
#
# users = []
# for user, num_complite in top_users:  # получаем id  с высокими оценками
#     if num_complite < max_complite:
#         break
#     users.append(str(user))
#
# max_users = " and ".join(users)
#
# s = 's' if len(users) > 1 else ""
#
# print(f"user {max_users} completed {max_complite} TODOS")
#
#
# def keep(todo):
#     is_completed = todo['completed']
#     has_max_count = str(todo["userId"]) in users
#     return is_completed and has_max_count
#
#
# with open('data.json', 'w') as f:
#     td = list(filter(keep, todos))
#     json.dump(td, f, indent=2)
#
# with open('data.json', 'r') as f:
#     print(json.load(f))


# ==================================================== CSV (comma separated values)
# csv.reader # чтение
# csv.writer # запись
import csv

# =============================================== reader

# with open('data.csv') as f:
#     reader = csv.reader(f, delimiter=';')
#     count = 0
#     for row in reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         else:
#             print(f"\t{row[0]} - {row[1]}. Родился в {row[2]} году.")
#         count += 1
#     print(f"Всего в файле {count} строки.")


# ======================================================= DictReader

# with open('data.csv') as f:
#     field_name = ["Имя", "Профессия", "Год рождения"]
#     reader = csv.DictReader(f, fieldnames=field_name)  # delimiter=';'
#     count = 0
#     for row in reader:
#         if count == 0:
#             print(f"Файл содержит столбцы: {', '.join(row)}")
#         print(f"\t{row['Имя']} - {row['Профессия']}. ", end='')
#         print(f"Родился в {row['Год рождения']} году. ")
#         count += 1
#     print(f"Всего в файле {count} строки.")


# -====================================================== Записываем в файл CSV

# with open("student.csv", mode='w') as f:
#     writer = csv.writer(f, delimiter=",", lineterminator="\r")
#     writer.writerow(["Имя", "Класс", "Возраст"])
#     writer.writerow(["Женя", "9", "15"])
#     writer.writerow(["Саша", "5", "12"])
#     writer.writerow(["Маша", "11", "18"])

# ============================= writer из списка

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("sw_data.csv", 'w') as f:
#     writer = csv.writer(f, lineterminator="\r")
#     for row in data:
#         writer.writerow(row)
#
#
# with open("sw_data.csv") as f:
#     print(f.read())
#
# ============================ writer quoting=csv.QUOTE_NONNUMERIC

# data = [['hostname', 'vendor', 'model', 'location'],
#         ['sw1', 'Cisco', '3750', 'London, Best str'],
#         ['sw2', 'Cisco', '3850', 'Liverpool, Better str'],
#         ['sw3', 'Cisco', '3650', 'Liverpool, Better str'],
#         ['sw4', 'Cisco', '3650', 'London, Best str']]
#
# with open("sw_data.csv", 'w') as f:
#     writer = csv.writer(f, lineterminator="\r", quoting=csv.QUOTE_NONNUMERIC)
#     for row in data:
#         writer.writerow(row)
#
#
# with open("sw_data.csv") as f:
#     print(f.read())


# ============================================== DictWriter

# with open("student1.csv", mode='w') as f:
#     names = ["Имя", "Возраст"]
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=names)  # если не работает через "," - то delimiter=";"
#     writer.writeheader()
#     writer.writerow({"Имя": "Саша", "Возраст": "6"})
#     writer.writerow({"Имя": "Маша", "Возраст": "15"})
#     writer.writerow({"Имя": "Вова", "Возраст": "14"})


# ==================================================

# data = [{
#     'hostname': 'sw1',
#     'location': 'London',
#     'model': '3750',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw2',
#     'location': 'Liverpool',
#     'model': '3850',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw3',
#     'location': 'Liverpool',
#     'model': '3650',
#     'vendor': 'Cisco'
# }, {
#     'hostname': 'sw4',
#     'location': 'London',
#     'model': '3650',
#     'vendor': 'Cisco'
# }]
#
# with open('dict.csv', 'w') as f:
#     writer = csv.DictWriter(f, delimiter=";", fieldnames=list(data[0].keys()))
#     writer.writeheader()
#     for d in data:
#         writer.writerow(d)


# ================================================================== 15.02.2022 ===================
# плагин pip install beautifulsoup4 или pip install bs4

# from bs4 import BeautifulSoup

# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")  # позволяет извлекать данные из html

# ПОИСК ДАННЫХ В HTML
# row = soup.find("div", class_="name")  # ищем div с классом "name" (class_) с подчерком,
# # find возвращает первый найденный элемент
# row = soup.find_all("div", class_="name")  # find_all возвращает все найденные элементы
# row = soup.find_all("div", class_="row")[1].find("div", class_="links")  # цепочка доступа к элементу
# row = soup.find_all("div", {"data-set": "salary"})  # другой способ доступа ( для данных с дифисом типа data-set)
# print(row)

# alena = soup.find("div", text='Alena').parent  # поиск по тексту, .parent - выводит родительский элемент,
# # .parent.parent (родитель родителя)
# alena = soup.find("div", text='Alena').find_parent(class_="row")  # поиск конкретного родителя по имени класса
# print(alena)

# row = soup.find("div", id="whois3")
# row = soup.find("div", id="whois3").find_next_sibling()  # найти следующий элемент от дизайнера
# row = soup.find("div", id="whois3").find_previous_sibling()  # найти предыдущий элемент от дизайнера
#
# print(row)

# ======================================================================================***

# def get_copywriter(tag):
#     whois = tag.find('div', class_="whois")
#     if "Copywriter" in whois:
#         return tag
#     return None
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")  # позволяет извлекать данные из html
# copywriter = []
# row = soup.find_all("div", class_="row")
# for i in row:
#     CW = get_copywriter(i)
#     if CW:
#         copywriter.append(CW)
# print(row)

# ===============================================================================*****


# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find("div", {"data-set": "salary"}).text  # получаем весь текст (только для первого найденого (find))
# print(row)
# row = soup.find_all("div", {"data-set": "salary"})  # для всех элементов получаем весь текст (find_all) через фор
# for i in row:
#     print(i.text)
#
# ===================
# ==== Поиск всех чисел в данных элементах через рег. выражение

# def get_salary(s):
#     pattern = r"\d+"
#     """1 вариант без скобок"""
#     # res = re.findall(pattern, s)[0]  # через [0] индекс уходим от скобок списка
#     """2 вариант без скобок"""
#     res = re.search(pattern, s).group()
#     print(res)
#
#
# f = open('index.html', encoding="utf-8").read()
# soup = BeautifulSoup(f, "html.parser")
# row = soup.find_all("div", {"data-set": "salary"})
# for i in row:
#     get_salary(i.text)


# ========================================================================

# import requests
#
# r = requests.get('https://ru.wordpress.org/')
# # print(r.status_code)  # возвращает код состояния(ответ тела сервера)
# # print(r.headers)  # вывод заголовков сайта
# # print(r.headers['content-type'])  # вывод конкретной инфы из header
#
# # print(r.content)
# print(r.text)  # получаем html разметку


# import requests

# # Получаем данные с сайта WordPress
#
# def get_html(url):
#     r = requests.get(url)  # получаем доступ к данным
#     return r.text
#
#
# def get_data(html):
#     # soup = BeautifulSoup(html, "html.parser")  # встроенный парсер питона "html.parser"
#     soup = BeautifulSoup(html, "lxml")  # другой парсер
#     p1 = soup.find("header", id="masthead").find("p", class_="site-title").text
#     return p1
#
#
# def main():
#     url = 'https://ru.wordpress.org/'
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()


# ========================================================

# Получаем данные с сайта WordPress
# import csv

#
# def get_html(url):
#     r = requests.get(url)  # получаем доступ к данным
#     return r.text
#
#
# def refined(s):
#     """чистит от слов и лишних символов"""
#     res = re.sub(r"\s+", "", s)  # sub - метод поиска и замены ( \D все что угодно кроме цифр)
#     return res
#
#
# def write_csv(data):
#     with open('plugins.csv', 'a') as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['rating']))  # в виде кортежа
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")  # другой парсер
#     s = soup.findAll("section", class_="plugin-section")[1]
#     plugins = s.find_all('article')
#
#     for plugin in plugins:
#         name = plugin.find("h3").text  # получаем заголовки
#         url = plugin.find("h3").find("a").get("href")  # получаем ссылки, .get("href")-получить данные из атрибута href
#         rating = plugin.find("span", class_="rating-count").find("a").text  # получаем рейтинг
#         r = refined(rating)  # ФУНКЦИЯ
#
#         data = {'name': name, "url": url, "rating": r}
#         write_csv(data)
#         # print(url)
#         # print(name)
#         # print(r)
#         # print(data)
#     # return len(plugins)
#
#
# def main():
#     url = 'https://ru.wordpress.org/plugins/'
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()


# ==============================


# ============================= DZ-Stas

# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# # def write_csv(data):
# #     with open('plugins111.csv', 'w', encoding='utf-8') as f:
# #         writer = csv.writer(f, lineterminator='\r')
# #         writer.writerow(data)  # ((data['name'], data['url'], data['rating']))
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     # p1 = soup.find("div class", id="col-md-6 col-lg-4 col-xl-3").find("div class", class_="categories-banner-name-div").text
#     p1 = soup.find("div", class_="row no-gutters")
#     for i in p1:
#         print(i.text)
#     print(p1)
#
#
# def main():
#     url = "https://www.4pc.by/"
#     print(get_data(get_html(url)))
#
#
# if __name__ == '__main__':
#     main()

# ========================================================== DZ-Stas


# ============================================ ***************************************** 17.02.22

import requests
import csv
from bs4 import BeautifulSoup

# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open("plugins1.csv", 'a', encoding='utf-8') as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow((data['name'], data['url'], data['snippet'], data['active'], data['cy']))
#
#
# def refind_cy(s):  # Возвращаем только числа с точками
#     return s.split(" ")[-1]  # split() возварщает список сфомированный по пробелам, [-1] = возвращаем последний элемент
#
#
# def get_page_data(html):
#     soup = BeautifulSoup(html, 'lxml')
#     element = soup.find_all("article", class_="plugin-card")
#     for el in element:
#         try:
#             name = el.find("h3").text
#         except ValueError:
#             name = ""
#         try:
#             url = el.find("h3").find('a').get('href')
#         except ValueError:
#             url = ""
#         try:
#             snippet = el.find('div', class_="entry-excerpt").text.strip()  # .strip() Убирает пробелы
#         except ValueError:
#             snippet = ""
#         try:
#             active = el.find("span", class_="active-installs").text.strip()
#         except ValueError:
#             active = ""
#         try:
#             c = el.find('span', class_="tested-with").text.strip()
#             cy = refind_cy(c)  # Возвращаем только числа с точками ( вызов функции )
#         except ValueError:
#             cy = ""
#
#         data = {
#             'name': name,
#             'url': url,
#             'snippet': snippet,
#             'active': active,
#             'cy': cy
#         }
#         write_csv(data)
#
#
# def main():
#     for i in range(1, 22):
#         url = f"https://ru.wordpress.org/plugins/browse/blocks/page/{i}/"  # запускаем 4 страницы
#         get_page_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

# ================================================================

from parse import Parser


def main():
    pars = Parser('https://www.ixbt.com/live/index/type/news/', 'new.txt')
    pars.run()


if __name__ == '__main__':
    main()
