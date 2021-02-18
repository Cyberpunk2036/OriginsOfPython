# Шестое задание
def concatenator(L):
    """Собирает из двух слов одно на нажатие согласия"""
    a = input("Предмет из двух слов?<Y/N>:\n")
    if a == "Y":
        L[0] = L[0] + " " + L[1]
        L.remove(L[1])
    return L

def dict_creator(L):
    """Создает словарь из данных списка"""
    Subjects = {i[0]:None for i in A}
    L = list(map(lambda x: x[1:], L))
    M = [[i.split("(") for i in L[j]] for j in range(len(L))]
    M = [[i[0] for i in j] for j in M]
    M = [[int(i) for i in j if i!="—"] for j in M]
    M = [sum(i) for i in M]
    Subjects = {A[i][0]: M[i] for i in range(len(A))}
    return Subjects


with open("Sixth_text_file.txt", "r") as file:
    A = file.readlines()
    print("Вот что в файле:")
    for i in A:
        print(i)
    print("Заполним словарь")
    A = [i.split() for i in A]
    A = [concatenator(i) for i in A]
    print(dict_creator(A))
