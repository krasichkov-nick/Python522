# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if - 1 <= a - c <= 1 and -1 <= b - d <= 1:
#     print('YES')
# else:
#     print('NO')   №  шахматный король
# import math
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if - 1 <= a - c <= 1 and -1 <= b - d <= 1:
#     print('YES')
# else:
#     print('NO')   #  шахматная ладья
from locale import windows_locale

# a_1 = int(input())        #  задача про отрезки
# b_1 = int(input())
# a_2 = int(input())
# b_2 = int(input())
# if a_2 < a_1:
#     a_1, b_1, a_2, b_2 = a_2, b_2, a_1, b_1
# if a_2 > b_1:
#     print("пустое множество")
# elif a_2 == b_1:
#     print(a_2)
# else:
#     if b_1 < b_2:
#         print(a_2, b_1)
#     else:
#         print(a_2, b_2)

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a - b) == (c - d) or (a + b) == (c + d):
#     print('YES')
# else:
#     print('NO')    #  ход слона
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a + b + c + d) % 2 == 0:
#     print('YES')
# else:
#     print('NO')    #  цвет шахматной доски

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# if (a + b + c + d) % 2 and a != c and b != d:
#     print('YES')
# else:
#     print('NO')  #  ход конем


# m, n = int(input()), int(input())
# for i in range(m + m % 2 - 1, n - 1, -2):
#         print(i)

# a = [int(input()) for i in range(int(input()))]

# n = int(input())
# s = 0
# for i in range(n):
#     num = int(input())
#     s += num
# print(s)
#

# s_1 = 0
# s_2 = 0
# n = int(input())
# for i in range(n):
#     num = int(input())
#     if num > s_1:
#         s_2 = s_1
#         s_1 = num
#     elif num > s_2:
#         s_2 = num
# print(s_1)
# print(s_2)

# n = int(input())
# a, b = 1, 1
#
# for i in range(n):
#     print(a, end=' ')
#     a, b = b, a + b # последовательность фибочи

# words = []
# a = input()
# while a != 'КОНЕЦ' and a != 'конец':
#     words.append(a)
#     a = input()
# for word in words:
#     print(word)

# words = []
# a = int(input())
# while a % 7 == 0:
#     words.append(a)
#     a = int(input())
# for word in words:
#     print(word)

# a = 0
# n = int(input())
# while 1 <= n <= 5:
#     if n == 5:
#         a += 1
#     n = int(input())
# print(a)

# a = 0
# n = int(input())
# while n >= 25:
#     a += 1
#     n = n - 25
# while n >= 10:
#     a += 1
#     n = n -10
# while n >= 5:
#     a += 1
#     n = n - 5
# while n >= 1:
#     a += 1
#     n = n -1
# print(a)

# num = 12345
# product = 1
# while num != 0:
#     last_digit = num % 10
#     product = product * last_digit
#     num = num // 10
# print(product)

# n = int(input())
# while n != 0:
#     last_digit = n % 10
#     n = n // 10
#     print(last_digit, end='')

# n = int(input())
# mn = 9
# mx = 0
# while n != 0:
#     last_digit = n % 10
#     if last_digit > mx:
#         mx = last_digit
#     if last_digit < mn:
#         mn = last_digit
#     n = n // 10
# print('Максимальная цифра равна', mx)
# print('Минимальная цифра равна', mn)

# n = int(input())
# s_1 = 0
# s_2 = 0
# s_3 = 1
# s_4 = 0
# s_5 = n
# s_6 = n % 10
# while n != 0:
#     last_digit = n % 10
#     s_1 += last_digit
#     s_2 += 1
#     s_3 *= last_digit
#     n = n // 10
# s_4 = s_1 / s_2
# s_5 = s_5 // 10 ** (s_2 - 1)
# print(s_1)  # сумма цифр
# print(s_2)  # кол-во цифр
# print(s_3)  # произведение цифр
# print(s_4)  # среднее арифметическое цифр
# print(s_5)  # первая цифра
# print(s_5 + s_6)  # сумма первой и последней цифр

# n = int(input())
# s_1 = 0
# while n != 0:
#     last_digit = n % 10
#     s_1 += last_digit
#     n = n // 10
# print(s_1)

# n = int(input())
# s_1 = 0
# s_2 = n
# while n != 0:
#     last_digit = n % 10
#     s_1 += 1
#     n = n // 10
# s_2 = (s_2 % 10 ** (s_1 - 1)) // 10 ** (s_1 - 2)
# print(s_2)

# n = int(input())
# flag = True
# last_digit = n % 10
# while n != 0:
#     last_digit_2 = n % 10
#     if last_digit_2 == last_digit:
#         last_digit_2 = last_digit
#     else:
#         flag = False
#         break
#     n = n // 10
# if flag == True:
#     print('YES')
# else:
#     print('NO')
#
# n = int(input())  # Вводим число число
# z = n % 10  # Находим последнюю цифру
# flag = 'YES'  # Вводим флажок
# while n != 0:  # Запускаем цикл
#     if z != n % 10:  # Сравниваем последнее число с последним числом каждой итерации
#         flag = 'NO'  # Если число не равно то флажок переходит в состояние NO
#     n = n // 10  # Удаляем лишнее
# print(flag)

# n = int(input())
# flag = True
# g = n % 10
# while n != 0:
#     s = n % 10
#     if s >= g:
#         g = s
#     else:
#         flag = False
#         break
#     n = n // 10
# if flag == True:
#     print('YES')
# else:
#     print('NO')

# n = input()  # слово наоборот
# for i in range(-1, -len(n) - 1, -1):
#     print(n[i])

# a = input()
# flag = 0
# for i in range(len(a)):
#     if a[i] in '0123456789':
#         flag = 'Цифра'
#         break
# else:
#     flag = 'Цифр нет'
# print(flag)

# n = input()
# a = 0
# for i in range(len(n) - 1):
#     if n[i] == n[i + 1]:
#         a += 1
# print(a)

# n = input()
# a = 0
# b = 0
# for i in range(len(n)):
#     if n[i] == '+':
#         a += 1
#     if n[i] == '*':
#         b += 1
# print('Символ + встречается', a, 'раз')
# print('Символ * встречается', b, 'раз')

# n = input()
# a = 0
# b = 0
# for i in range(len(n)):
#     if n[i] in 'ауоыиэяюеАУОЫИЭЯЮЕ':
#         a += 1
#     if n[i] in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
#         b += 1
# print('Количество гласных букв равно', a)
# print('Количество согласных букв равно', b)

# n = int(input())
# s = ""
# while n != 0:
#     g = n % 2
#     s = s + str(g)
#     n = n // 2
# for i in range(-1, -len(s) - 1, -1):
#     print(s[i], end="") # перевод в двоичную систему

# n = int(input())
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break

# n = input()
# a = n[0:len(n) - len(n) // 2]
# b = n[len(n) - len(n) // 2:len(n)]
# print(b + a)
#
# s = input()
# n = len(s)
#
# a = s[:(n + 1) // 2]
# b = s[(n + 1) // 2:]
# print(b + a)

# n = input()
# if n == n.title():
#     print('YES')
# else:
#     print('NO')

# n = input()
# print(n.swapcase())

# n = input().lower()
# if 'хорош' in n:
#     print('YES')
# else:
#     print('NO')

# n = input()
# s = 0
# a = n.lower()
# for i in range(len(n)):
#     if n[i] in a and n[i] not in '0123456789':
#         s += 1
# print(s)

# n = input()
# print(n.count(' ') + 1)

# n = input().lower()
# print('Аденин:', n.count('а'))
# print('Гуанин:', n.count('г'))
# print('Цитозин:', n.count('ц'))
# print('Тимин:', n.count('т'))

# n = int(input())
# s = 0
# for _ in range(n):
#     n = input()
#     if n.count('11') >= 3:
#         s += 1
# print(s)

# n = input()
# s = 0
# for i in range(10):
#     s += n.count(str(i))
# print(s)

# n = input()
# if n.endswith('.ru') or n.endswith('.com'):
#     print('YES')
# else:
#     print('NO')

# n = input()  # наиболее частый символ
# a = 0
# b = 0
# for i in n:
#     if n.count(i) >= a:
#         a = n.count(i)
#         b = i
# print(b)

# n = input()
# if n.count('f') == 1:
#     print(n.find('f'))
# elif n.count('f') > 1:
#     print(n.find('f'), n.rfind('f'))
# else:
#     print('NO')

# n = input()
# print(n[:n.find('h')] + n[n.rfind('h') + 1:])

# n = int(input())
# for i in range(1, n + 1):
#     a = input()
#     if a.isspace() is True or len(a) == 0:
#         print(i, ': COMMENT SHOULD BE DELETED', sep='')
#     else:
#         print(i, ': ', a, sep='')

# s = input()   #  Автомобильный номер
# flag = 'NO'
# a_cor = 'АВЕКМНОРСТУХ'
# if 9 <= len(s) <= 10:
#     a_text = s[0] + s[4:6]
#     b_digit = s[1:4] + s[7:]
#     c_und = s[6]
#     if b_digit.isdigit() and c_und == '_':
#         flag = 'YES'
#     for c in a_text:
#         if c not in a_cor:
#             flag = 'NO'
#             break
# print(flag)

# n = list(range(1, int(input()) + 1))
# print(n)

# n = int(input())
# s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
#      'x', 'y', 'z']
# print(s[:n])


# name = input()
# if 5 <= len(name) <= 15 and name.startswith('@') and name == name.lower() and name[1:].isalnum():
#     print('Correct')
# else:
#     print('Incorrect')

# text = f'By Imperial decree, Leto Atreides is now the fief of the planet {'Arrakis'}.'
# print(text)

# a, b = int(input()), int(input())
# s = f'Для чисел {a} и {b}:'
# s_1 = f'Сумма кубов: {a}**3 + {b}**3 = {a ** 3 + b ** 3}'
# s_2 = f'Куб суммы: ({a} + {b})**3 = {(a + b) ** 3}'
# print(s)
# print(' ', s_1)
# print(' ', s_2)

# a, b = int(input()), float(input())
# s = 100 - 0.2 * a
# if b > s:
#     print(f'Что-то пошло не так\n#{a} ДЕНЬ: ТЕКУЩИЙ ВЕС = {b} кг, ЦЕЛЬ по ВЕСУ = {s} кг')
# else:
#     print(f'Все идет по плану\n#{a} ДЕНЬ: ТЕКУЩИЙ ВЕС = {b} кг, ЦЕЛЬ по ВЕСУ = {s} кг')

# n = input()
# b = ord(n) + 1
# if n == 'Я':
#     print('Дальше букв нет')
# else:
#     print(chr(b))

# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

# n = input()
# for i in range(len(n)):
#     print(ord(n[i]), end=' ')

# a, b, c, d = input(), input(), input(), input()
# a_s, b_s, c_s, d_s = 0, 0, 0, 0
# for i in range(len(a)):
#     a_s += ord(a[i])
# for i in range(len(b)):
#     b_s += ord(b[i])
# for i in range(len(c)):
#     c_s += ord(c[i])
# for i in range(len(d)):
#     d_s += ord(d[i])
# mx = (max(a_s, b_s, c_s, d_s))
# if a_s == mx:
#     print(a)
# elif b_s == mx:
#     print(b)
# elif c_s == mx:
#     print(c)
# else:
#     print(d)

# n, s_old, s_new = input(), 0, 0
# eng, rus = 'eyopaxcETOPAHXCBM', 'еуорахсЕТОРАНХСВМ'
# for i in range(len(n)):
#     s_old += ord(n[i]) * 3
# for i in range(len(n)):
#     if n[i] in eng:
#         n = n.replace(n[i], rus[eng.find(n[i])])
#     s_new += ord(n[i]) * 3
# print(f"Старая стоимость: {s_old}🐝\nНовая стоимость: {s_new}🐝")

# n, s_old, s_new = input(), 0, 0
# eng, rus = 'eyopaxcETOPAHXCBM', 'еуорахсЕТОРАНХСВМ'
# for i in n:
#     s_old += ord(i) * 3
#     if i in eng:
#         eng_index = eng.index(i)
#         rus_index = eng_index
#         rus_n = rus[rus_index]
#         s_new += ord(rus_n) * 3
#     else:
#         s_new += ord(i) * 3
# print(f"Старая стоимость: {s_old}🐝\nНовая стоимость: {s_new}🐝")

# n = int(input())
# for i in range(1, n + 1):
#     if 5 <= i <= 9:
#         continue
#     if 17 <= i <= 37:
#         continue
#     if 78 <= i <= 87:
#         continue
#     print(i)

# n = 0
# while n < 10:
#     n += 2
#     print(n)
# else:
#     print('Цикл завершен.')

# count = 0
# p = 1
# for i in range(1, 11):
#     x = int(input())
#     if x >= 0:
#         p *= x
#         count += 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')

# mx = -10**6 - 1
# s = 0
# for i in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#     if x < 0 and x > mx:
#         mx = x
# if s < 0:
#     print(s)
#     print(mx)
# else:
#     print('NO')

# s = 0
# for i in range(7):
#     n = int(input())
#     if n % 2 == 0:
#         s += n
# if s < 0:
#     s = 0
# print(s)

# n = int(input())
# max_digit = -1
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:
#             max_digit = digit
#     n //= 10
# if max_digit == -1:
#     print('NO')
# else:
#     print(max_digit)

# n = int(input())
# while n >= 10:
#     n //= 10
# print(n)

# n = int(input())
# product = 1
# while n != 0:
#     digit = n % 10
#     product *= digit
#     n //= 10
# print(product)

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
#
# print(counter)

# n = int(input())
# for i in range(n):
#     for j in range(3):
#         print(n, end=' ')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=' ')
#     print()

# n = int(input())   #  разобраться!!!
# for i in range(n):
#     for j in range(i + 1):
#         if j >= n - i:
#             continue
#         print('*', end='')
#     print()

# n = int(input())
# for i in range(n + 1):
#     for j in range(i):
#         print(i, end='')
#     print()

# total = 0
# for x in range(1, 13):
#     for y in range(1, 12):
#         for z in range(1, 11):
#             if x * 28 + y * 30 + z * 31 == 365:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)

# total = 0
# for x in range(1, 10):
#     for y in range(1, 20):
#         for z in range(1, 200):
#             if x * 10 + y * 5 + z * 0.5 == 100 and x + y + z == 100:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)

# for a in range(1, 151):       #  Гипотеза Эйлера о сумме степеней
#     for b in range(a + 1, 151):
#         for c in range(b + 1, 151):
#             for d in range(c + 1, 151):
#                 e = int(((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)) ** 0.2)
#                 if e ** 5 == int((a ** 5) + (b ** 5) + (c ** 5) + (d ** 5)):
#                     print(a + b + c + d + e)
#                     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)

# n = int(input())
# s = 1
# for i in range(n + 1):
#     for j in range(1, i + 1):
#         print(s, end=' ')
#         s += 1
#     print()

# n = int(input())
# s = 1
# for i in range(n + 1):
#     for j in range(1, i + 1):
#         print(s, end=' ')
#         s += 1
#     print()

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2,
#            12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 in numbers and 17 in numbers:
#     print('YES')
# else:
#     print('NO')
# print(numbers[1:-1])

# n = int(input())
# numbers = []
# for _ in range(n):
#     n = input()
#     numbers.append(n)
# print(numbers)

# numbers = []
# for i in range(26):
#     numbers.append(chr(ord('a') + i) * (i + 1))
# print(numbers)

# n = int(input())
# numbers = []
# for _ in range(n):
#     n = int(input())
#     numbers.append(n ** 3)
# print(numbers)

# n = int(input())
# numbers = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         numbers.append(i)
# print(numbers)

# n = int(input())
# numbers = []
# a = 0
# for i in range(n):
#     b = int(input())
#     numbers.append(a + b)
#     a = b
# del numbers[0]
# print(numbers)

# n = int(input())
# numbers = []
# for _ in range(n):
#     n = int(input())
#     numbers.append(n)
# del numbers[1:len(numbers):2]
# print(numbers)

# n = int(input())
# numbers = []
# for _ in range(n):
#     n = input()
#     numbers.append(n)
# k = int(input())
# s = ''
# for i in range(len(numbers)):
#     if len(numbers[i]) > (k - 1):
#         s += numbers[i][k - 1]
# print(s)

# n = int(input())
# numbers = []
# for _ in range(n):
#     n = input()
#     numbers.extend(n)
# print(numbers)

# s = 0
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# for num in numbers:
#      s += num ** 2
# print(s)

# z = []
# x = []
# n = int(input())
# for _ in range(1, n + 1):
#     n = int(input())
#     z.append(n)
#     x.append(n ** 2 + 2 * n + 1)
# print(*z, sep='\n')
# print()
# print(*x, sep='\n')

# lst = []
# n = int(input())
# for _ in range(n):
#     n = int(input())
#     lst.append(n)
# lst.remove(min(lst))
# lst.remove(max(lst))
# print(*lst, sep='\n')

# lst = []
# n = int(input())
# for _ in range(n):
#     n = input()
#     if n not in lst:
#         lst.append(n)
# print(*lst, sep='\n')

# lst = []
# n = int(input())
# for _ in range(n):
#     n = input()
#     lst.append(n)
# z = input()
# for j in lst:
#     if z.lower() in j.lower():
#         print(j)

# lst_n = []
# lst_z = []
# lst_y = []
# n = int(input())
# for _ in range(n):
#     n = input()
#     lst_n.append(n)
# z = int(input())
# for _ in range(z):
#     z = input()
#     lst_z.append(z)
# for i in range(len(lst_n)):
#     count = 0
#     for j in range(len(lst_z)):
#         if lst_z[j].lower() in lst_n[i].lower():
#             count += 1
#     if count == len(lst_z):
#         lst_y.append(lst_n[i])
# print(*lst_y, sep='\n')

# n = int(input())
#
# # принимаем все строки
# strings = []
# for _ in range(n):
#     s = input()
#     strings.append(s)
#
# k = int(input())
#
# # принимаем все поисковые запросы
# search_queries = []
# for _ in range(k):
#     search_query = input()
#     search_queries.append(search_query)
#
# # идём по каждой строке
# for s in strings:
#     # идём по каждому запросу
#     for search_query in search_queries:
#         # если хотя бы какого-то поискового запроса не оказывается в строке,
#         # то выходим из этого цикла
#         if search_query.lower() not in s.lower():
#             break
#     else:
#         # если мы не вышли из цикла через break,
#         # значит, все поисковые запросы были найдены в строке
#         print(s)

# lst_n = []
# lst_z = []
# lst_a = []
# n = int(input())
# for _ in range(n):
#     n = int(input())
#     if n < 0:
#         lst_n.append(n)
#     if n == 0:
#         lst_z.append(n)
#     if n > 0:
#         lst_a.append(n)
# print(*(lst_n + lst_z + lst_a), sep='\n')

# text = input()
# print(*(text.split()), sep='\n')

# text = input().split()
# for i in text:
#     print(i[0], end='.')

# n = 1
# text = input().split()
# for i in text:
#     n = '+' * int(i)
#     print(*n, sep='')

# text = input().split('.')
# for i in range(len(text)):
#     if int(text[i]) > 255 or int(text[i]) < 0:
#         print('НЕТ')
#         break
# else:
#     print('ДА')

# text = input()
# n = input()
# print(n.join(text))

# n = input().split()
# s = 0
# for i in range(len(n)):
#     for j in range(i + 1, len(n)):
#         if int(n[j]) == int(n[i]):
#             s += 1
# print(s)

# numbers = [8, 9, 10, 11]
# numbers.pop(1)
# numbers.insert(1, 17)
# numbers.extend([4, 5, 6])
# numbers.remove(8)
# numbers = numbers * 2
# numbers.insert(3, 25)
# print(numbers)

# numbers = input().split()
# mn = min(numbers, key=int)
# mx = max(numbers, key=int)
# a = numbers.index(mn)
# b = numbers.index(mx)
# numbers[a], numbers[b] = numbers[b], numbers[a]
# print(*numbers)

# s = (input().lower()).split()
# print('Общее количество артиклей:', s.count('a') + s.count('an') + s.count('the'))

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a.pop(3))

# n = int(input())
# s = 0
# z = 1
# for i in range(1, n + 1):
#     z *= i
#     s += z
# print(s)

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for k in range(i-1, 0, -1):
#         print(k, end='')
#     print()
#
# a, b = int(input()), int(input())
# sm = 0
# mx = 0
# for i in range(a, b + 1):
#     s = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             s += j
#         if s >= sm and i >= mx:
#             sm = s
#             mx = i
# print(mx, sm)

# n = int(input())
# for i in range(1, n + 1):
#     s = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             s += 1
#     print(i, end='')
#     print('+' * s)

# n = int(input())
# while n > 9:
#     n = n // 10 + n % 10
# print(n)

# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     s = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             s += 1
#     if s == 2:
#         print(i)

# n = int(input())
# s = 0
# while n > 0:
#     if n % 2 == 0:
#         s += n % 10
#     n //= 10
# print(s)

# n = 8
# count = 0
# maximum = -10 ** 8 - 1
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# count = 0
# maximum = -1
# for i in range(4):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = int(input())
# for i in range(1, n + 1):
#     if i == 1 or n == i:
#         print('*' * 19)
#     else:
#         print('*' + ' ' * 17 + '*')

# n = int(input())
# while n > 999:
#     n //= 10
# print(n % 10)

# n = int(input())
# a = 0
# b = 0
# c = 0
# d = 0
# e = 1
# g = 0
# last_digit = n % 10
# while n > 0:
#     x = n % 10
#     if x == 3:
#         a += 1
#     if x == last_digit:
#         b += 1
#     if x % 2 == 0:
#         c += 1
#     if x > 5:
#         d += x
#     if x > 7:
#         e *= x
#     if x == 0 or x == 5:
#         g += 1
#     n //= 10
# print(a)
# print(b)
# print(c)
# print(d)
# print(e)
# print(g)

# [1729, 4104, 13832, 20683, 32832]

# a = []
# n = int(input()[1:])
# for _ in range(n):
#     n = input()
#     if '#' in n:
#         n = n[0:n.index('#')].rstrip()
#     a.append(n)
# for j in a:
#     print(j)

# n = input()
# a = n.split()
# b = [int(i) for i in a]
# print(b)
# b.sort()
# print(*b)
# b.sort(reverse=True)
# print(*b)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [i[1:] for i in keywords]
#
# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# lengths = [len(i) for i in keywords]
#
# print(lengths)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
#               'elif',
#             'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [i for i in keywords if len(i) >= 5]
#
# print(new_keywords)


# palindromes = [i for i in range(100, 1001) if str(i) == str(i)[::-1]]
#
# print(palindromes)

# numbers = [i ** 2 for i in range(1, int(input()) + 1)]
# for i in numbers:
#     print(i)

# n = input()
# a = n.split()
# b = [int(i) for i in a]

# numbers = [int(i) ** 3 for i in input().split()]
# for i in numbers:
#     print(i, end=' ')

# numbers = [print(int(i) ** 2, end=' ') for i in input().split() if int(i) % 2 == 0 and (int(i) ** 2) % 10 != 4]

# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97,
#      -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0,
#      -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63,
#      -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]
#
# n = len(a)
#
# for i in range(n - 1):
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#
# print(a)


# def draw_triangle():
#     for i in range(11):
#         print("*" * i)
#
#
# draw_triangle()

# def change_us(a, b):
#     a = 0
#     b = 0
#     print(a, b)
#
# x = 1
# y = 7
# print(x, y)
# change_us(x, y)
# print(x, y)


# def draw_triangle(fill, base):
#     for i in range(base):
#         for j in range(i + 1):
#             if j >= base - i:
#                 continue
#             print(fill, end='')
#         print()
#
#
# fill = input()
# base = int(input())
# draw_triangle(fill, base)


# def print_fio(name, surname, patronymic):
#     print(surname[0], name[0], patronymic[0], sep="")
#
#
# name, surname, patronymic = input().upper(), input().upper(), input().upper()
#
# print_fio(name, surname, patronymic)


# def print_digit_sum(num):
#     num = 0
#     for i in range(len(n)):
#         num += int(n[i])
#     print(num)
#
#
# n = input()
# print_digit_sum(n)

# def greet(name="Guest"):
#     return f"Hello, {name}!"
#
#
# print(greet("Alice"))
# print(greet())
