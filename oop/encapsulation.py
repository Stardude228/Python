"================Encapsulation==================="

# Encapsulation - one of OOP concepts
#1.data hiding (restricting access to certain methods and classes)
#2.collecting all the methods and attributes necessary for the class into a capsule (class)

"==================Attribute Access Modifiers====================="

# 1.public
# 2.protect
# 3.private
class A:
    attr1 = "public"
    _attr2 = "protected"
    __attr3 = "private"

A.attr1 #public
A._attr2 #protected
# A.__attr3 #AttributeError: type object 'A' has no attribute '__attr3'
A._A__attr3 # private


"==================getters / setters====================="
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, new_age):
        if new_age < 120 and new_age > 0:
            self.__age = new_age
        else:
            raise Exception("age can not be less than 0 or more than 120")

obj = Person("Nastya", 52)
# print(obj.__age) # AttributeError: 'Person' object has no attribute '__age'
print(obj.age)
# obj.age = -5 # Exception: age can not be less than 0 or more than 120
obj.age = 3
print(obj.age) # 3