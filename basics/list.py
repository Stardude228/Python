"====================List==================="
# lists - mutable, indexable, ordered, iterable type of data made for keeping data in certain order

list_ = [1,2,3, 'hello', [0.1, 2], {"a":3}]
list_[1] # 2
list_[4] # [0.1, 2]
list_[4][0] # [0.1]
list_[3][0] # ['h']
list_[-1]["a"] # ['3']

"====================Creation of Lists==================="
list1 = [1,2,3]
list2 = list('hello') # ['h', 'e', 'l', 'l', 'o']
list3 = list(range(1,11)) # [1,2,3,4,5,6,7,8,9,10]
list4 = [1] * 5 # [1,1,1,1,1]


"====================Methods of Lists==================="
# append adds one element to the end of the list
list_ = []
list_.append(1)
print(list_) # [1]
list_.append('hello')
print(list_) # [1, 'hello']

# clear clears the list
list_.clear()
print(list_) # []

# count counts a certain symbol in list
list_ = [1,2,1,3,1,4,1,5]
list_.count(1) # 4

list_ = ['hello', 'hello', 'hello']
list_.count('h') # 0
list_.count('hello') # 3

# extend combines two lists in the first one but does not effect the second one
list1 = [1,2,3]
list2 = [4,5,6]
list1.extend(list2)
print(list1) # [1,2,3,4,5,6]
print(list2) # [4,5,6]

# index returns the first index of a certain element
list1.index(3) # 2
list_.index(1) # 0

# insert inserts a cerain element under a certain index
list1 = [1,2,3]
list1.insert(0, 'hello')
print(list1) # ['hello', 1, 2, 3]

# pop deletes an element in a list by index
list1 = [1,2,3]
popped = list1.pop()
print(list1, popped) # [1,2] 3

# remove a certain first element in list
list_ = [1,2,1,3,1,4,1,5,1,6]
list_.remove(2)
print(list_) # [1,1,3,1,4,1,5,1,6]

# reverse reverses a list
list_ = [1,2,3,4,5]
list_.reverse()
print(list_) # [5,4,3,2,1]
new_list = list_[::-1] # [1,2,3,4,5]

# sort sorts a list in a ascending order (alphabetic)
list_ = [2,1,5,3,8,4,7,6,10,9]
list_.sort()
print(list_) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_ = ['a', 'c', 'd', 'b', 'f', 'e', 'A', 'C', 'B']
list_.sort()
print(list_) # ['A', 'B', 'C', 'a', 'b', 'c', 'd', 'e', 'f']

list_ = [1,2,3,'hello'] # TypeError: '<' not supported between instances of 'str' and 'int'
list_.sort()

# reverse=True сортирует по убыванию
list_ = [2,1,5,3,8,4,7,6,10,9]
list_.sort(reverse=True) # [10,9,8,7,6,5,4,3,2,1]

# user_list = input('Введите слова через пробел: ').split()
# if ',' in user_list:
#   print('error')
# else:
#   print(str(user_list))
#   computer_list = []
#   for i in range(len(user_list)):
#     computer_list.append(len(user_list[i]))
#   print(user_list)
#   print(computer_list)