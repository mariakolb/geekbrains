def my_func(num1, num2, num3):
    my_list = [num1, num2, num3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return 'Only number: '


print(my_func(int(input('Введите первое число: ')), (int(input('Введите второе число: '))), int(input('Введите третье число: '))))
