"""
1) Напишите программу, которая запрашивает с ввода семь чисел через запятую, добавляет их в список. На экран выводит первое и последнее число списка. Затем удаляет последнее число и вместо него вставляет слово “Makers”.
Например: 
Ввод: Введите цифры через запятую: 5, 7, 8, 1, 3, 0, 8
Вывод: 5 8
[5, 7, 8, 1, 3, 0, ‘Makers’]
"""
# user_data = input('Введите 7 цифр через запятую: ') 
# str_user_data = user_data.replace(', ', '')
# print(user_data[0], user_data[-1])
# list_user_data = list(str_user_data)
# list_user_data.pop()
# list_user_data.append('Makers')
# print(list_user_data)

"""
2) Напишите программу, которая генерирует 10 случайных чисел, добавляет их в список и возвращает вам список этих чисел в отсортированном виде в порядке возрастания.
"""
# import random
# list1 = []
# for i in range(10):
#   i = random.randint(1, 10)
#   list1.append(i)
# list1.sort()
# print(list1)
"""
3) Напишите программу, которая заполняет список словами, введенными с клавиатуры, измеряет длину каждого слова и добавляет полученное значение в другой список. Например, список слов – ['yes', 'no', 'maybe', 'ok', 'what'], список длин – [3, 2, 5, 2, 4]. Оба списка должны выводиться на экран. yes no maybe ok what
"""
# user_list = input('Введите слова через пробел: ').split()
# if ',' in user_list:
#   print('error')
# else:
#   computer_list = []
#   for i in range(len(user_list)):
#     computer_list.append(len(user_list[i]))
#   print(user_list)
#   print(computer_list)
  