# DZ_1

class Person:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    def __repr__(self):
        return repr((self.surname, self.name, self.age))


class SortKey:
    def __call__(self, pers, *args):
        self.pers = pers
        if len(args) == 1 and args[0] == 'surname':
            my_list = sorted(self.pers, key=lambda person: person.surname)
            for i in my_list:
                print(i)
        # if len(args) == 2 and args[0] == 'surname' and args[1] == 'name':
        #     print(sorted(g, key=lambda person: person.surname))


p = [Person('Иванов', 'Игорь', 28),
     Person('Петров', 'Степан', 21),
     Person('Сидоров', 'Антон', 25),
     Person('Петров', 'Анатолий', 28),
     Person('Иванов', 'Иван', 28)]

call = SortKey()
call(p, 'surname')

# Вообщем не победил второе условие задачи, мозг сломан )


