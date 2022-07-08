"""
1) Реализуйте программу по следующему описанию. Есть классы WhatsApp, SnapChat, Telegram. При регистрации в WhatsApp и SnapChat необходимо передавать свой номер телефона, который должен быть int. При регистрации в Telegram необходимо передавать номер телефона и username. Во всех классах есть метод send, в WhatsApp он принимает только text и выдает строку “I am sending a text ...” и вместо … должен быть сам текст сообщения. В SnapChat send принимает image и text, при этом image должен быть булевым типом данных. Если image True, то выдается сообщение “I am sending a text … with some image ”, если  False - сообщение “I am sending a text … without image”. В Telegram метод send принимает voice message в виде строки и выдает сообщение “I am sending a voice message ...”. Создайте объекты от этих классов и вызовите метод send у всех объектов.
"""

# class WhatsApp:
#   def __init__(self, number: int):
#     self.number = number

#   def send(self, text):
#     return f'I am sending a text {text}'
  
# class SnapChat:
#   def __init__(self, number: int):
#     self.number = number

#   def send(self, text, image):
#     if image == True:
#       return f'I am sending a text {text} with some image'
#     else:
#       return f'I am sending a text {text} without image'

# class Telegram:
#   def __init__(self, number: int, username: str):
#     self.number = number

#   def send(self, voice_message: str):
#     return f'I am sending a voice message {voice_message}'


# oomat = WhatsApp(996550223445)
# altai = SnapChat(996550223445)
# ertay = Telegram(996550223445, 'Ertay')

# print(oomat.send('I am WhatsApp user'))
# print(altai.send('I am SnapChat user', False))
# print(ertay.send('I am Telegram user'))


"""
2) Создайте два класса A и B. В обоих классах есть метод count. В классе A он подсчитывает, сколько гласных букв в слове, которое передается в качестве аргумента в методе count, а в классе B он подсчитывает количество согласных. Создайте объекты от этих классов и вызовите этот метод у каждого объекта.
"""

# class A:
#   vowels = 'аяуюоеёэиы'
#   def count(self, word):
#     number = 0
#     word = word.lower()
#     for i in word:
#       if i in self.vowels:
#         number += 1
#     return number

# class B:
#   consonants = 'бвгджзйклмнпрстфхцчшщ'
#   def count(self, word):
#     number = 0
#     word = word.lower()
#     for i in word:
#       if i in self.consonants:
#         number += 1
#     return number

# oomat = A()
# ertay = B()

# print(oomat.count('Классные шорты!'))
# print(ertay.count('Классные шорты!'))