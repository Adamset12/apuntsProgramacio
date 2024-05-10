"""
Adam Ben Ahmed Belachi
23/10/2023
MO3 UF1 A3
"""
try:
    import random
    RPS = int(input())
    if RPS in [1, 2, 3]:
        aleatori = int(random.uniform(1, 4))
        if RPS == aleatori: print("Empat")
        elif RPS < aleatori: print("Guanya el segon")
        else: print("Guanya el primer")
except ValueError or IndexError: print("Fica valors numérics vàlids")