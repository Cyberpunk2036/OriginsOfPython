# Пятое задание
with open("Fifth_text_file.txt", "w") as file:
    A = input("Введите набор чисел разделенные пробелами:\n")
    file.writelines(A)
with open("Fifth_text_file.txt", "r") as file:
    A = file.read()
    A = [int(i) for i in A.split()]
    print("Сумма чисел:", sum(A))