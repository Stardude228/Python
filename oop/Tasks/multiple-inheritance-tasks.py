"""
===============Introduction OOP tasks No.1===============
Создайте класс Auto в нем реализуйте метод ride который выводит сообщение 'Riding on a ground'.

Создайте класс Boat реализуйте метод swim, который выводит 'Floating on water'.

Создайте класс Amphibian который наследуется от класса Auto и Boat.

Создайте от него объект obj и вызовите все методы.
"""
# class Auto:
#     def ride(self):
#         print('Riding on a ground')

# class Boat:
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian()
# obj.ride()
# obj.swim()

"""
===============Introduction OOP tasks No.2===============
Создайте класс-миксин RadioMixin, и реализуйте в нем метод для проигрывания музыки play_music, который принимает в переменную title название песни.

Метод должен печатать строку "Песня называется title", где вместо title должно быть переданное название песни.

Создайте класс Auto, Boat, Amphibian и расширьте функционал этих классов при помощи миксина. Класс Amphibian также как в предыдущем задании должен наследоваться от классов Auto и Boat. Создайте экземпляры auto, boat и obj от трех классов и примените метод play_music.
"""
# class RadioMixin:
#     def play_music(self, title):
#         print(f'Песня называется {title}')
# class Auto(RadioMixin):
#     def ride(self):
#         print('Riding on a ground')

# class Boat(RadioMixin):
#     def swim(self):
#         print('Floating on water')

# class Amphibian(Auto, Boat):
#     pass

# obj = Amphibian()
# auto = Auto()
# boat = Boat()
# obj.play_music('One kiss')
# auto.play_music('Believer')
# boat.play_music('Особо крутая')

"""
===============Introduction OOP tasks No.3===============
Будильник. Создайте класс Clock, у которого будет метод current_time показывающий текущее время и класс Alarm, с методами on и off для включения и выключения будильника.

Далее, создайте класс AlarmClock, который наследуется от двух предыдущих классов.

Добавьте к нему метод alarm_on для установки будильника, при вызове которого должен включатся будильник.

Создайте экземпляр clock класса AlarmClock и примените к ниму методы current_time и alarm_on.
"""
# from datetime import datetime

# class Clock:
#     def current_time(self):
#         print(datetime.now().strftime("%H:%M:%S"))

# class Alarm:
#     def on(self):
#         print('On')
    
#     def off(self):
#         print('Off')

# class AlarmClock(Clock, Alarm):
#     def alarm_on(self):
#         super().on()

# clock = AlarmClock()
# clock.current_time()
# clock.alarm_on()

"""
===============Introduction OOP tasks No.4===============
Напишите абстрактный класс Coder с атрибутом класса count_code_time = 0 и абстрактными методами get_info и coding.

Создайте классы Backend и Frontend, которые наследуют все атрибуты и методы от класса Coder.

Класс Backend должен принимать дополнительно параметры experience и languages_backend, а Frontend такие параметры как — experience и languages_frontend соответственно.

Переопределите в обоих классах методы get_info и coding так, чтобы он принимал количество часов кодинга и при каждом вызове этого метода добавлял это значение к count_code_time.

Также бывают Fullstack разработчики, поэтому создайте данный класс так чтобы у него были атрибуты и методы предыдущих классов. При этом нее определяйте никаких методов и атрибутов в данном классе он должен наследовать их от родительских классов.

Создайте экземпляры a, b, c от классов Backend, Frontend, Fullstack соответственно и вызовите их методы.
"""
# from abc import ABC, abstractmethod
 
# class Coder(ABC):
#     count_code_time = 0

#     @abstractmethod
#     def get_info(self):
#         pass
    
#     @abstractmethod
#     def coding(self):
#         pass

# class Backend(Coder):
    
#     def __init__(self, experience, languages_backend):
#         self.experience = experience
#         self.languages_backend = languages_backend
    
#     def get_info(self):
#         print(f'{self.languages_backend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование')
    
#     def coding(self, code_time):
#         self.count_code_time += code_time

# class Frontend(Coder):
#     def __init__(self, experience, languages_frontend):
#         self.experience = experience
#         self.languages_frontend = languages_frontend

#     def get_info(self):
#         print(f'{self.languages_frontend} разработчик, уровень: {self.experience}, потрачено {self.count_code_time} часов на программирование')
    
#     def coding(self, code_time):
#         self.count_code_time += code_time

# class Fullstack(Backend, Frontend):
#     pass

# a = Backend('Junior', 'Python')
# b = Frontend('Middle', 'Javascript')
# c = Fullstack('Senior', 'Python and JS')

# a.coding(12)
# b.coding(45)
# c.coding(17)

# print(a.get_info()) 
# print(b.get_info()) 
# print(c.get_info()) 

"""
===============Introduction OOP tasks No.5===============
Создайте два класса: Square и Triangle.

Класс Square должен иметь атрибуты: side - длина стороны квадрата.

Класс Triangle должен иметь аттрибуты: height - высота, base - длина.

У каждого из вышеуказанных классов должен быть метод get_area, который высчитывает и возвращает площадь - результатом должно быть целое число.

Создайте третий класс Pyramid который наследуется от первых двух классов, init унаследуйте от Triangle, дополнительные аттрибуты присваивать нельзя.

Добавьте метод get_volume для расчета объема пирамиды(формула: 1/3 x основание^2 x высоту), метод должен возвращать целое число.
"""
# class Square:
#     def __init__(self, side):
#         self.side = side
#     def get_area(self):
#         return int(self.side**2)

# class Triangle:
#     def __init__(self, height, base):
#         self.height = height
#         self.base = base
#     def get_area(self):
#         return int((self.height * self.base) * 0.5)

# class Pyramid(Triangle, Square):
#     def __init__(self, height, base):
#         super().__init__(height, base)
#     def get_volume(self):
#         return int((1/3)* (self.base**2) * self.height)

"""
===============Introduction OOP tasks No.6===============
Создайте класс ToDo, с аттрибутом экземпляра класса, в виде словаря todos = {}.

У класса должен быть один метод set_deadline, который принимает дату дедлайна (в виде "31/12/2021") и возвращает количество дней оставшихся до дедлайна.

Также, класс ToDo должен наследоваться от четырех миксинов: CreateMixin, DeleteMixin, UpdateMixin, ReadMixin:

в классе CreateMixin определите метод create, который принимет в себя задачу todo и ключ key по которому нужно добавить задачу в словарь todos, если ключ уже существует верните "Задача под таким ключём уже существует".

класс DeleteMixin должен содержать метод delete, который удаляет задачу по ключу key, который передается как аргумент, и возвращает сообщение 'удалили название задачу', где вместо слова название должно быть название задачи.

класс UpdateMixin должен содержать метод update, который принимает в себя ключ key и новое значение new_value и заменяет задачу под данным ключом на новое значение.

класс ReadMixin должен содержать метод read, который возвращает отсортированный список задач.
"""
# import datetime

# class CreateMixin:
#     def create(self, key, todo):
#         if list(ToDo.todos.items()) == []:
#             ToDo.todos[key] = todo
#             return ToDo.todos
#         else:
#             for inner_key, value in ToDo.todos.items():
#                 if inner_key == key:
#                     return 'Задача под таким ключём уже существует'
#                 else:
#                     ToDo.todos[key] = todo
#                     return ToDo.todos

# class DeleteMixin:
#     def delete(self, key):
#         if list(ToDo.todos.items()) == []:
#             ToDo.todos[key] = todo
#             return ToDo.todos
#         else:
#             for inner_key, value in ToDo.todos.items():
#                 if inner_key != key:
#                     pass
#                 elif inner_key == key:
#                     temp = ToDo.todos[key]
#                     del ToDo.todos[key]
#                     return temp

# class UpdateMixin:
#     def update(self, key, new_value):
#         for inner_key, value in ToDo.todos.items():
#             if inner_key != key:
#                 return 'Not found'
#             elif inner_key == key:
#                 ToDo.todos[key] = new_value
#                 return ToDo.todos

# class ReadMixin:
#     def read(self):
#         list_ = [(key, value) for key, value in ToDo.todos.items()]
#         return list_

# class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
#     todos = {}
#     def set_deadline(self, deadline):
#         deadline_list = deadline.split('/')
#         today = datetime.date.today()
#         future = datetime.date(int(deadline_list[2]), int(deadline_list[1]), int(deadline_list[0]))
#         diff = future - today
#         return diff.days

# todo = ToDo()
# todo.set_deadline("31/12/2022")

# task = ToDo()
# print(task.create(1, 'Do housework'))
# print(task.create(1, 'Do housework'))
# print(task.create(2, 'Go for a walk'))
# print(task.update(1, 'Do homework'))
# print(task.delete(2))
# print(task.read())
# print(task.set_deadline('31/12/2021'))

"""
===============Introduction OOP tasks No.7===============
Напишите класс Game, с помощью которого можно создать объекты-игры, у объектов должны быть атрибуты:
type - тип игры
name - название игры,
extensions соответсвующий пустому списку - [].

У класса должны быть методы:
1. get_description, который принимает строку и возвращает описание к игре в виде названия игры и переданной строки:
Minecraft это инди-игра в жанре песочницы с элементами выживания и открытым миром.
Где Minecraft - это название игры, берется из атрибута name объекта.

2. get_extensions, который возвращает все подключенные расширения в виде строки разделенной пробелами, если же список extensions пуст, возвращайте сообщение:
Нет подключенных расширений   

Также напишите миксин ExtensionMixin, чтобы к игре можно было подключать расширения.
У миксина должно быть два метода:
1. add_extension, принимающий строку-название и добавляющий ее в список игры, также должен возвратить сообщение:
Добавлено новое расширение Multiverse-Core для игры Minecraft.
где Multiverse-Core это строка - название расширения

2. remove_extension, удаляющий расширение по названию, и возращающий строку в формате:
Multiverse-Core был отключен от Minecraft. 
Если же такого расширения нет в списке должна возвращаться строка:
Такого расширения нет в списке.
"""
# class ExtensionMixin:
#     def add_extension(self, extension):
#         self.extensions.append(extension)
#         return f'Добавлено новое расширение {extension} для игры {self.name}.'
#     def remove_extension(self, extension):
#         if extension in self.extensions:
#             self.extensions.remove(extension)
#             return f'{extension} был отключен от {self.name}.'
#         else:
#             return 'Такого расширения нет в списке.'

# class Game(ExtensionMixin):
#     def __init__(self, type, name):
#         self.type = type
#         self.name = name
#         self.extensions = []

#     def get_description(self, text):
#         return f'{self.name} это {text}'

#     def get_extensions(self):
#         return self.extensions if self.extensions else 'Нет подключенных расширений'

# game = Game(10, 'Minecraft')

# print(game.get_description('инди-игра в жанре песочницы с элементами выживания и открытым миром.'))
# print(game.add_extension('Multiverse-Core'))
# print(game.get_extensions())
# print(game.remove_extension('Multiverse-Core'))
# print(game.get_extensions())


"""
===============Introduction OOP tasks No.8===============
Создайте класс WalkMixin с методом walk, который будет выводить "я могу ходить"

Создайте класс FlyMixin с методом fly, который будет выводить "я могу летать"

Создайте класс SwimMixin с методом swim, который будет выводить "я могу плавать"

Создайте класс Human, который будет наследоваться от миксинов WalkMixin и SwimMixin
Создайте класс Fish, который будет наследоваться от миксина SwimMixin
Создайте класс Exocoetidae, который будет наследоваться от миксинов FlyMixin и SwimMixin
Создайте класс Duck, который будет наследоваться от всех 3 миксинов
Создайте обьекты от классов Human, Fish, Exocoetidae, Duck и вызовите методы, которые у них есть от миксинов

"""
# class WalkMixin:
#     def walk(self):
#         print("я могу ходить")

# class FlyMixin:
#     def fly(self):
#         print("я могу летать")

# class SwimMixin:
#     def swim(self):
#         print("я могу плавать")

# class Human(WalkMixin, SwimMixin):
#     pass

# class Fish(SwimMixin):
#     pass

# class Exocoetidae(FlyMixin, SwimMixin):
#     pass

# class Duck(WalkMixin, SwimMixin, FlyMixin):
#     pass

# human = Human() 
# fish = Fish()
# exocoetidae = Exocoetidae()
# duck = Duck()

# human.swim()
# human.walk()

# fish.swim()

# exocoetidae.swim()
# exocoetidae.fly()

# duck.swim()
# duck.fly()
# duck.walk()