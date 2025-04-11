# print("Мое первое домашнее задание на Github!!!!!!")
#
# print("Мое первое домашнее задание на Github!!!!!!")

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
class Convert:

    def __init__(self, kg=12):
        self.__kg = kg

    def __check_value(c):
        if isinstance(c, int) or isinstance(c, float):
            return True
        return False

    @property
    def kg(self):
        return f"{self.__kg} кг => {round(self.__kg * 2.2, 2)} фунтов"

    @kg.setter
    def kg(self, kg):
        if Convert.__check_value(kg):
            self.__kg = kg
        else:
            print("Килограми задаются только числами")


p1 = Convert(6)
print(p1.kg)
p1.kg = "sd"
# print(p1.kg)






# class WeightConverter:
#     def __init__(self, kg):
#         if isinstance(kg, (int, float)):
#             self.kg = kg
#         else:
#             print("Килограммы задаются только числами!")
#             self.kg = None
#
#     def to_pounds(self):
#         if self.kg is not None:
#             return self.kg * 2.20462
#         return None
#
#     def display_result(self):
#         if self.kg is not None:
#             print(f"{self.kg} кг => {self.to_pounds():.2f} фунтов")
#
#
# p1 = WeightConverter(5)
# p1.display_result()