from decimal import Decimal
number1 = Decimal(input('Введите первое число: '))
operation = (input('Выберите операцию из следующих + - * / % ** // : '))
number2 = Decimal(input('Введите второе число: '))

if operation == "+" :
    if (number1+number2)%1 == 0:
        print(f'Ответ: {int(number1 + number2)}')
    else:
        print(f'Ответ: {number1 + number2}')
elif operation == "-" :
    if (number1-number2)%1 == 0:
        print(f'Ответ: {int(number1 - number2)}')
    else:
        print(f'Ответ: {number1 - number2}')
elif operation == "*" :
    if (number1*number2)%1 == 0:
        print(f'Ответ: {int(number1 * number2)}')
    else:
        print(f'Ответ: {number1 * number2}')
elif operation == "/" :
    if (number1/number2)%1 == 0:
        print(f'Ответ: {int(number1 / number2)}')
    else:
        print(f'Ответ: {number1 / number2}')
elif operation == "%" :
    if (number1%number2)%1 == 0:
        print(f'Ответ: {int(number1 % number2)}')
    else:
        print(f'Ответ: {number1 % number2}')
elif operation == "**" :
    if (number1**number2)%1 == 0:
        print(f'Ответ: {int(number1 ** number2)}')
    else:
        print(f'Ответ: {number1 ** number2}')
elif operation == "//" :
    if (number1//number2)%1 == 0:
        print(f'Ответ: {int(number1 // number2)}')
    else:
        print(f'Ответ: {number1 // number2}')
else:
    print("Данной операции нет в системе")