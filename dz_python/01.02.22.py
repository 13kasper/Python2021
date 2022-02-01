
class Desc:
    def __set_name__(self, owner, name):  #
        self.__name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError("Значение должно быть целочисленным")
        instance.__dict__[self.__name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]


class Point3D:
    x = Desc()
    y = Desc()
    z = Desc()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def back(self):
        d = dict([('_x', self.x), ('_y', self.y), ('_z', self.z)])
        return d


p = Point3D(1, 2, 3)
print(p.back())
p.x = 5
print(p.back())
p.x = 5.2

