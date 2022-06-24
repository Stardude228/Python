"""
===============Built-in functions tasks No.1===============
Дан список:
Выведите сумму всех этих чисел, результат сохраните в новой переменной result и выведите в консоль.
Используйте встроенную функцию.
"""
# import functools 
# list_ = [1, 2, 3, 4]  
# result = 0
# result = functools.reduce(lambda x, y: x + y, list_)
# print(result)

"""
===============Built-in functions tasks No.2===============
Создайте переменную list_ и сохраните в нем список из чисел. Проверьте, что все числа больше трёх, результат сохраните в новой переменной result и выведите в консоль. Используйте встроенную функцию.
"""
# list_ = [1, 5, -9, 6, -4]
# result = all(int > 3 for int in list_) 
# print(result)

"""
===============Built-in functions tasks No.3===============
Создайте переменную list_ и сохраните в нем список из чисел. Проверьте, что в нём есть отрицательные числа, результат сохраните в новой переменной result и выведите в консоль.
"""
# list_ = [5, 8, 4, 6, 7]
# result = any(int < 0 for int in list_) 
# print(result) 

"""
===============Built-in functions tasks No.4===============
Создайте переменную list_ и сохраните в нем список из чисел. Создайте новый список, состоящий из квадратов этих чисел, результат сохраните в новой переменной result и выведите в консоль.
"""
# list_ = [1, 2, 3, 4]  
# result = list(map(lambda x: x ** 2, list_)) 
# print(result)

"""
===============Built-in functions tasks No.5===============
Создайте переменную list_ и сохраните в нем список из чисел. Отфильтруйте этот список, оставив только чётные числа, результат сохраните в новой переменной result и выведите в консоль.
"""
# list_ = [1, 2, 3, 4] 
# result = list(filter(lambda number : number%2 == 0 , list_))  
# print(result) 

"""
===============Built-in functions tasks No.6===============
Создайте переменную list_ и сохраните в нем список со строками. Отфильтруйте этот список, оставив только те строки, длина которых больше 7 символов. Результат сохраните в новой переменной result и выведите в консоль.
"""
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni',]
# result = list(filter(lambda string : len(string) > 7 , list_))
# print(result) 

"""
===============Built-in functions tasks No.7===============
Создайте переменную list_ и сохраните в нем список из чисел. Выведите произведение всех этих чисел. Результат сохраните в новой переменной result и выведите в консоль. Используйте библиотеку reduce.
"""
# import functools 
# list_ = [5, 6, 7, 8] 
# result = functools.reduce(lambda x, y: x * y, list_)
# print(result)

"""
===============Built-in functions tasks No.8===============
Создайте переменную list_ и сохраните в нем список из чисел. Посчитате количество чётных и нечётных чисел в этом списке в переменных list2 и list3. Результат сохраните в новой переменной result и выведите в консоль в виде строки:
"""
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ] 
# list2 = len(list(filter(lambda int : int % 2 == 0 , list_)))
# list3 = len(list(filter(lambda int : int % 2 == 1 , list_)))
# result = (f'even: {list2}, odd: {list3}')
# print(result)

"""
===============Built-in functions tasks No.9===============
Создайте переменную list_ и сохраните в нем список из чисел. Если число в списке меньше 0, замените его на False, если больше, то на True. Результат сохраните в новой переменной result и выведите в консоль.
"""
# list_ = [-1, 2, 3, 5, -3, 7] 
# result = list(map(lambda x: x > 0 , list_))
# print(result)

"""
===============Built-in functions tasks No.10===============
Создайте переменную list_ и сохраните в нем список со строками. Найдите самое длинное имя из списка функцией reduce. Результат сохраните в новой переменной result и выведите в консоль.
"""
# import functools
# list_ = ['Paul', 'George', 'Ringo', 'John'] 
# result = functools.reduce(lambda x, y: x if len(x) > len(y) else y, list_)
# print(result)