ege1 = "Математика — 78, Информатика — 75, Русский язык — 62"
subjects = ["Информатика", "информатика", "Физика", "ФИЗИКА"]

def get_tested(ege, subject):
    return False if ege.lower().find(subject.lower()) == -1 else True

for subject in subjects:
    print("ЕГЭ по дисциплине %s %sсдан" % (subject, '' if get_tested(ege1, subject) else 'не '))
