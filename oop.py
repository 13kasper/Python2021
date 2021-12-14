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


class Point:
    WIDTH = 5

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def __setattr__(self, key, value):
        if key == "WIDTH":
            raise AttributeError
        else:


    def check_val(z):
        if isinstance(z, int) or isinstance(z, float):
            return True
        return False

    def set_coords(self, x, y):
        if Point.check_val(x) and Point.check_val(y):
            self.__x = x
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def set_coords_x(self, x):
        if Point.check_val(x):
            self.__x = x
        else:
            print("Координаты должны быть числами")

    def set_coords_y(self, y):
        if Point.check_val(y):
            self.__y = y
        else:
            print("Координаты должны быть числами")

    def get_coords(self):
        return self.__x, self.__y

    def get_coords_x(self):
        return self.__x

    def get_coords_y(self):
        return self.__y

    def area(self):
        return (self.__x * self.__y) + Point.WIDTH



p1 = Point(5, 10)
p1.WiDTH = 10
print(p1.area())





