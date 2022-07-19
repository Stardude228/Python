"""
===============Encapsulation tasks No.1===============
Создайте класс A и объявите в нём 3 метода:
публичный(public) (возвращает строку 'Public method'),
защищённый(protected) (возвращает строку 'Protected method')
приватный(private) (возвращает строку 'Private method')

Затем создайте экземпляр в переменной obj1 данного класса и вызовите (с выводом в терминал) по очереди каждый из методов. Не забудьте, что нужно вызвать приватный метод так, чтобы ошибка не выводилась
"""
# class A:
#     def public(self):
#         return 'Public method'
#     def _protected(self):
#         return 'Protected method'
#     def __private(self):
#         return 'Private method'

# obj1 = A()
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())

"""
===============Encapsulation tasks No.2===============
Определите класс A, в нём объявите метод method1, который печатает строку "Hello World".

Затем, создайте класс B, который будет наследоваться от класса A.

Создайте экземпляр в переменной b1 от класса B, и через него вызовите метод method1.
"""
# class A:
#     def method1(self):
#         print('Hello World')

# class B(A):
#     pass

# b1 = B()
# b1.method1()

"""
===============Encapsulation tasks No.3===============
Объявите класс Car, в котором будет приватный атрибут экземпляра класса speed.

Затем, определите метод set_speed, который будет устанавливать значение скорости и метод show_speed, который возвращает значение скорости.

Создайте экземпляр в переменной car1 класса Car и вызовите все методы.
"""
# class Car:
#     __speed = 0

#     def show_speed(self):
#         return self.__speed
    
#     def set_speed(self, speed):
#         self.__speed = speed

# car1 = Car() 
# print(car1.show_speed()) 
# car1.set_speed(20) 
# print(car1.show_speed()) 

"""
===============Encapsulation tasks No.4===============
Перепишите класс Car из предыдущего задания.

Перепишите метод set_speed() с использование декоратора @speed.setter, а метод show_speed() с использованием декоратора @property.

Создайте обьект car1 класса Car.
"""
# class Car:
#     __speed = 0

#     @property
#     def speed(self):
#         return self.__speed
    
#     @speed.setter
#     def speed(self, speed):
#         self.__speed = speed
# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed) 