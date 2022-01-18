# DZ-13.01.22
#  Попытка №2 ) а тут нужен вообще инициализатор ?
#  и по переменной С, есть разница ставить по умолчанию - NONE или - 0
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
# p2 = Quadrate()  # почему подчеркивает ?
# p2.equation(1, 2, 3)


# DZ-17.01.22 =====================================================
# Вариант №1 печать в вложенном классе

# class Student:
#     def __init__(self, name):
#         self.name = name
#
#     class Comp:
#         def __init__(self, model, cpu, ram, r):
#             self.model = model
#             self.cpu = cpu
#             self.ram = ram
#             self.pc1 = r
#
#         def print_info(self):
#             n = self.pc1
#             print(n.name, "=>", self.model, self.cpu, self.ram)
#
#
# pc1 = Student("Иван")
# pc2 = pc1.Comp("HP", "i7", 16, pc1)
# pc2.print_info()

# Вариант №2 =====================================================
# В вложенном классе статичные парметры

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.bd = self.Comp()
#
#     def info(self):
#         f = self.bd.ret()
#         print(f"{self.name} => {str(f)[1:-1]}")
#
#     class Comp:
#         def __init__(self):
#             self.model = "HP"
#             self.cpu = "i7"
#             self.ram = 16
#
#         def ret(self):
#             return self.model, self.cpu, self.ram
#
#
# pc1 = Student("Иван")
# pc1.info()

# Вариант №3 В таком варианте не пойму как правильно передавать данные в вложенный класс
# т.е. если я передаю через экземпляр вложеного класса, то я в Студенте не могу вызвать класс
# ругается что недостаточно аргументов, как правильно передавать и вызывать вложенный класс ?

# class Student:
#     def __init__(self, name, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.name = name
#         self.bd = self.Comp(x, y, z)
#
#     def info(self):
#         f = self.bd.ret()
#         print(f"{self.name} => {str(f)[1:-1]}")
#
#     class Comp:
#         def __init__(self, model, cpu, ram):
#             self.model = model
#             self.cpu = cpu
#             self.ram = ram
#
#         def ret(self):
#             return self.model, self.cpu, self.ram
#
#
# x, y, z = ("HP", "i7", 16)
# pc1 = Student("Иван", x, y, z)
# pc1.info()

# Вариант № 4
# В данном варианте я передаю информацию в классе студент при вызове класса
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.bd = self.Comp("HP", "i7", 16)
#
#     def info(self):
#         f = self.bd.ret()
#         print(f"{self.name} => {str(f)[1:-1]}")
#
#     class Comp:
#         def __init__(self, model, cpu, ram):
#             self.model = model
#             self.cpu = cpu
#             self.ram = ram
#
#         def ret(self):
#             return self.model, self.cpu, self.ram
#
#
# pc1 = Student("Иван")
# pc1.info()

# Также просьба повторить на занятии про _str_ запутался как работает
# ( может ли метод _str_ принимать вызов класа и методов? )
