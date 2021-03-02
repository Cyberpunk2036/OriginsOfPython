# Третье задание
# Не смог сообразить, как работу выполняемую ValueError встроить в мой класс.
# Если при помощи ValueError возбуждать(raise) работу моего класса-исключения, то программа
# отрабатывает и выводит желаемый текст, но далее останавливается и цикл прекращается сам собой.
# Так как любое значнеие вводимое в input() будет текстовым, то я не сообразил, как осуществить
# проверку на приводимость к типу int, не вызывая ValueError
class MyException(Exception):
    def __init__(self, text):
        self.text = text

def cycle():
    """Выполняет проверку на нетекстовость и при удовлетворении, заносит в список"""
    inp = input("Вводите числа, остановка - 'stop': ")
    if inp == "stop":
        return False
    try:
        listt.append(int(inp))
    except ValueError:
        print(MyException("Вы ввели нечисловой объект, но я его пропущу!"))
    
   
listt = list()        
inp = True

while inp != False:
    inp = cycle()

print(listt)

        



    