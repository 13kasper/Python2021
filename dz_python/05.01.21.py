# DZ-05.01.21
import math


class Pair:
    gip = 0

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def set_a(self, a):
        self.a = a

    def set_b(self, b):
        self.b = b

    def get_sum(self):
        return f"Сумма: {self.a + self.b}"

    def get_proiz(self):
        return f"Произведение: {self.a * self.b}"


class Right_triangle(Pair):

    def __init__(self, a, b):
        super().__init__(a, b)

    def get_gip(self):
        gip = ((self.a ** 2) + (self.b ** 2)) ** 0.5
        return round(gip, 2)

    def get_pr(self):
        return self.a, self.b, self.get_gip()

    def get_pl(self):
        return (self.a * self.b) * 0.5


alt = Right_triangle(5, 8)

print(f"Гипотенуза АВС: {alt.get_gip()}")
print(f"Прямоугольный треугольник АВС: {alt.get_pr()}")
print(f"Площадь АВС: {alt.get_pl()}")
print()
print(alt.get_sum())
print(alt.get_proiz())

print()
alt.set_a(10)
alt.set_b(8)
print(f"Гипотенуза АВС: {alt.get_gip()}")
alt.set_a(10)
alt.set_b(20)
print(f"Гипотенуза АВС: {alt.get_gip()}")
print(alt.get_sum())
print(alt.get_proiz())
print(f"Площадь АВС: {alt.get_pl()}")