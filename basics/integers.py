# ////////////////////    Variables are references to memory locations where some data is stored

a = 4
b = 3
# print(id(a), a)

# ////////////////////    Data input and output

# print - the function of data output to the terminal
# input - data input function from the terminal

# a = input()
# print("You typed", a)

# ////////////////////    Numbers
# integers (int) = whole numbers (5, 10, 25, 35)
# float = real/material numbers (with a floating point) (0.3, 2.3412, 231.432334)
# decimal = exact real/material numbers. To use Decimal you gotta import it (from decimal import Decimal).
from cmath import sqrt
from decimal import Decimal
c = Decimal(0.1)
d = c + c + c
print(d)
# complex = complex numbers
complex(1, 5)

# ////////////////////   Operations  on numbers
5 + 5 # summation
10 - 4 # subtraction
2 * 3 # multiplication 
15 / 3 # division (float 5.0)
15 // 2 # integer-valued division (int 7)
5**2 # exponentiation
25 ** 0.5 # square root
5 % 2 # the remainder of devision

# the number module is a positive number of any number |-5| = 5
abs(-5) # 5
abs(10) # 10
abs(-2.4) # 2.4

# pow:
# 1. exponates a number to a certain power/degree
# 2. returns a remainder from the devision of the first action on the third number
pow(2, 3) # 8 = 2 ** 3
pow(2, 3, 4) # (2**3) // 4 = 0

# divmod - function that accepts 2 numbers and returns 2 numbers, where the 
# first number is whole number of devision and the second number is a remainder of devision
divmod(15, 2) # 7, 1
divmod(9, 3) # 3, 0

# round - function that rounds the number
round(5.6) # 6
round(3.5) # 4
round(4.4) # 4
round(7.49) # 7 (takes only the first number after the dot)
# can be adjusted the number of integers after the dot
round(10.0475, 3) # 10.048
round(10.0474, 3) # 10.047

# sqrt - function that finds the square root of the number, but to use it we gotta import it from library math
from math import sqrt
sqrt(36) # 6
sqrt(25) # 5
