qsec = int(input('Введите количество секунд: '))
hour = qsec // 3600
min = (qsec % 3600) // 60
sec = (qsec % 3600)  % 60
print(f"{hour:02}:{min:02}:{sec:02}")
