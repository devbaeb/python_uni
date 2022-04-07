my_list = ["победа","ничья", "поражение"]

print(type(my_list))

print(len(my_list))

print(my_list[1])

print(id(my_list[0]), id(my_list[1]), id(my_list[2]))
print(id(my_list))

print(type([]))
print([])

print([] and 'не пустой' or 'пустой')

print(type([[], []]), len([[], []]))

list1 = [[], []]
print(id(list1[0]), id(list1[1]))
