def get_word():
    word = input('Введите слово: ')
    return word

def is_palindrome(word):
    return word == word[::-1] and 'Палиндром' or 'Не палиндром'

def create_message(word, what_is):
    return 'Слово %s - %s' % (word, what_is)

def check_palindrome():
    word = get_word()
    what_is = is_palindrome(word)
    msg = create_message(word, what_is)
    print(msg)

check_palindrome()
