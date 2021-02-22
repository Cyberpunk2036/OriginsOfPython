# Второе задание
class Road:
    def __init__(self, length, width, width_polotna=5, mass=25):
        self._length = length
        self._width = width
        self.width_polotna = width_polotna
        self.mass = mass
    
    def calculate(self):
        print(f"Масса асфальта:{self._width*self._length*self.width_polotna*self.mass/1000} тонн")
        
a = Road(20, 5000)
a.calculate()