"""
===============Srtings tasks No.1===============
Присвойте переменной string любую строку.
Распечатайте первый символ этой строки.
"""
# string = 'Makers'
# print(string[0])

"""
===============Srtings tasks No.2===============
Присвойте переменной string любую строку.
Выведите последний символ этой строки
"""
# string = 'Makers'
# print(string[-1])

"""
===============Srtings tasks No.3===============
Задайте любую строку переменной string,
Распечатайте последние 2 символа.
"""
# string = 'Makers'
# print(string[-2])
# print(string[-1])

"""
===============Srtings tasks No.4===============
Объявите переменную string со значением в виде любой строки.
Затем переверните её и распечатайте результат.
"""
# string = 'Makers' 
# print(string[::-1])
# ##############################################################Makers does not accept
 
"""
===============Srtings tasks No.5===============
Объявите две переменные string1, string2 со значениями в виде любых строк.
Затем склейте их в одну строку через пробел.
Выведите получившуюся строку в терминал.
"""
# string1 = 'makers'
# string2 = 'bootcamp'
# print(f'{string1} {string2}')
# ##############################################################Makers does not accept
"""
===============Srtings tasks No.6===============
Объявите переменную string со значением в виде любой строки.
Продублируйте ее 4 раза.
Распечатайте результат.
"""
# string = 'hey'
# print(string * 4)

"""
===============Srtings tasks No.7===============
Объявите переменную string со значением в виде любой строки.
Выведите её длину в консоль.
"""
# string = 'world'
# print(len(string))

"""
===============Srtings tasks No.8===============
Создайте переменную string со значением 'The quick brown fox jumps over the lazy dog'.
Замените все повторения буквы o символом * и сохраните результат в новой переменной.
Распечатайте новую переменную.
"""
# string = 'The quick brown fox jumps over the lazy dog'
# new_str = string.replace('o', '*')
# print(new_str)

"""
===============Srtings tasks No.9===============
Создайте переменную string со значением в виде любой строки.
Переведите все её символы в верхний регистр.
Распечатайте результат.
"""
# string = 'world'
# print(string.upper())

"""
===============Srtings tasks No.10===============
Объявите переменную string со значением в виде любой строки.
Переведите все её символы в нижний регистр.
"""
# string = 'World'
# print(string.lower())

"""
===============Srtings tasks No.11===============
Создайте переменную string со значением в виде любой строки.
Обменяйте местами первый и последний символы и выведите результат в консоль.(ваш код должен работать со строками любой длины)
"""
# string = 'Hello'
# first = string[0]
# last = string[-1]
# new_str = last + string[1:-1] + first
# print(new_str)

"""
===============Srtings tasks No.14===============
Создайте переменную string со значением в виде любой строки.
Выведите только символы с нечётными индексами при помощи срезов.
"""
# string = 'Hello'
# print(string[1::2])

"""
===============Srtings tasks No.15===============
Объявите переменную string со значением в виде любой строки.
Поменяйте шестую букву на K.
"""
# string = 'helloworld'
# new_str = string[:6] + 'K' + string[7:]
# print(new_str)