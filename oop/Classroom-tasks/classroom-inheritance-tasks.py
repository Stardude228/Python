"""
1) Создайте класс Languages. В этом классе должен быть атрибут класса, который обозначает количество студентов, изучающих какой-либо язык программирования. От класса Languages создайте два дочерних класса: Python, JavaScript. В них  также должны быть атрибуты, указывающие на количество студентов, изучающих тот или иной язык. При создании объекта-студента от одного из дочерних классов, автоматически количество студентов в классах меняется. Если студент изучает язык Python, то количество студентов должно увеличиться на один и в классе Python и в классе Languages. Аналогично со студентами JavaScript. Далее, в дочерних классах должен быть переопределен метод coding, в классе Python он должен выдавать вам строку “I am Python student. I am coding now.”, а в классе JavaScript - “I am JavaScript student. I am coding now”. Создайте двух студентов от двух дочерних классов. Далее программа сама рандомно выбирает студента и предлагает вам угадать, какого студента она выбрала. После вашего выбора, он вызывает метод coding у загаданного студента и выдает вам результат: если вы отгадали правильно, пишет “Good job!”, если нет - “No bueno :(”
"""
# import random

# class Languages:
#   number_of_all_students = 0
  
#   def __init__(self):
#     Languages.number_of_all_students += 1

#   def coding(self, language):
#     print(f'I am {language} student. I am coding now')


# class Python(Languages):
#   number_of_students = 0
  
#   def __init__(self):
#     Python.number_of_students += 1
#     Languages.number_of_all_students += 1

#   def coding(self):
#     return super().coding('Python')


# class Javascript(Languages):
#   number_of_students = 0

#   def __init__(self):
#     Javascript.number_of_students += 1
#     Languages.number_of_all_students += 1

#   def coding(self):
#     return super().coding('Javascript')

# altai = Python()
# oomat = Javascript()

# list_ = ['oomat', 'altai']
# computer_choice = random.choice(list_)

# user_choice = input('Type your guess (Oomat/Altai): ').lower()
# if user_choice == 'oomat' and computer_choice == 'oomat':
#   print('Good job!')
#   oomat.coding()
# elif user_choice == 'altai' and computer_choice == 'altai':
#   print('Good job!')
#   altai.coding()
# else:
#   print('No bueno :(')


"""
2) Создайте свой класс MyList, который наследуется от list. Переопределите метод списка insert(), который обычно принимает первым аргументом индекс, а вторым - элемент. В своем классе MyList переопределите этот метод так, чтобы он принимал аргументы  в обратном порядке: первым - элемент, вторым - индекс
"""

# class My_List(list):
#   def insert(self, element, index):
#     super().insert(index, element)
# oomat = My_List((5,5,7,8))
# oomat.insert(12, 2)
# print(oomat)