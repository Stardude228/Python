"1. Написать функцию, которая выводит периметр, площадь и диагональ квадрата, после того как пользователь вводит сторону"
# def calculations():
#     side_len = int(input('Type a length of one side of the square: '))
#     s = side_len**2
#     p = side_len*4
#     d = (side_len**2 + side_len**2) ** 0.5
#     return (f" Square of the square is {s},\n Perimeter of the square is {p}, \n Length of diagonal of the square is {d}")
# print(calculations())

"""
2. Даны переменные a, b, c. Проведите такие операции которые по итогу дадут нам 
a = a + b
b = c - b  
c = a + b + c
Пример: Ввод: a = 0, b = 2, c = 5 Вывод: a = 2 b = 3 c = 7
"""
# a = 0 
# b = 2 
# c = 5
# a1 = a + b
# b1 = c - b  
# c = a + b + c
# a = a1
# b = b1
# print(a,b,c)

"3. Дано четырёхзначное число. Вывести YES если цифры в нём расположены по убыванию, в противном случае выведите NO."
# num = 52121
# num2 = list(str(num))
# num3 = list(str(num))
# num2.sort(reverse=True)
# if num3 == num2:
#     print('YES')
# else:
#     print('NO')

"4. Вывести все пятизначные которые делятся на 2, у которых средняя цифра нечетная, и сумма всех цифр делится на 4."
# for i in range(10000, 100000):
#     if not i % 2:
#         if str(i)[2] in '13579':
#             number = 0
#             for j in str(i):
#                 number += int(j)
#                 if not number % 4:
#                     print(i)

"5. Дано четырёхзначное число. Поменяйте местами наименьшую и наибольшую цифры."
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
"""
6. Дан список с визитами по городам и странам. Напишите код, который возвращает отфильтрованный список geo_logs легко помещается в оперативной памяти. 
Пример: geo_logs=[{"visit2":["Дели", "Индия"], "visit3":["Владимир", "Россия"], "visit9":["Курск", "Россия"]}]
"""

"7. Известно, что (x) кг конфет стоит (а) рублей. Определите, сколько стоит (y) кг этих конфет, а также сколько конфет можно купить на (k) рублей. Все значения вводит пользователь."
# def candies():
#     x = int(input('Type a number of kilogramm: '))
#     a = int(input('Type how much money it will cost: '))
#     y = int(input('Type amount of kilogramms that you want to buy: '))
#     k = int(input('Type amount of money that you are willing to spend on candies: '))
#     y_cost = int((a / x) * y)
#     k_kilo = int(k / (a / x))
#     print(f'{x} kilogramms of candies cost {a} rubles. {y} kilogramms will cost {y_cost} and for {k} rubles you can buy {k_kilo} kilogramms of candy')
# candies()

"8. FizzBuzz"
# for i in range(100):
#     if not i % 3 and not i % 5:
#         print('FizzBuzz')
#     elif not i % 3:
#         print('Fizz')
#     elif not i % 5:
#         print('Buzz')
#     else:
#         print(i)