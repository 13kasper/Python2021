class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def __repr__(self):
        return f'{self.__class__} {self.w} {self.h}'

    def __str__(self):
        return f'{self.w} {self.h}'

    def get_perimetr(self):
        return 2 * (self.w + self.h)


# print(__name__)

__author__ = 'Elena'
if __name__ == '__main__':
    print(f"Module {__name__} (author: {__author__})")
