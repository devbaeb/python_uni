ege4 = [ ["Математика",78], ["Информатика", 75], ["Русский язык", 62]]

print(ege4[1][0])

def total(ege):
    maths = ege[0][1]
    inf = ege[1][1]
    russian = ege[2][1]

    return maths + inf + russian

total_amount = total(ege4)

print("Общая сумма баллов: %d" % total_amount)



ege3 = [ "Математика", 78, "Информатика", 75, "Русский язык", 62 ]

def total2(ege):
    maths = ege[1]
    inf = ege[3]
    russian = ege[5]

    return maths + inf + russian

total_amount2 = total2(ege3)

print("Общая сумма баллов: %d" % total_amount2)



def convert_list(ege):
    ege_new = [ege[:2], ege[2:4], ege[4:]]
    return ege_new

total_amount3 = total(convert_list(ege3))

print("Общая сумма баллов: %d" % total_amount3)
