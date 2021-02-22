# Третье задаиние
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        # self.position = position
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, position, _income):
        super().__init__(name, surname, position, _income)
    def get_full_name(self):
        print(f"Имя: {self.name}, фамилия: {self.surname}")
    def get_total_income(self):
        # print(self.income["wage"])
        print("Полный доход: ", int(self._income["wage"])+int(self._income["bonus"]))
        
a = Position("Владимир", "Юрковский", "Звездно-планетарный инспектор", {"wage":"1000", "bonus":"75000"})
a.get_full_name()
a.get_total_income()