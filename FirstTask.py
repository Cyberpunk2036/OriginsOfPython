# Не совсем понятна формулировка первого задания, но надеюсь угадал
# Первое задание
from sys import exit
with open("New_text_file.txt", "w") as file:
    a = input("Введите строки текста:\n")
    while True:
        file.writelines(a+" ") if a != "" else exit()
        a = input()
