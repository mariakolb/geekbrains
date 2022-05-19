from sys import argv

print(argv)
time, rate, bonus = argv
salary = (int(time) * int(rate) + int(bonus))
print(f'За этот месяц отработано {time} часов\n Премия {bonus}\n Заработная плата: {salary}')
