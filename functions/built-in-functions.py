"=================Built-in functions================"

"lambda" # anonymous function
# lambda parameters: what function returns
add = lambda a, b: a + b
print(add(5,4)) # 9

"map" # function that accepts as the first argument some function and as the second argument some iterable object. Map returns generator where all elements are result of a function that is being accepted to which we send the element from sequence.
map_gen = map(int,['1', '2', '3'])
print(map_gen) # <map object>
print(list(map_gen)) 

# map(int['1', '2', '3'])
# int('1') -> 1
# int('2') -> 2
# int('3') -> 3
# list(map(int['1', '2', '3'])) -> [1, 2, 3, 4]

res = list(map (lambda a: a + 1, [1,2,3,4]))
print(res) # [2, 3, 4, 5]

"============map in cycle for============"
func = lambda a: a + 1
# def func(a):
#   return a + 1
res = []
for i in [1,2,3,4,5]:
    res.append(func(i))
print(res) # [2,3,4,5,6]

"filter" # function that returns a generator that also accepts a function and an interable object. A result will be a sequence of elements from the iterable object that gone through filter (checking)

list_ = ['Ertay', 'Oomat', 'Argen', 'Manas', 'Bekzat']
def start_vowels(name):
    vowels = 'EYAUOeyoia'
    return name.startswith(tuple(vowels))
    # if name[0] in vowels:
    #     return True
    # return False
res = list(filter(start_vowels, list_))
print(res) # ['Ertay', 'Oomat', 'Argen']

"============filter in cycle for============"
def start_vowels(name):
    vowels = 'EYAUOeyoia'
    return name.startswith(tuple(vowels))
list_ = ['Ertay', 'Oomat', 'Argen', 'Manas', 'Bekzat']
res = []
for name in list_:
    if start_vowels(name):
        res.append(name)
print(res) # ['Ertay', 'Oomat', 'Argen']

"reduce" # have to import from the library functools
# this function accepts a function and an iterable object and returns one result

from functools import reduce
list_ = [1,2,3,4,5,6,7]
def mul(a,b):
    return a*b
res = reduce(mul, list_)
print(res)

"================reduce in cycle for=================="
list_ = [1,2,3,4,5,6,7]
def mul(a,b):
    return a*b
res = list_[0]
for i in list_[1:]:
    res = mul(res, i)
print(res)

"enumarate" # function that accepts a sequence. Returns a generator where every element is a tuple that consist from number and element from sequence.
# (enumerate - by default numerates elements starting from 0)

list_ = ['a', 'b', 'c']
for i in enumerate(list_):
    print(i)
# (0, 'a')
# (1, 'b')
# (2, 'c')
for index, element in enumerate(list_):
    print('index - ', index, 'element - ', element)
# index -  0 element -  a
# index -  1 element -  b
# index -  2 element -  c
for i in enumerate(list_[1:]):
    print(i)
# (0, 'b')
# (1, 'c')
for i in enumerate(list_[1:],10):
    print(i)
# (10, 'b')
# (11, 'c')

"zip" # connects a sequence
list1 = [1,2,3,4]
list2 = ['a', 'b', 'c', 'd']
print(list(zip(list1, list2))) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
print(dict(zip(list1, list2))) # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
print([*zip(list1, list2)]) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
print(zip(list1, list2)) # <zip object>

list1 = [1,2,3,4]
list2 = ['a', 'b', 'c']
print(list(zip(list1, list2))) # [(1, 'a'), (2, 'b'), (3, 'c')]

list1 = [1,2,3,4]
list2 = ['a', 'b', 'c']
list3 = [0.97, 1.23, 3.0, 5.4]
print(list(zip(list1, list2, list3))) # [(1, 'a', 0.97), (2, 'b', 1.23), (3, 'c', 3.0)]

