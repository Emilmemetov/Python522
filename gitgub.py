# print("Мое первое домашнее задание на Github!!!!!!")
#
# print("Мое первое домашнее задание на Github!!!!!!")
from struct import pack_into
from urllib.response import addinfourl


# import random
#
#
# def game():
#     numbers = random.randint(1, 100)
#     a = 0
#     print("Я загадал число от 1 до 100. Попробуй угадать!")
#     while True:
#         try:
#             user_name = int(input("Введи свой варик: "))
#             a += 1
#             if user_name < numbers:
#                 print("Число больше!")
#             elif user_name > numbers:
#                 print("Число меньше!")
#             else:
#                 print(f"Поздровляю! Ты отгадал число {numbers} за {a} попыток)")
#                 break
#         except ValueError:
#             print("Пожалуйста, вводи только числа")
#
#
# game()

#
# class Car:
#
#     def __init__(self, model, year_of_manufacture, brand, engine_power, color, price):
#         self.model = model
#         self.year_of_manufacture = year_of_manufacture
#         self.brand = brand
#         self.engine_power = engine_power
#         self.color = color
#         self.price = price
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(f"Название модели: {self.model}\nГод выпуска: {self.year_of_manufacture}\nПроизводитель: {self.brand}"
#               f"\nМощность двигателя: {self.engine_power}\nЦвет машины: {self.color}\nЦена: {self.price}")
#         print("=" * 40)
#
#     def set_name(self, model):
#         self.model = model
#
#     def set_name2(self, year_of_manufacture):
#         self.year_of_manufacture = year_of_manufacture
#
#     def get_name(self):
#         return self.model
#
#     def get_name2(self):
#         return self.year_of_manufacture
#
#
# h1 = Car("Passat B8", "2018", "Volkswagen", "230 л.с.",
#          "Black", "15000$")
# h1.print_info()
# h1.set_name(" Passat B6")
# h1.set_name2("2008")
# h1.print_info()
# h1.get_name2()


# def guess_the_number():
#     number_to_guess = random.randint(1, 100)
#     attempts = 0
#     print("Я загадал число от 1 до 100. Попробуй угадать!")
#
#     while True:
#         try:
#             user_guess = int(input("Твой вариант: "))
#             attempts += 1
#
#             if user_guess < number_to_guess:
#                 print("Загаданное число больше!")
#             elif user_guess > number_to_guess:
#                 print("Загаданное число меньше!")
#             else:
#                 print(f"Поздравляю! Ты угадал число {number_to_guess} за {attempts} попыток.")
#                 break
#         except ValueError:
#             print("Пожалуйста, вводи только числа!")
#
# if __name__ == "__main__":
#     guess_the_number()
#
# class Convert:
#
#     def __init__(self, kg=12):
#         self.__kg = kg
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     @property
#     def kg(self):
#         return f"{self.__kg} кг => {round(self.__kg * 2.2, 2)} фунтов"
#
#     @kg.setter
#     def kg(self, kg):
#         if Convert.__check_value(kg):
#             self.__kg = kg
#         else:
#             print("Килограми задаются только числами")
#
#
# p1 = Convert(6)
# print(p1.kg)
# p1.kg = 5
# print(p1.kg)


# РЕШЕНИЕ ЗАДАЧИ С ДЕКОРАТОРАМИ!
# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, num, surname, percent, value):
#         self.__num = num
#         self.__surname = surname
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет # {self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"счет #{self.__num} принадлежащий {self.__surname} был закрыт")
#
#     @property
#     def num(self):
#         return self.__num
#
#     @num.setter
#     def num(self, num):
#         if isinstance(num, int):
#             self.__num = num
#         else:
#             print("Ошибка, номер счета не может быть строкой")
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         if isinstance(surname, str):
#             self.__surname = surname
#         else:
#             print("Фамилия должна быть строкой")
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
#         if isinstance(value, (int, float)) and value >= 0:
#             self.__value = value
#         else:
#             print("Ошибка! Баланс должен быть неотрицательным числом.")
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def convert_two_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Cостояние счета:{usd_val} {Account.suffix_usd}")
#
#     def convert_two_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состоянии счета:{eur_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс: {self.__value}{Account.suffix} ")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"# {self.__num}")
#         print(f"Владелец:{self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print("-" * 20)
#
#     # def edit_owner(self, surname):
#     #     self.__surname = surname
#
#     def add_percens(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def wirt_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val}{Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#
# acc = Account("12345", "Долгих", 0.03, 1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_two_usd()
# acc.convert_two_eur()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# acc.convert_two_usd()
# acc.convert_two_eur()
# print()
# acc.print_info()
# print()
# acc.add_percens()
# acc.wirt_money(100)
# print()
# acc.wirt_money(3000)
# print()
# acc.add_money(5000)
# acc.wirt_money(7000)
# print()

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def a_setter(self, new_a):
        self.a = new_a

    def b_setter(self, new_b):
        self.b = new_b

    def sum_number(self):
        res = self.a + self.b
        print(f"Сумма:", res)

    def pr_number(self):
        res = self.a * self.b
        print(f"Произведение:", res)


class RightTriangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def gipotenuza(self):
        res = round((self.a ** 2 + self.b ** 2) ** 0.5, 2)
        print("Гипотенуза AB: ", res)

    def triange(self):
        result = 0.5 * self.a * self.b
        print("Площадь AB: ", result)


p2 = RightTriangle(5, 8)
p2.gipotenuza()
p2.triange()
print()
p2.sum_number()
p2.pr_number()
print()
p3 = RightTriangle(18, 15)
p3.gipotenuza()
p4 = RightTriangle(10, 20)
p4.gipotenuza()
p4.sum_number()
p4.pr_number()
p4.triange()
