"==============OOP================"
# OOP - Object-oriented programming
class Person:
    name = 'Oomat'
    age = 18
    arms = 2
    legs = 2
    
    def walk(arg):
        print(arg)
        print('I am walking')
    
    def add_age(self):
        self.age += 1

person1 = Person()

# person1 = Person()
# person1.add_age() # New version
# # Person.add_age(person1) # Old version
# print(person1.age)

# Person.age = 17
# print(Person.age)

# person2 = Person()
# print(person2.age)


class Person:
    arms = 2
    legs = 2

    def __init__(self, name, age):
        """
        function that is being called when we create an object from class
        self - a link to a created object
        """
        self.name = name # мы добавляем в обьект self новый аттрибут name
        self.age = age # новый аттрибут age

    def add_age(self):
        """
        function that accepts an object and increases its age to 1
        """
        self.age += 1

    def __str__(self):
        """
        function that is being called when we want to print the object or when we transform the object into str
        function __str__ accepts nothing but self and returns string
        """
        return f"{self.name} - {self.age} y.o"

person1 = Person("Nastya", 50)
print(person1)

person2 = Person("Argo", 15)
print(person2)
