"""
Adam Ben Ahmed Belachi
23/10/2023
MO3 UF1 A3
"""
try:
    hora = input().split()
    if (int(hora[0]) < 24 and int(hora[1]) <= 59 and int(hora[2]) <= 59) != True: exit(0)
    hora[2] = int(hora[2]) + 1
    hora[1] = int(hora[1])
    hora[0] = int(hora[0])
    if int(hora[2]) == 60:
        hora[2] = 0
        hora[1] = int(hora[1]) + 1
    if int(hora[1]) == 60:
        hora[1] = 0
        hora[0] = int(hora[0]) + 1
    if int(hora[0]) == 24:
        hora[0] = 0
    print(f"{hora[0]:02d}:{hora[1]:02d}:{hora[2]:02d}")
except: print("Posa valors vàlids")