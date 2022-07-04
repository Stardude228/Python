"""
1) Создайте файл numbers.txt и напишите скрипт, который запишет в этот файл числа от 1 до 20. Затем создайте файл squares.txt. Напишите скрипт, который будет считывать числа из файла numbers.txt и записывать квадраты этих чисел в файл squares.txt
"""
# with open('numbers.txt', 'w+') as file1:
#   file1_range = ''
#   for i in range(1,21):
#     file1_range = file1_range + str(i) + ','
#   file1_range = file1_range.rstrip(',')
#   file1.write(str(file1_range))
  
#   file2 = open('squares.txt', 'w+')
#   file1.seek(0)
#   file2_range = file1.read()
#   file2_range = file2_range.split(',')
#   file2_range = [int(i) ** 2 for i in file2_range]
#   file2_range = str(file2_range).rstrip(']').lstrip('[')
#   file2.write(str(file2_range))
  
#   file1.seek(0)
#   file2.seek(0)
#   print(f'Initial numbers: {file1.read()}')
#   print(f'Final numbers: {file2.read()}')

"""
2) Создайте файл usernames.txt. Напишите скрипт, который будет запрашивать у пользователя имена, а эти имена будут помещаться в файл usernames.txt. При этом напротив каждого имени будет записано количество букв в юзернейме. Программа запрашивает имена до тех пор, пока пользователь не введёт слово: End.
"""
# file = open('usernames.txt', 'a+')
# file2 = open('usernames.txt', 'w') 
# file2.write('')
# file2.close()
# user_inp = 'not defined'
# user_inp = input('Type a username: ')

# while user_inp != 'End':
#   file.write(f'Username: {user_inp}, ')
#   file.write(f'Length of username: {len(user_inp)}\n')
#   file.seek(0)
#   print(file.read())
#   user_inp = input('Type a username: ')  
# else:
#   file.seek(0)
#   print(file.read())
#   file.close()
  