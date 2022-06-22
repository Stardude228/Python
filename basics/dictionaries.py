"=============Dictionaries==============="
# Dictionary (dict) is mutable, unindexable, iterable, disordered type of data which is kept in pairs (key: value)

dictionary = {'a': 'Hello', 'b':2, 'c':3}
print(dictionary['a']) # Hello

# All immutable types of data are capable of being keys
# All mutable types of data are capable of being values

dictionary1 = {
    1: 'Hello', 
    'a':4, 
    4.5:{"a":5},
    # {'s':5}:44 # TypeError: unhashable type: 'dict'
}

print(dictionary1[4.5]) #('a':5)
print(dictionary1[4.5]['a']) # 5
print(dictionary1['a']) # KeyError

"=============Creation of Dictionaries==============="
dict1 = {"a":3}
dict2 = dict( [ ('key1', 'value1'), ('key2', 'value2') ] )
# dict2 = {'key1':'value1', 'key2':'value2'}
dict3 = dict( ( ['key1', 'value1'], ('key2', 'value2') ) )
# dict3 = {'key1':'value1', 'key2':'value2'}
dict4 = dict(['ab', 'cd', 'de'])
# dict4 = {"a":"b", 'c':'d', 'd':'e'}
key1, value1 = 'ab'
dict4[key1] = value1
key2, value2 = 'cd'
dict4[key2] = value2
key3, value3 = 'de'
dict4[key3] = value3


dict5 = dict(['abc']) # ValueError: dictionary update sequence element #0 has length 3; 2 is required
key1, value1 = 'abc' #
dict5[key1] = value1

"=============Methods of Dictionaries==============="
dictionary.clear() # clears the dictionary
print(dictionary) # {}

dictionary2 = dictionary.fromkeys([1,2,3], 'hello')
print(dictionary2) # {1: hello,2: hello,3: hello}

dictionary3 = {'a': 1, 'a':2, 'a':3}
print(dictionary3) # {'a': 1, 'a':2, 'a':3}
dictionary3['a'] = 4
print(dictionary3) # {'a': 1, 'a':2, 'a':4}

dictionary3.get('a') # 1
dictionary3.get('c') # None
dictionary3.get('c', 5) # if there is no key, it will return 5
dictionary3.get('c', 5) # if there is a key, it will return 1 (it's value)

dictionary.keys() # dictionary keys(['a', 'b'])
dictionary.values() # dictionary values([1, 2])
dictionary.items() # dictionary items([('a', 1), ('b', 2)])

# update() combines the specific dictionary and dictionary
dict1 = {1:"a", 2:"b", 3:"c"}
dict2 = {3:"d", 4:"e"}
dict1.update(dict2)
print(dict1) # {1:"a", 2:"b", 3:"d", 4:"e"}
print(dict2) # {3:"d", 4:"e"}

# pop() deletes the specific key and value
popped = dict1.pop(3) # d
print(dict1) # {1:"a", 2:"b", 4:"e"}
print(popped) # d

# popitem() deletes the last key and value
dict1.popitem() # {4,"e"}
print(dict1) # {1:"a", 2:"b", 3:"d"}
