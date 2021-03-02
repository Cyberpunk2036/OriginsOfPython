# Седьмое задание
class Complex:
    def __init__(self, a):
        self.a = a
    def __add__(self, other):
        return self.a + other.a
    
    def __mul__(self, other):
        return self.a * other.a
A =[complex(5, 2), complex(2, 1)]   
a = Complex(A[0])
b = Complex(A[1])
if (A[0] + A[1]) == (a + b) and (A[0] * A[1]) == (a * b):
    print(f"Сумма: {a * b}\nПроизведение: {a + b}")
else:
    print("Несовпадние, где-то закралась ошибка")
    
