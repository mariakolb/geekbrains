words = input('Введите несколько слов разделенные пробелами: ').split()
for i, item in enumerate(words, 1):
    print(f'{i}) {item[:10]}')