"==============Inheritance================="

"Inheritance - concept of OOP where we can inherit, change and use attriburtes and methods in subsidiary object from parental class"

class A:
    def method(self):
        print('method in class A')

object_a = A()
object_a.method() # method in class A

class B(A):
    "Inherits all methods and attributes from class A"

object_b = B()
object_b.method() # method in class A

"Class A - parental class"
"Class B - subdiary class"

class C(A):
    "Inherits all methods and attributes from class A and changed the method called method"
    def method(self):
        print('method in class C')

object_a = A()
object_a.method() # method in class A
object_c = C()
object_c.method() # method in class C

"Redefinition - we give the same name but another value"

"super() - function that allows us to address to parental class and provoke some methods and attributes"

class A:
    def my_range(self, n):
        return list(range(1, n+1))

class B(A):
    def my_range(self):
        # Through super we address to parental method
        return super().my_range(6)

object_a = A()
object_a.my_range(3) # [1,2,3]

object_b = B()
object_b.my_range() # [1,2,3,4,5,6]

"==============Types of inheritance================="
# Single inheritance
# Plural inheritance
# Multilevel inheritance
# Hierarchy inheritance
# Hybrid inheritance