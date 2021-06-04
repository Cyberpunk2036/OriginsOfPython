class Suite:
    def __init__(self, h):
        self.suite = 2 * h + 0.3


class Coat:
    def __init__(self, v):
        self.coat = v / 6.5 + 0.5


class Clothes:
    def __init__(self, name):
        self.name = name
        self.lis = list()

    def list_append(self, h=0, v=0):
        self.lis.append(Suite(h).suite)
        self.lis.append(Coat(v).coat)

    def summ(self):
        return sum(self.lis)


a = Clothes("Пальто+Костюм")
a.list_append(2, 3)
a.list_append(2, 3)
a.list_append(2, 3)
print(a.summ())
