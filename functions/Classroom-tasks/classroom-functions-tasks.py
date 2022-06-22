"""
1) Напишите функцию get_info, которая запрашивает у пользователя имя и фамилию, последовательно. Далее внутри get_info вызовите другую функцию generate_password, которая будет генерировать пароль при помощи конкатенации имени и фамилии пользователя и рандомных 7 чисел (в промежутке от 0 до 9). В конце функция get_info возвращает пользователю сгенерированный пароль.
"""
# from random import sample

# def get_info():
#   name = input('Type your name: ')
#   surname = input('Type your surname: ')
#   print(generate_password(name, surname))

# def generate_password(name, surname):
#     numbers = (sample(range(0, 10), k = 7))
#     empty_string = ''
#     for i in numbers:
#         empty_string = empty_string + str(i)
#     password = name + surname + empty_string
#     return (f'Your generated password is - {password}')

# get_info()
"""
2) Напишите калькулятор на функциях. У вас должна быть основная функция get_data, которая запрашивает два числа, и действие (сложение, вычитание, умножение, деление). И в зависимости от выбранного действия get_data должна вызывать ту или иную функцию, в которой будет прописан алгоритм выполнения действий. В конце выдается результат через функцию result.
"""
# def get_data():
#   number1 = int(input('Type first number: '))
#   number2 = int(input('Type second number: '))
#   operation = input('Type an operation + - * / ')

#   def result(number1, number2, operation):
#     if operation == '+' :
#       summation(number1, number2)
#     elif operation == '/' :
#       division(number1, number2)
#     elif operation == '-' :
#       subtraction(number1, number2)
#     elif operation == '*' :
#       multiplication(number1, number2)
#     else:
#       return('Type a correct operation')
  
#   def summation(number1, number2):
#       print(number1 + number2)
#   def division(number1, number2):
#       print(number1 / number2)
#   def subtraction(number1, number2):
#       print(number1 - number2)
#   def multiplication(number1, number2):
#       print(number1 * number2)
  
#   result(number1, number2, operation)

# get_data()
"""
3) Напишите функцию, которая будет принимать 2 обязательных параметра: вкус мороженого и размер. И также функция может принимать необязательные параметры, которые могут выступать в качестве топпинга к мороженому. Выдайте результат
"""
# def ice_cream(taste, size, topping = 'peanuts', something = None):
#     if something == '' or something == ' ' or something.isdigit() == True:
#         print(f'You got {size} centimeter, {taste} ice cream with {topping} on top')
#     elif something != '':
#        print(f'You got {size} centimeter, {taste} ice cream with {topping} on top')
#        print(f'Your additions: {something}')

# ice_cream(input('Type a taste of your ice cream: ').lower(), input('Type a size of your ice cream (number): ').lower(), input('Type a topping of your ice cream: ').lower(), something = input('Type your additions: ').lower())