"===============Dictionary tasks No.1==============="
# try
# except
# else
# finally

"===============Dictionary tasks No.2==============="
# b = 10
# c = 11
# try:
#     print(a)
# except:
#     print('Error')

"===============Dictionary tasks No.3==============="
# try:
#     data1 = int(input())
#     data2 = int(input())
#     output = data1 / data2
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# print(output)

"===============Dictionary tasks No.4==============="
# try:
#     num1 = int(input())
#     num2 = int(input())
#     data = num1 + num2
# except:
#     print('Введите число!')
# print(data)

"===============Dictionary tasks No.5==============="
# dict_ = {'key1': 'value1', 'key2': 'value2'} 
# try:
#     print(dict_[key3])
# except:
#     print('Нет такого ключа!')

"===============Dictionary tasks No.6==============="
# list_ = [1, 4, 9, 16, 25, 36]
# try:
#     print(list_[12])
# except:
#     print('Нет такого элемента!')

"===============Dictionary tasks No.7==============="
# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError('Доступ запрещён')
# except:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

"===============Dictionary tasks No.8==============="
# try:
#     num1 = int(input())
#     num2 = int(input())
#     data = num1 / num2
# except ValueError or ZeroDivisionError:
#     print('Произошла ошибка!')
# print(data)

"===============Dictionary tasks No.9==============="
# cash = int(input())
# if cash < 0:
#     raise ValueError("Сумма не может быть отрицательной!")
# else:
#     print(cash)

"===============Dictionary tasks No.10==============="
# inp1 = input()
# inp2 = input()
# try:
#     print(int(inp1) + int(inp2))
# except:
#     print(inp1 + inp2)

"===============Dictionary tasks No.11==============="
# try:
#     inp1 = input('Type numbers and words through space: ').split()    
#     list1 = list(inp1)
#     list_ = []
#     for i in list1:
#         list_.append(int(i))
# except Exception:
#     raise Exception(' Данный элемент не является числом!')
# print(list_)