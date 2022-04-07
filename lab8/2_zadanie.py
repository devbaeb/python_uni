mark1 = ["хорошо", "удовлетворительно"]

print(mark1, id(mark1))

mark1.append("неудовлетворительно")

mark1.insert(0, "отлично")

print(mark1, id(mark1))

print(mark1[:3])

mark2 = ["чётный", "нечётный"]

print(mark2, id(mark2))

mark3 = mark2 * 2

print(mark3, id(mark3))
