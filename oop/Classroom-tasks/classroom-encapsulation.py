"""
Создайте класс Terminal. Создайте объект-карточку от этого
класса, передав номер своей карточки и пин код. При этом,
необходимо проверить валидность карточки: номер карточки
должен содержать строго 16 цифр, а пин код - 4 цифры (для этого
используйте инкапсуляцию). При создании карточки в ней
содержится 0 сом. Далее в классе должны быть следующие
методы:

=== метод put, который будет принимать в качестве
аргументов: пин код карточки, вторым аргументом -
сумму денег, которую вы хотите закинуть на эту
карточку. Прежде, чем закидывать деньги, необходимо
проверить введенный пин код на совпадение
(используйте инкапсуляцию)

=== метод get_money, который также принимает первым
аргументом пин код, вторым аргументом - сумму денег,
которую вы хотите извлечь из карточки. Здесь также
необходимо использовать валидацию: проверка пин
кода + сумма денег должна быть округленной до
десятичных чисел, типа 10, 100, 200, 5000 и т.д. (67,
899, 45.6 - невалидные данные). И только после
проверки деньги извлекаются.

Примените данные методы к своей карточке несколько раз и в
конце выдайте, сколько денег на карточке. Примечание: нельзя
извлечь сумму денег, если она больше, чем сумма денег на
карточке; также нельзя вытащить пин код карточки (эти данные
должны быть скрыты)
"""
class Terminal:
    
    def __init__(self, number, pin_code):
        if str(number).isdigit() and str(pin_code).isdigit():
            if len(str(number)) == 16 and len(str(pin_code)) == 4:
                self.number = number
                self.__pin_code = pin_code
                self.amount = 0
            else:
                print('Your card number should have exactly 16 numbers and the pin code only 4 numbers!')
        else:
            print('Your card number and pin code should consist only from numbers!')
    
    def pin_check(self, pin_code):
        if pin_code == self.__pin_code:
            return True
        else:
            return False

    def amount_check(self, amount):
        if int(amount) % 10 == 0:
            return True
        else:
            return False
    
    def put(self, pin_code, amount):
        if self.pin_check(pin_code):
            if self.amount_check(amount):
                self.amount += amount
            else:
                print('Not valid amount of money!')
        else:
            print('Incorrect pin code!')

    
    def get_money(self, pin_code, amount):
        if self.pin_check(pin_code):
            if self.amount_check(amount):
                if int(amount) < self.amount:
                    self.amount -= amount
                else:
                    print('You do not have enough money!')
            else:
                print('Not valid amount of money!')
        else:
            print('Incorrect pin code!')

terminal = Terminal(1234567890123456, 1234)
terminal.put(1234, 1000)
terminal.get_money(1234, 500)
print(terminal.amount)
