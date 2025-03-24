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

lst_1 = [-2, 3, 8, -11, -4, 6, -9]
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

text = "Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;"
with open("test.txt", "w") as f:
    f.write(text)

with open("test.txt", "r") as f:
    lst = f.read().split("\n")

print(lst)

pos1 = int(input("Введите позицию 1-й строки: ")) - 1
pos2 = int(input("Введите позицию 2-й строки: ")) - 1
s = len(lst)

if (pos1 < 0) or (pos1 >= s) or (pos2 < 0) or (pos2 >= s):
    print(f'\nВ файле {s} строки.\nВводимые значения должны быть в диапазоне от 1 до {s}\nВведите корректные значения'
          f' позиций строк для их замены')
    exit()

lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

with open("test.txt", "w") as f:
    f.write("\n".join(lst))

print(lst)
