# Первое задание
from sys import argv

script_name, working, rate, prize = argv

print("Запуск скрипта:", script_name)
print("Выработка в часах:", working)
print("Значение ставки в час:", rate)
print("Величина премии:", prize)
print("Итоговый расчет:", (int(working)*int(rate)) + int(prize))