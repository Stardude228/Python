"====================Strings===================="
# strings are type of data that are designed to preserve text (sequence of symbols),
# which are concluded into single and double quotation marks
# Syntax
string1 = 'a string with single quotation marks'
string2 = "a string with double quotation marks"
# error = 'incorrect string"
string3 = "Don't" # inside of double quotation marks all single quotation marks are just symbols
string4 = '"Makers Bootcamp"' # inside of single quotation marks all double quotation marks are just symbols
string5 = '''
Multiline text
with single quotaion marks
you can leave any quotation marks that 'you' "want"
""""
'''

string6 = """
Multiline text
with single quotaion marks
you can leave any quotation marks that 'you' "want"
''''
"""
string7 = 'a' * 5 #aaaaa

"====================Screening of Strings===================="
# Screening of special symbols
'\n' # shift on the new line
'\t' # tabulation
'\\'  # display of \ (because it is considered to be symbol that affects our code)
'\''  # display of '
"\""  # display of ""
'\r' # return of carriages into the beginning of line
'\v' # shift to the new line with an offset of the length of the previous line 

'hello\nworld'
# hello
# world

'hello\tworld'
# hello    world

'to screen it requires a symbol\\'
# to screen it requires a symbol\

'My website is Latracal \rSolution'
# Solutionte is Latracal

'hello\vworld'
# hello 
#      world

"====================Formatting of Strings===================="
title = 'Plov'
price = 1500
f'Title: {title}, Price: {price}'
# 'Title: Plov, Price: 1500'

format2 = 'Title: %s, Price: %s'
print(format2 % ("Gulyash", "250"))
print(format2 % ("Samsy", "70"))
# Title: Gulyash, Price: 250
# Title: Samsy, Price: 70

format3 = 'Title: {}, Price: {}'
print(format3.format('Shakarap', '35'))
# Title: Shakarap, Price: 35

"====================Methods of Strings===================="
# Methods of type of data - functions that are being called through a dot
print(dir(str)) # shows us all the methods of class (type of data)

'HELLO'.lower() # 'hello'
'hello'.upper() # 'HELLO'
'Hello'.swapcase() # 'hELLO'
'hello'.title() # 'Hello'
'hello world'.title() # 'Hello World'
'hello world'.capitalize() # 'Hello world'

'hello'.center(11) # '   Hello   '
'hello'.center(11, '-') # '---Hello---'

'hello'.count('l') # '2'
'hello'.count('ll') # '1'

'hello world'.startswith('hell') # 'True'
'hello world'.endswith('ld') # 'True'
'hello world'.startswith('H') # 'False'

'hello world'.find('h') # '0'
'hello world'.rfind('h') # '10'

'hello world'.split() # ['hello', 'world']
'hello world'.split('0') # ['hell', ' w', 'rld']
'$'.join(['hello world']) # 'hello$world'
' '.join(['hello world']) # 'hello world'

# concatenation - coupling of words
# 'hello' + 'world' = 'hello world'

"====================Indexes===================="
# Index - serial number of a symbol in a string
'h e l l o   w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
string = 'hello world'
string[0] # 'h'
string[10] # 'd'
string[5] # ' '

# slice - substring of a string
string[0:5] # 'hello'
string[0:6] # 'hello '
string[2:4] # 'll'
string[0:5][2:4] # 'll'
string[:5] # 'hello'
string[6:] # 'world'
string[:] # 'hello world'
string[0:11:2] # 'hlowrd'
string[::3] # 'hlwl'
string[::-1] # 'dlrow olleh'
string[::-2] # 'drwolh'






