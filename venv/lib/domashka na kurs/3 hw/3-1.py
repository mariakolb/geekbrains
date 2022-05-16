def numbs(num1, num2):
    try:
        num1, num2 = int(num1), int(num2)
        numb = num1 // num2
    except ZeroDivisionError:
        return 'Деление на ноль невозможно'
    return numb


print(numbs(input('Введите первое число: '), input('Введите второе число: ')))
