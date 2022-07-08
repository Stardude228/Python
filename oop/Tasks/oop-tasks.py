"""
===============Introduction OOP tasks No.1===============
Создайте класс для песен Song. Каждая песня имеет название - title, автора - author и год выпуска - year.

Добавьте три метода:

show_author

show_title

show_year

выводящие утверждения о каждом атрибуте экземпляра класса Song.

Создайте экземпляр song класса Song с вашей любимой песней и примените все методы.
"""

# class Song:
    
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
    
#     def show_title(self):
#         print(f'Название этой песни {self.title}')
#     def show_author(self):
#         print(f'Автор этой песни {self.author}')
#     def show_year(self):
#         print(f'Эта песня вышла в {self.year} году')

# song = Song('Happy', 'Pharell Williams', 2013)

# song.show_title()
# song.show_author()
# song.show_year()


"""
===============Introduction OOP tasks No.2===============
Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, в переменной color, и число Пи(3.14) - в переменной pi.

Экземпляры класса Circle в свою очередь должны иметь обязательное свойство - радиус, в переменной radius.

Также, класс должен иметь метод расчета площади круга - get_area(формула расчета площади: число Пи умножить на радиус в квадрате)

cоздайте экземпляр класса,
переопределите цвет экземпляра и
примените метод get_area().
Распечатывать результат не нужно, методы должны возвращать результат ключевым словом return.
"""

# class Circle:
#     color = 'Синий'
#     pi = 3.14
    
#     def __init__(self, radius):
#         self.radius = radius
    
#     def get_area(self):
#         return (self.pi) * (self.radius**2)

# circle = Circle(2)
# circle.color = 'red'
# circle.get_area()

"""
===============Introduction OOP tasks No.3===============
Создайте класс BankAccount, у объектов данного класса есть аттрибут balance со значением по умолчанию 0: balance = 0.

Определите метод withdraw с параметром amount, который будет отнимать сумму от баланса и распечатывать текущий баланс.

Добавьте еще один метод deposit, который также имеет параметр amount и соответсвенно добавляет сумму к балансу и распечатывает баланс.
"""
# class BankAccount:
#     balance = 0

#     def withdraw(self, amount):
#         self.balance = self.balance - amount
#         print(f'Ваш баланс: {self.balance} сом')
    
#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print(f'Ваш баланс: {self.balance} сом')

# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500)

"""
===============Introduction OOP tasks No.4===============
Создайте класс Taxi, объекты которого имеют такие атрибуты как название компании - name, стоимость посадки - cost, стоимость за каждый пройденный километр - cost_km.

Добавьте к классу метод get_total_cost, принимающий параметр km - сколько километров составила поездка и возвращающий стоимость поездки.

Создайте три экземпляра класса Taxi для трех разных компаний Namba, Yandex и Jorgo и расчитайте стоимость поездки на каждой из них.
"""
# class Taxi:
    
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
    
#     def get_total_cost(self, km):
#         return f'Такси {self.name}, стоимость поездки: {(self.cost_km * km) + self.cost} сом'

# taxi1 = Taxi('Namba', 40, 10)
# taxi2 = Taxi('Yandex', 50, 15)
# taxi3 = Taxi('Jorgo', 60, 20)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))

"""
===============Introduction OOP tasks No.5===============
Создайте класс телефонной книги Phone. У контактов должны быть такие аттрибуты:

name - имена
last_name - фамилии
phone - телефонные номера
Добавьте метод get_info, который выводит информацию о контакте
Затем, создайте объект от класса Phone в переменной contact и примените метод get_info.
"""
# class Phone:
    
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
    
#     def get_info(self):
#         return f'Контакт: {self.name} {self.last_name}, телефон: +{self.phone}'

# contact = Phone('John', 'Snow', 996556688977)
# print(contact.get_info())

"""
===============Introduction OOP tasks No.6===============
Напишите класс Salary для расчета налогов на заработную плату. У класса должна быть обязательная переменная класса - percent = 8, обозначающий процент налога на ежемесячную зарплату - 8%.

Объекты класса должны иметь, в качестве атрибутов сумму зарплаты salary и стаж работы в месяцах - experience.

Также у класса должен быть метод count_percent, расчитывающий сумму налога заплаченного за весь стаж работы.

Создайте экземпляр класса obj и посчитайте сумму вашего налога.

Каждый месяц с зарплаты в 10000 сомов снимается 8% на налоги, т.е 800 сом, за 10 месяцев трудового стажа эта сумма будет 8000.0 сом
"""
# class Salary:
#     percent = 8

#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         return (((self.salary * self.experience) * self.percent) / 100)

# obj = Salary(10000, 10)
# print(obj.count_percent()) 

"""
===============Introduction OOP tasks No.7===============
Вам дан такой код:

winner1 = Nobel("Литература", 1971, "Пабло Неруда") 
print(winner1.category, winner1.year, winner1.winner) 
print(winner1.get_year())

winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ") 
print(winner2.category, winner2.year, winner2.winner) 
print(winner2.get_year())
который выводит в терминал такие значения:

Литература 1971 Пабло Неруда
выиграл 51 лет назад 

Литература 1994 Кэндзабуро Оэ 
выиграл 28 лет назад

Напишите класс Nobel и метод класса get_year() таким образом, чтобы данный вам код вывел указанные значения в терминале.
Дату сколько лет назад была получена премия в методе get_year() не вписывать вручную, а высчитывать используя datetime
"""

# class Nobel:

#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
    
#     def get_year(self):
#         current_year = 2022
#         return f'выиграл {current_year - self.year} лет назад'

"""
===============Introduction OOP tasks No.8===============
Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:

В начале, проверьте, что пароль состоит из минимум 8 символов, но меньше 15, если условие не соблюдено, должны выйти ошибка с текстом:
Password should be longer than 8, and less than 15 

Вторая проверка должна проверять что пароль содержит цифры, и в случае отсутствия цифр, выводить ошибку с текстом:
Password should contain numbers too 

Третья проверка, проверяет содержит ли пароль буквы и в случае не совпадения, выводит ошибку с текстом:
Password should contain letters as well 

В конце проверьте, содержит ли пароль хотя бы один из символов: '@', '#', '&', '$', '%', '!', '~', '*', если условие не выполнено выводите ошибку с текстом:
Your password should have some symbols 
если одно из условий не выполнено, выводите соответствующее исключение, если же все условия выполнены метод validate должен возвращать строку:

Ваш пароль сохранен.
Также переопределите метод __str__, чтобы при попытке распечатать сам пароль, вам выдавалась строка из звездочек количество которых равно длине пароля.

К примеру, если пароль joe@123456, при попытке распечатать пароль, в терминал должно выводиться: **********

пишите код для проверки пароля в указанном порядке
"""
# class Password:

#     def __init__(self, password):
#         self.password = password
    
#     def __str__(self):
#         return len(self.password) * '*'

#     def validate(self):
#         if len(self.password) > 15 or len(self.password) < 8:
#             raise Exception('Password should be longer than 8, and less than 15')
#         if self.password:
#             letters = 0
#             numbers = 0
#             other_symbols = 0
#             for i in self.password:
#                 if i in 'яыаеиоюэуёйфчцвсмкптрнгьлшдбщзхъжбabcdefghijklmnopqrstuvwxyx':
#                     letters += 1
#                 elif i in '1234567890':
#                     numbers += 1
#                 elif i in '@#&$%!~*':
#                     other_symbols += 1
#                 else:
#                     pass
#             if numbers == 0:
#                 raise Exception('Password should contain numbers too')
#             if letters == 0:
#                 raise Exception('Password should contain letters as well')
#             if other_symbols == 0:
#                 raise Exception('Your password should have some symbols')
#         return 'Ваш пароль сохранен.'

# oomat = Password('ooooo@oo123456')
# print(oomat.validate())
# print(oomat)

"""
===============Introduction OOP tasks No.9===============
Создайте класс Math, у экземпляра которого должно быть свойство value. У классa Math должно быть 3 метода:

get_factorial - возвращает факториал числа(перемножить все составные числа до самого числа)

get_sum - возвращает сумму цифр числа

get_mul_table - возвращает таблицу умножения для числа до 10 в формате:

5x1=5
5x2=10
5x3=15
5x4=20
5x5=25
5x6=30
5x7=35
5x8=40
5x9=45
5x10=50

Создайте экземпляр класса и примените к нему все методы.

Например, если экземпляром класса Math является число 11,

вызов get_factorial возвратит такой результат:

39916800 
т.к 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10 x 11 = 39916800

метод get_sum, возвратит:

2 
т.к число 11 состоит из двух цифр 1 и 1, сумма 1 + 1 = 2

метод get_mul_table возвратит:

11 x 1 = 11 
11 x 2 = 22 
11 x 3 = 33 
11 x 4 = 44 
11 x 5 = 55 
11 x 6 = 66 
11 x 7 = 77 
11 x 8 = 88 
11 x 9 = 99 
11 x 10 = 110 
результат методов возвращайте ключевым словом return, print() использовать не надо.
"""

# class Math:

#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return self.value
    
#     def get_factorial(self):
#         value = self.value
#         res = 1
#         for i in range(1, value+1):
#             res = res * i
#         return res
    
#     def get_sum(self):
#         value = self.value
#         res = 0
#         value = str(value)
#         for i in value:
#             res = res + int(i)
#         return res
    
#     def get_mul_table(self):
#         value = self.value
#         list_ = [f'{self.value}x{i}={i*self.value}\n' for i in range(1,11)]
#         with open('task1.txt', 'w+') as file:
#             for i in list_:
#                 file.write(i)
#             file.seek(0)
#             res = file.read()
#             return res
    
# mathem = Math(11)
# print(mathem.get_factorial())
# print(mathem.get_sum())
# print(mathem.get_mul_table())

"""
===============Introduction OOP tasks No.10===============
Создайте класс ToDo, экземплярами данного класса являются строки-задачи(сходить в кино, сделать домашку, выгулять собаку и.т.д).

У класса должна быть переменная класса instances значением которой является пустой словарь.

Создайте внутри класса метод give_priority, который имеет параметр priority, куда принимает число - приоритет вашей задачи (1, 2, 3) и записывает вашу задачу в словарь instances с ключом в виде числа - priority, а значением в виде вашей задачи.

Например:

{3: 'сходить в кино'}
приоритет сходить в кино у вас не самый высокий.

{1: 'сделать домашку'}
в этом случае это у вас самая важная задача, с приоритетом 1.

При каждом вызове метода give_priority - словарь в instances обновляется. Если вы создали три объекта от класса ToDo и к каждому объекту вызвали метод give_priority и дали приоритет, то ваш словарь в instances в конце будет выглядеть примерно так:
{3: 'сходить в кино', 1: 'сделать домашку', 2: 'выгулять собаку'} 

У класса должен быть метод list_of_tasks, который возвращает вам список отсортированных задач по приоритету:
[(1, 'сделать домашку'), (2, 'выгулять собаку'), (3, 'сходить в кино')]
"""
# class ToDo:
#     instances = {}

#     def __init__(self, thing):
#         self.thing = thing

#     def give_priority(self, priority: int):
#         ToDo.instances[priority] = self.thing

#     def list_of_tasks(self):
#         res = []
#         for key, value in ToDo.instances.items():
#             res.append((key,value))
#         res.sort()
#         return res

# thing3 = ToDo('сходить в кино')
# thing1 = ToDo('сделать домашку')
# thing2 = ToDo('выгулять собаку')

# thing2.give_priority(2)
# thing1.give_priority(1)
# thing3.give_priority(3)

# print(thing1.list_of_tasks())


