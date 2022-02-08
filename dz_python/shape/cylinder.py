# import circle
# import rectangle
# import math
#
#
# class Cylinder(circle.Circle, rectangle.Rectangle):
#     def __init__(self, r, v):
#         self.r = r
#         self.v = v
#
#     def get_volume(self):
#         return round(math.pi * (self.r ** 2) * self.v, 2)
#
#     def print_info(self):
#         print(f'Площадь круга: {self.get_circle_square()}')
#         print(f"Объем: {self.get_volume()}")





# from shapes import rectangle
# from shapes import circle
#
#
# class Cylinder(rectangle.Rectangle, circle.Circle):
#
#     def __init__(self, r, h):
#         circle.Circle.__init__(self, r)
#         rectangle.Rectangle.__init__(self, self.get_circle_circumference(), h)
#
#     def get_volume(self):
#         res = self.get_circle_square() * self.h
#         print(f"Объём: {round(res, 2)}")
#         return res
#
#     def print_cylinder(self):
#         print(f"Основание: {self.r}, высота: {self.h}")