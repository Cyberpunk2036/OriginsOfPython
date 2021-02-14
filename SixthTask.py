# Шестое задание
from sys import argv
import itertools
# Первый пункт
num = argv
print("Начальное число:", num[1])
print("Конченое число:", num[2])

C = list()
for el in itertools.count(int(num[1])):
    if el > int(num[2]):
        break
    C.append(el)
print("Сгенерированный список:", C)
# Второй пункт
print()
print("Количество повторений элементов списка:", num[3])
for i in range(int(num[3])):
    q = 0
    for el in itertools.cycle(C):
        if q > len(C)-1:
            break
        print(el, end=" ")
        q += 1
    print()
