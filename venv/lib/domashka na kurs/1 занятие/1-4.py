n = int(input('Введите целое положительное число: '))
max_n = 0
num = n

while num > 0:
    n1 = num % 10 #отделяем последнюю цифру
    if n1 > max_n:
        max_n = n1
        if max_n == 9:
            break
    num = num // 10 #отсекаем последнюю цифру
print(f'Наибольщая цифра в числе {n} равна {max_n}')
