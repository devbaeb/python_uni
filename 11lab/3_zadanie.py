def check_input(data):
    if data == [] or data == '':
        words = []
        print('Пустые данные!')
    else:
        if data[0] == '[' and data[-1] == ']':
            words = eval(data)
        else:
            words = [data]
    words = [word for word in words if isinstance(word, str) and word.isalpha()]
    return words

print(check_input(''))
print(check_input('[]'))
print(check_input('ПроизвольнаяСтрока'))
print(check_input('["Произвольный", "список"]'))
print(check_input('123ПроизвольнаяСтрока##'))
print(check_input('["Произвольный$$", "список", "000"]'))

