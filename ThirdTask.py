# Третье задание
with open("Th_text_file.txt", "r") as file:
    A = file.readlines()
    A = [i.split() for i in A]
    print("Фамилии самых низкооплачиваемых сотрудников:")
    for i in A:
        print(i[0]) if float(i[1]) < float(20000) else True
    B = [float(i[1]) for i in A]
    print("Средняя величина дохода сотрудников:", str(sum(B)/len(B)))