import math


class Circle:
    def __init__(self, r):
        self.r = r

    def l(self):
        return round(self.r * math.pi, 2) * 2

    def get_circle_square(self):
        return round(math.pi * (self.r ** 2), 2)

    def print_circle(self):
        print(f"Радиус: {self.r}")

    def print_info(self):
        print(f'Длина окружности: {self.l()}')

    def print_pl(self):
        print(f'Площадь круга: {self.get_circle_square()}')
