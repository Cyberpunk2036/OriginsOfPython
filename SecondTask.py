# Второе задание
class MyException(Exception):
    def __init__(self, text):
        self.text = text

while True:
    inputt = list(map(lambda x: int(x), input("Введите делимое и делитель через пробел: ").split()))
    try:
        if inputt[1] == 0:
            raise MyException("Вы ввели ноль в делителе! Попробуйте ввести другое число")
        print(inputt[0]/inputt[1])
        break
    except MyException as err:
        print(err)

    