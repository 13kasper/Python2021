from abc import ABC, abstractmethod
import math


class Shape(ABC):

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def painting(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


class Square(Shape):
    def __init__(self, x=0, y=0, color='red'):
        self.x = x
        self.y = y
        self.color = color

    def perimeter(self):
        return 2 * (self.x + self.y)

    def square(self):
        return self.x * self.y

    def painting(self):
        for pain in range(self.x, 0, -1):
            print(self.y * '*')

    def print_info(self):
        print(f"Сторона: {self.x}\nЦвет: {self.color}\nПлощадь: {self.square()}\nПериметр: {self.perimeter()}")


class Rectangle(Shape):
    def __init__(self, x=0, y=0, color='red'):
        self.x = x
        self.y = y
        self.color = color

    def perimeter(self):
        return 2 * (self.x + self.y)

    def square(self):
        return self.x * self.y

    def painting(self):
        for pain in range(self.x, 0, -1):
            print(self.y * '*')

    def print_info(self):
        print(
            f"Сторона: {self.x}\nШирина: {self.y}\nЦвет: {self.color}\nПлощадь: {self.square()}\nПериметр: {self.perimeter()}")


class Triangle(Shape):
    def __init__(self, x=0, y=0, z=0, color='red'):
        self.x = x
        self.y = y
        self.z = z
        self.color = color

    def perimeter(self):
        return (self.z + self.y + self.x) / 2

    def square(self):
        d = self.perimeter()
        return round(math.sqrt(d * (d - self.x) * (d - self.y) * (d - self.z)), 2)

    def painting(self):
        for pain in range(0, self.y+1):
            print(' ' * (self.y - pain), '* ' * pain)

        # print('\n'.join([f"{' ' * (self.y - x - 1)}{'*' * (2 * x + 1)}" for x in range(0, self.y)]))

    def print_info(self):
        print(
            f"Сторона 1: {self.x}\nСторона 2: {self.y}\nСторона 3: {self.z}\nЦвет: {self.color}\nПлощадь: {self.square()}\nПериметр: {self.perimeter()}")


var = Square(3, 3)
var1 = Rectangle(3, 7, "green")
var2 = Triangle(11, 6, 6, "yellow")

for i in (var, var1, var2):
    i.perimeter()
    i.square()
    i.print_info()
    i.painting()
    print()