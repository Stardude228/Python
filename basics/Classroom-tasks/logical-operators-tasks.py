"""
  По теме: Логические и условные Операторы
"""
"""
1) Создайте программу, которая будет требовать пароль и проверять, содержатся ли в нем только числа, при этом длина пароля не должна быть менее 8 символов . Если все эти условия выполняются, то программа выдает вам сообщение ‘Ваш пароль сохранен’, если же нет - то программа должна указать необходимое условие для сохранения вашего пароля.

Например:
Ввод: Введите пароль: Makers12345
Вывод: Ваш пароль должен хранить только числа

Ввод: Введите пароль: a12345
Вывод: Ваш пароль должен содержать не менее 8 символов
Ваш пароль должен содержать только буквы

"""
password = input('Введите пароль: ')
if password.isnumeric() == True and len(password) > 8:
  print('Всё правильно')
elif password.isnumeric() != True:
  if len(password) < 8:
    print('Ваш пароль должен содержать не менее 8 символов и должен содержать только буквы')
  else:
    print('Ваш пароль должен хранить только числа')
else:
  print('error')
"""
2) Напишите программу, которая должна рассчитывать средний балл по следующим предметам: математике, английскому языку и литературе. Проходной балл составляет более 69 баллов. Если ученик набрал проходной балл, то ему выдается сообщение о том, что он допущен к экзаменам. Если он не набрал нужное количество баллов, то ему выдается сообщение о том, что у него недопуск к экзаменам.

Например: 
Ввод: Введите свои баллы по математике, английскому языку и литературе через запятую: 78, 90, 67
Вывод: Вы допущены к экзаменам. Ваш средний балл составляет 78.3 

"""
data = input('Введите свои баллы по математике, английскому языку и литературе через запятую: ').split(',')
gpa = ((int(data[0]) + int(data[1]) + int(data[2])) / 3)
grade = round(gpa, 1)
if grade > 69:
  print(f'Вы допущены к экзаменам. Ваш средний балл составляет {grade}')
else:
  print(f'Вы недопущены к экзаменам. Ваш средний балл составляет {grade}')
"""
3) Напишите мини-игру Камень-Ножницы-Бумага. Вы играете с компьютером. Для этого используйте встроенный модуль random.

Например:
Ввод: Ваш выбор: Камень
Выбор компьютера: Ножницы
Вывод: Вы выиграли!

Ввод: Ваш выбор: Бумага
Выбор компьютера: Ножницы
Вывод: Вы проиграли!
"""
import random
list1 = ['камень','ножницы','бумага']

user_choice = input('Ваш выбор: ').lower()
computer_choice = random.choice(list1)
if user_choice == "камень" and computer_choice == "ножницы":
  print('Компьютер выбрал', computer_choice)
  print('Вы выиграли!')
elif user_choice == "камень" and computer_choice == "бумага":
  print('Компьютер выбрал', computer_choice)
  print('Вы проиграли!')
elif user_choice == "ножницы" and computer_choice == "бумага":
  print('Компьютер выбрал', computer_choice)
  print('Вы выиграли!')
elif user_choice == "ножницы" and computer_choice == "камень":
  print('Компьютер выбрал', computer_choice)
  print('Вы проиграли!')
elif user_choice == "бумага" and computer_choice == "камень":
  print('Компьютер выбрал', computer_choice)
  print('Вы выиграли!')
elif user_choice == "бумага" and computer_choice == "ножницы":
  print('Компьютер выбрал', computer_choice)
  print('Вы проиграли!')
elif user_choice == computer_choice:
  print('Вы и компьютер выбрали', computer_choice)
  print('Ничья!')
else:
  print("Пожалуйста введите правильные данные")