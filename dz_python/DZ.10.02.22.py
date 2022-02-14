import json

sl = {}


class St:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def __str__(self):
        return f"{self.dictionary}"

    def add_dict(self):
        key = input('Введите страну: ')
        value = str(input('Введите столицу: '))
        self.dictionary[key] = value
        return self.dictionary

    def del_dict(self):
        key = str(input("Какую страну удалить? :"))
        del self.dictionary[key]
        return self.dictionary

    def seach_dict(self):
        key = input("Введите название страны: ")
        if key in self.dictionary:
            print(f"В стране {key} столица: {self.dictionary[key]}")
        else:
            print("Такой страны нет в словаре")

    def edit_dict(self):
        key = input("В какой стране изменить столицу?: ")
        if key in self.dictionary:
            value = input("Введите новую столицу: ")
            self.dictionary[key] = value
        else:
            print("Такой страны нет")

    def write_dictionary(self, x):
        try:
            data = json.load(open('dictionary.json'))
        except FileNotFoundError:
            data = {}

        data.update(self.dictionary)
        with open('dictionary.json', 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=5)

    def load_dictionary(self):
        with open('dictionary.json', 'r', encoding='utf-8') as f:
            print(json.load(f))

    def print_info(self):
        print(self.dictionary)


sl1 = St(sl)

print()
while True:
    option = input(
        "Выбирете действие:\n1 - Добавление данных\n2 - Удаление данных\n3 - Поиск данных"
        "\n4 - Редактирование данных\n5 - Сохранение данных\n6 - Просмотр данных\n\nВведите номер:  ")
    print()
    if option == "1":
        sl1.add_dict()
        print()
        sl1.print_info()
        print()
    elif option == "2":
        sl1.del_dict()
        print()
        sl1.print_info()
        print()
    elif option == "3":
        sl1.seach_dict()
        print()
    elif option == '4':
        sl1.edit_dict()
        print()
        sl1.print_info()
        print()
    elif option == '5':
        sl1.write_dictionary(sl1)
        print()
    elif option == '6':
        sl1.load_dictionary()
        print()
    else:
        break
