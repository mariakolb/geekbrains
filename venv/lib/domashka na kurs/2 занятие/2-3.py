month = int(input('Input the month in number: '))
month_dict = {1: 'jan', 2: 'feb', 3: 'mar', 4: 'apr', 5: 'may', 6: 'jun', 7: 'jul', 8: 'aug', 9: 'sept', 10: 'oct',
              11: 'nov', 12: 'dec'}
if month in month_dict:
    print(f'{month} month of the year is {month_dict[month]}')


month = int(input('Input the month in number: '))
month_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
if month in month_list:
    print(f"{month} month of the year is {month_list[month-1]}")

#Не могу разобраться, почему здесь не работает print

seasons_dict = {'winter': [12, 1, 2], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
month_num = int(input('Input the number of the month: '))
if month_num in sum(seasons_dict.values(), []):
    for i in seasons_dict.items():
        if month_num in i[1]:
            print(i[0])
            break


#Эту задачу смотрела как Вы делаете, как раз не могла понять, как достать значения ключей из подсписков :)