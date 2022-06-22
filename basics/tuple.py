"===================Tuple====================="
# tuple - immutable, indexable, ordered, iterable type of data made for keeping data in certain order (no difference between list but occupies less data)
tuple1 = (1,2,3) # (1,2,3)
tuple1 = ('hello', 2.5, (2,3) [1,2,3])
tuple3 = tuple('hello') # ('h', 'e', 'l', 'l', 'o')
tuple4 = 1,2,3 # (1,2,3)
tuple5 = (5) # 5 (int)
tuple6 = 5, # (5,)

"===================Methods of Tuple====================="
# count counts a certain symbol in list
list_ = (1,2,1,3,1,4,1,5)
list_.count(1) # 4

list_ = ('hello', 'hello', 'hello')
list_.count('h') # 0
list_.count('hello') # 3

# index returns the first index of a certain element
list_ = (1,2,1,3,1,4,1,5)
list_.index(3) # 3
list_.index(1) # 0