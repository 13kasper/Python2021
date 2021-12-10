class Book:
    name = ""
    year = ""
    author = ""
    genre = ""
    publisher = ""
    price = ""

    def print_book(self):
        print("КНИГА".center(40, "="))
        print(f"Название книги: {self.name}\nГод выпуска: {self.year}\nАвтор: {self.author}"
              f"\nЖанр: {self.genre}\nИздатель: {self.publisher}\nЦена: {self.price}")
        print("*" * 40)

    def input_book(self, name, year, author, genre, publisher, price):
        self.name = name
        self.year = year
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.price = price

    def get_name(self, name):
        self.name = name

    def set_name(self):
        return self.name

    def get_year(self, year):
        self.year = year

    def set_year(self):
        return self.year

    def get_author(self, author):
        self.author = author

    def set_author(self):
        return self.author

    def get_genre(self, genre):
        self.genre = genre

    def set_genre(self):
        return self.genre

    def get_publisher(self, publisher):
        self.publisher = publisher

    def set_publisher(self):
        return self.publisher

    def get_price(self, price):
        self.price = price

    def set_price(self):
        return self.price


price1 = "400$"
book1 = Book()
book1.print_book()
print()
book1.input_book("Мальчик в сандалях", "1899", "Сугубо тот", "Драма", "ОАВ", price1)
book1.print_book()
print()
book1.get_name("Мальчик без сандаль")
book1.print_book()
print(book1.set_name())
book1.get_genre("Комедия")
book1.print_book()
print(book1.set_genre())
