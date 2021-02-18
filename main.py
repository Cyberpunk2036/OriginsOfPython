# Не совсем понятна формулировка первого задания, но надеюсь угадал
# Первое задание
import sys
with open("New_text_file.txt", "w") as file:
    a = input("Введите строку текста:\n")
    while True:
        file.writelines(a+" ") if a != "" else sys.exit()
        a = input()
