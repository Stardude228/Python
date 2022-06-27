"""
1) Есть глобальная переменная, которая обозначает размер самой главной первой матрешки. Напишите функцию, в которой к размеру главной матрешки прибавляется размер второй матрешки, который определен в этой функции. То же самое сделайте и с третьей функцией внутри второй. Верните результат сложения.
"""
main = 5
def matreshka(var):
  
  def small_matreshka(inner_var):
    third = 1
    nonlocal var
    var = third + inner_var
    return third + inner_var
  
  second = 3
  small_matreshka(var)
  return second + var
  
print(matreshka(main))
"""
2) Есть глобальная переменная, которая содержит пустой список. Вам необходимо написать функции, одна из которых add() - добавляет в этот список имена, которые вводит пользователь. А другая функция remove() - удаляет эти имена из списка по индексу, который вводит пользователь. Вызовите функции в рандомном порядке 10 раз и в конце выведите список.
"""

list_ = []

def add_():
  user_name = input('Type a name: ')
  list_.append(user_name)

def remove_():
  try:
    user_index = int(input('Type an index that has to be deleted: '))
    indexes = []
    for i in list_:
      indexes.append(list_.index(i))
    if user_index not in indexes:
      raise ValueError
  except:
    print('There is no such an index')
  while user_index not in indexes:
    if user_index in indexes:
      indexes.remove(user_index)
      break
    else:
      print(f'Here is a list of all indexes: {indexes}')
      print(f'Here is a list of all names: {list_}')
      user_index = int(input('Please type a correct index: '))
      
  else:
      list_.remove(list_[user_index])
add_()
remove_()
add_()
remove_()
add_()
add_()
remove_()
remove_()
add_()
remove_()
print('List of names', list_)