# Четвертое задание
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.name = name
        self.is_police = is_police
        self.color = color
    def go(self):
        if self.speed > 0: print("Машина поехала")
    def stop(self):
        if self.speed == 0: print("Машина остановилась")
    def turn(self):
        pass
    def show_speed(self):
        print(f"Текущая скорость: {self.speed}")
        
class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 60: 
            print("Превышена скорость движения!")
        else:
             print(f"Текущая скорость: {self.speed}")
        
class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        
class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        if self.speed > 40: 
            print("Превышена скорость движения!")
        else:
            print(f"Текущая скорость: {self.speed}")
    

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

a = TownCar(70, "red", "Marva", False)
a.go()
a.show_speed()
a.stop()
print("-"*20)
b = SportCar(120, "black", "Ferrari", False)
b.go()
b.show_speed()
b.stop()
print("-"*20)
c = WorkCar(30, "black", "Mercedes-Benz", False)
c.go()
c.show_speed()
c.stop()
print("-"*20)
d = PoliceCar(60, "white", "Opel", True)
d.go()
d.show_speed()
d.stop()
