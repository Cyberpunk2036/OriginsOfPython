# Седьмое задание
import math

n = int(input("Введите граничное число: "))

def factorials(a):
    """Генерирует значения факториалов от 1 до введенного числа включистельно"""
    for el in range(1, n+1):
        yield math.factorial(el)

fac = factorials(n)

for i in fac:
    print(i)

