"""
===============Integers tasks No.1===============
Объявите переменную num со значением типа данных int и распечатайте ее
"""
# num = 11
# print(num)

"""
===============Integers tasks No.2===============
Объявите переменную word со значением типа данных str и распечатайте ее
"""
# word = '11'
# print(word)

"""
===============Integers tasks No.3===============
Объявите переменные number и string.
Переменной number присвойте числовое значение (целое число от 1 до 10),
Переменной string присвойте строку (не более 10 символов).
Умножьте переменную string на number
Распечатайте результат
"""
# number = 5 
# string = 'Oomat'
# print(string * number)

"""
===============Integers tasks No.4===============
Объявите две переменные x, y со значениями в виде целых чисел.
Сложите их и распечатайте результат
"""
# x = 4
# y = 5
# print(x + y)

"""
===============Integers tasks No.5===============
Создайте две переменные x, y со значением типа int.
Разделите первое на второе и распечатайте результат
"""
# x = 4
# y = 5
# print(x / y)

"""
===============Integers tasks No.6===============
Создайте 2 переменные positive и negative

positive - положительное целое число
negative - отрицательное целое число
Распечатать модули этих чисел, при помощи встроенной функции abs()
"""
# positive = 5
# negative = -32
# print(abs(positive))
# print(abs(negative))

"""
===============Integers tasks No.7===============
Создайте целое число x.
Возведите его в куб с помощью встроенной функции
Распечатайте результат.
"""
# x = 3
# print(pow(x,3))

"""
===============Integers tasks No.8===============
Создать две переменные x, y со значением типа int.
Найдите остаток от деления первого на второе и распечатайте результат
"""
# x = 6
# y = 2
# print(x%y)

"""
===============Integers tasks No.9===============
Создать целое число y.
Возведите его в квадрат и найдите остаток от деления на 5 и распечатайте результат.
"""
# y = 5
# print(y**2%5)

"""
===============Integers tasks No.10===============
Примите от пользователя 3 числа inp1, inp2, inp3 из вкладки INPUT,
Перемножьте первые два числа,
Найдите остаток от деления на третье число.
Распечатайте полученный результат.
"""
# inp1 = int(input())
# inp2 = int(input())
# inp3 = int(input())
# print(inp1*inp2%inp3)

"""
===============Integers tasks No.11===============
Примите от пользователя 2 целых числа num1, num2,
Cоздайте ещё одну переменную num3 со значением типа float.
Найдите остаток от деления первых двух чисел,
Умножьте остаток на третье число
Распечатайте результат
"""
# num1 = int(input())
# num2 = int(input())
# num3 = 4.2
# print(num1 % num2 * num3)

"""
===============Integers tasks No.12===============
Создать десятичное число с переменной decimal.
Найдите и распечатайте его квадрат, куб, квадратный корень.
"""
# decimal = 4.2
# print(decimal ** 2)
# print(decimal ** 3)
# print(decimal ** 0.5)

"""
===============Integers tasks No.13===============
В переменные a, b запишите два числа, которые будут обозначать два катета прямоугольного треугольника .
Рассчитайте длину гипотенузы треугольника c, воспользовавшись теоремой Пифагора.
Note: Теорема Пифагора: a ** 2 + b ** 2 = c ** 2.

Распечатайте результат
"""
# a = 2
# b = 3
# c = a ** 2 + b ** 2
# print(c ** 0.5)

"""
===============Integers tasks No.14===============
Задать радиус окружности в переменной r.
Рассчитайте площадь окружности в переменной s.
Note: Для получения числа π можете воспользоваться модулем math.

Распечатайте результат
"""
# import math 
# r = 3
# s = math.pi * r ** 2
# print(s)

"""
===============Integers tasks No.15===============
Объявите три переменные с целочисленными значениями first, second, third.
Затем обменяйте их значения в одно действие.
Переменной first присвойте значение переменной second.
Переменной third присвойте значение переменной first.
Переменной second присвойте значение переменной third.
"""
# first = 1
# second = 2
# third = 3
# first, second, third = second, third, first 
# print(first, second, third)