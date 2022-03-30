import sys

def get_word():
    word = input('Введите слово: ')
    if word.isalpha():
        return word
    elif word == '':
        print('Пустая строка')
        sys.exit()
    else:
        print('Недопустимый символ')
        sys.exit()

def is_palindrome(word):
    word_lower = word.lower()
    return True if word_lower[::-1] == word_lower else False

def is_palindrome_old(word):
    return word == word[::-1] and 'Палиндром' or 'Не палиндром'

def create_message(word, what_is):
    prefix = '' if what_is else 'не '
    return 'Слово "%s" - %s' % (word, prefix + 'палиндром')

def check_palindrome():
    word = get_word()
    what_is = is_palindrome(word)
    msg = create_message(word, what_is)
    print(msg)

check_palindrome()
