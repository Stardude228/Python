def swap_big_small():
    integers = input('Type your number: ')
    max_number = max(integers)
    min_number = min(integers)
    index_of_maximum = integers.index(max_number)
    index_of_minimal = integers.index(min_number)
    integers2 = list(integers)
    integers2.pop(index_of_maximum)
    integers2.insert(index_of_maximum, min_number)
    integers2.pop(index_of_minimal)
    integers2.insert(index_of_minimal, max_number)
    integers = ''.join(integers2)
    return integers
print(swap_big_small())