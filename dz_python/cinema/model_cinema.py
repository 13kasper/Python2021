class Cinema:
    def __init__(self, name, genre, producer, year, duration, studio, actor):
        self.name = name
        self.genre = genre
        self.producer = producer
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actor = actor

    def __str__(self):
        return f"{self.name}({self.genre})"


class CinemaModel:
    def __init__(self):
        self.films = {}

    def add_cinema(self, dict_article):
        cinema = Cinema(*dict_article.values())
        self.films[cinema.name] = cinema

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, title):
        movie_title = self.films[title]
        dict_films = {
            'Название фильма': movie_title.name,
            'Жанр: ': movie_title.genre,
            'Продюсер: ': movie_title.producer,
            'Год выпуска': movie_title.year,
            'Продолжительность': movie_title.duration,
            'Студия: ': movie_title.studio,
            'В главной роли: ': movie_title.actor
        }
        return dict_films

    def remove_film(self, name):
        return self.films.pop(name)
