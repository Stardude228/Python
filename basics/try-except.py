"==================Exceptions======================"
# Exceptions (mistakes) - objects, that disrupt the work of the code if it was provoked

SyntaxError # exception that pops up when there is a syntax error in code 

# (      -  SyntaxError: unexpected EOF while parsing
# (When we did not close brackets or quotation marks)

# a -             SyntaxError: invalid syntax
# (When we did something wrong in python syntax)

NameError # Exception that pops up when we call a nonexistent variable

# nonasdasd -            NameError: name 'nonasdasd' is not defined

IndexError # Exception that pops up when we call upon to nonexistent index

list_ = [1,2,3,4]
# list_[1000] -       IndexError: list index out of range
# list_.pop(1000) -       IndexError: pop index out of range

KeyError # Exception that pops up when we call upon to nonexistent key
dict_ = {"a": 1}
# dict_["b"]   - KeyError: "b"
# dict_.pop("b")   - KeyError: "b"
# print(dict_.get(["b"]))  # Not an exception but it will result None if there is no such a key


ValueError # pops up when we try to unpack some sequence where the number of elements and variables does not match
# or when we send incorrect type of data

# a,b,c = 'ab'      - ValueError: not enough values to unpack (expected 3, got 2)
a,b = "ab" # 2 symbols can be unpacked into 2 variables
# int('10d') # ValueError: invalid literal for int() with base 10: '10d'

TypeError # when we try to use unusual methods for some type of data
# or when we try to send into the function or method more or less arguments than expedcted

# for i in 123456:   - TypeError: 'int' object is not iterable

# 5 + '5'      - TypeError: unsupported operand type(s) for +: 'int' and 'str'
# '5' + 5      - TypeError: can only concatenate str (not "int") to str

# hash([1,2,3])   - TypeError: unhashable type: 'list'
# {[1,2,3]: 'hello' }   - TypeError: unhashable type: 'list'

# input('hello', 1)     - TypeError: input expected at most 1 argument, got 2

IndentationError  #  when we use incorrect tabs or spaces
#  a = 4     -   IndentationError: unexpected indent
# for i in range(10):
# print(i)   -   IndentationError: expected and indented block

ZeroDivisionError # You can't divide by 0

"=================Exception processing==================="
# in order for code not disrupting his process during incorrect data

# try:
    # code that may result an error
# except an error that may pop up:
    # code that will work if the code had an error
# else:
    # code that will work if try did not have any errors
# finally:
    # code that will work anyway

try:
    num = int(input())
except ValueError:
    print('Type a number')
else:
    print('Typed number')
# if input will be a number - block else will work
# if input will be a string - block except will worka