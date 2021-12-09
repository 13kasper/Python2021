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

class Person:
    skill = 10  # Квалификация сотрудника

    def print_info(self, name, surname):
        self.name = name
        self.surname = surname
        print(f"Данные сотрудника: {self.name} {self.surname}")

    def add_skill(self, k):
        self.skill += k
        print(f"Квалификация сотрудника: {self.name} {self.skill}")



person1 = Person()
person1.print_info("Виктор", "Резник")
person1.add_skill(3)
print()
person2 = Person()
person2.print_info("Анна", "Каренина")




