from model_cinema import CinemaModel
from view_cinema import UserInterface


class Controller:
    def __init__(self):
        self.interface = UserInterface()
        self.model = CinemaModel()

    def run(self):
        reply = None
        while reply != 'q':
            reply = self.interface.reply()
            self.check_user_answer(reply)

    def check_user_answer(self, reply):
        if reply == '1':
            films = self.interface.add_films()
            self.model.add_cinema(films)

        elif reply == '2':
            reply = self.model.get_all_films()
            self.interface.show_all_films(reply)

        elif reply == '3':
            movie_title = self.interface.get_title_film()
            try:
                film = self.model.get_single_film(movie_title)
            except KeyError:
                self.interface.show_incorrect_film_error(movie_title)
            else:
                self.interface.show_single_film(film)

        elif reply == '4':
            remove_name = self.interface.get_title_film()
            try:
                remove = self.model.remove_film(remove_name)
            except KeyError:
                self.interface.show_incorrect_film_error(remove_name)
            else:
                self.interface.remove_film(remove)
