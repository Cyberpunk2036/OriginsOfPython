# Четвертое задание
with open("Frt_text_file.txt","r") as file:
    A = file.readlines()
    A = [i.split() for i in A]
    Rus = ["Один", "Два", "Три", "Четыре"]
    B = [Rus[i]+A[i][1]+A[i][2]+"\n" for i in range(len(Rus))]
    with open("Fourth_new_text.txt", "w") as four:
        four.writelines(B)