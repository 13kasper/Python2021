class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_rect_perimeter(self):
        return round(self.a * 2 + self.b * 2)

    def pl(self):
        return round(self.a * self.b)

    def print_info(self):
        print(f"Периметр : {self.get_rect_perimeter()}")

    def print_rect(self):
        print(f"Стороны: {self.a}, {self.b}")





