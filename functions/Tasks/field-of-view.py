"""
===============Scopes tasks No.1===============
Вам дана вложенная функция:Внесите изменения в функции bar таким образом чтобы при вызове функции foo и при попытке распечатать переменную var в глобальной области видимости, выводился следующий результат:
"""
# def foo():
#     global var
#     var = 'переменная foo'
#     print('переменная в foo: ', var)
#     def bar():
#         global var
#         var = 'переменная bar'
#         print('переменная в foo: ', var)
#     bar()
#     var = 'переменная foo' 
# foo()


"""
===============Scopes tasks No.2===============
У вас есть глоабльная переменная x со значением Я глобальная переменная!. Напишите функцию my_func()которая изменяет значение этой переменной на Я могу изменяться, т.е если вы после вызова функции распечатаете переменную x вне функции она должна возвращать вам значение Я могу изменяться.
"""
# x = 'Я глобальная переменная!'
# print(x)
# def my_func():
#     global x
#     x = 'Я могу изменяться'
# my_func()
# print(x)
# print(globals())

"""
===============Scopes tasks No.3===============
Дана глобальная переменная num со значением 3. Напишите функцию mul которая будет возвращать квадрат этой переменной и записывать результат в глобальную переменную num. Вызовите функцию три раза, и распечатайте переменную num.
"""
# num = 3
# def mul():
#     global num
#     num = num ** 2
#     return num
# mul()
# mul()
# mul()
# print(num)

"""
===============Scopes tasks No.4===============
Напишите небольшую программу для подсчета доходов и расходов.

У вас есть глобальная переменная balance = 0 общий счет.

Программа должна состоять из трех функций: get_salary(amount) - функция для увеличения баланса, которая принимает в аргументы amount - заработная плата и увеличивает переменную balance на число переданное в amount.

pay_bills(amount, log_name) - уменьшает баланс на количество amount , log_name - принимает строку - на что были потрачены деньги и распечатывает результат, например если мы вызвали pay_bills(300, 'интернет')

функция распечатывает строку в виде "Вы заплатили 300 сом за интернет"
И функция get_balance(), которая будет распечатывать вам строку:У вас на счету `n` сом
где n - это текущее значение глобальной переменной balance.

Вызовите функции в данном порядке:
get_salary(1000)
get_balance()
pay_bills(400, 'кабельное тв')
get_balance()
Результат в консоли:
У вас на счету 1000 сом
Вы заплатили 400 сом за кабельное тв
У вас на счету 600 сом
"""

# balance = 0

# def get_salary(amount):
#     global balance
#     balance = balance + amount

# def pay_bills(amount, log_name):
#     global balance
#     balance = balance - amount
#     print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     global balance
#     print(f'У вас на счету {balance} сом')

# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()

"""
===============Scopes tasks No.5===============
В Python есть встроенная арифметическая функция pow(), pow принимает два обязательных аргумента x, y и один необязательный z и возвращает результат в виде x**y % z - возводит первое число в степень y и если передано третье число, делит результат на третье число и возвращает остаток.
У вас есть глобальная переменная result = 0. Напишите функции pow_first(x,y), отвечает за первую часть встроенной функции pow и pow_second(z), отвечает за вторую часть pow(z). Вызовите эти функции, а затем выведите переменную result.
"""
# result = 0

# def pow_first(x, y):
#     global result
#     result = x ** y
# def pow_second(z):
#     global result
#     result = result % z

# pow_first(2, 3)
# pow_second(3)
# print(result)

"""
===============Scopes tasks No.6===============
Мурат с друзьями на выходных решил собратся и пойти в ночной клуб.Но в ночной клуб пропускают только тех, кому 17+. Создайте словарь ключами которого являются имена Мурата и его друзей, а значениями являются их возраст.
Напишите программу которая определяет кого пустить в ночной клуб а кого нет.
"""
# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}
# for name, age in a.items():
#     if age >= 17:
#         print(f'{name}, Вы можете войти в клуб')
#     else:
#         print(f'{name}, извините, Вы не проходите по age-control')

"""
===============Scopes tasks No.7===============
Вам дан список a из нескольких имён в нижнем регистре. Напишите программу которая превращает имена из списка в имена, где первая буква имени в верхнем регистре.Запишите результат в новый список b и выведите переменную b.
"""
# a = ['pipi', 'papa', 'mama']
# b = []
# for i in a:
#     i = i.title()
#     b.append(i)
# print(b)

"""
===============Scopes tasks No.8===============
Напишите функцию count_symbols() которая принимает строку и возвращает количество гласных, согласных букв и остальных символов. Используйте только кириллические символы. Распечатайте вызов функции.
"""
# def count_symbols(string):
#     string = string.lower()
#     vowels = 0
#     consonant = 0
#     other_symbols = 0
#     for i in string:
#         if i in 'яыуаеиоюэё':
#             vowels += 1
#         elif i in 'йфчцвсмкптрнгьблшщджзхъ':
#             consonant += 1
#         else:
#             other_symbols += 1
#     return(f'Количество гласных: {vowels}, согласных: {consonant}, остальных символов: {other_symbols}')
# print(count_symbols('Мурат супер!'))

"""
===============Scopes tasks No.9===============
Создайте пустой список a. Напишите программу которая должна записывать в ваш список числа от 0 до 10. Распечатайте переменную a.
"""
# a = []
# def write_down():
#     for i in range(0,11):
#         a.append(i)
# write_down()
# print(a)

"""
===============Scopes tasks No.10===============
Определите перемнную a в котором будут хранится список из целых чисел.Напишите программу которая выводит все элементы этого списка, которые меньше 7.
"""
# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]
# b = []
# numbers = ''
# def lower_than_seven():
#     for i in a:
#         if i < 7:
#             b.append(i)
#     for j in b:
#         global numbers
#         numbers += str(j)
# lower_than_seven()
# print(numbers)