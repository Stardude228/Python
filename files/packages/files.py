"========= Работа с файлами ========"
# try:
#     # open - opens a file for reading
#     file = open('file.txt')
#     # method read() reads the whole file
#     # output = file.read()
#     # readline() # reads only one line
#     # output = file.readline()
#     # output2 = file.readline()
#     # readlines() reads all lines and returns a list with lines
#     # output = file.readlines()
#     # print(output)
    
#     # seeker - cursor that reads file
#     # s1 = file.read()
#     # file.seek(0) # shift cursor to the begining
#     # s2 = file.read()
#     # print("s1: ", s1)
#     # print("s2: ", s2)

#     # lineL1 = file.readline()
#     # print("➡ lineL1 :", lineL1)
#     # line2 = file.readline()
#     # print("➡ line2 :", line2)

#     # Считывание всех строк
#     # for line in file.readlines():
#     #     print(line)
# except:
#     pass
# finally:
#     file.close()

# Context manager
# with open('file.txt') as file:
#     print(file.read())

# Modes of opening of files
# r (read) - standard type of opening, only for reading, will cause an error if there is no file
# w (write) - type of opening only for writing, will create a new file if there is no file
# with open('write_file.txt', 'w') as file:
    # write() writes string into the file
    # file.write('hello everyone')
    # writelines() writes an elements of iterable object
    # file.writelines(['Hello', 'World'])
    # if you need every string to start with a new line
    # file.write('\n'.join(['hello', 'world']))

# a (append) - adds to the end of file
# with open('write_file.txt', 'a') as file:
#     file.write('Hello world')

# w+ - opens a file as for writing and for reading, creates a new file if there is no file
# r+ - opens a file as for reading and for writing, causes errot if there is no file
# a+ - opens a file as for additional writing, creates a new file if there is no file
# with open('non-exist-file.txt', 'w+'): pass


"========= Packages and Modules ========="
# import file_package
# file_package.sum_file()

# One file (file_package.py) - it is a package
# from file_package import sum_file, read_sum_file
# sum_file(5, 100)

# a = 10
# b = read_sum_file()
# print(a + b)

# A folder with packages is a module