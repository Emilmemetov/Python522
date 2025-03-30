# name = "admin"
# print("Hello", name)
# age = 20.2
# print(age)
#
# print(type(name))
# print(type(age))
#
# print(id(name))
# print(id(age))
from typing import reveal_type


# a = b = c = 10
# a, b, c = 5, "Hello", 7.2
# print(a)
# print(b)
# print(c)

# name = "admin"
# print(name)

# import keyword
# print(keyword.kwlist)

# PI = 3.14
# print(PI)

# a = 5
# print(a)
# a = "Hello"
# print(a)
# a = 1.2
# print(a)

# a = 5
# b = 20
# print("a:", a)
# print("b:", b)
#
# # c = a  # 1
# # a = b  # 2
# # b = c  # 1
#
# print("a:", a)
# print("b:", b)

# print("строка "
#       "символов")
# print('\tстрока \nсимв      олов')

# a = 5
# b = 20
# print("a:", a)
# print("b:", b)
#
# # a = a + b  # 3
# # b = a - b  # 1
# # a = a - b  # 2
#
# a, b = b, a
#
# print("a:", a)
# print("b:", b)

# print("Документ \"file.txt\" находится по пути: \rD:\\\\folder\\file.txt")

# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"  # конкатенация
# print(s3)
# s4 = s3 * 5
# print(s4)

# print(6 + 2)
# print(6.2 + 2.4)
# print(6 - 2)
# print(6 * 2)
# print(7 / 2)
# print(6 / 2)
#
# print(7 // 2)
# print(6 // 2)
#
# print(6 ** 2)
#
# print(7 % 2)

# a = 5
# b = 7
# c = 3
# d = a + b + c
# print(d)
# f = a * b * c
# print(f)
# g = d / 3
# print(g)

# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# a = 5
#
# a += 3  # a = a + 3
# print(a)  # 8
#
# a -= 3  # a = a - 3
# print(a)  # 5
#
# a *= 4  # a = a * 4
# print(a)  # 20

# num = 9753  # 4
# print("Исходное число:", num)
# a = num % 10
# print("a:", a)
# num = num // 10
# # print(num)
# b = num % 10
# print("b:", b)
# num = num // 10
# # print(num)
# c = num % 10
# print("c:", c)
# num = num // 10
# # print(num)
# d = num % 10
# print("d:", d)
# print("Обратное число:", a * 1000 + b * 100 + c * 10 + d)


# num = 4321  #
# print("Исходное число:", num)
# res = num % 10 * 1000  # 1000
# num //= 10
# res += num % 10 * 100  # 200    res = res + num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print("Обратное число:", res)

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# # res = num1 + str(num2)
# print(res)

# print(int(3.981))
# print(type(round(3.581)))
# print(type(round(3.589, 2)))

# num1 = "2.5"
# num2 = 10
# res = float(num1) + num2  # 2.5 + 10
# print(res)

# name = "Виктор"
# age = 20
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут ", name, ". Мне ", age, " лет.", end=" ", sep="")
# print("Hello Python")

# name = input("Введите имя: ")
# print("Hello,", name)


# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))  # power = 2
# # num = int(num)
# # power = int(power)
# res = num ** power  # 5 ** 2
# print("Число", num, "в степени", power, "равно:", res)

# num1 = int(input("Введите число 1: "))
# num2 = int(input("Введите число 2: "))
# num3 = int(input("Введите число 3: "))
# num4 = int(input("Введите число 4: "))
# sum_1 = num1 + num2
# sum_2 = num3 + num4
# res = sum_1 / sum_2
# print(round(res, 2))

# b1 = True
# b2 = False
# # print(b1)
# # print(b2)
# # print(type(b1))
# # print(type(b2))
#
# # print(5 == 5)
# # print(5 == 3)
# print(int(b1))  # 1
# print(int(b2))  # 0
# print(b1 + 5)  # 1 + 5 = 6
# print(b2 + 5)  # 0 + 5 = 5

# print(bool("Python"))
# print(bool(""))
# print(bool(" "))
# print(bool(-5))
# print(bool(0))
# print(bool(0.2))
# print(bool(0.0))
# print(bool(True))
# print(bool(False))
# print(bool(None))


# test = None
# print(test)
# print(type(test))
# test = 5
# print(test)

# print(5 == 5)
# print(5 == 3)
# print(2 + 5 == 3 + 4)  # 7 == 7
# print(2 + 5 != 3 + 4)  # 7 != 7
# print(8 > 5)
# print(8 >= 8)
# print(5 < 10)
# print(5 <= 5)
# print("hello" > "Hello")  # 104 > 72

# print(2 < 4 < 9)  # True : True => True
# print(2 > 4 < 9)  # False : True => False
#
# print(2 * 5 > 7 >= 4 + 3)  # 10 > 7 >= 7  True : True => True
# print(3 * 3 <= 7 >= 2)  # 9 <= 7 >= 2  False : True => False


# n = int(input("Введите пятизначное число: "))  # 12345
# a = n % 10
# n //= 10
# b = n % 10
# n //= 10
# c = n % 10
# n //= 10
# d = n % 10
# n //= 10
# e = n % 10
# print("Произведение:", a * b * c * d * e)
# print("Среднее арифметическое:", (a + b + c + d + e) / 5)

# print(5 - 3 == 2 and 1 + 3 == 4)  # True and True  => True
# print(5 - 3 == 2 and 1 + 3 < 4)  # True and False  => False
# print(5 - 3 > 2 and 1 + 3 == 4)  # False and True  => False
# print(5 - 3 > 2 and 1 + 3 < 4)  # False and False  => False

# print(5 - 3 == 2 or 1 + 3 == 4)  # True and True  => True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True and False  => True
# print(5 - 3 > 2 or 1 + 3 == 4)  # False and True  => True
# print(5 - 3 > 2 or 1 + 3 < 4)  # False and False  => False

# print(not 9 - 5)  # not True  => False
# print(not 7 - 7)  # not False => True

# a = 10
# b = 10
# if a > b:
#     print(a, ">", b)
# if b > a:
#     print(b, ">", a)
# if b == a:
#     print(b, "==", a)

# cnt = 5
# if cnt < 10:
#     cnt = cnt + 1
# else:
#     cnt = cnt - 1
# print(cnt)

# a = 40
# b = 50
# if a > b:
#     print(a, ">", b)
# elif b == a:
#     print(b, "==", a)
# else:
#     print(b, ">", a)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
#     print("Приятного просмотра")
# else:
#     print("Доступ запрещен")

# a = input("Введите первую строну: ")
# b = input("Введите вторую строну: ")
# c = input("Введите третью строну: ")
#
# if a == b == c:  # '10' == '10' == '10'
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Треугольник равнобедренный")
# else:
#     print("Треугольник разносторонний")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5)
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует")

# month = int(input('Введите номер месяца:'))
# if (month == 12) or 1 <= month <= 2:
#     print('Зима')
# if 3 <= month <= 5:
#     print('Весна')
# if 6 <= month <= 8:
#     print('Лето')
# if 9 <= month <= 11:
#     print('Осень')


# day = int(input('Ввведите номер месяца (цифрой): '))
# if 1 <= day <= 12:  # (day >= 1) and (day <= 5):
#     print('Время года - ', end='')
#     if day == 1 or day == 2 or day == 12:
#         print('Зима')
#     if 3 <= day <= 5:  # day == 4 or day == 5 or day == 3
#         print('Весна')
#     if day == 6 or day == 7 or day == 8:
#         print('Лето')
#     if day == 9 or day == 10 or day == 11:
#         print('Осень')
# else:
#     print('Такого времени года не существует')

# day = int(input('Ввведите номер месяца (цифрой): '))
#
# if day == 1 or day == 2 or day == 12:
#     print('Зима')
# elif 3 <= day <= 5:  # day == 4 or day == 5 or day == 3
#     print('Весна')
# elif day == 6 or day == 7 or day == 8:
#     print('Лето')
# elif day == 9 or day == 10 or day == 11:
#     print('Осень')
# else:
#     print('Такого времени года не существует')

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")


# match выражение:
#     case шаблон_1:
#         действие_1
#     case шаблон_2:
#         действие_2
#     case _:
#        действие по умолчанию

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case 'user':
#         print("Пользователь")
#     case _:
#         print("Пароль не верен")

# day = 'вторник'
# time = 13
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 12 or 14 <= time <= 17:
#         print("Рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# a, b = 30, 20
#
# print(a if a < b else b)


# a, b = 20, 20
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = int(input("Введите число от 1 до 99: "))  # 45
# kop = a  # 45
# if 11 <= kop <= 14:
#     print(a, "копеек")
# elif 1 <= a <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")
# else:
#     print("Недопустимое значение")

# try:  # попытаться
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки или Нельзя делить на ноль")
# else:  # когда в блоке try не возникло исключения
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполнится в любом случае
#     print("Конец программы")

# n = input("Введите первое число: ")  # '10'
# m = input("Введите второе число: ")  # qqq
#
# try:
#     n = int(n)  # 10
#     m = int(m)  #
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# Циклы

# while условие:
#     блок_инструкций

# i = 0  # счетчик
# while i < 5:  # условие
#     print("i =", i)
#     i += 1  # изменение счетчика


# итерация - один шаг цикла

# i = 0
# while i < 100:
#     print("i =", i)
#     i += 10


# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 2
# while i <= 20:
#     if i % 2:  # i % 2 == 1, i % 2 != 0 - нечетные числа, i % 2 == 0 - четные числа
#         print(i, end=" ")
#     i += 1

# i = 2
# while i <= 20:
#     print(i, end=" ")
#     i += 2

# n = int(input("Количество символов: "))
# print("*" * n)
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# +-+-+-+

# n = int(input("Количество символов: "))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print("+", end="")
#     else:
#         print("-", end="")
#     i += 1


# n = int(input("Количество символов: "))
# print("+" * n)


# n = int(input("Количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2:
#         print(a, end=" ")
#         res += a  # res = res + a
#     a += 1
# print("\nСумма:", res)

# n = input("Введите целое число: ")  # 'пять'
#
# while type(n) is not int:  # type(n) != int
#     try:
#         n = int(n)  # 8
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")  # '8'
#
# if n % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input("Введите положительное число: "))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n  # res = res * n
# print("Результат:", res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i =", i)

# i = 1
# while i < 5:  # 2
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:  # 1
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1


# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print("^", end="")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#    print(element)

# for i in "Hello!", "World":
#     print(i)

# range(start=0, stop, step=1)

# a = 10
# for i in range(0, 10, 1):  # i = 0, i < 10, i += 1  # i = 10, i > 0, i -= 1
#     print(i, end=" ")
#
# print()
#
# i = 1
# while i < 10:
#     print(i, end=" ")
#     i *= 2


# a = int(input("Введите целое число: "))
#
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# for i in range(10, 100):
#     if i % 11 == 0:
#         print(i, end=" ")
#
# print()
#
# for i in range(11, 100, 11):
#     print(i, end=" ")
#
# print()
#
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Цикл закончен")

# for i in range(3):  # 3
#     print("+++")
#     for j in range(2):  # 0
#         print("-----")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# letter = [i * 2 for i in "Hello"]
# print(letter)
#
# for i in "Hello":
#     print(i * 2)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)
#
# for i in range(30):
#     if i % 2 == 0:
#         print(i, end=", ")


# Список (list)
# nums = [8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
# print(nums)
# print(type(nums))
# print(nums[0])
# print(nums[1])
# print(nums[10])
# print(nums[-1])
# # print(nums[len(nums)-1])
# print("Кол-во:", len(nums))
# nums[1] = 256
# nums[3] += 100
# print(nums)

# s = []
# print(s)
# print(type(s))
#
# t = list("Python")
# print(t)
# print(type(t))
#
# print(range(0, 8, 2))
# print(list(range(1, 18, 2)))

# a = [1, 3, 5, 7, 9]
# b = [11, 13, 15, 17]
# print(a + b)
# print(a * 3)

# a = [1, 3, 5, 7, 9]
#
# for i in a:
#     print(i)

# a = [0 for _ in range(5)]
# print(a)  # [0, 0, 0, 0, 0]

# a = [i for i in range(5)]
# print(a)  # [0, 1, 2, 3, 4]

# n = 15
# a = [i ** 2 for i in range(2, n)]
# print(a)  # [0, 1, 2, 3, 4]

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)

# lst = [9, 6, 3, 5]
#
# for i in range(len(lst)):  # 0 1 2 3
#     print(lst[i], end=" ")
#
# print()
#
# for v in lst:  # 9 6 3 5
#     print(v, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# res = 0
# # for i in range(len(a)):  # 0 1 2 3 4
# #     if a[i] < 0:
# #         res += a[i]
#
# for i in a:  # 9, -2, 7, -3, 4
#     if i < 0:
#         res += i
#
# print(res)


# n = list(range(21, 41))
# print(n)
# count = sum_ = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         count += 1
# #     else:
# #         sum_ += n[i]
#
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         sum_ += i
#
# print("Количество четных элементов списка:", count)
# print("Сумма нечетных элементов списка:", sum_)

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=" ")
# print()
#
# for i in range(0, len(a), 2):
#     print(a[i], end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")

# a = [9, 7, 8, 4, 2]
# print(a)
# a[0], a[1] = a[1], a[0]
# print(a)

# Срез

# список[start:stop:step]
# a = [9, 7, 8, 4, 2, 1, 3]
# print(a)
# print(a[1:4])
# print(a[5:])
# print(a[1:4:2])
# print(a[::-2])
# print(a[-1:0:-1])
# print(a[10:20])

# lst = list(range(1, 8))
# print(lst)
# print(lst[::-1])
# print(lst[::2])
# print(lst[1::2])
# print(lst[:1])
# print(lst[-1:])
# print(lst[3:4])
# print(lst[4:])
# print(lst[4:1:-1])
# print(lst[2:5])

# a = [1, 2, 3, 4, 5, 6, 7]
# print(a)
# a[1:3] = [0, 0, 0, 0]
# print(a)
# a[1:2] = [20]
# print(a)
# a[2] = [120, 45]
# print(a)

# a[100:111] = [100]
# print(a)
# print(a[9])
# print(len(a))

# Методы списков
# print(dir(list))
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# s = [9, 7, 8, 4, 2, 1, 3]
# print(s)
# s.append(99)  # добавляет элемент в конец списка
# print(s)
# s.extend([11, 12, 13])  # добавляет список элементов в конец списка
# print(s)
# s.insert(2, 100)  # добавляет элемент (второй параметр) по заданном индексу (первый параметр)
# print(s)

# s.insert(20, 5)
# print(s)

# s = []
# n = int(input("Количество элементов в списке: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # s.append(x)
#     s.insert(0, x)  # [7, 8, 9]
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7, 2]
# c = []  # [2, 1, 4, 3]
#
# for i in a:  # 2
#     for j in b:  # 2
#         if i in c:
#             continue
#         if i == j:  # 2 == 2
#             c.append(i)
#             break
# print(c)

# a = [5, 9, 2, 1, 4, 3, 2, 4]  #
# b = [4, 2, 1, 3, 7, 2]  #
# c = []
#
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)

# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
#
# if len(b) > len(a):
#     for i in range(len(a)):  # 0, 1, 2, 3, 4
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):  # 0, 1, 2, 3, 4
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
#
# print(c)

# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):  # 0, 1, 2, 3, 4
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
#
# print(c)

# s = [9, 7, 8, 4, 2, 8, 1, 3]
# print(s)
# item = 7
# if item in s:
#     s.remove(item)  # удаляет первое вхождение элемента по значению
# print(s)

# last = s.pop()  # удаляет последний элемент из списка
# print(last)
# print(s)
#
#
# try:
#     second = s.pop(10)  # удаляет элемент по заданному индексу
# except IndexError:
#     second = "Такого индекса нет"
# print(second)
# print(s)
#
# s.clear()  # удаляет элементы из списка
# print(s)

# s = [9, 7, 8, 4, 2, 8, 1, 3]
# print(s)
#
# s[5:] = []
# print(s)
#
# del s[:]
# print(s)

# s = [9, 7, 8, 4, 2, 8, 1, 3, 8]
# print(s)
#
# # num = s.count(9)  # количество вхождений заданного элемента
# # print(num)
#
# ind = s.index(8, 3, 7)  # ищет первое вхождение заданного элемента, возвращает индекс на котором
# # нашел элемент, можно задать диапазон поиска
# print(ind)

# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(m)
# for i in m:
#     if m.count(i) == 1:
#         print(i, end=" ")
# print()
# mas = [i for i in m if m.count(i) == 1]
# print(mas)

# a = [1, 2, 3]
# b = a.copy()
# print("a =", a, id(a))
# print("b =", b, id(b))
# b.append(20)
# print("a =", a)
# print("b =", b)
# a.append(100)
# print("a =", a, id(a))
# print("b =", b, id(b))


# m = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# # print(m)
# # m.reverse()
# # # print(m)
# m.sort(reverse=True)
# print(m)
#
# # s = ["Виталий", "Сергей", "Александр", "Анна"]
# # s.sort(key=len, reverse=True)
# # print(s)
#
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
#
# print("lst:", sorted(s, reverse=True))
# print(s)
# print()


# import random

# print(random.random())
# print(random.randint(5, 10))
# print(random.randrange(5, 10, 2))
# print(round(random.uniform(10.5, 25.5), 2))

# city_list = ["Москва", "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# print(random.choice(city_list))
# print(random.choice(s))
# print(random.choices(city_list, k=3))
# print(random.choices(s, k=3))
# random.shuffle(s)
# print(s)


# import random
#
# mas = [random.randint(50, 100) for i in range(5)]
# print(mas)
# print(len(mas))
# print(max(mas))
# print(min(mas))
# print(sum(mas))

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# max_ = max(mas)
# print(max_)
# mas.remove(max_)
# mas.insert(0, max_)
# print(mas)


# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
#
# min_ = min(mas)
# print("Min:", min_)
#
# ind = mas.index(min_)
# print("Index min:", ind)
#
# del mas[:ind]
# print(mas)


# m = [
#     [1, 2, 3, 4],  # 0
#     [5, 6, 7, 8],  # 1
#     [9, 10, 11, 12]  # 2
# ]
# print(m)
#
# # print(len(m))
# # print(m[1][2])
# # print(m[2][1])
#
# print("Вариант 1")
# for row in range(len(m)):
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print("Вариант 2")
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# m = ["Hello", "World", [44, [1, 2, 3], 55, ["Python", "new"]]]
# print(m)
# print(m[1][2])
# print(m[2][1][1])
# print(m[2][3][0][3])

# import math
#
# print(math.sqrt(4))
# print(math.ceil(3.2))
# print(math.floor(3.8))


# import math as m
#
# print(m.sqrt(4))
# print(m.ceil(3.2))
# print(m.floor(3.8))

# from math import *
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))

# from math import sqrt, ceil, floor
#
# print(sqrt(4))
# print(ceil(3.2))
# print(floor(3.8))
# import math
# print(dir(math))

# from math import pi
#
# # print(pi)
# radius = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * radius * pi, 2))

# import time
# import locale

# print(time.time())
# print(time.ctime(739210060))
# res = time.localtime()
# print(res)
# print(res.tm_year, "-", res.tm_mon, "-", res.tm_mday, sep="")
# print(time.strftime("Today is %B %d, %Y"))
# # print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(539210060)))
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня: %B %d, %Y"))

# start = time.time()
# print("Запуск программы")
# time.sleep(5)
# res = time.time() - start
# print("Программа выполнилась за", res, "сек.")

# import math
# from math import sqrt, pi
#
# s = None
# shape = int(input("Выбор фигуры:\n1-треугольник\n2-прямоугольник\n3-круг\n: "))
# if shape == 1:
#     a = int(input("Введите строну a = "))
#     b = int(input("Введите строну b = "))
#     c = int(input("Введите строну c = "))
#     p = (a + b + c) / 2
#     s = sqrt(p * (p - a) * (p - b) * (p - c))
# elif shape == 2:
#     a = int(input("Введите строну a = "))
#     b = int(input("Введите строну b = "))
#     s = a * b
# elif shape == 3:
#     radius = int(input("Введите радиус = "))
#     s = pi * radius ** 2
# else:
#     print("Такой фигуры нет")
#
# print(round(s, 2))


# Функции

# def hello(first_name, age):   # аргументы
#     print("Меня зовут:", first_name, "Мой возраст:", age)
#
#
# hello("Irina", 28)  # параметры
# hello("Ivan", 25)


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, "+", "-")
# symbol(7, "X", "0")

# def get_sum(a, b):
#     print("Сумма:", end=" ")
#     c = a + b
#     return c
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 5))
# print(maximum(5, 15))

# def zadacha(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# x = int(input("a = "))
# y = int(input("y = "))
# print(zadacha(x, y))


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def one_big(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if one_big(a, b):
#     print("Первое число больше второго")
# else:
#     print("Второе число больше первого")

# print(one_big(10, 5))
# print(one_big(5, 10))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":  # "A" <= "S" <= "Z"
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":  # "0" <= "8" <= "9"
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль")
# else:
#     print("Это ненадежный пароль")

# res = 10
#
#
# def get_sum(a, b, c=0, d=1):
#     inner = 20
#     return a + b + c + d + res + inner
#
#
# print(get_sum(1, 5, 2, 7))

# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2, c=5))
# print(get_sum("С", "л", d="н", c="о"))


# def set_param(count=20, symbol="-"):
#     print(symbol * count)
#
#
# set_param(10, "+")
# set_param(5, "*")
# set_param(15, "#")
# set_param(7)
# set_param()


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Irina", 23)
#
#
# def display_info(name, age):
#     print("Hello,", name)
#
#
# display_info("Irina", 23)
# display_info(23, "Irina")
# display_info(age=23, name="Irina")
# display_info("Igor", age=23, name="Irina")


# lt1 = "Hello"
# lt2 = "Hello"
# print(lt1, id(lt1))
# print(lt2, id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1, id(lst1))
# print(lst2, id(lst2))
# print(lst1 == lst2)
# print(lst1 is lst2)

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))
# lst1.pop(1)
# print(lst1, id(lst1))

# lt1 = "Hello"
# print(lt1, id(lt1))
# lt1 = lt1[5:10]
# print(lt1, id(lt1))
# lt1 = lt1 + "!"
# print(lt1, id(lt1))

# a = 5
# print(a, id(a))
# a = 7
# print(a, id(a))


# Кортеж (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
# lst[1] = 100
# print(lst)

# a = ()
# print(a, type(a))
# b = tuple()
# print(b, type(b))


# a = (1, 2, 3)
# print(a, type(a))
#
# b = tuple("Hello")
# print(b, type(b))


# b = tuple("Hello")
# print(b)
#
# print(b[1])
# print(b[1:3])

# s1 = tuple(input("-> ") for i in range(5))
# print(s1)

# s1 = tuple(i for i in range(5))
# print(s1)

# from random import randint
#
# s1 = tuple(randint(50, 100) for i in range(5))
# print(s1)

# t1 = tuple("hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3 * 2)
# print(t3)
# print(t3.count("a"))
# print(t3.index("l", 4, -2))
# print(dir(list))
# print(dir(tuple))

# v = "a"
# if v in t3:
#     print(t3.index(v))
# else:
#     print("Такого символа нет")


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) == 1:
#             return tpl[tpl.index(el):]  # tpl[2:]
#         else:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1  # tpl[5]
#             return tpl[first:second]  # [1:5]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# t = (10, "Python", True, [1, 2, 3], ["hello", "world"])
# print(t, id(t))
# t[4][0] = "new"
# print(t, id(t))
# print(len(t))
# t[4].append("hi")
# print(t, id(t))

# Распаковка кортежа

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # Распаковка кортежа
# # x, y, z = 1, 2, 3
# print(x, y, z)


# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# # user = get_user()
# # print(user)
# # first_name, year, married = user
#
# first_name, year, married = get_user()
# print(first_name, year, married)


# lst = [1, 2, 3, 4, 5, 6]
# print(lst, type(lst))
# tpl = tuple(lst)
# print(tpl, type(tpl))
# lst2 = list(tpl)
# print(lst2, type(lst2))

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
# for county in countries:
#     county_name, county_population, cities = county
#     print("\nСтрана: ", county_name, ", население = ", county_population, sep="")
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород: ", city_name, ", население = ", city_population, sep="")


# tpl = tuple(input("Введите строку: "))
# print(tpl)
#
# lst = []
# for i in range(len(tpl)):
#     if tpl[i] not in lst:
#         lst.append(tpl[i])
#
# for i in range(len(lst)):
#     print("Количество", lst[i], "=", tpl.count(lst[i]))


# Множество (set)

# s = {"red", "yellow", "green", "yellow", "green"}
# print(s, type(s))
# print(len(s))

# a = set("hello")
# print(a, type(a))

# s = {x * x for x in range(10)}
# print(s)

# lst = [1, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 6]
# lst = ["red", "yellow", "green", "yellow", "green"]
# print(lst)
# num = set(lst)
# print(num)
# lst2 = list(num)
# print(lst2)

# t = {'yellow', 'red', 'green'}
# print('red' in t)
# print('blue' in t)
# for i in t:
#     print(i)


# lst = ['ab_1', "ac_1", 'bc_1', 'bc_2']
# print({i for i in lst if 'a' in i})
# print(['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst])
# tpl = tuple('A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in lst if i[1] == 'c')
# print(tpl)

# print(dir(set))

# a = {"red", "yellow", "green"}
# print(a)
# a.add("blue")
# print(a)
# # a.remove("yellow")
# # a.remove("black")  # KeyError
# color = "black"
# # if color in a:
# #     a.remove(color)
# # a.discard(color)
# # a.pop()
# a.clear()
# print(a)


# print({i / 2 for i in range(1000, 1010)})

# from random import randint
#
#
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5, 0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print("0 =", tpl3.count(0))

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b  # {0, 1, 2, 3, 4}
# # print(c)#
# # c = a & b  # {1, 2, 3}
# # print(c)
# # c = a - b  # {0}
# # print(c)
# c = a ^ b  # {0}
# print(c)
# # a |= b
# # print(a)
# # a &= b
# # print(a)
# # a -= b
# # print(a)
# a ^= b
# print(a)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# c = a >= b
# print(c)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = {6, 2}
# e = {8, 2}
# d = b ^ c ^ a ^ e  # {0, 4, 6, 8}
# d = a.symmetric_difference(b).symmetric_difference(c).symmetric_difference(e)  #
# print(d)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {1, 2}
# s7 = {1, 2}

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# g = {9, 8}
# su = a.symmetric_difference(b).symmetric_difference(c).symmetric_difference(d).symmetric_difference(
#     e).symmetric_difference(f).symmetric_difference(g)
# print(su)
# print(len(su))
# print(min(su))
# print(max(su))

# a = {1, 2}
# b = {3}
# c = {4, 5}
# d = {3, 2, 6}
# e = {6}
# f = {7, 8}
# g = {9, 8}
# h = a | b | c | d | e | f | g
# print(h)
# print('Unic elems count', (len(h)))
# print('Min elem: ', min(h))
# print('Max elem: ', max(h))

# s1 = "Hello"
# s2 = "How are you"
# s3 = set(s1) & set(s2)
# print(s3)
# for i in s3:
#     print(i, end=" ")

# s = frozenset([1, 2, 3, 4, 5, 6])
# print(s)
# s1 = frozenset("hello")
# print(s1)


# Словарь (dict)

# lst = ["one", "two"]
# d = {"first": "one", "second": "two"}
#
# print(lst[1])
# print(d["second"])

# d = {0: "text", "one": 45, (1, 2): "Кортеж", True: [5, 9, 8, 7, 7], False: "один", 1: "Список"}
# print(d)


# d = {1: "one", "second": "two"}
# print(d)
# print(type(d))
#
# d1 = dict(first="one", second="two")
# print(d1)
# print(type(d1))

# lst = [
#     ["one", 1],
#     ["two", 2],
#     ["three", 3]
# ]
#
# print(lst)
# d = dict(lst)
# print(d)

# d = {i: i ** 2 for i in range(1, 7)}  # 1,2,3,4,5,6
# print(d)
#
# for i in d:
#     print("key =", i, "value =", d[i])

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# res = 1
# for key in d:
#     res *= d[key]
#
# print(res)

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(d)
# del d["x2"]
# print(d)

# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# print(d)

# d = {i: input("-> ") for i in range(1, 5)}
# print(d)
# dislike = int(input("Какой элемент исключить: "))
# del d[dislike]
# print(d)

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

# print(dir(dict))


# d = {1: "one", 2: "two", 3: "three"}
# print(d.keys())
# print(d.values())
# print(d.items())
#
# for i, j in d.items():
#     print(i, ":", j)

# d = {1: "one", 2: "two", 3: "three"}
# d2 = d.copy()
# print("D =", d)
# print("D2 =", d2)
#
# d2[2] = "four"
# print("D =", d)
# print("D2 =", d2)


# d = {1: "one", 2: "two", 3: "three"}
# print(d)
# # d.clear()
# # item = d.pop(6, "Такого ключа не существует")
# item = d.popitem()
# print(d)
# print(item)


# d = {1: "one", 2: "two", 3: "three"}
# # value = d[6]
# # value = d.get(2, "Такого ключа не существует")
# # print(value)
# # item = d.setdefault(4, "four")
# # print(d)
# # print(item)
#
#
#
# sales_data = {'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#               'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#               'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#               'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}}

# for x in sales_data:
#     print(x)
#     for y in sales_data[x]:
#         print("\t", y, ":", sales_data[x][y])

# for x, y in sales_data.items():
#     print(x)
#     for i, j in y.items():
#         print("\t", i, ":", j)


# #
# # person = input("Имя: ")
# # region = input("Регион: ")
# # print(sales_data[person][region])
# # new_data = int(input("Новое значение: "))
# # sales_data[person][region] = new_data
# # print(sales_data[person])
# # a = {10: "A", 20: "B", 2: "C"}
# a = [(10, "A"), (20, "B"), (2, "C")]
# # c = d | a
# # print(c)
# d.update(a)
# print(d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# new_d = dict()
# # new_d['name'] = d.pop('name')
# # new_d['salary'] = d.pop('salary')
# new_d['name'], new_d['salary'] = d.pop('name'), d.pop('salary')
# print(d)
# print(new_d)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
#
# d['location'] = d.pop('city')
# print(d)


# d = {'один': 1, "два": 2, "три": 3, "четыре": 4}
# new_d = {value: key for key, value in d.items()}
# print(d)
# print(new_d)


# d = {'один': 1, "два": 2, "три": 3, "четыре": 4}
# new_d = {key: value for key, value in d.items() if value <= 2}
# print(new_d)
#
# d = {i: i * 5 for i in [10, 20, 30, 40, 50]}
# print(d)
#
# s = "Hello"
# d1 = {key: key * 3 for key in s}
# print(d1)

# d = {'один': 1, "два": 2, "три": 3, "четыре": 4}
#
# print(list(d.values()))
# print(list(d.keys()))
# print(list(d.items()))


# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = dict()  # {'one': [1, 2, 3], 'two': [10, 20], 'three': [], 'four': []}
# s = None
#
# for i in a:  # 20
#     if type(i) is str:
#         d[i] = []
#         s = i  # "two"
#     else:
#         d[s].append(i)
#
# print(d)

# zip

# d = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(d)

# a = [1, 2, 3, 4]
# b = ['one', 'two', 'three']
# d = {v: k for k, v in zip(a, b)}
# print(d)

# one = {'name': 'Igor', 'surname': 'Pavlov', 'job': 'Consultant'}
# two = {'name': 'Irina', 'surname': 'Vetrova', 'job': 'Manager'}
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)

# s = [(1, 'a'), (2, 'b'), (3, 'c')]
# a, b = zip(*s)
# print(a)
# print(b)

# letters = ['b', 'd', 'a', 'c']
# numbers = [4, 1, 3, 2]
# d = dict(zip(letters, numbers))
# print(d)
#
# data1 = list(zip(letters, numbers))
# print(data1)
# data1.sort()
# print(data1)
# d2 = dict(data1)
# print(d2)
#
# data2 = list(zip(numbers, letters))
# print(data2)
# data2.sort()
# print(data2)
# d3 = {v: k for k, v in data2}
# print(d3)


# letters = ['b', 'd', 'a', 'c']
# numbers = [4, 1, 3, 2]
#
# data = sorted(zip(letters, numbers))
# print(dict(data))


# one = {'один': 1, "два": 2, "четыре": 8}
# two = {"три": 3, "четыре": 4}
#
# print({**two, **one})   # {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# print(one | two)
#
# for k, v in {**one, **two}.items():
#     print(k, "->", v)


# colors = ['red', 'green', 'blue']
# ind = 1
# for color in colors:
#     print(str(ind) + "-й цвет: " + color)
#     ind += 1
#
# print()
# for index, color in enumerate(colors, start=10):
#     print(str(index) + "-й цвет: " + color)

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
#
# for i, (k, v) in enumerate(d.items(), 1):
#     print(i, ") ", k, ": ", v, sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# def func(*args):
#     return args
#
#
# print(func(5))
# print(func(1, 2, 3, 'abc'))
# print(func())


# def summa(*params):
#     res = 0
#     for n in params:
#         res += n
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(7, 8, 9))


# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))


# def average(*args):
#     sr = sum(args) / len(args)
#     print(sr)
#     res = []
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
#
# print(average(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(average(3, 6, 1, 9, 5))

# c = int(input("Введите количество элементов списка: "))
# a = {input(str(i) + "-й студент: "): int(input("Введите средний бал: ")) for i, _ in enumerate(range(c), 1)}
# print(a)
# ind = 1
# for i in a:
#     ind += 1
# for ind, i in enumerate(a, 1):
#     print(str(ind) + "-й студент: " + i, "\nБалл =", a[i])

# sr_bal = round(sum(a.values()) / c)
# print('Средний бал: ', sr_bal, '\nСтуденты с балом выше среднего: ')
# # for i in a:
# #     if a[i] > sr_bal:
# #         print(i)
#
# for k, v in a.items():
#     if v > sr_bal:
#         print(k)

# students = {}
# c = int(input("Введите количество элементов списка: "))
# for i in range(c):
#     name = input(str(i + 1) + "-й студент: ")
#     point = int(input("Балл: "))
#     students[name] = point
#
# sr_bal = round(sum(students.values()) / c)
# print('Средний бал: ', sr_bal, '\nСтуденты с балом выше среднего: ')
#
# for k, v in students.items():
#     if v > sr_bal:
#         print(k)


# def func(a, b, *args):
#     return a, b, args
#
#
# print(func(5, 7))
# print(func(1, 2, 3, 4, 5))


# def scores(student, *score):
#     print("Student Name:", student)
#     for i in score:
#         print(i)
#
#
# scores("Igor", 100, 95, 88, 92, 99)
# scores("Ivan", 77, 32, 88)

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(name="Irina"))


# def info(**data):
#     for k, v in data.items():
#         print(k, ":", v)
#     print()
#
#
# info(name="Irina", surname="Vetrova", age=22)
# info(name="Igor", phone="987456", email="igor@mail.ru", age=22)

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {"one": "first"}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name="bob", age=31, weight=61, eyes_color='grey')
# print(my_dict)


# def func(a, *args, b=100, **kwargs):
#     return kwargs, a, b, args
#
#
# print(func(1, 2, 3, 4, 5, 6, c=55, d=66, b=20, e=77))


# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs["one"])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)


# Области видимости (scope)

# name = "Tom"  # глобальная область видимости
#
#
# def hi():
#     global name
#     name = "Sam"
#     surname = "Jonson"  # локальная область видимости
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# # print(name)
# hi()
# bye()
# print(name)


# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()
# print(i)


# import builtins
#
# names = dir(builtins)
#
# for t in names:
#     print(t)


# print = 5
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(max(lst))

# x = 5
#
#
# def add_two(a):
#     x = 2  # 2
#
#     def add_some():
#         x = 3
#         print("x =", x)  # 4
#         return a + x  # 5
#     print("x в наружной функции =", x)
#     return add_some()  # 3  6
#
#
# print(add_two(3))  # 1  7


# Вложенные функции

# def outer(who):
#     def inner():
#         print("Hello,", who)
#
#     inner()
#
#
# outer("World")


# def outer():
#     a = 6
#
#     def inner(b):
#         a = 4
#         print("Сумма:", a + b)
#
#     print("a =", a)
#     inner(5)
#
#
# outer()


# x = 25
#
#
# def fn():
#     global t
#     a = 30  # 35
#
#     def inner():
#         nonlocal a
#         a = 35
#         # print("a =", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t  # 25 + 35
# print(c)  # 60
# x = 5
#
#
# def fn1():
#     x = 25  # 55
#
#     def fn2():
#         x = 33  # 55
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print("fn2.x =", x)  # 33 -> 55
#
#     fn2()
#     print("fn1.x =", x)  # 25 -> 55
#
#
# fn1()


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#         # print(a, b)
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))  # [1, 7]


# def rect_paral(a, b, c):
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#     return s
#
#
# print(rect_paral(2, 4, 6))
# print(rect_paral(5, 8, 2))
# print(rect_paral(1, 6, 8))


# def rect_paral(a, b, c):
#     global s
#
#     def inner(i, j):
#         return i * j
#
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#
#
# s = 0
# rect_paral(2, 4, 6)
# print(s)
# rect_paral(5, 8, 2)
# print(s)
# rect_paral(1, 6, 8)
# print(s)

# def rect_paral(a, b, c):
#     s = 0
#
#     def inner(i, j):
#         nonlocal s
#         s += i * j
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#     return 2 * s
#
#
# print(rect_paral(2, 4, 6))
# print(rect_paral(5, 8, 2))
# print(rect_paral(1, 6, 8))


# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# a = outer(5)
# print(a(10))
#
# b = outer(6)
# print(b(10))

# c = outer(5)(10)
# print(c)

# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "!"
#         return a, b, c
#
#     return func2


# func = func1()
# print(func())


# def func(city):
#     s = 0  # 1  # 1
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
#
# res1()
#
# res2()
# res2()
# res2()
# res2()
# res2()


# Анонимные функции (lambda)

# def func(x, y):
#     res = x + y
#     return res
#
#
# print(func(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)("a", "b"))

# func1 = lambda x, y: x + y
#
# print(func1(1, 2))
# print(func1(5, 2))


# print((lambda a, b, c: a + b + c)(10, 20, 30))
# print((lambda a, b, c=3: a + b + c)(10, 20))
# print((lambda a, b=2, c=3: a + b + c)(10))
# print((lambda a=1, b=2, c=3: a + b + c)())
# a = (lambda *args: sum(args))(1, 2, 3, 4, 5, 6, 7)
# print(a)
# print((lambda *args: sum(args))(6, 7))

# print((lambda **kwargs: kwargs)(a=1, b=2, c=3))
# print((lambda **kwargs: sum(kwargs.values()))(a=1, b=2, c=3))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
#
# for t in c:
#     print(t("abc__"))


# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(42)
# print(f(3))
#
#
# def outer(n):
#     return lambda x: x + n
#
#
# f = outer(42)
# print(f(3))
#
# outer = lambda n: lambda x: x + n
# f = outer(42)
# print(f(3))
#
#
# f = (lambda n: lambda x: x + n)(42)
# print(f(3))
#
# print((lambda n: lambda x: x + n)(42)(3))
#
# res = (lambda n: lambda x: "x > n" if x > n else "x < n")(42)(3)
# print(res)

# print((lambda n: lambda x: lambda y: x + n + y)(2)(4)(6))

# d = {'b': 10, 'a': 15, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# print(lst)
# d2 = dict(lst)
# print(d2)


# def func(i):
#     return i[1]
#
#
# d = {'b': 10, 'a': 15, 'c': 4}
# lst = list(d.items())
# print(lst)
# lst.sort(key=func)
# print(lst)
# d2 = dict(lst)
# print(d2)

# players = [
#     {'name': "Антон", 'last name': 'Бирюков', 'rating': 9},
#     {'name': "Алексей", 'last name': 'Бодня', 'rating': 10},
#     {'name': "Федор", 'last name': 'Сидоров', 'rating': 4},
#     {'name': "Михаил", 'last name': 'Семенов', 'rating': 6},
# ]
#
# res1 = sorted(players, key=lambda item: item["last name"])
# print(res1)
#
# res2 = sorted(players, key=lambda item: item["rating"], reverse=True)
# print(res2)
#
# res3 = sorted(players, key=lambda item: item["rating"])
# print(res3)

# lst = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
#
# print(lst[3](12, 2))

# d = {
#     1: lambda: print("Январь"),
#     2: lambda: print("Февраль"),
#     3: lambda: print("Март"),
#     4: lambda: print("Апрель"),
#     5: lambda: print("Май"),
#     6: lambda: print("Июнь"),
#     7: lambda: print("Июль"),
#     8: lambda: print("Август"),
#     9: lambda: print("Сентябрь"),
#     10: lambda: print("Октябрь"),
#     11: lambda: print("Ноябрь"),
#     12: lambda: print("Декабрь")
# }
#
# d[3]()

# map()

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# print(list(map(mult, lst)))
#
# print(list(map(lambda t: t * 2, lst)))
#
# print(set(map(lambda t: t * 2, [2, 8, 12, -5, -10])))
#
# lst1 = [2, 8, 12, -5, -10]
# lst2 = [8, -10, 12, 2, -5]
#
# print(dict(map(lambda x, y: (x, y), lst1, lst2)))
# print(list(map(lambda x, y: [x, y], lst1, lst2)))


# t = (2.88, -1.78, 100.55)
#
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))

# areas = [3.564789, 5.789456, 4.012456, 56.451266, 9.4567891, 32.45678912]
# print(list(map(round, areas, range(1, 10))))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))


# filter()

# t = ('abcd', 'qwe', 'zxcvb', 'def', 'hjk')
#
# print(tuple(filter(lambda s: len(s) == 3, t)))

# lst = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# print(list(filter(lambda s: s > 75, lst)))

# import random
#
# lst = [random.randint(0, 40) for i in range(10)]
# print(lst)
# # print(list(filter(lambda s: 10 <= s <= 20, lst)))
# print(list(filter(lambda s: s in range(10, 21), lst)))

# nums = [45, 55, 60, 37, 100, 105, 220]
#
# print(list(filter(lambda x: x % 15 == 0, nums)))
# print(list(filter(lambda x: not x % 15, nums)))

# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10)))))
#
# print([x ** 2 for x in range(10) if x % 2])


# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return "Hello, I am func 'hello'"
#
#
# text = hello
# print(text())


# def my_decorator(func):
#     def inner():
#         print("До кода")
#         func()
#         print("После кода")
#     return inner
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def inner():
#         print("-" * 30)
#         func()
#         print("*" * 30)
#     return inner
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
#
# @my_decorator
# def test():
#     print("Hello, I am func 'test'")
#
#
# func_test()
# test()


# lst = [input("-> ") for i in range(5)]
# print(lst)
# num = list(map(int, lst))
# print(num)

# def circle(fn):
#     def wrap():
#         return "(" + fn() + ")"
#
#     return wrap
#
#
# def angle(fn):
#     def wrap():
#         return "<" + fn() + ">"
#
#     return wrap
#
#
# @angle
# @circle
# def expression():
#     return '5 + 2'
#
#
# print(expression())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# def outer(fn):
#     def inner(arg1, arg2):
#         print("Данные:", arg1, arg2)
#         fn(arg1, arg2)
#
#     return inner
#
#
# @outer
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Ветрова")


# def outer(fn):
#     def inner(*args, **kwargs):
#         print("args:", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#
#     return inner
#
#
# @outer
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, end="\n\n")
#
#
# print_data("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_data("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)


# summa(5, 2)
# sub(5, 2)


# def multiply(arg):
#     def my_decorator(func):
#         def wrap(*args, **kwargs):
#             print(args)
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return my_decorator
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:
#                     raise TypeError("Неверный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) is not kwargs[k]:
#                     raise TypeError("Неверный тип данных")
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Hello"))
# print(typed_fn2("Hello", "World", "!"))
# # print(typed_fn2(3, 4, 5))
# print(typed_fn3("Hello", "World", z=5))
# print(typed_fn3("Hello", "World", z="!"))

# Строки

# print(bin(18))  # 0b10010 - двоичная система счисления
# print(oct(18))  # 0o22 - восьмеричная система счисления
# print(hex(18))  # 0x12 - шестнадцатеричная система счисления
#
# print(0b10010)
# print(0o22)
# print(0x12 + 0b10010 + 4)

# q = "Pyt"
# w = "hon"
# e = q + w
# print(e)
# # print(e * 3)
# # print("y" in e)
# # print("a" in e)
# # print(e[1])
# print(e[::-1])

# def change_char_to_str(s, old, new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == old:
#             s2 += new
#         else:
#             s2 += s[i]
#         i += 1
#
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# str2 = change_char_to_str(str1, "N", "P")
# print(str1)
# print(str2)

# print(u"Привет")
# print("Привет")


# print("C:\\file.txt")
# print(r"C:\file.txt\\"[:-1])
# print(r"C:\file.txt" + "\\")
# print("C:\\file.txt\\")

# print(b'1ab2c3')

# name = "Дмитрий"
# age = 25
# print(f"Меня зовут {name}. Мне {age} лет.")

# x = 10
# y = 5
# print(f"{x=}, {y=}")
# print("x=", x, ", y=", y, sep="")
# print(f"{round(10/7, 2)}")
# print(f"{10/7:.3f}")
# num = 74
# print(f"{{{{{num}}}}}")

# dir_name = "folder"
# file_name = "file.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)


# s = """Многострочный
#  те         кст
# """
# print(s)
# st = '''Много    строчный
# текст
# '''
# print(st)


# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     res = n ** 2
#     return res
#
#
# print(square(5))
# print(square.__doc__)
# print(sum.__doc__)
# print(min.__doc__)
# print(len.__doc__)

# from math import pi


# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания.
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('а'))
# print(ord('б'))


# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# st = "Test string for me"
# arr = [ord(x) for x in st]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
#
# if a > b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")


# print("apple" > "Apple")
# print(ord("a"))
# print(ord("A"))


# from random import randint
#
# SHORT = 8
# LONG = 16
# MIN_ASCII = 33
# MAX_ASCII = 123
#
#
# def random_password():
#     rand_len = randint(SHORT, LONG)
#     result = ""
#     for i in range(rand_len):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result


# print("Случайный пароль:", random_password())


# print(dir(str))

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Первый символ в строке в верхнем регистре, остальные в нижнем
# print(s.lower())  # все символы в нижнем регистре
# print(s.upper())  # все символы в верхнем регистре
# print(s.swapcase())  # инвертирование регистра символов
# print(s.title())  # первая буква каждого слова в верхнем регистре
# print(s.count("h", 1, -4))  # подсчет кол-ва заданных символов
# print(s.lower().count("i"))
# print(s.find("Python"))  # возвращает первый индекс подстроки
# print(s.find("h", 1, -4))  # если вхождение не найдено, то возвращается "-1"
# print(s.index("Python"))  # возвращает первый индекс подстроки
# print(s.index("h", 1, -4))  # если вхождение не найдено, то возвращается исключение ValueError
# st = "один два"
# st = "Hello World"
# one = st[:st.find(" ")]
# two = st[st.find(" ") + 1:]
# print(two + " " + one)


# print(s.rfind("h", 1, -4))  # возвращает последний индекс подстроки, если вхождение не найдено, то возвращается "-1"
# print(s.rindex("h", 1, -4))  # возвращает последний индекс подстроки, если вхождение не найдено,
# то возвращается исключение ValueError

# st = "I am learning Python. hello, WORLD!"
# print(st[:st.find('h')] + st[st.rfind("h") + 1:])

# print(s.startswith("he"))  # возвращает True, если строка начинается с заданной подстроки
# print(s.startswith("I am", 14))
# print(s.find("I am"))
#
# print(s.endswith("Python"))  # возвращает True, если строка заканчивается заданной подстрокой

# print('Фbc123'.isalnum())  # определяет состоит ли строка из букв и цифр
# print('abc%123'.isalnum())
# print(''.isalnum())
#
# print("ABCsvb".isalpha())  # определяет состоит ли строка из букв
# print("ABCsvb!".isalpha())
#
# print("45678".isdigit())  # определяет состоит ли строка из цифр

# print("abc".islower())  # определяет состоит ли строка из букв в нижнем регистре,
# # допускается наличие любых других символов
# print("Abc".islower())
# print("@#$$a23123".islower())
#
# print("ABC".isupper())  # определяет состоит ли строка из букв в верхнем регистре,
# # допускается наличие любых других символов
# print("#$$ABC2123".isupper())

# print('py'.center(10))  # выравниваем строку по центру
# print('py'.center(10, "-"))
# print('py'.center(1))


# print("    py".lstrip())  # удалит пробелы слева
# print("py    ".rstrip())  # удалит пробелы справа
# print("   py   ".strip())  # удалит пробелы слева и справа
#
# print("https://.python.org".lstrip("htps:/"))
# print("https://.python.org".rstrip("org."))
# print("https://.python.org".strip("htps:/org."))
#
# print("https://.python.org".lstrip("htps:/").rstrip("org."))


# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# print(str1.replace("Nython", "Python", 2))  # поиск и замена


# st = "-"
# seq = ("a", "b", "c")
# print(st.join(seq))  # объединяет итерируемую последовательность в строку
#
# print("..".join(['1', '99']))
# print(":".join("abc"))
# print(":".join("a"))


# print("Строка разделенная пробелами".split())  # строку преобразовывает в список по символу разделителю
# print("www.python.org".split("."))
# print("www.python.org.ru".split(".", 2))
#
#
# print("www.python.org".rsplit("."))
# print("www.python.org.ru".rsplit(".", 2))


# st = "Никонов Валерий Анатольевич"
# st = input("Введите ФИО: ").split()
# print(st)
# print(f"{st[0]} {st[1][0]}. {st[2][0]}.")


# num = input("Введите числа через пробел: ").split()
# print(num)
# num = list(map(float, num))
# print(num)
# print(sum(num))

# s = "I am learning Python. hello, WORLD!"
# a = s[:s.find("h")]
# b = s[s.find("h"):s.rfind("h") + 1]
# c = s[s.rfind("h") + 1:]
# print(a + b[::-1] + c)

# Регулярные выражения

# import re
# from itertools import count

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel-lo] Wor_ld 2000000000000000000"
# reg = r"\."
# print(re.findall(reg, s))  # список, содержащий все совпадения
# print(re.search(reg, s))  # месторасположение первого совпадения объекта
# # print(re.search(reg, s).span())
# # print(re.search(reg, s).start())
# # print(re.search(reg, s).end())
# # print(re.search(reg, s).group())
# print(re.match(reg, s))  # поиск совпадения только с начала строки
# print(re.split(reg, s))  # список, в котором строка разбита по заданном шаблону
# print(re.sub(reg, "!", s))  # поиск и замена

# print(dir(re))
# reg = r"[205]"
# reg = r"[0-9]"
# reg = r"[6-9]"
# reg = r"[12][0-9][0-9][0-9]"
# reg = r"[А-яЁё]"
# reg = r"[а-яА-ЯЁё]"

# reg = r"[A-Za-z\]\[-]"
# reg = r"[^0-9]"
# reg = r"[0-9]."
# reg = r"[0-9]..."
# reg = r"\d"
# reg = r"\D"
# reg = r"\s"
# reg = r"\S"
# reg = r"\S"
# reg = r"\w"
# reg = r"\W"
# reg = r"\AЯ ищу"
# reg = r"Wor_ld\Z"
# reg = r"сов\B"
# reg = r"\w+"
# reg = r"\d+"
# reg = r"20*"
# print(re.findall(reg, s))

# Кол-во повторений
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - от 0 до 1 повторения


# st = "Час в 24-часовом формате от 00 до 23. 2021-06-15T18:55. Минуты, в диапазоне от 00 до 59. 2021-06-15T01:09."
# reg = "[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, st))

# d = "Цифры: 7, +17, -24, 0013, 0.3"
# reg = r"[+-]?[\d.]+"
# print(re.findall(reg, d))

# d = "05-03-1987  # Дата рождения"
#
# print("Дата рождения:", re.sub(r"\s\s#.+", "", d))
#
# print(re.sub("-", ".", d))
#
# print("Дата рождения:", re.sub(r"\s\s#.+", "", re.sub("-", ".", d)))

# st = "author=Пушкин А.С.; title  = Евгений Онегин; price =200; year= 1831"
# # reg = r"\w+\s*=\s*\w+\s*\w+\.?\w?\.?"
# # reg = r"\w+\s*=[\w\s.]*"
# reg = r"\w+\s*=[^;]+"
# print(re.findall(reg, st))
#
# reg1 = r";\s"
# print(re.split(reg1, st))

# st = "12 сентября 2025 года  456789456"
# # reg = r"\d{4}"
# reg = r"\d{2,4}"
# # reg = r"\d{4,}"
# print(re.findall(reg, st))

# st = "+7 499 456-45-78, +74994564578, +7 (499) 456 45 78, 74994564578"
# reg = r"\+?7\d{10}"
# print(re.findall(reg, st))


# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта. 6789. [Hel-lo] Wor_ld 2000000000000000000"
# # reg = r"^\w+\s\w+"
# reg = r"\w+\s\w+$"
# print(re.findall(reg, s))


# def validate_login(login):
#     return re.findall(r"^[A-Za-z0-9_-]{3,16}$", login)
#
#
# print(validate_login("Python_master"))
# print(validate_login("P0012yt"))


# text = "<body>Примет жадного совпадения соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))

# *?, +?, ??
# {m,n}?, {,n}?, {m,}?


# st = "Петр, Ольга и Виталий отлично учатся!"
# reg = r"Петр|Ольга|Виталий|Наталья"
# print(re.findall(reg, st))

# st = "int = 4, float = 4.0f, double = 8.0, int"
# # reg = r"\w+\s*=\s*\d[.\w+]*"
# # reg = r"int\s*=\s*\d[.\w+]*|float\s*=\s*\d[.\w+]*"
# # reg = r"(?:int|float)\s*=\s*\d[.\w+]*"
# reg = r"((int|float)\s*=\s*(\d[.\w+]*))"
# print(re.findall(reg, st))

# d = "Word2016, PS6, AI5"
# reg = r"([A-Za-z]+)\d+"
# # reg = r"[A-Za-z]+(\d+)"
# print(re.findall(reg, d))
# print(re.search(reg, d))


# st = "5 + 7*2 - 4"
# # reg = r"\s*[+*-]\s*"
# reg = r"\s*([+*-])\s*"
# print(re.split(reg, st))

# s = "Я ищу совпадения в 2025 году. И я их найду в 2 счёта."
# reg = r"([0-9]+)\s(\D+)"
# print(re.search(reg, s).group(1))
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])


# s = "Самолет прилетает 10/23/2025. Будем рады вас видеть после 10/24/2025."
# reg = r"(\d{2})/(\d{2})/(\d{4})" # тут в фигурных даем сколько хотим цифр
# print(re.sub(reg, r"\2.\1.\3", s)) #делаем поиск и замену с помощью номера круглой скобки,меняем их местами и ставим .


# s = "yandex.com and yandex.ru"
# reg = r"(([a-z0-9-]{2,}\.)+[a-z]{2,4})"
# print(re.sub(reg, r"http://\1", s))


# s = "25-12-2021"  # 1900 - 2000
# reg = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])$"
# print(re.findall(reg, s))


# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))

# text = "hello world"
# print(re.findall(r"\w\+", text))
# print(re.findall(r"\w\+", text, re.DEBUG))

# text = "helLo worLd"
# reg = "l"
# print(re.findall(reg, text, re.IGNORECASE))

# text = """
# one
# two
# """
#
# # print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one.\w+", text, re.DOTALL))
#
# print(re.findall(r"one$", text))
# print(re.findall(r"one$", text, re.MULTILINE))


# print(re.findall("""
# [a-z.-]+    # part 1
# @           # @
# [a-z.] +    # part 2
# """, "test@mail.ru", re.VERBOSE))


# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))

# Рекурсия

# def elevator(n):  # 5
#     if n == 0:  # базовый случай
#         print("Вы в подвале")
#         return
#     # print("=>", n)
#     elevator(n - 1)  # 5 4 3 2 1
#     print(n, end=" ")
#
#
# n1 = int(input("На каком этаже вы находитесь: "))
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# # def sum_list(lst):  # [9]
# #     if len(lst) == 1:
# #         print(lst, "=> lst[0]:", lst[0])
# #         return lst[0]  # 9
# #     else:
# #         print(lst, "=> lst[0]:", lst[0])
# #         return lst[0] + sum_list(lst[1:])  # 1 + 3 + 5 + 7
# #
# #
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):  # 15, 16
#     convert = "0123456789ABCDEF"
#     if n < base:
#         return convert[n]  # "F"
#     else:
#         return to_str(n // base, base) + convert[n % base]  # to_str(254 // 16, 16) + 'E'
#
#
# print(to_str(254, 16))


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Berb"], "Alex", ["Bea", "Bill"], "Ann"]
# print(len(names))
# print(names[0])
# print(isinstance(names[0], list))
# print(names[1])
# print(isinstance(names[1], list))
# print(names[1][1])
# print(isinstance(names[1][1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Berb"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):  # ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Berb"], "Alex", ["Bea", "Bill"], ]
#     count = 0  # 10
#     for item in item_list:  # "Ann"
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))


# Файлы

# f = open("text.txt", 'r')
# # f = open(r"E:\Python522\text.txt", 'r')
# print(f)
# print(*f)
# f.close()
# print(f.closed)
# print(f.mode)
# print(f.name)
# print(f.encoding)

# f = open("text.txt", 'r')
# print(f.read(3))
# print(f.read())
# f.close()


# f = open("xyz.txt", "w")
# f.write("This is line1.\nThis is line2.\nThis is line3.\n")
# f.close()


# f = open("xyz.txt")
# # print(f.read())
#
# # print(f.readline())
# # print(f.readline(8))
# # print(f.readline())
# # print(f.readline())
#
# print(f.readlines(26))
# print(f.readlines())
# f.close()


# f = open("xyz.txt")
# for line in f:
#     print(line)
# f.close()

# count = 0
#
# f = open("xyz.txt")
# for line in f:
#     print(line)
#     count += 1
# f.close()
#
# print(count)


# f = open("xyz.txt")
# print(len(f.readlines()))
# f.close()


# f = open("test.txt", "w")
# f.write("Hello\nWorld\n")
# f.close()
#
# f = open("test.txt", "a")
# f.write("New text")
# f.close()

# lines = ["This is line1. ", "This is line2.\n", "This is line3."]
#
# f = open("test1.txt", "a")
# # f.write("New text")
# f.writelines(lines)
# f.close()

# names = ["Adam", ["Bob", ["Chet", "Cat"], "Barb", "Berb"], "Alex", ["Bea", "Bill"], "Ann"]
#
#
# def count_items(item_list):
#     a = 0
#     for items in item_list:
#         if isinstance(items, list):
#             a += count_items(items)
#         else:
#             a += 1
#     return a
#
#
# print(count_items(names))


# f = open(r"/Users/memetmemetov/Desktop/Python522/test1.txt")
# print(f)
# print(*f)

# f = open("xyz. txt", "w")
# f.write("Привет1.\n Привет2.")

# f = open("text2.txt", 'w')
# lst = [str(i) for i in range(1, 100, 5)]
# print(lst)
# for index in lst:
#     f.write(index + "\t")
# f.close()


# lst = "строка #1\n строка #2\n строка #2\n"
#
# with open("one.txt", "w") as f:
#     f.write(lst)
#
# with open("one.txt", "r") as fr, open("two.txt", "w") as fw:
#     for line in fr:
#         line = line.replace("строка", "линия")
#         fw.write(line)


# text = "Замена строки в текстовом файле\nизменить строку в списке\nзаписать список в файл\n"
#
# with open("test2.txt", "w") as f:
#     f.write(text)
#     line = f.readlines()

# import os
#
# print(os.getcwd())
# print(os.listdir(".."))
# print(os.mkdir("folder")®)


def kata_13_december(*args):
    new = list()
    for i in range(len(args)):
        if args[i] % 2 != 0:
            new.append(args[i])
    return new


print(kata_13_december(1, 3, 5, 6, 8, 7, 2, 4, 6, 8, 10))
# def kata_13_december(*args):
#     new = list()
#     for i in range(len(args)):
#         if args[i] % 2 != 0:
#             new.append(args[i])
#     return new
#
#
# print(kata_13_december(1, 3, 4, 2, 7))
