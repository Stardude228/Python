# x = int(input())
# y = int(input())
# if x % y == 0:
#     print('x делится на y')
#     print(x // y)
# else:
#     print('x не делится на y')
#     print(x // y)
#     print(int(x % y))

# user_data = input('Введите 7 цифр через запятую: ') 
# str_user_data = user_data.replace(', ', '')
# print(user_data[0], user_data[-1])
# list_user_data = list(str_user_data)
# list_user_data.pop()
# list_user_data.append('Makers')
# print(list_user_data)
# list_ = ['Helloworld!'] 
# new_list = list_[0][-1] + list_[0][1:-1] + list_[0][0]  
# print(new_list)

# name_of_list = ['Helloworld!']
# new_list= str(name_of_list).lstrip("['").rstrip("]'")
# number = 0
# if len(new_list) % 2 == 0:
#     number = len(new_list) // 2
#     new_list = new_list[number:] + new_list[:number]
#     print(list(new_list))
# else:
#     number = len(new_list) // 2 
#     new_list = new_list[number+1:] + new_list[:number] + new_list[number]
#     print(list(new_list))

# list_ = ['world', 'hello']
# new_list = [list_[-1], list_[0]]
# print(new_list)

# list_ = ['world', 'hello']
# new_list = [list_[-1], list_[0]]
# print(new_list)

# suitcase = []
# things = ['футболка', 'шорты', 'сланцы', 'очки', 'кепка']
# for i in things:
#     suitcase.append(i)
# suitcase.pop()
# suitcase.insert(0, 'панама')
# print(suitcase)

# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# res = []
# for i in nums:
#     if i < 5:
#         res.append(i)
# print(res)

# user_nums = input()
# user_list = list(user_nums)
# del user_list[1::2]
# print(user_list)
# print(tuple(user_list))

# list1 = [11, 23, 45, 7, 9] 
# list2 = [21, 4, 16, 8, 10]
# print(sum(list1+list2))

# user_data = input().split(',')
# list_ = []
# for i in user_data:
#     if i == ',':
#         continue
#     else:
#         list_.append(int(i))
# list_.sort()
# print(list_)


# list_ = [2, 1, 3, 5, 51, 3]
# for i in list_:
#     if list_.count(i) != 1:
#         print('yes')
#         break
# else:
#     print('ERROR')

# list_ =  [2, 1, 3, 20, 11, 5, 12, 6, 1]
# set_ = set(list_)
# if len(list_) != len(set_):
#     print('yes')
# else:
#     print('ERROR')

# dict_ = {1: 'hello', 2: {'makers': 2, 'bootcamp': 4}, 'makers': 25, 3: 'bootcamp'}
# res = {
#     key if type(key) == int else val
#     : 
#     val if type(val) != dict else {val2: key2 for key2, val2 in val.items()}
#     for key, val in dict_.items()
# }
# print(res)