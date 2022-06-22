"============Cycles============="
# cycles - это блок кода который повторяется несколько раз
# for - цикл, который работает с итерируемыми обьектами. цикл заканчивает свою работу, когда он дошел до конца (до последнего элемента) в итерируемом обьекте
# while - цикл, который работает до тех пор пока условие верное

count = 10
while count != 0:
    print(count)
    count = count - 1
print("end")
# 10 9 8 7 6 5 4 3 2 1 end

a = 0
while a:
    print("hello")
# will not work because bool(a) False

for i in [1,2,3]:
    print(i)
# 1 2 3

for i in range(5):
    print(i)
# 0 1 2 3 4

for i in range(1, 10):
    print(i)
# 1 2 3 4 5 6 7 8 9

for i in 12345:
    print(i)
# TypeError: 'int' object is not iterable

for i in '12345':
    print(i)
# '1' '2' '3' '4' '5'

num = 12345678
sum = 0
for i in str(num):
    # sum = sum + i 
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    sum = sum + int(i)
print(sum) # 36

string = 'hello'
string2 = 'world'
for i in range(len(string)):
    print(i, string[i], string2[i])
# 0 h w
# 1 e o
# 2 l r
# 3 l l
# 4 o d

for i in []:
    print(i)
# will not work because there is no elements

list_ = [1,2,3]
for i in list_:
    print(i)
    # list_.append("hello") 
    # will work infinitely


string = 'hello'
for i in string:
    print(i)
    string = string + "hello"
    print(string)
# will work only 5 times, because the variable string has a link on 70 line that has changed, while the cycle don't (68 line) 



"===============Keywords в циклах================="
# break - exits the cycle
# continue - shifts to the next iteration

for i in range(10):
    if i == 3:
        continue
    print(i)
# 0 1 2 4 5 6 7 8 9

for i in range(10):
    print(i)
    if i == 3:
        continue
# 0 1 2 3 4 5 6 7 8 9

for i in range(10):
    print(i)
    if i == 3:
        break
# 0 1 2 3

for i in range(10):
    if i == 3: break
    print(i)
# 0 1 2

for i in range(10):
    if i < 3: continue
    print(i)
# 3 4 5 6 7 8 9


for i in range(10):
    print(i)
    for j in range(10):
        print(j)
        if j == 5: break
    if i == 2: break

for i in range(1, 11): print(i)
# 1 2 3 4 5 6 7 8 9 10

list_ = [2,1,3,6,2,5,2,8,2]
while 2 in list_:
    list_.remove(2)
print(list_)

"===================Iteration of dictionaries====================="
dict1 = {"a":1, "b":2, "c":3, "d":4}

# during the iteration of a dictionary we get its keys
for key in dict1:
    print(key)
# "a" "b" "c" "d"

# during the iteration of a dict1.keys() we get its keys
for key in dict1.keys():
    print(key)
# "a" "b" "c" "d"

# during the iteration of a dict1.values() we get its values
for value in dict1.values():
    print(value)
# 1 2 3 4

for key in dict1:
    print(dict1[key])
    # we get values

# during the iteration of a dict1.items() we get keys and values in a tuple
for items in dict1.items():
    key = items[0]
    value = items[1]
    print(key, value)

# we can unpack the tuple on 2 variables
for key, value in dict1.items():
    print(key, value)

for a, b, c in  [(1,2,3), (4,5,6), (7,8,9)]:
    print(a,b,c)
# a=1 b=2 c=3 (iter1)
# a=4 b=5 c=6 (iter2)
# a=7 b=8 c=9 (iter3)

for a, b in  [(1,2), (2,3), (3,4)]:
    print(a,b)
# a=1 b=2 (iter1)
# a=2 b=3 (iter2)
# a=3 b=4 (iter3)

for i in []:
    print("for")
else:
    # works only if cycle did not work at all
    print("else")

while 0:
    print("while")
else:
    # will not work only if it was interrupted by break
    print("else")

a = 1
while a:
    print("while") 
    if a == 1:
        break
else:
    # will not work only if it was interrupted by break
    print("else")