"===================Working with files===================="
# open - allows us to open a file
"==Opening modes=="
# r - read (only for reading)
# w - write (truncating the file first which means deletes everything in file before writing anything)
# a - append (everything new will be added to the end of the file)
# x - creates a file, returns an error if such a file exists 
# rb - read binary (reading in binary form)
# wb - write binary (writing in binary form)
# ab - append binary (appending new data in binary form)

"when we do not indicate the mode of opening the reading mode is default"
# open('test.txt') FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

"when we indicate the mode as (w) it will create a new file if there is no file or will truncate the existing one"
# open('test.txt', 'w')  - creates a new file

"when there is no file (a) will create a new one"
# open('test.txt', 'a')  - creates a new file

"==Read=="
file = open('test.txt') # opens a file in reading mode
res = file.read() # reads whole file and returns a string
print(file.read(5)) # empty string because the cursor is on the end of file
file.seek(0) # cursor is now placed on the index 0 (in the beginning)
print(file.read(5)) # hello (read 5 symbols)
print(file.read(5)) # hello worl (read next 5 symbols)
print(file.tell()) # tells the current location of cursor (10 because the cursor is placed on 10th index)
file.seek(0)
print(file.readlines()) # reads all file and return a list of lines ['Hello world\n', 'Makers Bootcamp \n', 'Line1\n', 'Line2\n', 'Line3\n']
file.seek(0)
print(file.readlines(28))


"==Write=="
file = open('test.txt', 'w') # created a file and cleaned it
# res = file.read()   io.UnsupportedOperation: not readable
# we can not use method read when we are in write or append modes
file.write('Hello world\n') # Wrote (hello world) in file
file.write('Makers Bootcamp\n') # continued to write since we did not opened the file again
file.writelines(['Line1\n', 'Line2\n', 'Line3\n']) # accepts a list of strings and continues to write them in file
file.close() # closes a file (it is necessary to close a file)
# file.write('HELLO') # ValueError: I/O operation on closed file. because we closed the file

file = open("test.txt", 'w+')
file.write("Hello world\nMakers\nBootcamp")
file.seek(0)
res = file.read()
file.seek(0)
file.write("New lines\n")
file.write(res)
file.close()

"==With=="
# With - structure that raises method __enter__ in the beginning and __exit__ in the end 

# class Test:
#     def __enter__(self):
#         print('Start of work: ')
#         return self
    
#     def __exit__(self, *args, **kwargs):
#         print('End of work')

#     def hello(self):
#         print('Hello world')

# with Test() as test:
#     test.hello()


with open("test.txt", 'w+') as file:
    file.write("Hello world\nMakers\nBootcamp")
    file.seek(0)
    res = file.read()
    file.seek(0)
    file.write("New lines\n")
    file.write(res)

with open("test.txt") as file:
    print(file.read())
    print(file.closed) # False
print(file.closed) # True

string = 123456789
print(int("".join(map(lambda x: x+x, list(str(string))))))
112233445566778899
