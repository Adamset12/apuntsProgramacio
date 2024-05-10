"""
Adam Ben Ahmed Belachi
23/10/2023
MO3 UF1 A3
"""
try:
    day = int(input())

    dias_setmana = ["dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte", "diumenge"]
    dias_num_setmana = [1, 2, 3, 4, 5, 6, 7]
    i = 0
    while i < 8:
        if dias_num_setmana[i] == day:
            print(dias_setmana[i])
            i = 8
        i += 1
except ValueError or IndexError: print("Fica un valor vàlid")