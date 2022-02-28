def add_film(x):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {x} ".center(50, '='))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserInterface():
    @add_film('Ввод данных')
    def reply(self):
        print("Действия с фильмом:")
        print("1 - Добавление фильма"
              "\n2 - Каталог фильмов"
              "\n3 - Просмотр определенного фильма"
              "\n4 - Удаление фильма"
              "\nq - выход из программы")
        data_input = input("Выберите вариант действия: ")
        return data_input

    @add_film('Создание фильма:')
    def add_films(self):
        dict_article = {
            "Название": None,
            "Жанр": None,
            "Режисера": None,
            "Год выпуска": None,
            "Длительность": None,
            "Студию": None,
            "Актеры": None
        }
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} фильма: ")
        return dict_article

    def show_all_films(self, films):
        for i, film in enumerate(films, 1):
            print(f"{i}. {film}")

    @add_film('Ввод названия фильма')
    def get_title_film(self):
        title_film = input('Введите название фильма: ')
        return title_film

    def show_single_film(self, name):
        for key in name:
            print(f"{key} фильма - {name[key]}")

    @add_film('Сообщение об ошибке')
    def show_incorrect_film_error(self, film):
        print(f'Фильма с названием {film} не существует')

    @add_film('Удаление фильма: ')
    def remove_film(self, name):
        print(f"Фильм {name} - был удален")
