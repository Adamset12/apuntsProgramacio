"""
Grupo: Izan Arnaiz, Adam Benahmed y Axel Benitez.
Fecha de entrega: 16/10/2023.
ASIX A1 M03 UF1.

Descripción:

Ejercicio opcional -- Conversión de Fahrenheits a Celsius.
"""


# Crea una funcion la cual aplica la conversion de Fahrenheit a Grados Celsius y devuelve  el resultado
def Conversion(c):
    conversion = (9 / 5) * c + 32
    return conversion


print(Conversion(int(input("Dime un numero para conversionar: "))))
