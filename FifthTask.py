# Пятое задание
class Stationery:
    def __init__(self, title):
        self.title = title
        print(f"Вы запустили: {self.title}")
    
    def draw(self):
        print("Запуск отрисовки")
        
class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Переопределение для ручки")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Переопределение для карандаша")
        
class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        print("Переопределение для кисти")

a = Stationery("Родительский класс")
a.draw()

b = Pen("Ручка")
b.draw()

c = Pencil("Карандаш")
c.draw()

d = Handle("Кисть")
d.draw()