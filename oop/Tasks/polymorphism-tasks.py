"""
===============Polymorphism tasks No.1===============
Объявите 3 переменные - a, b и c.
В а запишите строку, в b - список и в с сохраните словарь. Затем запишите все три переменные в список, пройдитесь по нему циклом и распечатайте длину каждого из объектов.
"""
# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'}
# list_ = [a, b, c]
# for i in list_:
#     print(len(i))

"""
===============Polymorphism tasks No.2===============
Создайте классы Dog и Cat с одинаковым методом voice.
Для собак он должен печатать "Гав", для кошек "Мяу".
Объявите для каждого из классов по экземпляру, для класса Cat экземпляр в переменной barsik, а для Dog экземпляр rex.
Затем, вне класса объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice().
"""
# class Dog:
#     def voice(self):
#         print('Гав')

# class Cat:
#     def voice(self):
#         print('Мяу')

# barsik = Cat()
# rex = Dog()

# def to_pet(animal):
#     animal.voice()

# to_pet(barsik) 
# to_pet(rex) 

"""
===============Polymorphism tasks No.3===============
Создайте 3 класса: Person с параметрами name и last_name, Employee с work и status, Student c university и course, при этом Employee и Student должны наследоваться от Person.

Определите во всех трёх классах метод get_info():

для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.

для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании Рога и копыта на должности директор.

для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.

Вне класса, определите функцию get_human_info(), которая будет принимать объект одного из трёх классов и вызывать у него метод get_info и распечатывать результат этой функции.

Создайте для каждого класса по экземпляру, для Person экземпляр person, для Employee экземпляр employee и student для класса Student.

Вызовите метод get_human_info у каждого экземпляра печатать результат.
"""
# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'

# class Employee(Person):
#     def __init__(self, name, last_name, work, status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я работаю в компании {self.work} на должности {self.status}'

# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}, я учусь в {self.university} на {self.course} курсе'

# def get_human_info(class_):
#     print(class_.get_info())

# employee = Employee('oomat', 'latipov', 'empire', 'senior')
# student = Student('oomat', 'latipov', 'KGMA', '4')
# person = Person('Oomat', 'Latipov')

# get_human_info(person)
# get_human_info(employee) 
# get_human_info(student) 

"""
===============Polymorphism tasks No.4===============
Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.

Затем, наследуйте от Shape три класса: Triangle, Square и Circle.

треугольник создаётся с заданными основанием base и высотой height
квадрат создаётся с заданной длиной стороны length
круг создаётся с заданным радиусом radius

Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.

Затем, создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area()

Подсказка: для создания абстрактных классов воспользуйтесь модулем abc - https://docs.python.org/3/library/abc.html
"""
# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def get_area(self):
#         pass
        
# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = int(base)
#         self.height = int(height)
#     def get_area(self):
#         return round(((self.base * self.height) * 0.5), 2)
        
# class Square(Shape):
#     def __init__(self, side):
#         self.side = int(side)
#     def get_area(self):
#         return round((self.side * self.side), 2)

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = int(radius)
#     def get_area(self):
#         return self.radius ** 2 * math.pi

# triangle = Triangle(123, 453)
# square = Square(564)
# circle = Circle(456)

# print(triangle.get_area())
# print(square.get_area())
# print(circle.get_area())

"""
===============Polymorphism tasks No.5===============
Создайте класс OS, экземпляры которого имеют аттрибут version - версия системы. От OS наследуйте три класса - Windows, MacOS, Linux.

У всех трех классов должен быть метод copy который принимает в аргументы text и возвращает соответствующую строку.
Создайте экземпляры класса, от Windows - в переменной win, от MacOS - mac, а от Linux в переменной lin.
Примените к каждому объекту метод copy, следующим образом:
"""
# class OS:
#     def __init__(self, version):
#         self.version = version
    
#     def copy(self, text):
#         return text

# class Windows(OS):
#     def __init__(self, version):
#         super().__init__(version)
    
#     def copy(self, text):
#         return (f'скопирован текст "{text}" горячими клавишами CTRL + C')

# class MacOS(OS):
#     def __init__(self, version):
#         super().__init__(version)
#     def copy(self, text):
#         return (f'скопирован текст "{text}" горячими клавишами COMMAND + C')

# class Linux(OS):
#     def __init__(self, version):
#         super().__init__(version)
#     def copy(self, text):
#         return (f'скопирован текст "{text}" горячими клавишами CTRL + SHIFT + C')

# win = Windows(2)
# mac = MacOS(2)
# lin = Linux(2)

# print(win.copy('Полиморфизм — одна из основных парадигм ООП'))
# print(mac.copy('Полиморфизм - разное поведение одного и того же метода в разных классах'))
# print(lin.copy('На самом деле одинаковым является только имя метода, его исходный код зависит от класса'))

"                                     Works but does not make any sense                              "

"""
===============Polymorphism tasks No.6===============
Создайте класс Language, экземпляры которого имеют такие свойства как level и type. Наследуйте от данного класса два других класса - Python и JavaScript. 

И у Python, и у JavaScript должно быть два метода:
write_function, принимает такие аргументы как func_name и arg
create_variable, с аргументами var_name, value

Создайте экземпляр от класса Python в переменной py.
Затем, примените методы к экземпляру класса Python:
print(py.write_function('get_code', 'a')) 
print(py.create_variable('name', 'John'))

вывод должен быть такой:
def get_code(a):    
name = 'John'

Создайте экземпляр от класса JavaScript в переменной js.
Примените метод следующим образом:
print(js.write_function('validate', 'form')) print(js.create_variable('password', 'john@123'))

Вывод должен быть таким:
function validate(form) {     }; 
let password = 'john@123'
"""
# class Language:
#     def __init__(self, level, type):
#         self.level = level
#         self.type = type 

# class Python(Language):
#     def write_function(self, func_name, arg):
#         func = f"def {func_name}({arg}):"
#         return func
#     def create_variable(self, var_name, value):
#         if type(value) == str: 
#             var = f"{var_name} = '{value}'"
#             return var
#         else:
#             var = f"{var_name} = {value}"
#             return var

# class JavaScript(Language):
#     def write_function(self, func_name, arg):
#         var = '     '
#         func = f"function {func_name}({arg}) " + "{     };" 
#         return func
#     def create_variable(self, var_name, value):
#         if type(value) == str: 
#             var = f"let {var_name} = '{value}';"
#             return var
#         else:
#             var = f"let {var_name} = {value};"
#             return var

# py = Python('None', 'None')
# js = JavaScript('None', 'None')

# print(py.write_function('get_code', 'a')) 
# print(py.create_variable('name', 'John'))

# print(js.write_function('validate', 'form')) 
# print(js.create_variable('password', 'john@123'))

"""
===============Polymorphism tasks No.7===============
Создайте класс Money, объекты которого имеют аттрибуты country и symbol. Наследуйте от него классы Dollar и Euro. У данных методов должна быть переменная класса rate, курс к сому, Dollar - 84.80, Euro - 98.40. Добавьте к этим классам метод exchange, который принимает количество которое нужно обменять в переменную amount и возвращает такую строку:

$ 100 равен 8480.0 сомам
€ 80 равен 7872.0 сомам
"""
# class Money:
#     def __init__(self, country, symbol):
#         self.country = country
#         self.symbol = symbol

# class Dollar(Money):
#     rate = 84.80
#     def exchange(self, amount):
#         return f'$ {amount} равен {amount * self.rate} сомам'

# class Euro(Money):
#     rate = 98.40
#     def exchange(self, amount):
#         return f'€ {amount} равен {amount * self.rate} сомам'

"""
===============Polymorphism tasks No.8===============
Создайте классы Mercury, Venus, Jupiter, которые наследуют метод __init__ от родительского класса Planet. У объектов данного класса должен быть аттрибут orbit, орбита в классе Venus состовляет 225 земных дней, Mercury 88 земных дней, а на Jupiter 12 дней. У всех этих классов должен быть метод get_age, принимающий возраст в переменную earth_age и расчитывающий ваш возраст на данной планете.

Метод должен возвращать возраст на Mercury в годах, на Venus в днях и на Jupiter в часах. Например, если возраст earth_age равен 20:

на Венере ваш возраст составляет 11842 дней
на Юпитере ваш возраст составляет 5326080 часов
на Меркурии ваш возраст составляет 82 лет
"""
# class Planet:
#     def __init__(self, orbit):
#         self.orbit = orbit

# class Mercury(Planet):
#     def get_age(self, earth_age):
#         return f'на Меркурии ваш возраст составляет {earth_age * 365 // self.orbit} лет'

# class Venus(Planet):
#     def get_age(self, earth_age):
#         return f'на Венере ваш возраст составляет {round((earth_age * 365 / self.orbit) * 365)} дней'
    
# class Jupiter(Planet):
#     def get_age(self, earth_age):
#         return f'на Юпитере ваш возраст составляет {round(earth_age * 365 / self.orbit) * 365 * 24} часов'

# oomat = Mercury(88)
# altai = Venus(225)
# ertay = Jupiter(12)

# print(oomat.get_age(20))
# print(altai.get_age(20))
# print(ertay.get_age(20))