"""
Grupo: Izan Arnaiz, Adam Benahmed y Axel Benitez.
Fecha de entrega: 16/10/2023.
ASIX A1 M03 UF1.

Descripción:

Programa que define a que edad debe trabajar una persona, si está entre 16 y 65 años puede trabajar,
si no lo está no tiene suficiente edad o ya es mayor para trabajar.
"""

# Si el usuario tiene menos de 16 años o más de 65 años, no puede trabajar, por el contrario, puede trabajar.
edad = int(input("Dime tu edad: "))
if edad < 16 or edad > 65:
    print("NO! Puedes trabajar")
else:
    print("Puedes trabajar")
