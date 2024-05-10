"""
Adam Ben Ahmed Belachi
23/10/2023
MO3 UF1 A3
"""
import math
try:
    datos = input().split()

    if math.pi * (float(datos[0])/2) ** 2 > float(datos[1]) * float(datos[2]): print("Compra la rodona")
    else:
        print("Compra la rectangular")
except ValueError: print("Fica valors númerics")