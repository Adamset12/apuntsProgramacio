"""
Adam Ben Ahmed Belachi
23/10/2023
MO3 UF1 A3
"""
try:
    RPS = input().split()
    if int(RPS[0]) in [1, 2, 3] and int(RPS[1]) in [1, 2, 3]:
        if int(RPS[0]) == int(RPS[1]): print("Empat")
        elif int(RPS[0]) < int(RPS[1]): print("Guanya el segon")
        else: print("Guanya el primer")
except: print("Fica valors vàlids")