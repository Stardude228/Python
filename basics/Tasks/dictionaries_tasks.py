"===============Dictionary tasks No.1==============="
# a = {'x': 1, 'y': 2, 'z': 1}
# b = list(a.keys())
# print(b[0])

"===============Dictionary tasks No.2==============="
# a = {'a': 1, 'b': 2, 'c': 1}
# print(a.pop('a'))

"===============Dictionary tasks No.3==============="
# a = {'a': 1, 'b': 2, 'c': 1}
# a['f'] = 55
# print(a)

"===============Dictionary tasks No.4==============="
# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

"===============Dictionary tasks No.5==============="
# a = {'a': 1, 'b': 2, 'c': 1}
# print(list(a.keys()))

"===============Dictionary tasks No.6==============="
# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

"===============Dictionary tasks No.7==============="
# a = {'a': 1, 'b': 2, 'c': 1}
# for i in a:
    # print(i)

"===============Dictionary tasks No.8==============="
# a = {'a': 1, 'b': 2, 'c': 1}
# for i in a.values():
#     print(i)

"===============Dictionary tasks No.9==============="
# a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
# b = {}
# for key, val in a.items():
#     if not val % 2: 
#         b[key] = 2
#     else:
#         b[key] = val
# print(b)

"===============Dictionary tasks No.10==============="
# a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}
# b = {}
# for key, val in a.items():
#     if val == None: 
#         del val
#     else:
#         b[key] = val
# print(b)

"===============Dictionary tasks No.11==============="
# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# b = {}
# for key, val in a.items():
    # b[key] = val / 5
# print(b)

"===============Dictionary tasks No.12==============="
# a = {'apple': 2, 'orange': 5, 'banana': 10}
# b = {}
# for key, val in a.items():
#     if not val % 2:
#         del val
#     else:
#         b[key] = val
# print(b)

"===============Dictionary tasks No.13==============="
# a = {'a': 1, 'b': 2, 'c': 3}
# b = {}
# for key, val in a.items():
#     b[val] = key
# print(b)

"===============Dictionary tasks No.14==============="
# a = {'a': 3, 'b': 2}
# print(sum(list(a.values())))

"===============Dictionary tasks No.15==============="
# dict4 = dict(['ab', 'cd', 'de'])
# dict1 = {"a":3}
# a3 = dict({('Russia', 'Moscow')})

"===============Dictionary tasks No.16==============="
# a= {'a': 10, 'b': 9, 'c': 3}
# result = 1
# for k in a:
#     result = result * a[k]
# print(result)

"===============Dictionary tasks No.17==============="
# string = "pythonist"
# dict_ = {}
# for i in string:
#     number_of_repeat = string.count(i)
#     for j in range(number_of_repeat):
#         dict_[i] = j+1
# print(dict_)