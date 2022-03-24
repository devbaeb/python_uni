var1 = 'глобальная'

def my_func():
    global var1
    global var2
    var1 = 'локальная'
    var2 = 'вторая'
    print(var1)

my_func()
print(var1)
print(var2)
