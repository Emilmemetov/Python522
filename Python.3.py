# Задача: разработайте программу для подсчёта общего количества товаров, поступивших на склад за день. Пользователь
# должен вводить количество каждой партии товара до тех пор, пока не введёт число 0, сигнализирующее о конце рабочего
# дня. Если количество товара введено отрицательно или в формате, отличном от числа, программа должна сообщать об
# ошибке и предлагать повторный ввод. В конце работы программа должна вывести общее количество принятых товаров.
from random import choice
from types import LambdaType

# res = 0
# while True:
#     try:
#         a = int(input("Введите количество товаров: "))
#         if a == 0:
#             break
#         if a < 0:
#             continue
#         res += a
#     except ValueError:
#         print("Ошибка, введите коректное число! ")
#
#
# print(res)

# while True:
#     try:
#         a = int(input("Введите количество дней для анализа: "))
#         if a < 0:
#             print("Ошибка, отрицательные числа вводить нельзя, повторите! ")
#             continue
#         break
#     except ValueError:
#         print("Ошибка, введите коректное число")
# res = 0
# for i in (range(1, a + 1)):
#     while True:
#         try:
#             b = int(input("Введите количество товаров поступивших на склад: "))
#             if a < 0:
#                 print("Ошибка, некерактное число, повторите! ")
#                 continue
#             res += i
#             break
#         except ValueError:
#             print("Ошибка: введите корректное целое число.")
# c = res / i
# print(c)


# goods = {
#     "1": ['Core-i3-4330', 9, 4500],
#     "2": ['Core i5-4670K', 3, 8500],
#     "3": ['AMD FX-6300', 6, 3700],
#     "4": ['Pentium G3220', 8, 2100],
#     "5": ['Core i5-4350', 5, 6500],
# }
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n == "0":
#         break
#     else:
#         if n in goods:
#             while True:
#                 try:
#                     count = int(input("Количество: "))
#                     goods[n][1] += count
#                     break
#                 except ValueError:
#                     print("Значение некорректно. Введите число")
#         else:
#             print("Такого ключа не существует")
#
# for i in goods:
#     print(i, ") ", goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# print(dir(dict))

# dictionary = {
#     "яблоко": "apple",
#     "книга": "book",
#     "машина": "car",
#     "солнце": "sun",
#     "река": "river",
#     "дом": "house",
#     "кот": "cat",
#     "собака": "dog",
#     "стол": "table",
#     "стул": "chair"
# }
# for i in dictionary.keys():
#     if len(i) < 6:
#         print(i)
# for j in dictionary.values():
#     if len(j) < 5:
#         print("\t", j)

# music = {}
# while True:
#     print("Меню: ")
#     print("1. Добивить жанр")
#     print("2. Удалить жанр ")
#     print("3. Показать все жанры")
#     print("4. Выйти из программы")
#     a = input("Выберите действие:")
#
#     if a == "1":
#         b = input("Добавьте жанр")
#         year = input("Введите год, когда жанр стал любимым")
#         music[b] = [year]
#         print("Жанр добивлен")
#     if a == "2":
#         b = input("Введите жанр для удаления")
#         del music[b]
#     elif a == "3":
#         print(music)
#     else:
#         print("Список пуст")
#     if a == "4":
#         break

sotr = {}
while True:
    print("Меню:")
    print("1. Добавьте нового сотрудника ")
    print("2. Удалите сотрудника ")
    print("3. Просмотреть список всех сотрудников ")
    print("4. Выйти из программы ")
    a = input("Выберите действие: ")
    if a == "1":
        employee = input("Добавьте сотрудника")
        job_title = input("Добавьте должность")
        sotr[employee] = job_title
        print(sotr)
    elif a == "2":
        c = input("Введите сотрудника для удаления")
        if employee in sotr:
            del [sotr]
            print("Сотрудник удалён!")
        else:
            print("Сотрудник не найден")




