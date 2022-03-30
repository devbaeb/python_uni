def grade1(mark):
    if mark >= 85 and mark <= 100:
        return 'отлично'
    elif mark >=71:
        return 'хорошо'
    elif mark >= 60:
        return 'удовлетворительно'
    elif mark >= 0:
        return 'неудовлетворительно'

mark = int(input('Оценка по школьной шкале: '))
print(grade1(mark))
