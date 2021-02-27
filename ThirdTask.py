class Cell:
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

    def __sub__(self, other):
        return self.n - other.n

    def __mul__(self, other):
        return self.n * other.n

    def __truediv__(self, other):
        return self.n // other.n

    def make_order(self, m):
        self.m = m
        self.celoe = (self.n // self.m)
        self.dobav = self.n - (self.celoe * self.m)
        self.string = ""
        if self.dobav == 0:
            for i in range(self.celoe):
                 self.string += "*" * self.m + "\\n"
            self.string = self.string[:-2]
        else:
            for i in range(self.celoe):
                 self.string += "*" * self.m + "\\n"
            self.string += "*" * self.dobav
        return self.string

a = Cell(12)
b = Cell(3)

summ = Cell(a + b)
print("Сложение:", summ.n)

sub = Cell(a - b)
print("Вычитание:", sub.n)

mul = Cell(a * b)
print("Умножение:", mul.n)

truediv = Cell(a / b)
print("Деление:", truediv.n)

print(a.make_order(5))