"================Fields of view(Scopes) and space of names=================="
locals()  # - returns dictionary with all local variables
globals()  # - returns dictionary with all local variables

# LEGB - local, enclosed, global, build-in

"Build-in"  # - built-in space of names (all built-in variables (print, input, sum, max, min, len, abs, int, str, dict ...))

"Global" # - global space of names (all variables that we created inside of a file) 
# in order to learn all global variables we can use the function globals

"Enclosed" # - space between other spaces (between inner space and outer space)

"Local" # - some closed space

a = 10
d = 7

def func(b, c):
    # local space
    a = 5
    print(locals())
    # {'b': 5, 'c': 2, 'a': 5}
# func(5,2)

def func():
    # enclosed space
    a = "func"
    def inner_func():
        # local space
        a = "inner_func"
        print(locals()) # {'a': 'inner_func'}
    inner_func()
    print(locals()) # {'a': 'func', 'inner_func': <function func.<locals>.inner_func at 0x7fa171fa8d30>}

# func()

эртай = 'алиби'

def func():
    nastya = 'python21'
    print(эртай) # алиби

# func()
# print(nastya)   - NameError: name 'nastya' is not defined


count = 0

def add():
    print(count)
    count += 1 # UnboundLocalError: local variable 'count' referenced before assignment

def add():
    global count # access to change the global variable count
    count += 1
    print(count)

add()
add()
add()
print(count)
# 1 2 3 3


a = 'global'

def outer_func():
    a = 'enclosed'

    def inner_func():
        a = 'local'
        print(a) # local
    
    print(a) # enclosed
    inner_func()

print(a) # global
outer_func()

# global enclosed local


def count(i):
    counter = 0
    
    def add():
        nonlocal counter # access to read and change the local variable counter 
        print(counter)
        counter += 1
    
    for _ in range(i):
        add()

count(10)
# 0 1 2 3 4 5 6 7 8 9

def func():
    a = '1'
    def inner_func():
        def inner2_func():
            nonlocal a # access to read and change the local variable ag
            a = 2
        inner2_func()
    inner_func()
    print(a)
func() # 2