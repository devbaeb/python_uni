ege2 = ["Математика - 78", "Информатика - 75", "Русский язык - 62"]

def get_info(s):
    new_string = s.split(" - ")
    return [new_string[0], int(new_string[1])]

lst3 = list()
lst4 = []

for i in ege2:
    for j in get_info(i):
        lst3.append(j)
    lst4.append(get_info(i))


print(lst3)
print(lst4)


def subjects(ege):
    subj = []
    for i in ege:
        for j in get_info(i):
            if type(j) == str:
                subj.append(j)
    return subj

def marks(ege):
    marks = []
    for i in ege:
        for j in get_info(i):
            if type(j) == int:
                marks.append(j)
    return marks

print(subjects(ege2))
print(marks(ege2))
