user_list = input('Enter the number with space - ').split()
for i in range(1, len(user_list), 2):
    user_list.insert(i - 1, user_list.pop(i))
print(user_list)

#Там внизу рассмотрела еще как Вы решали, но сама делала через pop


#my_list = list(input('Enter the members - '))
#for i in range(1 , len(my_list), 2):
    #my_list[i - 1], my_list[i] = my_list[i], my_list[1 - i]
#print(my_list)

#for i in range(0, len(my_list) - 1, 2):
    #my_list[i + 1], my_list[i] = my_list[i], my_list[1 + i]
#print(my_list)

#my_list = input('Enter the numbers of the list with space: ').split()
#print('Input list: ', my_list)
#idx = len(my_list) if len(my_list) % 2 == 0 else len(my_list) - 1

#my_list[:idx:2], my_list[1:idx:2] = my_list[1:idx:2], my_list[:idx:2]
#print('Changed list: ', my_list)