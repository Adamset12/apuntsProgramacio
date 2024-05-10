"""
Adam Ben Ahmed Belachi
23/10/2023
MO3 UF1 A3
"""
try:
    Numeros = input().split()
    print(max(int(Numeros[0]), int(Numeros[1])))
except ValueError:
    print("Fica valors numérics")