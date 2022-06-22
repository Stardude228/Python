"=============Logical operators==============="
# Logical operators - expressions, that return True, if it is truth, False - if it is false

5 == 5 # True
4 == 5 # False

5 != 5 # False
5 != 2 # True

5 > 10 # False
10 > 5 # True
5 > 5 # False

5 < 10 # True
10 < 5 # False
5 < 5 # False

5 <= 10 # True
10 <= 5 # False
5 <= 5 # True

5 >= 10 # False
10 >= 5 # True
5 >= 5 # True

"=============And Or==============="
# and is used for 2 conditions at the same time
# or is used for either first condition or another
a = 5
b = 6

a == 5 and b == 6 # True (both of the sides are true)
a == 5 and b == 5 # False (right side is True but the left side is false)
a == 4 and b == 5 # False (both of the sides are false)

a == 5 or b == 6 # True (both of the sides are true)
a == 5 or b == 5 # True (right side is True but the left side is false)
a == 4 or b == 5 # False (both of the sides are false)

# if both sides are true - it will result True
# if both sides are false - it will result False
# if one sides is true and the second one is false - it will result:
# 1. if there is (and) it will result false
# 2. if there is (or) it will result true

not True # False
not False # True
not a == 5 # False (because a == 5)
not a == 4 # True (because a == 5)
2 in [1,2,3,4,5] # True
"a" in {"b":3, "c":"a"} # False because a is not a key

"=============Boolean Type==============="
# Boolean type of data has only two results either True or False
bool(1) # True
bool(0) # False
bool(-100) # True

bool('Hello') # True
bool('') # False
bool(' ') # True

bool('True') # True
bool('False') # False

"=============None Type==============="
# None - is a  type with a single value None, that is used for absense of data
bool(None) # False
bool('None') # True

a = None
print(a is None) # True
# "is" is a checking method on the full compliance 

"=============Conditional Operators==============="
# Conditional Operators are used for ramifications of input data; the code will work differently if there are various input data
a = int(input("Type a number: "))
if a > 0:
    print(f"Your number is positive")
elif a < 0:
    print(f"Your number is negative")
else:
    print(f"Your number is neither positive and neither negative")


"=============FizzBuzz==============="
# if a number is multiple to 3 - print Fizz
# if a number is multiple to 5 - print Buzz
# if a number is multiple to 3 and 5 - print FizzBuzz
# if a number is not multiple to 3 or 5 - print number

a = int(input("Type a number: "))
if a % 3 == 0: 
    if a % 5 == 0:
        print('FizzBuzz')
    else:
        print('Fizz')
elif a % 5 == 0:
    print('Buzz')
else:
    print(f'Your number is {a}')


"=============Ternary operators==============="
# condition in one line
# body1 if condition else body2

res = 'Hello' if a == 5 else 'Bye'
print(res)
# Hello if a == 5
# Bye if a != 5 

