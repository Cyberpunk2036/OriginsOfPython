# Первое задание
import time

class TrafficLight:
    def running(self, colors = ["Красный", "Желтый", "Зеленый"]):
        self.__color = colors
        print(f"Сейчас цвет светофора: {self.__color[0]}")
        time.sleep(2)
        print(f"Сейчас цвет светофора: {self.__color[1]}")
        time.sleep(3)
        print(f"Сейчас цвет светофора: {self.__color[2]}")
        time.sleep(7)
        print(f"Сейчас цвет светофора: {self.__color[0]}")

a = TrafficLight()
a.running()
        
        
            
                