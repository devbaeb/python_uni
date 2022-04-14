ege1 = "Математика — 78,     Информатика — 75,             Русский язык — 62"

def convert_list(ege):
    new_ege = ege.split(',')
    res = []
    for i in new_ege:
        res.append(i.strip().split(" - "))
    return res

ege_new = convert_list(ege1)

print(ege_new)
