# DZ-22.01.22

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
#     def __gt__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return self.__x > other.x and self.__y > other.y and self.__y > other.y
#
#     def __ge__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return self.__x >= other.x and self.__y >= other.y and self.__y >= other.y
#
#     def __lt__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return self.__x < other.x and self.__y < other.y and self.__y < other.y
#
#     def __le__(self, other):
#         if not isinstance(other, Point3D):
#             raise ValueError(self.RIGHT)
#         else:
#             return self.__x <= other.x and self.__y <= other.y and self.__y <= other.y
#
#
# pt = Point3D(6, 3, 9)
# pt2 = Point3D(6, 3, 9)
# print(f"Координаты 1-й точки {pt}")
# print(f"Координаты 2-й точки {pt2}")
#
# pt3 = pt > pt2
# print(f"pt больше pt2 ? : {pt3}")
#
# pt4 = pt >= pt2
# print(f"pt больше или равно pt2 ? : {pt4}")
#
# pt5 = pt < pt2
# print(f"pt меньше pt2 ? : {pt5}")
#
# pt6 = pt <= pt2
# print(f"pt меньше или равно pt2 ? : {pt6}")
