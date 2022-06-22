"====================Comprehension===================="
# Comprehension - generation of sequence in one string using cycle

# 1. action for element in iterable object 
# 2. action for element in iterable object if filter 

"====================List Comprehension===================="

"Create a list that consists from numbers from 1 to 10"
list_ = []
for i in range(1, 11):
    list_.append(i)
# list_ = [1,2,3,4,5,6,7,8,9,10]

list_ = list( ( i for i in range(1, 11) ) )
# list_ = [1,2,3,4,5,6,7,8,9,10]

list_ = [ i for i in range(1, 11) ]
# list_ = [1,2,3,4,5,6,7,8,9,10]

"Create a list that consists from numbers from 1 to 10 that are even"
list_ = []
for i in range(1, 11):
    if not i % 2:
        list_.append(i)
# list_ = [2,4,6,8,10]

list_ = [ i for i in range(1, 11) if not i%2]
# list_ = [2,4,6,8,10]

list_ = [ i for i in range(2, 11, 2)]
# list_ = [2,4,6,8,10]

list_ = [print(i) for i in range(10)]
print(list_)
# [None None None None None None None None None None]

list_ = ['hello' for i in range(10)]
# ['hello','hello','hello','hello','hello','hello','hello','hello','hello','hello',]

print([input() for i in range(10)])
# Asks input very single time and print everything in one list

"Create a list that consists from numbers ranging from 1 to 10 but instead of even numbers write 'even' or 'odd'"
list_ = [ 'odd' if i % 2 else 'even' for i in range(1, 11) ]
print(list_)
# ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']

"Create a list that consists from random numbers and strings but write 'even' instead of even numbers or 'odd' instead of odd numbers"
list1 = [1, 'hello', 2, 3, 5, 6.0, 'a', 'qwe']
list2 = ['odd' if i % 2 else 'even' for i in list1 if type(i) == int or type(i) == float]
print(list2)
# ['odd', 'even', 'odd', 'odd', 'even']

"================Dict Comprehension========================"
"Create dictionary, where the keys are numbers from 1 to 10 but the values are the same numbers but strings"
dict_ = dict( (i, str(i)) for i in range(1,11) )
# {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10'}

"There are 2 lists. Create new dictionary and take elements of the first list as keys and elements of the second list as values"
list1 = [1,2,3,4]
list2 = ['a','b','c','d']
dict_ = dict( ( ([list1[index],list2[index]])for index in range(len(list1))) )
# {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

dict_ =  { list1[index]:list2[index] for index in range(len(list1)) }

"Copy a dict"
dict1 = {'a':1, "b": 2, 3:"c"}
dict2 = { key:value for key, value in dict1.items() }

"Change values and keys"
dict2 = { value:key for key, value in dict1.items() }

"Copy a dict but make a sum of values as a single value"
dict1 = {
    "a":[1,2,3], 
    "b":[2,3,4], 
    "c":[2,3,4]
    }
dict2 = { key:sum(value) for key, value in dict1.items() }
# { "a":6, "b":9, "c":9 }

"====================Nested comprehensions====================="
# "Create a dict, where keys are gonna be numbers from 1 to 10, but the values are numbers from 1 to key"
dict1 = { i: list(range(1, i+1)) for i in range(1,6) }
# {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

dict1 = { i: [j for j in range(1,i+1)] for i in range(1,6) }
# {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4], 5: [1, 2, 3, 4, 5]}

list_ = [
    [i for i in range(5)]
    for i in range(10)
]
# [[0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4], 
# [0, 1, 2, 3, 4]]