"""
Adam Ben Ahmed Belachi
23/10/2023
MO3 UF1 A3
"""
try:
    ppplcookies = input().split()
    if (int(ppplcookies[1]) % int(ppplcookies[0])) != 0: print("Let's Fight")
    else: print("Let's Eat!")
except: print("Input inválido")