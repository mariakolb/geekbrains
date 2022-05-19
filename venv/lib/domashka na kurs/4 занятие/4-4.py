from random import randint
my_list = [randint(1, 44) for _ in range(20)]
list4 = [el for el in my_list if my_list.count(el) == 1]
print(f'Первоначальный список: {my_list}\n'
      f'Cписок без повторений: {list4}')