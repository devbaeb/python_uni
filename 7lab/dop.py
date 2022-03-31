class Natural(int):
    def __init__(self, x):
        self.x = int(x)
        self.return_x()

    def __sub__(self, __x):
        if type(__x) == int or type(__x) == Natural:
            return Natural(super().__sub__(__x))
        else:
            return super().__sub__(__x)

    def __add__(self, __x):
        if type(__x) == int or type(__x) == Natural:
            return Natural(super().__add__(__x))
        else:
            return super().__add__(__x)

    def __mul__(self, __x):
        if type(__x) == int or type(__x) == Natural:
            return Natural(super().__mul__(__x))
        else:
            return super().__mul__(__x)

    def __floordiv__(self, __x):
        if type(__x) == int or type(__x) == Natural:
            return Natural(int(self)//(__x))
        else:
            return int(self).__floordiv__(__x)

    def __pow__(self, __x):
        if type(__x) == int or type(__x) == Natural:
            return Natural(super().__pow__(__x))
        else:
            return super().__pow__(__x)

    #def __truediv__(self, __x):
    #    if type(__x) == int or type(__x) == Natural:
    #        return Natural(super().__truediv__(__x))
    #    else:
    #        return super().__truediv__(__x)

    #def __mod__(self, __x):
    #    if type(__x) == int or type(__x) == Natural:
    #        return Natural(super().__mod__(__x))
    #    else:
    #        return super().__mod__(__x)

    def return_x(self):
        if self.x >= 0:
            return self.x
        else:
            raise ValueError('less than zero')

x = Natural(10)
y = Natural(3)

print(type(x-y))
