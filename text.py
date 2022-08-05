# def swap_big_small():
#     integers = input('Type your number: ')
#     max_number = max(integers)
#     min_number = min(integers)
#     index_of_maximum = integers.index(max_number)
#     index_of_minimal = integers.index(min_number)
#     integers2 = list(integers)
#     integers2.pop(index_of_maximum)
#     integers2.insert(index_of_maximum, min_number)
#     integers2.pop(index_of_minimal)
#     integers2.insert(index_of_minimal, max_number)
#     integers = ''.join(integers2)
#     return integers
# print(swap_big_small())

# import random

# class Languages:
#   number_of_all_students = 0
  
#   def __init__(self):
#     self.number_of_all_students += 1

#   def coding(self, language):
#     print(f'I am {language} student. I am coding now')


# class Python(Languages):
#   number_of_students = 0
  
#   def __init__(self):
#     self.number_of_students += 1
#     super().number_of_all_students + 1

#   def coding(self):
#     super().coding('Python')


# class Javascript(Languages):
#   number_of_students = 0
  
#   def __init__(self):
#     self.number_of_students += 1
#     super().number_of_all_students + 1

#   def coding(self):
#     super().coding('Javascript')

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

# print(Python.number_of_students)
# print(Javascript.number_of_students)
# print(Languages.number_of_all_students)

# def chain(init_val, functions):
#     if 'add10' in functions and 'mul30' in functions:
#         @property
#         def add10(init_val):
#             return init_val + 10
#         @property
#         def mul30(init_val):
#             return init_val * 30
#         add10()
#         mul30()
#     elif 'mul30' in functions:
#         @property
#         def mul30(init_val):
#             return init_val * 30
#         mul30()
#     elif 'add10' in functions:
#         @property
#         def add10(init_val):
#             return init_val + 10
#         add10()
#     else:
#         return init_val

# chain(50, [add10, mul30])

# wow
