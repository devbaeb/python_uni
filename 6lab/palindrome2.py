def get_word():
    global word
    word = input('Введите слово: ')

def is_palindrome():
    global what_is
    what_is = word == word[::-1] and 'Палиндром' or 'Не палиндром'

def create_message():
    global msg
    msg = 'Слово %s - %s' % (word, what_is)

def check_palindrome():
    get_word()
    is_palindrome()
    create_message()
    print(msg)

check_palindrome()
