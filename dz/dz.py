# dz_1
#
# a = "papa"
# b = "mama"
# print("a:", a)
# print("b:", b)
#
# a, b = b, a
# print("a:", a)
# print("b:", b)
#
# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
#
# a = a + b
# b = a - b
# a = a - b
# print("a:", a)
# print("b:", b)
# dz_2
#
# num = int(input("Введите пятизначное число: "))
# num1 = num // 10000
# num2 = num % 10000 // 1000
# num3 = num % 1000 // 100
# num4 = num % 100 // 10
# num5 = num % 10
# res1 = num1 * num2 * num3 * num4 * num5
# res2 = (num1 + num2 + num3 + num4 + num5) / 5
# print("Произведение цифр пятизначного числа:", res1)
# print("Среднее арифметическое цифр пятизначного числа:", round(res2, 2))
# dz_3
#
# n = int(input('Введите число от 1 до 99: '))
# if 1 <= n <= 99:
#     if 11 <= n <= 14:
#         print(n, 'копеек')
#     elif n % 10 == 1:
#         print(n, 'копейка')
#     elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
#         print(n, 'копейки')
#     else:
#         print(n, 'копеек')
# else:
#     print('Ошибка ввода данных')
#
# a = int(input('Введите число от 1 до 99: '))
# kop = a
# if 11 <= kop <= 14:
#     print(a, 'копеек')
# elif 1 <= a <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, 'копейка')
#     elif 2 <= kop <= 4:
#         print(a, 'копейки')
#     else:
#         print(a, 'копеек')
# else:
#     print('недопустимое значение') # дз работает быстрее
# dz_4
#
# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
# print('Результат: ', res)
# dz_5
#
# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# s = 0
# for i in a:
#     if i < 0:
#         s += i
# print('Сумма отрицательных элементов: ', s)
# dz_6
#
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# for i in range(len(s)):
#     for j in range(len(s)):
#         if i != j and s[i] == s[j]:
#             break
#     else:
#         print(s[i], end=' ')
#
# s = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# print(s)
# for i in s:
#     if s.count(i) == 1:
#         print(i, end=' ')
# dz_7
# from math import sin, pi
# print('Выберите фигуру:', '\n', '1 - треугольник', '\n', '2 - прямоугольник', '\n', '3 - круг', sep='')
# n = int(input())
# while n < 1 or n > 3:
#     print('Выберите фигуру:', '\n', '1 - треугольник', '\n', '2 - прямоугольник', '\n', '3 - круг', sep='')
#     n = int(input())
# if n == 1:
#     print('Введите сторону a:', '\n', 'Введите сторону b:', '\n', 'Введите сторону c:', sep='')
#     a, b, c = int(input()), int(input()), int(input())
#     print('Площадь треугольника:', round(1 / 2 * c * b * sin(a), 2))
# elif n == 2:
#     print('Введите сторону a:', '\n', 'Введите сторону b:', sep='')
#     a, b = int(input()), int(input())
#     print('Площадь прямоугольника:', round(a * b, 2))
# else:
#     print('Введите радиус a:')
#     a = int(input())
#     print('Площадь круга:', round(pi * a ** 2, 2))
# dz_8
# from math import pi, sqrt
#
#
# def square_rectangle(a, b):
#     return a * b
#
#
# def square_triangle(a, b, c):
#     p = None
#     p = (a + b + c) / 2
#     return sqrt(p * (p - a) * (p - b) * (p - c))
#
#
# def square_circle(a):
#     return pi * a ** 2
#
#
# s = None
# figure = int(input('Выберите фигуру:\n1-прямоугольник\n2-треугольник\n3-круг\n: '))
# if figure == 1:
#     x = int(input('Введите сторону a - '))
#     y = int(input('Введите сторону b - '))
#     s = square_rectangle(x, y)
# if figure == 2:
#     x = int(input('Введите сторону a - '))
#     y = int(input('Введите сторону b - '))
#     z = int(input('Введите сторону c - '))
#     s = square_triangle(x, y, z)
# if figure == 3:
#     x = int(input('Введите радиус - '))
#     s = square_circle(x)
# print('Площадь фигуры:', round(s, 2))
# dz_9
# from random import randint
#
# s1 = tuple(randint(0, 5) for _ in range(10))
# s2 = tuple(randint(-5, 0) for _ in range(10))
# s3 = s1 + s2
# print('Третий кортеж: ', s3)
# print('Количество нулей в третьем кортеже: ', s3.count(0))
#
# from random import randint
#
#
# def ran (a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5, 0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print('0=', tpl3.count(0))
# dz_10
# from tokenize import group

# d = {
#     'John': {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom': {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne': {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451},
# }
#
# for i in d:
#     print(i)
#     for j in d[i]:
#         print(j, ':', d[i][j])
# name, region = input('Имя: '), input('Регион: ')
# print(d[name][region])
# a = int(input('Новое значение: '))
# d[name][region] = a
# print(d[name])
# dz_11
# n = int(input('Количество студентов: '))
# a = []
# b = []
# for i in range(n):
#     c = input(str(i + 1) + '-й студент: ')
#     a.append(c)
#     d = int(input('Балл: '))
#     b.append(d)
# sr = round(sum(b) / n, None)
# d = dict(zip(a, b))
# print('Средний балл: ', sr, '. ', 'Студенты с баллом выше среднего:', sep='')
# for i in d:
#     if d[i] > sr:
#         print(i)
# dz_12
#
# Вариант 1
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
#
# Вариант 2
# s = 0
#
#
# def rect_paral(a, b, c):
#     def inner(i, j):
#         return i * j
#     global s
#     s = 2 * (inner(a, b) + inner(a, c) + inner(b, c))
#
#
# rect_paral(2, 4, 6)
# print(s)
# rect_paral(5, 8, 2)
# print(s)
# rect_paral(1, 6, 8)
# print(s)
#
# Вариант 3
#
#
# def rect_paral(a, b, c):
#     ss = 0
#
#     def inner(i, j):
#         nonlocal ss
#         ss += i * j
#
#     inner(a, b)
#     inner(a, c)
#     inner(b, c)
#
#     return 2 * ss
#
#
# print(rect_paral(2, 4, 6))
# print(rect_paral(5, 8, 2))
# print(rect_paral(1, 6, 8))
# dz_13
#
# from math import pi
#
# d = {'Круг': 2, 'Прямоугольник': (10, 13), 'Трапеция': (7, 5, 3)}
# print('Площадь окружности радиуса 2:', (lambda r: pi * r ** 2)(d['Круг']))
# print('Площадь прямоугольника размером 10*13:',
#       (lambda a: lambda b: a * b)(d['Прямоугольник'][0])(d['Прямоугольник'][1]))
# print('Площадь трапеции для a=7, b=5, h=3:',
#       (lambda a: lambda b: lambda h: (a + b) * h / 2)(d['Трапеция'][0])(d['Трапеция'][1])(d['Трапеция'][2]))
# dz_14
#
#
# def my_decorator(func):
#     def wrap(*args):
#         func(*args)
#         return print('Среднее арифметическое чисел', ', '.join(str(i) for i in args), '=', sum(args) / len(args))
#
#     return wrap
#
#
# @my_decorator
# def return_num(*args):
#     return print('Сумма чисел', ', '.join(str(i) for i in args), '=', sum(args))
#
#
# return_num(2, 3, 3, 4)
# dz_15
#
# st = "I am learning Python. hello, World!"
# print(st[:st.find('h') + 1] + st[st.find('h'):st.rfind('h')][::-1] + st[st.rfind('h') + 1:])
# dz_16
#
# import re
# st = input("Введите дату в формате dd-mm-YYYY: ")
# reg = r"[0-3][0-9]-[0-1][0-9]-[1-2][0-9][0-9][0-9]"
# #  1.не понял как выполнить условие ^^^ соответствия века (19 или 20)
# #  2.также при введении неверных данных метод re.split не отрабатывает
# #  и выбрасывает ошибку (ему нечего разбивать)
# #  3.не выполнено условие задачи вывода данных в кортеже, как?
# # print(re.findall(reg, st))
# reg2 = r"-"
# print(re.split(reg2, *(re.findall(reg, st))))
# dz_17

# lst_1 = [-2, 3, 8, -11, -4, 6, -9]
#
#
# def count_otr(lst):
#     if len(lst) == 0:
#         return 0
#     else:
#         n = 1 if lst[0] < 0 else 0
#         return n + count_otr(lst[1:])
#
#
# print(count_otr(lst_1))

# lst_1 = [-2, 3, 8, -11, -4, 6, -9]
#
#
# def count_otr(lst):
#     if not lst:
#         return 0
#     count = 0
#     if lst[0] < 0:
#         count += 1
#     return count + count_otr(lst[1:])
#
#
# print(count_otr(lst_1))

# dz_18
# text = "Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;"
# with open("test.txt", "w") as f:
#     f.write(text)
#
# with open("test.txt", "r") as f:
#     lst = f.read().split("\n")
#
# print(lst)
#
# pos1 = int(input("Введите позицию 1-й строки: ")) - 1
# pos2 = int(input("Введите позицию 2-й строки: ")) - 1
# s = len(lst)
#
# if (pos1 < 0) or (pos1 >= s) or (pos2 < 0) or (pos2 >= s):
#     print(f'\nВ файле {s} строки.\nВводимые значения должны быть в диапазоне от 1 до {s}\nВведите корректные значения'
#           f' позиций строк для их замены')
#     exit()
#
# lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
#
# with open("test.txt", "w") as f:
#     f.write("\n".join(lst))
#
# print(lst)
# dz_19
#
# print("Заливка прошла успешно :)")
# dz_20
#
#
# import os
# import shutil
#
# dir_name = "Work"
#
# os.makedirs("Work/empty_files", exist_ok=True)
# dir_new = "Work/empty_files"
#
# for root, directory, file in os.walk(dir_name):
#     for file_size in file:
#         d = os.path.join(root, file_size)
#         p = os.path.getsize(d)
#         if p > 0:
#             print(d, p, '- bytes')
#         else:
#             shutil.move(d, dir_new)
#             # os.replace(d, dir_new)  #  не получилось переместить файлы,
#             # выдает ошибку права доступа
#             print(file_size, 'из каталога', root, 'был перемещен в каталог Work/empty_files')
# dz_21
# class Auto:
#
#     def __init__(self, model, year, produce, power, color, price):
#         self.model = model
#         self.year = year
#         self.produce = produce
#         self.power = power
#         self.color = color
#         self.price = price
#
#     def print_info(self):
#         print(" Данные автомобиля ".center(40, "*"))
#         print(f"Название модели: {self.model}\nГод выпуска: {self.year}\n"
#               f"Производитель: {self.produce}\nМощность двигателя: {self.power}\n"
#               f"Цвет машины: {self.color}\nЦена: {self.price}")
#         print("=" * 40)
#
#     def set_model(self, model):
#         self.model = model
#
#     def get_model(self):
#         return self.model
#
#     def set_year(self, year):
#         self.year = year
#
#     def get_year(self):
#         return self.year
#
#     def set_produce(self, produce):
#         self.produce = produce
#
#     def get_produce(self):
#         return self.produce
#
#     def set_power(self, power):
#         self.power = power
#
#     def get_power(self):
#         return self.power
#
#     def set_color(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#     def set_price(self, price):
#         self.price = price
#
#     def get_price(self):
#         return self.price
#
#
# a1 = Auto("X7 M501", "2021", "BMW", "530 л.с.", "white", "10790000")
# a1.print_info()
# a1.set_power(32)
# a1.print_info()
# dz_22
# class Convert:
#     def __init__(self, x=12):
#         self.__x = x
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     @property
#     def x(self):
#         return f"{self.__x} кг =>, {round(self.__x * 2.205, 2)} фунтов"
#
#     @x.setter
#     def x(self, x):
#         if Convert.__check_value(x):
#             self.__x = x
#         else:
#             print("Килограммы задаются только числами")
#
#
# p1 = Convert()
# print(p1.x)
# p1.x = 41
# print(p1.x)
# p1.x = "abc"
# dz_23

#
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
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def get_num(self):
#         return self.__num
#
#     def get_surname(self):
#         return self.__surname
#
#     def get_percent(self):
#         return self.__percent
#
#     def get_value(self):
#         return self.__value
#
#     def set_num(self, num):
#         self.__num = num
#
#     def set_surname(self, surname):
#         self.__surname = surname
#
#     def set_percent(self, percent):
#         self.__percent = percent
#
#     def set_value(self, value):
#         self.__value = value
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} закрыт!")
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
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print("-" * 20)
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#
# acc = Account("12345", "Долгих", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# acc.set_surname("Дюма")
# acc.print_info()
# print()
#
# acc.set_num(54321)
# acc.print_info()
# print()
#
# acc.set_percent(0.1)
# acc.print_info()
# print()
#
# acc.set_value(10000)
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

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
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
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
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, surname):
#         self.__surname = surname
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
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.__num} принадлежащий {self.__surname} закрыт!")
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
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         eur_val = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {eur_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"#{self.__num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print("-" * 20)
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#
# acc = Account("12345", "Долгих", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
#
# acc.surname = "Дюма"
# acc.print_info()
# print()
#
# acc.num = 98765
# acc.print_info()
# print()
#
# acc.percent = 0.2
# acc.print_info()
# print()
#
# acc.value = 10000
# acc.print_info()
# print()
#
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
#
# acc.withdraw_money(3000)
# print()
#
# acc.add_money(5000)
# print()
#
# acc.withdraw_money(3000)
# print()

# dz_24
#
# class Pair:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @staticmethod
#     def verify_a(a):
#         if not isinstance(a, int) or isinstance(a, float) or a <= 0:
#             raise TypeError("Вводимое значение должно быть положительным числом")
#
#     @staticmethod
#     def verify_b(b):
#         if not isinstance(b, int) or isinstance(b, float) or b <= 0:
#             raise TypeError("Вводимое значение должно быть положительным числом")
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, a):
#         self.verify_a(a)
#         self.__a = a
#
#     @property
#     def b(self):
#         return self.__b
#
#     @b.setter
#     def b(self, b):
#         self.verify_b(b)
#         self.__b = b
#
#     def composition(self):
#         print(f"Произведение: {self.a * self.b}")
#
#     def amount(self):
#         print(f"Сумма: {self.a + self.b}")
#
#
# class RightTriangle(Pair):
#     def __init__(self, a, b):
#         super().__init__(a, b)
#
#     def hypotenuse_t(self):
#         return round((self.a ** 2 + self.b ** 2) ** 0.5, 2)
#
#     def hypotenuse(self):
#         print(f"Гипотенуза треугольника ABC: {self.hypotenuse_t()}")
#
#     def triangle_info(self):
#         print(f"Треугольник ABC со сторонами ({self.a}, {self.b}, {self.hypotenuse_t()})")
#
#     def square(self):
#         p = (self.a + self.b + self.hypotenuse_t()) / 2
#         s = round(((p * (p - self.a) * (p - self.b) * (p - self.hypotenuse_t())) ** 0.5), 2)
#         print(f"Площадь треугольника ABC: {s}")
#
#
# r1 = RightTriangle(5, 8)
# r1.hypotenuse()
# r1.triangle_info()
# r1.square()
# print()
# r1.amount()
# r1.composition()
# print()
# r1.a = 10
# r1.b = 15
# r1.hypotenuse()
# r1.a = 24
# r1.hypotenuse()
# r1.amount()
# r1.composition()
# r1.square()
# dz_25

# class Human:
#     def __init__(self, surname, name, age):
#         self.surname = surname
#         self.name = name
#         self.age = age
#
#     def human_info(self):
#         print(self.surname, self.name, self.age, end="")
#
#
# class Student(Human):
#     def __init__(self, surname, name, age, vector, group, bal):
#         super().__init__(surname, name, age)
#         self.vector = vector
#         self.group = group
#         self.bal = bal
#
#     def student_info(self):
#         return f"{self.human_info()}, {print("", self.vector, self.group, self.bal)}"
#
#
# class Teacher(Human):
#     def __init__(self, surname, name, age, prof, skill):
#         super().__init__(surname, name, age)
#         self.prof = prof
#         self.skill = skill
#
#     def teacher_info(self):
#         return f"{self.human_info()}, {print("", self.prof, self.skill)}"
#
#
# class Graduate(Student):
#     def __init__(self, surname, name, age, vector, group, bal, tema):
#         super().__init__(surname, name, age, vector, group, bal)
#         self.tema = tema
#
#     def graduate_info(self):
#         return f"{self.student_info()}, {print(self.tema)}"
#
#
# s1 = Student("Батодалаев", "Даши", 16, "ГК", "Web_011", 5)
# s2 = Student("Загидуллин", "Линар", 32, "РПО", "PD_011", 5)
# s3 = Graduate("Шугани", "Сергей", 15, "РПО", "PD_011", 5, "Защита персональных данных")
# s4 = Teacher("Даньшин", "Андрей", 38, "Астрофизика", 110)
# s5 = Student("Маркин", "Даниил", 17, "ГК", "Python_011", 5)
# s6 = Teacher("Башкиров", "Алексей", 45, "Разработка приложений", 20)
# s1.student_info()
# s2.student_info()
# s3.graduate_info()
# s4.teacher_info()
# s5.student_info()
# s6.teacher_info()
# dz_26

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.dd = self.Comp().show()
#
#     def show(self):
#         print(self.name, "=>", self.dd)
#
#     class Comp:
#         def __init__(self, model="HP", cpu="i7", memory=16):
#             self.model = model
#             self.cpu = cpu
#             self.memory = memory
#
#         def show(self):
#             return f"{self.model}, {self.cpu}, {self.memory}"
#
#
# s1 = Student("Roman")
# s2 = Student("Vladimir")
# s1.show()
# s2.show()

# class Clock:
#     __DAY = 86400
#
#     def __init__(self, sec: int):
#         if not isinstance(sec, int):
#             raise ValueError("Секунды должны быть целым числом")
#         self.sec = sec % self.__DAY
#
#     def get_format_time(self):
#         s = self.sec % 60
#         m = (self.sec // 60) % 60
#         h = (self.sec // 3600) % 24
#         return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"
#
#     @staticmethod
#     def __get_form(x):
#         return str(x) if x > 9 else "0" + str(x)
#
#     def __add__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec + other.sec)
#
#     def __sub__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         if other.sec > self.sec:
#             return Clock((self.sec - other.sec) * (-1))
#         return Clock(self.sec - other.sec)
#
#     def __mul__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec * other.sec)
#
#     def __floordiv__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec // other.sec)
#
#     def __mod__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return Clock(self.sec % other.sec)
#
#     def __eq__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec == other.sec
#
#     def __ne__(self, other):
#         return not self.__eq__(other)
#
#     def __lt__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec < other.sec
#
#     def __it__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec < other.sec
#
#     def __le__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec <= other.sec
#
#     def __ge__(self, other):
#         if not isinstance(other, Clock):
#             raise ArithmeticError("Правый операнд должен быть типом данных Clock")
#         return self.sec >= other.sec
#
#
# c1 = Clock(200)
# c2 = Clock(300)
# c3 = c1 + c2
# c4 = c1 - c2
# c5 = c1 * c2
# c6 = c1 // c2
# c7 = c1 % c2
# print(c1.get_format_time())
# print(c2.get_format_time())
# print(c3.get_format_time())
# print(c4.get_format_time())
# print(c5.get_format_time())
# print(c6.get_format_time())
# print(c7.get_format_time())
# print("Операторы ==, !=")
# print(c1 == c2)
# print(c1 != c2)
# print("Операторы <, >")
# print(c1 < c2)
# print(c1 > c2)
# print("Операторы <=, >=")
# print(c1 <= c2)
# print(c1 >= c2)
#
# from abc import ABC, abstractmethod
#
#
# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("=" * 20)
#         fn(*args, **kwargs)
#         print("=" * 20)
#
#     return wrap
#
#
# class Shape:
#     def __init__(self, figura, a, color):
#         self.type = figura
#         self.a = a
#         self.color = color
#
#     @abstractmethod
#     def perimetr(self):
#         pass
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def show(self):
#         pass
#
#     @abstractmethod
#     def info(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, a, color):
#         super().__init__("Квадрат", a, color)
#
#     def perimetr(self):
#         return self.a * 4
#
#     def area(self):
#         return self.a ** 2
#
#     def show(self):
#         for i in range(self.a):
#             print(self.a * "*")
#
#     @dec
#     def info(self):
#         print(
#             f"{self.type}\nСторона: {self.a}\nЦвет: {self.color}\nПериметр: {self.perimetr()}"
#             f"\nПлощадь: {self.area()}")
#         return self.show()
#
#
# class Rectangle(Shape):
#     def __init__(self, a, b, color):
#         super().__init__("Прямоугольник", a, color)
#         self.b = b
#
#     def perimetr(self):
#         return (self.a + self.b) * 2
#
#     def area(self):
#         return self.a * self.b
#
#     def show(self):
#         for i in range(self.a):
#             print(self.b * "*")
#
#     @dec
#     def info(self):
#         print(
#             f"{self.type}\nСторона 1: {self.a}\nСторона 2: {self.b}\nЦвет: {self.color}\nПериметр: {self.perimetr()}"
#             f"\nПлощадь: {self.area()}")
#         return self.show()
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c, color):
#         super().__init__("Треугольник", a, color)
#         self.b = b
#         self.c = c
#
#     def perimetr(self):
#         return self.a + self.b + self.c
#
#     def area(self):
#         p = self.a + self.b + self.c
#         return round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5, 2)
#
#     def show(self):
#         for i in range(self.a):
#             for j in range(i + 1):
#                 if j >= self.a - i:
#                     continue
#                 print("*", end=" ")
#             print()
#
#     @dec
#     def info(self):
#         print(
#             f"{self.type}\nСторона 1: {self.a}\nСторона 2: {self.b}\nСторона 3: {self.c}\nЦвет: {self.color}\n"
#             f"Периметр: {self.perimetr()}\nПлощадь: {self.area()}")
#         return self.show()
#
#
# s1 = Square(3, "red")
# s1.info()
# s2 = Rectangle(3, 7, "green")
# s2.info()
# s3 = Triangle(11, 6, 6, "yellow")
# s3.info()


# import json
# from random import choice
#
#
# def gen_person():
#     name = ''
#     tel = ''
#     number = ''
#
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'k', 'l', 'n']
#     nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#
#     while len(number) != 10:
#         number += choice(nums)
#
#     while len(name) != 7:
#         name += choice(letters)
#
#     while len(tel) != 10:
#         tel += choice(nums)
#
#     person = {number: {'name': name, 'tel': tel}}
#
#     return person
#
#
# def write_json(person_dict):
#     try:
#         data = json.load(open("persons.json"))
#     except FileNotFoundError:
#         data = {}
#
#     data.update(person_dict)
#     with open('persons.json', 'w') as f:
#         json.dump(data, f, indent=2)
#
#
# for i in range(5):
#     write_json(gen_person())

#
# import json

# countries = {}
#
#
# def add_country():
#     country = input("Введите название страны: ")
#     capital = input("Введите название столицы: ")
#     countries[country] = capital
#     save_data()
#
#
# def save_data():
#     with open("countries.json", "w") as f:
#         json.dump(countries, f)
#         print("Данные сохранены.")
#
#
# def load_data():
#     global countries
#     try:
#         with open("countries.json", "r") as f:
#             print(json.load(f))
#     except FileNotFoundError:
#         print("Файл с данными не найден.")
#
#
# def remove_country():
#     country = input("Введите название страны для удаления: ")
#     if country in countries:
#         del countries[country]
#         save_data()
#     else:
#         print("Такой страны нет в словаре.")
#
#
# def search_country():
#     country = input("Введите название страны для поиска: ")
#     if country in countries:
#         print(f"Столица страны {country}: {countries[country]}")
#     else:
#         print("Такой страны нет в словаре.")
#
#
# def edit_country():
#     country = input("Введите название страны для редактирования: ")
#     if country in countries:
#         new_capital = input("Введите новое название столицы: ")
#         countries[country] = new_capital
#         save_data()
#     else:
#         print("Такой страны нет в словаре.")
#
#
# while True:
#     print(
#         "*" * 20,
#         "\nВыбор действия:\n"
#         "1 - добавление данных\n"
#         "2 - удаление данных\n"
#         "3 - поиск данных\n"
#         "4 - редактирование данных\n"
#         "5 - просмотр данных\n"
#         "6 - завершение работы")
#     n = int(input("Ввод: "))
#     if n == 6:
#         print("Программа завершена")
#         print("*" * 20)
#         break
#     elif n == 1:
#         add_country()
#     elif n == 2:
#         remove_country()
#     elif n == 3:
#         search_country()
#     elif n == 4:
#         edit_country()
#     elif n == 5:
#         load_data()

# import json


# class CountryCapital:
#     @staticmethod
#     def load(file_name):
#         try:
#             data = json.load(open(file_name, encoding="utf-8"))
#         except FileNotFoundError:
#             data = {}
#         finally:
#             return data
#
#     @staticmethod
#     def add_country(file_name):
#         new_country = input("Введите название страны: ").lower()
#         new_capital = input("Введите название столицы: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name, encoding="utf-8"))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         data[new_country] = new_capital
#
#         with open(file_name, "w", encoding="utf-8") as f:
#             json.dump(data, f, indent=2, ensure_ascii=False)
#
#     @staticmethod
#     def load_from_file(file_name):
#         with open(file_name, encoding="utf-8") as f:
#             print({k.capitalize(): v.capitalize() for k, v in json.load(f).items()})
#
#     @staticmethod
#     def delete_country(file_name):
#         del_country = input("Введите название страны: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name, encoding="utf-8"))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         if del_country in data:
#             del data[del_country]
#
#             with open(file_name, "w", encoding="utf-8") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#
#         else:
#             print("Такой страны в базе нет")
#
#     @staticmethod
#     def search_data(file_name):
#         country = input("Введите название страны: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name, encoding="utf-8"))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             print(f"Страны {country.capitalize()} столица {data[country].capitalize()} есть в словаре")
#         else:
#             print(f"Страны {country.capitalize()} нет в словаре")
#
#     @staticmethod
#     def edit_data(file_name):
#         country = input("Введите страну для корректировки: ").lower()
#         new_capital = input("Введите новое название столицы: ").lower()
#
#         # try:
#         #     data = json.load(open(file_name, encoding="utf-8"))
#         # except FileNotFoundError:
#         #     data = {}
#         data = CountryCapital.load(file_name)
#
#         if country in data:
#             data[country] = new_capital
#             with open(file_name, "w", encoding="utf-8") as f:
#                 json.dump(data, f, indent=2, ensure_ascii=False)
#         else:
#             print("Такой страны в базе нет")
#
#
# file = "list_capital.json"
# while True:
#     index = input("Выбор действия:\n1-добавление\n2-удаления\n3-поиск\n4-редактирование\n5-просмотр\n6-завершение\nВвод: ")
#     if index == "1":
#         CountryCapital.add_country(file)
#     elif index == "2":
#         CountryCapital.delete_country(file)
#     elif index == "3":
#         CountryCapital.search_data(file)
#     elif index == "4":
#         CountryCapital.edit_data(file)
#     elif index == "5":
#         CountryCapital.load_from_file(file)
#     elif index == "6":
#         break
#     else:
#         print("Введен некорректный номер")


# import csv
# import requests
# import json
#
#
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
#
#
# with open("todos_writer.csv", "w") as f:
#     writer = csv.DictWriter(f, delimiter=";", lineterminator="\r", fieldnames=todos[0].keys())
#     writer.writeheader()
#     for d in todos:
#         writer.writerow(d)

# c = frozenset([1, 2, 3]) == {1, 2, 3}
# print(c)

# from bs4 import BeautifulSoup
# import requests
# import csv
#
#
# def get_html(url):
#     r = requests.get(url)
#     return r.text
#
#
# def write_csv(data):
#     with open("dz_plugins.csv", "a") as f:
#         writer = csv.writer(f, delimiter=";", lineterminator="\r")
#         writer.writerow([data["name"], data["url"], data["price"]])
#
#
# def get_data(html):
#     soup = BeautifulSoup(html, "lxml")
#     p1 = soup.find_all("div", class_="item")
#     for item in p1:
#         name = item.find("a", class_="name").text
#         url = item.find("div", class_="buyfloat").find("a").get("href")
#         price = item.find("i", class_="pprice").text
#
#         data = {"name": name, "url": url, "price": price}
#         write_csv(data)
#
#
# def main():
#     url = "https://pos-center.ru/tag-grocery-store/"
#     get_data(get_html(url))
#
#
# if __name__ == '__main__':
#     main()

from parsers import Parser


def main():
    for i in range(1, 4):
        pars = Parser(f"https://optimumbelt.ru/products/category/men?page={i}", 'belt.txt')
        pars.run()


if __name__ == '__main__':
    main()