def sum_num():
    s = 0
    while True:
        in_list = input('Введите число, для выхода введите "x": ').split()
        for num in in_list:
            if num.lower() == "x":
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    print('Для выхода из программы введите "x".')
        print(f'Сумма чисел составила {s}')


print(sum_num())
