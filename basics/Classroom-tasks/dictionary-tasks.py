"""
1) Создайте словарь university, и заполните данными, которые бы отражали количество учащихся на разных факультетах (программирование, экономика, медицина). Внесите изменения в словарь согласно следующему: а) в одном из факультетов изменилось количество учащихся, б) в университете появился новый факультет(лингвистика), с) в университете был расформирован (удален) другой факультет (медицины). Вычислите общее количество учащихся в университете.
"""
# university = {
#   'computer science': 435,
#   'economics': 566,
#   'medicine': 211
# }
# university['computer science'] = 422

# university2 = {
#   'linguistics': 433
# }
# university.update(university2)

# university.pop('medicine')

# number_of_students = list(university.values())

# print(int(number_of_students[0]) + int(number_of_students[1]) + int(number_of_students[2]))
"""
2) Создайте словарь, где ключами являются числа, а значениями – строки. Поменяйте ключи и значения местами.
Например: исходный словарь - {1: ‘a’, 2: ‘b’, 3: ‘c’}
На выходе - {‘a’: 1, ‘b’: 2, ‘c’: 3}
"""
# dictionary = {1: 'a', 2: 'b', 3: 'c'}
# values = list(dictionary.values())
# keys = list(dictionary.keys())
# new_order = {values[0]: keys[0],
#             values[1]: keys[1],
#             values[2]: keys[2]}
# print(new_order)
"""
3) Создайте программу, которая запрашивает у вас количество гостей, которых вы хотите пригласить. Далее запрашивает у вас имена гостей поочередно. Как только вы введете последнего гостя программа должна выдать вам список гостей и их порядковые номера в виде словаря.
"""
# number_of_guests = int(input('Количество гостей: '))
# guest_dictionary = {}
# for i in range(number_of_guests):
#   names = input('Введите имя гостя: ')
#   guest_dictionary[i+1] = names
# print(guest_dictionary)
"""
4) Вы идете в магазин за продуктами. У вас есть список продуктов, в котором перечислены наименования продуктов и количество. Каждый раз, когда вы кладете тот или иной продукт в корзину, вы убираете этот продукт из списка. После того, как ваш список опустеет, вы идете к кассе и расплачиваетесь. Реализуйте данную задачу в вашем коде.
* Используйте все знания, которые вы получили
"""

# dictionary = {
#   "potato": 3,
#   "milk": 5,
#   "tomato": 4,
#   "carrot": 2
# }
# number_of_groceries = len(list(dictionary.keys()))
# print(dictionary)
# for i in range(number_of_groceries):
#   user_input = input()
#   dictionary.pop(f'{user_input}')
#   print(dictionary)


