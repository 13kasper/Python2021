# DZ-1
# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname="user", num="####", percent=0.0, value=0):
#         self.__surname = surname  # фамилия владельца
#         self.__num = num  # номер счета
#         self.__percent = percent  # процент начисления
#         self.__value = value  # сумма в рублях
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был открыт')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт')
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def set_num(self, num):
#         self.__num = num
#
#     def set_percent(self, percent):
#         self.__percent = percent
#
#     def set_value(self, value):
#         self.__value = value
#
#     def get_surname(self):
#         return self.__surname
#
#     def get_num(self):
#         return self.__num
#
#     def get_percent(self):
#         return self.__percent
#
#     def get_value(self):
#         return self.__value
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         """Редактирование курса рубля по отношению к доллару"""
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         """Редактирование курса рубля по отношению к евро"""
#         cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         """Конвертация"""
#         return value * rate
#
#     def convert_to_usd(self):
#         """Перевод в доллары"""
#         usd_val = Account.convert(self.__value, Account.rate_usd)  # статический метод вызывается через имя класса
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         """Перевод в доллары"""
#         eur_val = Account.convert(self.__value, Account.rate_euro)  # статический метод вызывается через имя класса
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def add_persents(self):
#         """начисление процентов"""
#         self.__value += self.__value * self.__percent
#         print("проценты были успешно начислены!!!")
#         self.print_balance()
#
#     def withdraw_money(self, val):  # принимает переменную - сумма которую хотим снять
#         """Снимаем баланс"""
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято")
#         self.print_balance()
#
#     def add_money(self, val):
#         """Добавляем баланс"""
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         """вывод информации о счете"""
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"#{self.__num}\nВладелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")  # .0%  Указываем как отображать %
#         print("-" * 20)
#
#
# acc = Account()
# acc.set_surname("Василий")
# acc.set_num("#12345")
# acc.set_percent(0.03)
# acc.set_value(1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# acc.add_persents()
# print()
# acc.withdraw_money(700)
# print()
#
# acc.add_money(5000)

# # var2
# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname="user", num="####", percent=0.0, value=0):
#         self.__surname = surname  # фамилия владельца
#         self.__num = num  # номер счета
#         self.__percent = percent  # процент начисления
#         self.__value = value  # сумма в рублях
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был открыт')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет #{self.__num} принадлежащий {self.__surname} был закрыт')
#
#     def edit_owner(self, surname):
#         """Меняем владельца"""
#         self.surname = surname
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.__surname = surname
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, num):
#         self.__num = num
#
#     @property
#     def percent(self):
#         return self.__percent
#
#     @percent.setter
#     def percent(self, percent):
#         self.__percent = percent
#
#     @property
#     def value(self):
#         return self.__value
#
#     @value.setter
#     def value(self, value):
#         self.__value = value
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         """Редактирование курса рубля по отношению к доллару"""
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         """Редактирование курса рубля по отношению к евро"""
#         cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         """Конвертация"""
#         return value * rate
#
#     def convert_to_usd(self):
#         """Перевод в доллары"""
#         usd_val = Account.convert(self.__value, Account.rate_usd)  # статический метод вызывается через имя класса
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         """Перевод в доллары"""
#         eur_val = Account.convert(self.__value, Account.rate_euro)  # статический метод вызывается через имя класса
#         print(f'Состояние счета: {eur_val} {Account.suffix_eur}')
#
#     def add_persents(self):
#         """начисление процентов"""
#         self.__value += self.__value * self.__percent
#         print("проценты были успешно начислены!!!")
#         self.print_balance()
#
#     def withdraw_money(self, val):  # принимает переменную - сумма которую хотим снять
#         """Снимаем баланс"""
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято")
#         self.print_balance()
#
#     def add_money(self, val):
#         """Добавляем баланс"""
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено")
#         self.print_balance()
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         """вывод информации о счете"""
#         print("Информация о счете")
#         print("-" * 20)
#         print(f"#{self.__num}\nВладелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")  # .0%  Указываем как отображать %
#         print("-" * 20)
#
#
# acc = Account()
# acc.surname = "Василий"
# acc.num = "#555555"
# acc.percent = 0.03
# acc.value = 1000
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
#
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# acc.add_persents()
# print()
# acc.withdraw_money(700)
# print()
#
# acc.add_money(5000)