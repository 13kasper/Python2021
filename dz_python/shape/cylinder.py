import circle
import rectangle
import math


class Cylinder(circle.Circle, rectangle.Rectangle):
    def __init__(self, r, v):
        self.r = r
        self.v = v

    def get_volume(self):
        return round(math.pi * (self.r ** 2) * self.v, 2)

    def print_info(self):
        print(f'Площадь круга: {self.get_circle_square()}')
        print(f"Объем: {self.get_volume()}")


