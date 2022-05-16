def st_fun(x, y):
    try:
        res = x ** y
    except TypeError:
        return 'Введите положительное число и целое отрицательное число'
    return res

print(st_fun(4, -2))