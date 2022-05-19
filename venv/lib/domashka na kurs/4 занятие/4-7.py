from itertools import count
from math import  factorial

def gen():
    for el in count(1):
        yield factorial(el)

n = 0
for i in gen():
    if n == 4:
        break
    else:
        n += 1
    print(f'Факториал числа {n} равен {i}')
