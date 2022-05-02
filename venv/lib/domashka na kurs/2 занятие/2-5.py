my_list = [7, 5, 3, 3, 2]
num = int(input('Введите число: '))
i = 0
for n in my_list:
    if num <= n:
         i += 1
my_list.insert(i, float(num))
print(my_list)
