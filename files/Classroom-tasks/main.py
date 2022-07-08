"""
1) Используйте файл HarryPotterBooks.json. Напишите скрипт, который соберет все даты выпуска книг, посчитает их среднее арифметическое и запишит получившееся число в файл result.txt

{
   "books": [
       {
           "title": "Philosopher's Stone",
           "year": 1997
       },
       {
           "title": "Chamber of Secrets",
           "year": 1998
       },
       {
           "title": "Prisoner of Azkaban",
           "year": 1999
       },
       {
           "title": "Goblet of Fire",
           "year": 2000
       },
       {
           "title": "Order of the Phoenix",
           "year": 2003
       },
       {
           "title": "Half-Blood Prince",
           "year": 2005
       },
       {
           "title": "Deathly Hallows",
           "year": 2007
       }
   ]
}
"""
# import json

# with open('HarryPotterBooks.json', 'r') as data:
#     list_ = json.load(data)
#     list_ = list_['books']
#     list_ = [inner_value for i in list_ for inner_key, inner_value in i.items() if inner_key == 'year']
#     res = sum(list_) / len(list_)

# with open('result.txt', 'w+') as result:
#   result.write(str(res))
#   result.seek(0)
#   print(result.read())