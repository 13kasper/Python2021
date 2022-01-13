# DZ-13.01.22
#  Кажется я не правильно понял дз, но сделал как понял
from abc import ABC, abstractmethod
import math


class Root(ABC):

    @abstractmethod
    def line(self, a, b):
        if a == 0 and b == 0:
            print('Бесконечность')
        elif a != 0 and (b == 0 or a <= b):
            print(f"The root of '3x+7=0' is: {round((-b / a), 2)}")
        else:
            raise TypeError('Корней нет')

    @abstractmethod
    def quad(self, a, b, c):
        d = b ** 2 + 4 * a * c
        if d > 0:
            x1 = (b + math.sqrt(d)) / (2 * a)
            x2 = (b - math.sqrt(d)) / (2 * a)
            print(f"The roots of '1x^2-2x-3=0' are: {x1}, {x2}")
        elif d == 0:
            x = b / (2 * a)
            print(f"Корень = {x}")
        else:
            print("Корней нет")


class Linear(Root):
    def line(self, a, b):
        super().line(a, b)

    def quad(self, a, b, c):
        super().quad(a, b, c)


p1 = Linear()
p1.line(3, 7)
p2 = Linear()
p2.quad(1, 2, 3)

