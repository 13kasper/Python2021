# DZ_1
# class Person:
#     sort2 = []
#
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#         Person.sort2.append(self)
#
#     def __str__(self):
#         return "{} {} {}".format(self.surname, self.name, self.age)
#
#     def print(self, a, b, c):
#         print(f"{self.surname} {self.name} {self.age}")
#
# class Stat(Person):
#
#     def __call__(self, *args, **kwargs):
#         return type.__call__(*args, **kwargs)
#
#
# p = [Person('Иванов', 'Игорь', 28), Person('Петров', 'Степан', 28),
#      Person('Сидоров', 'Антон', 28), Person('Петров', 'Анатолий', 28),
#      Person('Иванов', 'Иван', 28)]
#
# # for i in Person.sort2:
# #     print(i)


# ======================

# class Person:
#
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def __repr__(self):
#         return repr((self.surname, self.name, self.age))
#
#
# p = [Person('Иванов', 'Игорь', 21), Person('Петров', 'Степан', 28),
#      Person('Сидоров', 'Антон', 23), Person('Петров', 'Анатолий', 26),
#      Person('Иванов', 'Иван', 33)]
#
# print(sorted(p, key=lambda person: person.name))

#
class Person:

    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def __repr__(self):
        return repr((self.surname, self.name, self.age))


class SortKey:
    def __call__(self, pers, arg, name=None):
        self.pers = pers
        self.name = name
        self.arg = arg
        g = list(pers)
        if arg == 'surname':
            print(sorted(g, key=lambda person: person.surname))


p = [Person('Иванов', 'Игорь', 28), Person('Петров', 'Степан', 21),
     Person('Сидоров', 'Антон', 25), Person('Петров', 'Анатолий', 11),
     Person('Иванов', 'Иван', 28)]

call = SortKey()
call(p, 'surname')





# class Person:
#     def __init__(self, surname, forename, old):
#         self.surname = surname
#         self.forename = forename
#         self.old = old
#
#
# class SortKey:
#     """Класс функтор который по заданным ключам производит сортировку переданного списка экземпляров классов,
#     переданный список должен состоять из однотипных элементов. не допускается списки типа [class Person, class Date],
#     так же не поддерживаются стандартные типы данных пример [{1:1}, {2:3}]
#     В качестве ключей сортировки используется имена атрибутов класса """
#
#     def __init__(self, *args):
#         self.__sortKey = args  # ключевые поля по которым будет проводится сортировка
#
#     def __call__(self, lst):
#         # Если в параметрах передается пустой список то мы возвращаем пустой список
#         if not lst:
#             return lst
#         # Если хоть один переданный ключ не соответствует атрибутам элементов списка инициализируем исключение и
#         # сообщаем об ошибке и возможных атрибутах, в test скидываются ошибочные ключи
#         test = [key for key in self.__sortKey if key not in lst[0].__dict__.keys()]
#         if test:
#             raise KeyError(f"ОШИБКА {tuple(test)} таких ключей нет, в данном списке "
#                            f"имеются следующие ключи {tuple(lst[0].__dict__.keys())}")
# # А это собственно решение, одна строчка
#         return sorted(lst, key=lambda item: [item.__dict__[key] for key in self.__sortKey])
#
#
# # Проверка
#
# persons_list = [Person("Фуфел", "БИван", 26),
#                 Person("Артемкин", "БНиколай", 21),
#                 Person("Артемкин", "Алексей", 25), ]
#
# mySort = SortKey("old")
#
# print("Выводим persons_list ДО сортировки")
# [print(index, tuple(item.__dict__.values())) for index, item in enumerate(persons_list, 1)]
# persons_list = mySort(persons_list)
# print("Выводим persons_list ПОСЛЕ сортировки")
# [print(index, tuple(item.__dict__.values())) for index, item in enumerate(persons_list, 1)]

# А вот собственно мой кошмар
# # создаем список в который распаковываем атрибуты (Persons)
#  temp = [item._dict_ for item in lst]
#        # сортируем в соответствии с переданными ключами (полями)
#
#         temp = sorted(temp, key=lambda element: [element[key] for key in self.__sortKey if key in element.keys()])
#         # Возвращаем отсортированный список, предварительно обратно упаковываем в тод же класс
#         # 1 параметр Имя будущего класса
#         # 2 Классы от которых новый клас наследуется пример: tuple(Persons, Test1)
#         # 3 Список аргументов (Dict)
#         return [type(lst[index].__class__.__name__, (lst[index].__class__.__bases__), lst[index].__dict__) for
#                 index, item in enumerate(temp)]
