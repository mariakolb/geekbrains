from functools import reduce

def my_list(el_1, el_2):
    return el_1 * el_2

list5 = [el for el in range(100, 1001, 2)]
print(f'Первоначальный список: {list5}'
      f'Произведение списка: {reduce(my_list, list5)}')