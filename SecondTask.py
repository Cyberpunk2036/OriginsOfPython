# Второе задание
with open("Text.txt", "r") as file:
    a = file.readlines()
    print("Количество строк:", len(a))
    n = ["В "+str(i)+"-ой строке:" for i in range(1, len(a)+1)]
    for i in range(len(a)):
        print(n[i], len(a[i]), "символов")
