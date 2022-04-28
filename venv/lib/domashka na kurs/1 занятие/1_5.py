vrch = int(input('Введите значение выручки: '))
izd = int(input('Введите значение издержки: '))
result = vrch - izd
if result > 0:
    print ('Финансовый результат : прибыль')
else: print ('Финансовый результат: убыток')