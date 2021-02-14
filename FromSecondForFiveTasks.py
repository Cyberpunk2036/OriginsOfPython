# Второе задание
A = [int(i) for i in input("Введите числа списка через пробел:\n").split()]
B = [A[i] for i in range(1, len(A)) if A[i] > A[i-1]]
print(B)

# Третье задание
print([i for i in range(20, 240) if (i%20 == 0) or (i%21 == 0)])

# Четвертое задание
A = [int(i) for i in input("Введите числа списка через пробел:\n").split()]
B = [i for i in A if A.count(i) == 1]
print(B)

# Пятое задание
from functools import reduce

def reduce_func(prev_el, el):
    return prev_el * el

A = [i for i in range(100, 1001) if i%2 ==0]
print(reduce(reduce_func, A))


