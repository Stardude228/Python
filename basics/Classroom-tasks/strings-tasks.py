"""
  По теме: Строки
"""
"""
1) Напишите программу, которая будет запрашивать пользовательские данные: имя, фамилию, возраст. Далее программа должна проделать следующие операции: в имени убрать все буквы ‘a’(если они есть), в фамилии - разделить все буквы разделителем *. В конце программа выдает вам объединенную строку, состоящую из полученных имени и фамилии, при этом данная строка должна повторяться столько раз, сколько составляет возраст пользователя.

Например:
Ввод: Введите имя, фамилию и возраст через пробел: John Snow 4
Вывод: JоhnS*n*o*wJоhnS*n*o*wJоhnS*n*o*wJоhnS*n*o*w

"""
print('Введите свои пользовательские данные:')
user_info = input('Введите имя, фамилию и возраст через пробел: ').split()
user_name = user_info[0]
user_surname = user_info[1]
user_age = int(user_info[2])

final_user_name = user_name.replace('a', '')
final_user_surname = '*'.join(user_surname)

print((final_user_name + final_user_surname) * user_age)

"""

2) Напишите программу, которая высчитывает количество гласных букв в введенной пользователем строке. И программа выдает вам следующее предложение: В вашей строке насчитано n гласных букв.

Например:
Ввод: Введите строку: I love Makers Bootcamp!
Вывод: В вашей строке насчитано 8 гласных букв

Примечание: не использовать конкатенацию

"""
user_string = str(input('Введите строку: '))
lowered_user_string = user_string.lower()

found_a = lowered_user_string.count('a')
found_e = lowered_user_string.count('e')
found_i = lowered_user_string.count('i')
found_y = lowered_user_string.count('y')
found_o = lowered_user_string.count('o')
found_u = lowered_user_string.count('u')

final_result = found_a + found_e + found_i + found_y + found_o + found_u
print('В вашей строке насчитано', final_result, 'гласных букв')

"""
3) Напишите программу, которая просит пользователя ввести свой юзернейм (одним словом) и генерирует пароль из юзернейма, добавив в конец строки символ $, в середину символ &, и заменив строчные буквы на заглавные и наоборот.

Например:
Ввод: Введите юзернейм: JohnSnow
Вывод: Вам сгенерирован пароль: jOHN&sNOW$
"""
username = str(input('Введите юзернейм: '))
username_length = int(len(username) // 2)

username_part1 = username[:username_length].swapcase()
username_part2 = username[username_length:].swapcase()

print(f"Вам сгенерирован пароль: {username_part1}&{username_part2}$")
