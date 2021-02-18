# Седьмое задание

import json

with open("Seventh_text_file.txt", "r") as file:
    A = file.readlines()
    A = [i.split() for i in A]
    B = [int(i[2])-int(i[3]) for i in A]
    n = 0
    for i in B:
        if i >0 : n+=1
    C = sum([i for i in B if i > 0])/n
    EndList = {A[i][0]:B[i] for i in range(len(A))}
    EndList["Average"] = C
    EndList = [EndList]
    with open("Seventh_json_file", "w") as jsonf:
        json.dump(EndList, jsonf)

