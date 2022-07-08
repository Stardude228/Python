"""
1) Напишите программу по следующему описанию. Есть класс "Снайпер". От него создаются два экземпляра. Каждому устанавливается здоровье в 100 очков. В случайном порядке они стреляют друг в друга. Тот, кто стреляет, здоровья не теряет. У того, в кого стреляют, оно уменьшается на 20 очков от одного выстрела. После каждого выстрела надо выводить сообщение, какой снайпер атаковал, и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, программа завершается сообщением о том, кто одержал победу.
"""
# import random
# class Sniper:
#   attack_force = 20
  
#   def __init__(self, healthpoints, attack_force):
#     self.healthpoints = healthpoints
#     self.attack_force = attack_force
  
#   def __str__(self):
#     return f"{self.healthpoints}"

#   def attack(self, enemy):
#     enemy.healthpoints = enemy.healthpoints - self.attack_force

# oomat = Sniper(100, 20)
# altai = Sniper(100, 20)

# list_of_names = [oomat, altai]
# random.choice(list_of_names)

# while True:
#   if oomat.healthpoints <= 0:
#     print(f'Altai has won!')
#     break
#   elif altai.healthpoints <= 0:
#     print(f'Oomat has won!')
#     break
#   if random.choice(list_of_names) == oomat:
#     oomat.attack(altai)
#     print(f'Oomat hit Altai \n A = {altai} O = {oomat}')
#   elif random.choice(list_of_names) == altai:
#     altai.attack(oomat)
#     print(f'Altai hit Oomat \n A = {altai} O = {oomat}')

"""
2) Напишите программу по следующему описанию. Есть класс Hogwarts. В нем определены следующие атрибуты-факультеты: 
Gryffindor, Ravenclaw, Hufflepuff, Slytherin. От класса Hogwarts создаются объекты-студенты. При создании студентов необходимо указать баллы за их следующие качества: courage (храбрость), intelligence (интеллект), justice (справедливость), ambition (амбиции). У студентов не могут быть качества одинакового уровня. В зависимости от того, какое качество студента преобладает, метод sorting_hat будет распределять студента в один из факультетов и выдавать в какой факультет поступил студент.
Примечание: 
Преобладает courage -> Gryffindor
Преобладает intelligence -> Ravenclaw
Преобладает justice -> Hufflepuff
Преобладает ambition -> Slytherin
"""
# class Hogwarts:
#   gryffindor = 'Gryffindor'
#   ravenclaw = 'Ravenclaw'
#   hufflepuff = 'Hufflepuff'
#   slytherin = 'Slytherin'

#   def __init__(self, courage, intelligence, justice, ambition):
#     self.courage = courage
#     self.intelligence = intelligence
#     self.justice = justice
#     self.ambition = ambition
  
#   def sorting_hat(self):
#     if self.courage > self.intelligence and self.courage > self.justice and self.courage > self.ambition:
#       print(f'This student goes to {self.gryffindor}!')
#     elif self.intelligence > self.courage and self.intelligence > self.justice and self.intelligence > self.ambition:
#       print(f'This student goes to {self.ravenclaw}!')
#     elif self.justice > self.intelligence and self.justice > self.courage and self.justice > self.ambition:
#       print(f'This student goes to {self.hufflepuff}!')
#     elif self.ambition > self.intelligence and self.ambition > self.justice and self.ambition > self.courage:
#       print(f'This student goes to {self.slytherin}!')
#     else:
#       print('Incorrect values. Values cannot be the same!')

# harry = Hogwarts(100, 70, 70, 30)
# ron = Hogwarts(30, 40, 70, 20)
# hermione = Hogwarts(60, 100, 90, 30)

# harry.sorting_hat()
# ron.sorting_hat()
# hermione.sorting_hat()
