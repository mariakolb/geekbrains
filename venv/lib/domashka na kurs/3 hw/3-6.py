def int_func():
    for word in input('Введите слово через пробел маленькими латинскими буквами: ').split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - только маленькие латинские буквы")


int_func()
