"===============Comprehension tasks No.1==============="
# list_ = [i for i in range(1,101)]
# print(list_)

"===============Comprehension tasks No.2==============="
# list_ = [i for i in range(1,50,2)]
# print(list_)

"===============Comprehension tasks No.3==============="
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [i for i in list_ if i > 0 and not i % 2 ]
# print(int_list)

"===============Comprehension tasks No.4==============="
# list_ = [i**2 for i in range(1,26) ]
# print(list_)

"===============Comprehension tasks No.5==============="
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(i) for i in str_list]
# print(int_list)

"===============Comprehension tasks No.6==============="
# list_ = [i**2 if not i % 2 else i for i in range(1, 11)]
# print((list_))

"===============Comprehension tasks No.7==============="
# list_ = [True if not i % 2 else False for i in range(1, 11)]
# print(list_)

"===============Comprehension tasks No.8==============="
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude' ]
# new_list = ['shorter' if len(i) <= 4 else 'longer' for i in list_name ]
# print(new_list)

"===============Comprehension tasks No.9==============="
# dict_ = {num : num**2 for num in range(1,11)}
# print(dict_)

"===============Comprehension tasks No.10==============="
# data = int(input())
# dict_ = {i:i**2 for i in range(1,501) if not i % data}
# print(dict_)

"===============Comprehension tasks No.11==============="
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {i:list(range(1,v+1)) for i,v in a.items()}
# print(dict_)

"===============Comprehension tasks No.12==============="
# dict_ = {'first': 1, 'second': 2, 'third': 3}
# a = {key:str('even'if value % 2 == 0 else 'odd') for key, value in dict_.items()}
# print(a)

"===============Comprehension tasks No.13==============="
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# splitted = string_.split()
# list_ = [i for i in splitted if i.isdigit()]
# print(list_)

"===============Comprehension tasks No.14==============="
# dict_ = {
#     'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
#     'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#     'Nik': {'history': 84, 'math': 85, 'literature': 87}
#     }
# new_dict = {key:
#     list( ({inner_key: inner_value for inner_key, inner_value in value.items() if inner_value == max(value.values())} ).keys() )[0]
#     for key, value in dict_.items()}
# print(new_dict)

"Myrzayim Task14"
# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
# 'Olga': {'history': 92, 'math': 96, 'literature': 81},
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}

# new_dict = {key: in_k 
#             for key, value in dict_.items() 
#             for in_k, in_v in value.items() 
#             if list(value.keys()).index(in_k) == list(value.values()).index(max(list(value.values())))}
#             #if in_v == max(value.values())}
# print(new_dict)

"Eljaz Task14"
# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
#          'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
#          'Nik': {'history': 84, 'math': 85, 'literature': 87}
#          }

# list1 = [k for k in dict_.keys()]
# # # через цикл for
# # list1 = []
# # for k in dict_.keys():
# #     list1.append(k)

# list2 = []
# for k, v in dict_.items():
#     for inner_k in v.keys():
#         if inner_k == max(v, key = v.get): # вытаскиваем ключ внутреннего словаря,
#             list2.append(inner_k)          # значения которого максимальное через функцию max()

# new_dict = {list1[index]: list2[index] for index in range(len(list1))}

# # new_dict = dict((list1[index] ,list2[index]) for index in range(len(list1)))
# # new_dict = dict(zip(list1, list2)) # через функцию zip()

# print(new_dict)

"===============Comprehension tasks No.15==============="
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# dict_ = {key:
#     int(str(list(({inner_key: inner_value for inner_key, inner_value in value.items() if inner_value == max(list(value.values()))}).values())).lstrip("['").rstrip("]'"))
#     for key, value in my_dict.items()}
# print(dict_)

"===============Comprehension tasks No.16==============="
# list_ = [i / 2 for i in range(0, 11) if not i % 2]
# print(list_)

"===============Comprehension tasks No.17==============="
# dict_ = {1: 'Hello', 2: 'World', 3: 'John'}
# dict2 = {key:(len(value) if key % 2 == 0 else len(value) ** 3) for key, value in dict_.items()}
# print(dict2)

"===============Dictionary tasks No.18==============="
# set1 = {i for i in range(10)}
# set2 = {i for i in range(8,18)}
# full_set = set1.union(set2)
# if len(set1) + len(set2) > len(full_set):
#     difference = len(set1) + len(set2) - len(full_set)
#     print(f"В этом сете было {difference} повторения, его длина составляет {len(full_set)}")
# else:
#     print("Ваш объединенный сет полностью уникальный!")