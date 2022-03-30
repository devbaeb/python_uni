def grade1(mark):
    if mark == 5:
        return 'отлично'
    if mark == 4:
        return 'хорошо'
    if mark == 3:
        return 'удовлетворительно'
    if mark == 2:
        return 'неудовлетворительно'

mark = int(input('Оценка по школьной шкале: '))
print(grade1(mark))
