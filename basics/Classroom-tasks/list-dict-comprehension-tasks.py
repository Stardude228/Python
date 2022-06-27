"""
1) Создайте список имён. Далее создайте отфильтрованный список имён, где будут содержаться имена, начинающиеся с гласных букв. Используйте list comprehension.
"""
names = {"Arafat", "Beknaz", "Argen"}
vowels = 'a','o','e','i','o','u','A','O','E','I','O','U'
names_stats_a = [name for name in names if name.startswith(vowels)]
print(names_stats_a)
"""
2) Создайте вложенный словарь, в котором ключами будут имена студентов, а значениями - другой словарь, в котором ключи - названия предметов, а значения - баллы за предмет данного студента. Далее с помощью dictionary comprehension обновите этот словарь, присвоив по 2 экстра балла каждому студенту по каждому предмету.
Например: 
a = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
Результат:
{'Sam': {'math': 97, 'literature': 90}, 'Alice': {'math': 72, 'literature': 100}}
"""
a = {'Sam': {'math': 95, 'literature': 88}, 'Alice': {'math': 70, 'literature': 98}}
results = {key:{k:v+2 for k, v in val.items()} for key,val in a.items()}
print(results)
"""
3) Создайте список чисел от 1 до 10. Создайте множество, в котором поместите квадраты этих чисел, если число делится на 2 без остатка, в противном случае поместите в список утроенные значения чисел.
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [i**2 if i % 2 == 0 else i*3 for i in list1]
print(list2)
"""
4) Нужно принять строку от пользователя (латиницей) и посчитать в ней количество гласных символов используя list comprehension.
Например:
    input : goremyka
    output : 4
"""
data = input('Введите строку:')
number = 0
list1 = list(data)
result = [number + 1 for i in list1 if str(i) in 'AEOIYUaoeiyu']
print(sum(result))
