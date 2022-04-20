s = ["первый", "2-ой", "третий", 4, [5], "последний"]

print([i for i in s if isinstance(i, str) and i.isalpha()])
