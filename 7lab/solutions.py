def number_of_solutions(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        print('нет действительных решений')
    else:
        print('есть корни')
        if d > 0:
            print('два различных корня')
        else:
            print('два равных корня')

number_of_solutions(1, 1, 1)
print('')
number_of_solutions(1, 2, 1)
print('')
number_of_solutions(1, -3, 2)
