"""
===============Files tasks No.1===============
Откройте файл task1.txt. В нём записаны числа от 1 до 10 в столбец. Выведите первые 5 элементов в вашем файле в терминал (Подсказка: используйте метод для построчного считывания).
"""
# file = open('task1.txt')
# numbers = file.readlines(8)
# for i in numbers:
#     print(i)
# file.close()

"""
===============Files tasks No.2===============
Откройте файл task2.txt. В нём записаны числа от 1 до 10 в столбец. Распечатайте все числа, не используя методы.
"""
# file = open('task2.txt')
# for i in file:
#     print(i)
# file.close()

"""
===============Files tasks No.3===============
Откройте файл task3.txt в режиме записи. Запишите в него числа от 0 до 9 через символ *. Затем вернитесь в начало файла и распечатайте записанные числа. Вывод должен быть:
"""
# with open('task3.txt', 'w+') as file:
#     numbers = [str(i) for i in range(10)]
#     numbers2 = ''
#     for i in numbers:
#         numbers2 += i + '*'
#     file.write(numbers2)
#     file.seek(0)
#     print(numbers2)

"""
===============Files tasks No.4===============
Откройте файл task4.txt. В нём в нескольких строках записан текст. Прочтите содержимое и распечатайте количество строк.
"""
# with open('task4.txt') as file:
#     res = file.read()
#     lines_number = 0
#     for i in res:
#         if i == '\n':
#             lines_number += 1
#     print(lines_number)

"""
===============Files tasks No.5===============
Откройте файл task5.txt. В нём записаны целые числа. Прочтите эти числа, затем найдите максимальное затем минимальное число. Затем запишите эти числа в новый файл task6.txt через символ - (сначала минимальное, потом максимальное)
"""
# with open('task5.txt') as file:
#     res = file.read().split(' \n')
#     def func(i):
#         return int(float(i))
#     res1 = list(map(func, res))
#     max_number = max(res1)
#     min_number = min(res1)

# file2 = open('task6.txt', 'w+')
# file2.write(f'{min_number}-{max_number}')
# file2.seek(0)
# print(file2.read())
# file2.close()


# with open('task5.txt') as file:
#     num = [int(i) for i in file]
#     with open('task6.txt', 'w') as file1:
#         file1.write(f'{min(num)}-{max(num)}')